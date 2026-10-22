# Soporte técnico Apple autorizado

## Triage y atribución

Registra síntoma, fuente, fecha, modelo/arquitectura/OS declarados o medidos y restricciones. Separa anfitrión/objetivo/simulador. No captures contraseñas, PIN, tokens, claves de recuperación ni contenido ajeno al caso. Usa identificadores reducidos en informes compartidos.

Consulta permisos y disponibilidad de cada proveedor. Ausente/desconocido no equivale a sano. No instales utilidades externas ni eleves privilegios de todo el módulo para una consulta puntual.

## macOS

Consultas nativas según versión/permisos: system_profiler, sw_vers, sysctl, ioreg, pmset, df, vm_stat, diskutil de lectura, fdesetup status, csrutil status, spctl, socketfilterfw, profiles status, scutil/networksetup, log y tmutil. Verifica paths/opciones contra man/ayuda del equipo; no inventes flags.

CPU/memoria/swap/almacenamiento/térmico corresponden al Mac que los ejecuta. No existe temperatura universal ni salud SSD remota garantizada. Estado MDM no autoriza retirarlo.

Red: destino autorizado, número de peticiones/paquetes y tiempo acotados. No escaneo de redes ni carga intensiva por defecto. Los logs pueden contener información privada.

## iPhone/iPad

Finder controla confianza, sincronización y respaldos. Compartir archivos sólo para apps compatibles; no ofrece acceso universal al disco. Cifrado de backup se configura en Finder y la contraseña se conserva fuera del informe.

IPA en una biblioteca no significa app instalable. App Store, Configurator o distribución administrada requieren firma, licencias y autorizaciones válidas. No prometas exportar apps protegidas o instalar cualquier IPA.

## Firmware y recuperación

- Recovery se ejecuta en el equipo objetivo; distinguir Apple silicon e Intel. Reinstalar sin borrar y borrar/reinstalar son decisiones distintas, con efecto explícito sobre datos.
- DFU/Revive/Restore dependen de modelo, puerto, cable y versión del anfitrión. Intel sin T2 no tiene el mismo flujo DFU de Apple silicon/T2.
- IPSW: manifiesto/hash detectan metadatos/integridad local, no autenticidad Apple ni firma vigente. Validar archivo/modelo y dejar firma/activación a la herramienta oficial. No fuerces imágenes no autorizadas.
- Restore borra; Revive no debe transformarse automáticamente en Restore. No hay bucles ilimitados ni reintentos destructivos encadenados.
- Activation Lock, iCloud y MDM: recuperación del titular/Apple o liberación autorizada por administrador/ABM/ASM. Restaurar no garantiza su retirada. No desarrollar bypass o ataques de credenciales.

## Operaciones con efectos

Borrado/formateo/APFS/cachés/desmontaje/restore requieren identificación del objetivo, autorización y respaldo/riesgo. Conserva guardas del disco anfitrión/interno y confirmación explícita. Bloqueos compartidos entre ventanas/procesos; no eliminarlos ni matar al propietario automáticamente. No ejecutar estas acciones sobre dispositivos reales durante pruebas de código.

Para robustez, usa fixtures locales, límites y resultados parciales. Un generador de entradas sintéticas no demuestra salud de hardware ni seguridad de código arbitrario.

## Expediente

Incluye alcance, evidencia de cada proveedor, hipótesis y cambios realizados, resultado confirmado o pendiente y siguiente paso. Diferencia notas del técnico, datos medidos y operaciones sólo guiadas. No certifiques sanitización, respaldo restaurable ni cierre de incidente sin su prueba correspondiente.
