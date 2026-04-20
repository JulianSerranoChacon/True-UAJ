import json
import os
import pandas as pd
import matplotlib.pyplot as plt

def drawHexbinHeatmap(data_list, background_image, output_file, target_level, gridsize=(152, 303), extent=[0, 152, 0, 303]):
    if not data_list:
        print(f"Error: No hay datos para procesar.")
        return

    df = pd.DataFrame(data_list)
    data = df[df['levelID'] == target_level]

    if data.empty:
        print(f"Aviso: No se encontraron impactos (hits) para el Level ID: {target_level}")
        return

    fig, ax = plt.subplots(figsize=(8, 16)) 

    try:
        img = plt.imread(background_image)
        ax.imshow(img, extent=extent, aspect='auto')
    except Exception as e:
        print(f"Aviso: No se encontró {background_image}")

    # CAMBIOS AQUÍ: Offset de X a 30, Y a -15 y mantenemos Greens
    hb = ax.hexbin(
        x=(data["x"] - 9), 
        y=(data["y"] - 60), 
        gridsize=gridsize,
        extent=extent,
        cmap='Greens',
        mincnt=1,
        alpha=0.7
    )

    # BLOQUE FINAL ORIGINAL (INTACTO)
    cb = fig.colorbar(hb, ax=ax)
    cb.set_label('Número de Impactos')
    ax.set_title(f'Heatmap de Impactos Recibidos - Nivel {target_level}')
    
    plt.savefig(output_file, dpi=600, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    folder_path = '../.././Assets/Sessions'
    all_hits = []
    # Nivel a procesar
    ID_NIVEL_DESEADO = 5 

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
    drawHexbinHeatmap(
        data_list=all_hits,
        background_image="bgNivel3.png",
        output_file=f"./HeatMaps/resultado_hits_nivel_3.png",
        target_level=ID_NIVEL_DESEADO,
        gridsize=(152, 303),
        extent=[0, 152, 0, 303]
    )