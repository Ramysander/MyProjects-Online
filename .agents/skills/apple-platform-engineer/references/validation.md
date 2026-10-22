# Build, validación y distribución

## Matriz de entorno

- macOS + Xcode/CLT: comprobar versión y SDK reales. Para simuladores/app iOS se requiere Xcode y runtime apropiado; CLT por sí solas no bastan.
- Linux/Windows: permite inspección y pruebas de Swift portátil si el compilador y las reglas del repo lo permiten. SwiftUI/AppKit/UIKit, SDK Apple, firma y DMG no quedan verificados allí.
- Dispositivos físicos: su uso debe estar autorizado; no son requisito implícito para verificar fuentes ni ejecutar tests puros.

## Comandos orientativos, no receta fija

Inspección en macOS, cuando haga falta:
```
xcodebuild -version
xcrun --find swiftc
xcrun --sdk macosx --show-sdk-path
xcodebuild -list -project RUTA.xcodeproj
xcrun simctl list devices available
```

Descubre scheme/configuration/destination reales antes de invocar build/test. Evita ejecutar por defecto scripts que instalen, borren, aprovisionen, conecten dispositivos o requieran licencia/credenciales. Usa la receta del repositorio si existe; no sustituyas un build integrado por un swiftc que omite recursos.

Para SwiftPM: `swift build`/`swift test` desde la raíz adecuada sólo si plataforma y reglas lo permiten. Para Xcode: `xcodebuild ... build/test` con scheme y destino explícitos, salidas aisladas y resultado/xcresult de la corrida actual. Ejecuta tests sin hardware con simuladores cuando corresponda.

## Evidencia

Distingue PASSED/FAILED/SKIPPED/EXPECTED FAILURE/NOT RUN. Comprueba conteo y target: cero tests no valida el comportamiento. Conserva exit status al capturar salida. Ante fallo, diagnostica primero y cambia una causa, no repitas ciegamente.

Incluye regresiones de datos/rutas/serialización/compatibilidad y errores cuando son relevantes. Para generadores, compila un resultado representativo; si no puedes, declara que sólo comprobaste su gramática/estructura.

## Firma y distribución

- Bundle ID, versión/build, entitlements y permisos TCC coherentes. No inventes capacidades ni permisos de sandbox.
- iOS: desarrollo/simulador/TestFlight/App Store/MDM son rutas distintas. Firma y aprovisionamiento deben corresponder al equipo y distribución autorizados. No extraigas claves ni pidas contraseñas en chat.
- macOS: ad hoc para pruebas locales no es Developer ID ni notarización. Usa el flujo del repo, verifica firma, arquitecturas y recursos. Hardened runtime/entitlements conforme al producto, no para desactivar validaciones.
- Antes de declarar una entrega notarizada, verifica respuesta/ticket mediante herramientas Apple disponibles. Credenciales en Keychain/configuración segura, nunca fuente/logs/ZIP.
- DMG: sólo generarlo en macOS con herramientas adecuadas; `hdiutil verify`, checksum y app verificada. No montar ni desmontar unidades reales como prueba del constructor.
- Publicar/subir no está implícito en compilar; comprueba autorización previa aplicable y privacidad del destino.

El informe final debe decir qué se ejecutó en qué entorno y qué queda pendiente, sin llamar a una sintaxis válida una aplicación funcional.
