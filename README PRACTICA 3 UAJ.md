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

