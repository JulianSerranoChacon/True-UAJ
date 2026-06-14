import json
import os
import pandas as pd
import matplotlib.pyplot as plt

def drawHexbinHeatmap(data_list, background_image, output_file, target_level, figsize, x_offset, y_offset, hex_color, gridsize, extent):
    if not data_list:
        print(f"Error: No hay datos para procesar.")
        return

    # Convertir a DataFrame
    df = pd.DataFrame(data_list)
    
    # Filtrar por el nivel que queremos procesar
    data = df[df['levelID'] == target_level]

    if data.empty:
        print(f"Aviso: No se encontraron impactos (hits) para el Level ID: {target_level}")
        return

    fig, ax = plt.subplots(figsize=figsize) 

    try:
        img = plt.imread(background_image)
        ax.imshow(img, extent=extent, aspect='auto')
    except Exception as e:
        print(f"Aviso: No se encontró {background_image}, generando mapa con fondo neutro.")

    # Dibujamos el mapa
    hb = ax.hexbin(
        x=(data["x"] + x_offset), 
        y=(data["y"] + y_offset),
        gridsize=gridsize,
        extent=extent,
        alpha=0.6,
        cmap=hex_color,
        mincnt=1,
        linewidths=1.5
    )
    
    plt.colorbar(hb, ax=ax, label='Cantidad de Impactos')
    ax.set_title(f"Heatmap: Player Hits - Nivel {target_level}", fontsize=14)
    fig.savefig(output_file, dpi=600, bbox_inches='tight')
    print(f"¡Éxito! Imagen guardada como: {output_file}")

if __name__ == '__main__':
    folder_path = '../../Datos Telemetria/'
    all_hits = []

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Crea la carpeta {folder_path} y mete el archivo json dentro.")
    else:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.json'):
                file_path = os.path.join(folder_path, file_name)
                print(f"Procesando: {file_name}...")

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    for event in data:
                        if event.get("type") == "playerHit":
                            
                            hit = {
                                "x": event.get("cordX"),
                                "y": event.get("cordY"),
                                "levelID": event.get("levelID")
                            }
                            
                            if hit["x"] is not None and hit["y"] is not None:
                                all_hits.append(hit)
                            
                except Exception as e:
                    print(f"Error procesando {file_name}: {e}")


    # Dibujar el heatmap con la lista de hits ya limpia

    # Nivel 1
    drawHexbinHeatmap(
        data_list=all_hits,
        background_image="bgNivel1.png",
        output_file=f"./HeatMaps/resultado_hits_nivel_1.png",
        target_level=3,
        figsize=(9, 12),
        x_offset=59,
        y_offset=9,
        hex_color='Reds',
        gridsize=(99, 155),
        extent=[0, 99, 0, 155],
    )

    # Nivel 2
    drawHexbinHeatmap(
        data_list=all_hits,
        background_image="bgNivel2.png",
        output_file=f"./HeatMaps/resultado_hits_nivel_2.png",
        target_level=4,
        figsize=(8, 16),
        x_offset=19,
        y_offset=(-58),
        hex_color='Reds',
        gridsize=(153, 337),
        extent=[0, 153, 0, 337]
    )

    # Nivel 3
    drawHexbinHeatmap(
        data_list=all_hits,
        background_image="bgNivel3.png",
        output_file=f"./HeatMaps/resultado_hits_nivel_3.png",
        target_level=5,
        figsize=(8, 16),
        x_offset=(-9),
        y_offset=(-60),
        hex_color='Greens',
        gridsize=(152, 303),
        extent=[0, 152, 0, 303]
    )