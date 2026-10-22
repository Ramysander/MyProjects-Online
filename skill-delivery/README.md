# Apple Platform Engineer — skill v1 (2026-10-22)

Skill especializado en Swift/SwiftUI/AppKit/UIKit, proyectos y paquetes, concurrencia, pruebas, distribución y soporte técnico Apple autorizado.

## Archivos
- Fuente en `.agents/skills/apple-platform-engineer/` del repositorio.
- Paquete instalable: `apple-platform-engineer.zip`.
- Integridad: `apple-platform-engineer.zip.sha256`.

## Instalar en tu Mac con Codex que admita skills locales
1. Descarga el ZIP desde GitHub y descomprímelo.
2. Copia la carpeta completa `apple-platform-engineer` dentro de `~/.agents/skills/` para uso personal, o en `.agents/skills/` dentro de un proyecto para uso por repositorio. No copies sólo SKILL.md; conserva referencias y scripts.
3. Si ya existe una versión, conserva una copia y revisa las diferencias antes de sustituirla.
4. Abre una nueva sesión o recarga los skills según tu cliente y comprueba que aparezca el nombre.

La copia en este repositorio no instala el skill en otro equipo. Tampoco lo registra en el catálogo de skills de nube; ese servicio necesita su mecanismo de instalación/publicación, si lo ofrece. No se afirma activación en esta conversación.

## Invocación

```
Usa $apple-platform-engineer. Lee AGENTS.md y PROJECT_STATUS.md,
confirma carpeta/versión y continúa la implementación SwiftUI.
Ejecuta las verificaciones compatibles con el entorno y no operaciones
sobre dispositivos reales durante las pruebas.
```

Ejemplos: crear biblioteca SwiftPM, implementar pantalla iOS/macOS, resolver un fallo de Xcode/SwiftUI, revisar concurrencia, preparar firma/DMG o diagnosticar un caso de soporte con evidencia del anfitrión/objetivo.

## Preflight opcional

Desde la carpeta del skill:

```
python3 scripts/apple_preflight.py --root /ruta/al/proyecto
```

Inspecciona archivos principales, proyectos Xcode de primer nivel y herramientas disponibles en PATH. No ejecuta versiones, builds, red ni consultas de dispositivos. No garantiza SDK, licencia, aprovisionamiento, simuladores ni firma.

## Validación realizada
Frontmatter y metadatos YAML, enlaces relativos, compilación sintáctica Python, preflight sobre MacTech IT y pruebas con fixtures de raíz vacía, SwiftPM/Xcode y rutas inválidas. ZIP y contenido exacto verificados. No se ha evaluado calidad de ejecución del skill en una sesión macOS/Xcode ni registrado el paquete en nube.
