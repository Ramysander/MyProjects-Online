# MacTech IT — entregas de código fuente

## 0.12.0 build 21 — Centro de dispositivos y biblioteca

ZIP: `MacTechIT_0.12.0_Source.zip`; checksum en el .sha256 adyacente.

Biblioteca local para vídeos, música, aplicaciones empaquetadas, documentos, firmware IPSW y carpetas de respaldos. Importar/exportar copias sin sobrescribir; SHA-256 incremental. IPSW con metadatos BuildManifest, filtro por versión/build/modelos y apertura de restauración oficial supervisada en Finder. No flashea automáticamente ni comprueba firma Apple en vivo. Copias iOS y transferencias reales dependen de Finder, confianza, apps compatibles y permisos; no sustituye todo iTunes ni instala IPA arbitrarios.

Datos en Documents/MacTech IT Library, separados de MobileSync. No se certifica cifrado/restaurabilidad del respaldo archivado.

PASS Linux: 44 scripts, 82 snippets, archivos/manifest/hash sintéticos, integración y gramática de 13 Swift/102 bloques. Swift, GUI, dispositivos, firmas y DMG NO EJECUTADOS. No se incluye firmware real ni datos de clientes ni un DMG no verificado.

Extraiga en carpeta nueva; lea AGENTS.md, docs/PROJECT_STATUS.md y docs/DEVICE_SERVICE.md. Compile en macOS con `/bin/bash Build_DMG.command`.

Se conservan las entregas 0.11.1 (build 20), 0.11.0 y 0.10.0 y sus checksums.
