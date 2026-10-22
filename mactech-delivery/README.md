# MacTech IT — entregas de código fuente

## 0.13.0 build 22 — IT Custom

ZIP: `MacTechIT_0.13.0_Source.zip`; checksum SHA-256 adyacente.

IT Custom: editor de fuente/pruebas/notas, tres plantillas (SwiftUI, Codable, parser JSON), destinos iOS 15+/macOS 12+, revisión JSON, snippets propios con búsqueda/edición/copia/arrastre y exportación de biblioteca Swift para Xcode. No ejecuta código del usuario ni instala apps.

Robustez acotada: casos deterministas de host/nombre/proyecto JSON, máximo 5.000/3 s, informe JSON/notas. Captura de rendimiento de ESTA Mac reutiliza Runner existente, sin estrés continuo ni operaciones de dispositivos en pruebas.

PASS Linux: 44 scripts/82 comandos, fixtures de archivo/firmware previos, 27 archivos Swift generados inspeccionados, gramática de 16 Swift y 124 bloques. Compilación Swift, selftests, GUI/Xcode y DMG NO EJECUTADOS. No se entrega un DMG sin verificar.

Extraiga en carpeta nueva; lea AGENTS.md, docs/PROJECT_STATUS.md y docs/IT_CUSTOM.md. Compile en macOS con `/bin/bash Build_DMG.command`. El log debe indicar 0.13.0 build 22 y la ruta de esa carpeta.

Se conservan las entregas anteriores y sus checksums.
