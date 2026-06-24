# Practica 3 Usabilidad y Análisis de videojuegos

## Autores
- Julián Serrano Chacón  
- Jiale He
- Jose Antonio Carmona Alfonsel
- Javier Alonso Ruiz  
- Pablo Marcos Serrano  
- Luis Javier Navarrete Pulupa

## Información general del repositorio

En este Repositorio tenemos la practica 3 entera, Para la parte de analisis y Métricas tenemos todos lo códigos y componentes en la carpeta Analisis.

Dentro de la carpeta Analisis tenemos los documentos del diseño de la evaluación
y Resultados y Conclusiones, ambos en formato pdf, además de la carpeta 
HeatMapsYMetricas en donde se pueden crear graficos de heatmaps 
y metricas ejecutando el archivo doMetrics.bat los cuales se crearan en 
sus respectivas carpeta (Metricas y HeatMaps)

## Como procesar los datos en el analisis

Los datos de telemetría se almacenarán en este directorio: "C:\Users\Usuario\AppData\LocalLow\RetroGames Studios\El Custodio de Babel\Datos_Telemetria"

Para procesar los datos debemos coger los .json del directorio antes mencionado y pasarlos a la carpeta de "datos_entrada" dentro de la carpeta de "Analisis", en la raíz.

## Contexto
La práctica se ha realizado sobre el juego creado para proyectos 1 [El custodio de Babel](https://github.com/Proyectos1-FDI-UCM/c2223-Grupo01), es un juego de plataformas que recuerda a los Mega Man originales.

## Tracking

### Manejo de eventos

### [Tracker](./Assets/Scripts/Tracking/Tracker.cs)

Clase Manager del sistema de telemetría.

### [CirculaQueue](./Assets/Scripts/Tracking/CircularQueue.cs)
Implementación en c# del TAD de cola circular para el manejo de eventos.

### [Tracker Event (clase padre)](./Assets/Scripts/Tracking/TrackerEvent.cs)
Clase Padre que contiene información compartida por todos los eventos (hios de esta clase).

### [Eventos](./Assets/Scripts/Tracking/Eventos)

- [Sesion Start](./Assets/Scripts/Tracking/Eventos/Sesion/SesionStart.cs)
- [Sesion End](./Assets/Scripts/Tracking/Eventos/Sesion/SesionEnd.cs)
- [PlayerCheckPoint](./Assets/Scripts/Tracking/Eventos/PlayerCheckPoint.cs)
- [PlayerDeath](./Assets/Scripts/Tracking/Eventos/PlayerDeath.cs)
- [Player End](./Assets/Scripts/Tracking/Eventos/PlayerEnd.cs)
- [Player Healing](./Assets/Scripts/Tracking/Eventos/PlayerHealing.cs)
- [PlayerHit](./Assets/Scripts/Tracking/Eventos/PlayerHit.cs)
- [EnemyBulletHit](./Assets/Scripts/Tracking/Eventos/Precision/EnemyBulletHit.cs)
- [EnemyMeleeHit](./Assets/Scripts/Tracking/Eventos/Precision/EnemyMeleeHit.cs)
- [PlayerMelee](./Assets/Scripts/Tracking/Eventos/Precision/PlayerMelee.cs)
- [Player Shoot](./Assets/Scripts/Tracking/Eventos/Precision/PlayerShoot.cs)

### Serializacion

### [ISerializer](./Assets/Scripts/Tracking/Serializacion/ISerializer.cs)
Clase padre del resto de serializadores diseñada para que se pueda implementar el patrón command el cual usa el polimorfismo para poder escalar fácilmente creando la posibiliadad de añadir nuevos formatos de serialización cómodamente.

### [JSonSerializer](./Assets/Scripts/Tracking/Serializacion/JsonSerializer.cs)
Clase que serializa los eventos a Json llamando a la funcion ToJson de los eventos (se autoserializan).


### Persistencia

### [IPersistance](./Assets/Scripts/Tracking/Persistance/IPersistance.cs)

Clase padre del resto de tipos de persistencia del sistema de telemetría que gracias al patrón Command, se puede añadir nuevos formatos de persistencia fácilmente.

### [FilePersistance](./Assets/Scripts/Tracking/Persistance/FilePersistance.cs)

Clase que se encarga la implemetación del metodo Flush() de la clase IPersistance para volcar todos los datos de telemetría al disco del ordenador.

### [ServerPersistance](./Assets/Scripts/Tracking/Persistance/ServerPersistance.cs)

Clase que se encarga la implemetación del metodo Flush() de la clase IPersistance para volcar todos los datos de telemetría a un servidor en la red (No implementado, pero con opción de implementar a futuro).


