import json
import os
import pandas as pd
import matplotlib.pyplot as plt

def drawHexbinHeatmap(data_list, background_image, output_file, target_level, gridsize=(153, 337), extent=[0, 153, 0, 337]):
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

    # Proporción vertical (8x16 es buena para 153x337)
    fig, ax = plt.subplots(figsize=(8, 16)) 

    try:
        img = plt.imread(background_image)
        ax.imshow(img, extent=extent, aspect='auto')
    except Exception as e:
        print(f"Aviso: No se encontró {background_image}, generando mapa con fondo neutro.")

    # Dibujamos el mapa
    hb = ax.hexbin(
        x=(data["x"] + 19), 
        y=(data["y"] - 58),
        gridsize=gridsize,
        extent=extent,
        alpha=0.6,
        cmap='Reds',
        mincnt=1,
        linewidths=0.1
    )
    
    plt.colorbar(hb, ax=ax, label='Cantidad de Impactos')
    ax.set_title(f"Heatmap: Player Hits - Nivel {target_level}", fontsize=14)
    fig.savefig(output_file, dpi=600, bbox_inches='tight')
    print(f"¡Éxito! Imagen guardada como: {output_file}")

if __name__ == '__main__':
    folder_path = '../.././Assets/Sessions'
    all_hits = []
    # ID de la sesion para ponerla en el nombre del archivo
    ID_SESION = "desconocida"
    # Nivel a procesar
    ID_NIVEL_DESEADO = 4 

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
                        # Extraemos el sesID del primer evento que lo contenga (como sesStart)
                        if ID_SESION == "desconocida" and "sesID" in event:
                            ID_SESION = event["sesID"]
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
        background_image="bgNivel2.png",
        output_file=f"./HeatMaps/resultado_hits_nivel_2_{ID_SESION}.png",
        target_level=ID_NIVEL_DESEADO,
        gridsize=(153, 337),
        extent=[0, 153, 0, 337]
    )