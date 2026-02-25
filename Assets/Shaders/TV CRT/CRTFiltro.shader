Shader "Custom/CRTPostProcess"
{
    Properties
    {
        _MainTex ("Texture", 2D) = "white" {}
        _Curvature ("Curvature", Range(0, 1)) = 0.15
        _ScanlineIntensity ("Scanline Intensity", Range(0,1)) = 0.6
        _ScanlineDensity ("Scanline Density", Range(100,2000)) = 800
        _RGBSplit ("RGB Split", Range(0,0.01)) = 0.002
        _VignetteIntensity ("Vignette", Range(0,1)) = 0.3
    }

    SubShader
    {
        Tags { "RenderPipeline"="UniversalPipeline" }

        Pass
        {
            Name "CRT"
            ZWrite Off
            Cull Off

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct Varyings
            {
                float4 positionHCS : SV_POSITION;
                float2 uv : TEXCOORD0;
            };

            TEXTURE2D(_MainTex);
            SAMPLER(sampler_MainTex);

            float _Curvature;
            float _ScanlineIntensity;
            float _ScanlineDensity;
            float _RGBSplit;
            float _VignetteIntensity;

            Varyings vert (Attributes v)
            {
                Varyings o;
                o.positionHCS = TransformObjectToHClip(v.positionOS.xyz);
                o.uv = v.uv;
                return o;
            }

            float4 frag (Varyings i) : SV_Target
            {
                float2 uv = i.uv;

                // CURVATURA
                float2 centered = uv * 2 - 1;
                centered *= 1 + _Curvature * dot(centered, centered);
                uv = centered * 0.5 + 0.5;

                // RGB SPLIT
                float r = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, uv + float2(_RGBSplit, 0)).r;
                float g = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, uv).g;
                float b = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, uv - float2(_RGBSplit, 0)).b;
                float3 color = float3(r,g,b);

                // SCANLINES REALES (MUY VISIBLES)
                float scan = sin(uv.y * _ScanlineDensity);
                float scanMask = scan * 0.5 + 0.5;
                color *= lerp(1.0, scanMask, _ScanlineIntensity);

                // VIGNETTE
                float dist = distance(i.uv, float2(0.5,0.5));
                color *= 1 - dist * _VignetteIntensity;

                return float4(color,1);
            }

            ENDHLSL
        }
    }
}