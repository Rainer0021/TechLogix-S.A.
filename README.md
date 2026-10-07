#Super User
user: Tech_Admin
clave: 123321
#ADMIN
user: Admin
clave: clave123321
#ASISTENTE
user: Asistente-A
clave: clave123321

## Historial de Prompts y Desarrollo del Proyecto

Ayudame a configurar la conexión a PostgreSQL alojada en Neon, utilizando el motor de base de datos de Django e inicialización de la aplicación principal del proyecto (`TechLogixAPP`).

Crea los modelos `Categoria` y `Producto` (con campos de SKU, precio, stock y fecha de ingreso), junto con su respectivo registro y personalización (`list_display`, `list_filter` y `search_fields`).

Desarrolla las vistas funcionales para el catálogo público con filtrado por categoría y búsqueda, y las operaciones CRUD protegidas para la gestión de inventario, implementando formularios seguros con validación de tokens CSRF y enrutamiento en `urls.py`.

Crea una plantilla base compartida (`base.html`) utilizando Bootstrap 5 para el diseño responsivo, separando los estilos personalizados en un archivo CSS independiente (`styles.css`) y estructurando las plantillas hijas para el inicio, catálogo y panel de administración.

Ayudame a configurar que al iniciar sesión **únicamente el Superusuario** sea redirigido al panel nativo (`/admin/`), mientras que los demás perfiles accedan al panel personalizado (`/admin_panel/`).

Ayudame a Ajustar el flujo de cierre de sesión para evitar redirecciones imprecisas y mantener al usuario dentro de la navegación de la aplicación.

Inserción de categorías y productos iniciales mediante la consola interactiva de Django (`python manage.py shell`) para poblar la base de datos de forma inmediata.