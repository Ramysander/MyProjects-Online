# Desarrollo de proyectos Apple

## Crear un proyecto

1. Define app/biblioteca/CLI/extensión, usuarios, datos, plataformas, versiones mínimas y distribución. Infiere de contexto; pregunta por ambigüedad decisiva.
2. Para biblioteca, usa SwiftPM y un `swift-tools-version` compatible; productos/targets/dependencias explícitos y lockfile cuando aplique. Para app iOS/macOS, utiliza el mecanismo Xcode ya adoptado o herramientas de generación presentes en el repo. No añadas generadores externos sin necesidad.
3. Separa dominio puro, persistencia/red/procesos e interfaz. Dependencias mínimas, justificadas y fijadas según el proyecto.
4. Incluye una función vertical útil con estados vacío/cargando/error, accesibilidad, datos de prueba y pruebas de comportamiento. No crees scaffolding como sustituto de la función pedida.
5. Asegura integración de archivos nuevos en targets, Copy Bundle Resources, build phases/scripts y empaquetado. Distingue referencia a archivo y pertenencia al target.

## SwiftUI/AppKit/UIKit

- Divide vistas extensas, filas y modificadores; no anides búsquedas, ternarios y filtros complejos dentro de Text/ForEach.
- ViewBuilder de SDK antiguos admite hasta diez componentes directos; no supongas que herramientas nuevas eliminan límites en el SDK del usuario.
- Para macOS 12/iOS 15: ObservableObject/Published/StateObject son la base habitual. Observation y SwiftData exigen versiones más nuevas; usa alternativas o disponibilidad explícita.
- StateObject mantiene un modelo propio; ObservedObject observa uno compartido. Evita crear un segundo Runner para resolver una dependencia de una sheet.
- Gestiona selección oculta al filtrar, borradores sin guardar y cambios de contexto que invalidan confirmaciones. Deshabilita acciones por causa concreta y muestra el motivo.
- Usa navegación, teclado, VoiceOver, Dynamic Type y contraste según plataforma. Una captura no demuestra comportamiento de accesibilidad.

## Concurrencia y procesos

- Captura una instantánea de datos antes de iniciar tareas; no leas/mutes estado observable desde múltiples hilos sin aislamiento.
- En migración Swift 6, resuelve capturas Sendable y límites de actores; no suprimas comprobaciones globalmente.
- Para tareas externas: binarios conocidos, argumentos separados, stdin no interactivo salvo flujo Terminal autorizado, pipes drenados, cancelación/timeout y exit status real.
- Un PID, puerto abierto o `open Finder` no acredita que una operación terminó. No confundas tiempo de apertura con tiempo de transferencia/restauración.

## Archivos, snippets y plugins

- Valida nombres de módulo con reglas cerradas; rechaza traversals, controles y nombres reservados. Los nombres introducidos no deben convertirse en Swift/shell arbitrario dentro de manifests.
- Rechaza enlaces o escapes de raíz según la política del módulo. Acota JSON/plist/ZIP y evita ZIP Slip/descompresión excesiva.
- No combines `Data.WritingOptions.atomic` y `withoutOverwriting`; usa staging + publicación cuando necesites integridad del conjunto y no sobrescritura.
- Texto de snippets no equivale a una acción segura. Para comandos parametrizados, valida tipos y cita argumentos. Expande sólo tokens de la plantilla original, no del input introducido.
- Copy/drag no añade Enter ni salto final a comandos Shell. El código Swift multilínea se destina a un editor, no a Terminal.
- Distingue revisión estructural, compilación y aprobación humana. No cargues plugins ni ejecutes código al importar archivos.
