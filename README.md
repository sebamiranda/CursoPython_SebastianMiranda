# 🐍 Django REST API - Curso Python

API RESTful desarrollada con **Django** y **Django REST Framework** como proyecto de práctica y aprendizaje. Implementa las mejores prácticas de desarrollo backend con Python.

## 🚀 Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación
- **Django 4.x** - Framework web
- **Django REST Framework** - Toolkit para APIs REST
- **SQLite / PostgreSQL** - Base de datos
- **pip** - Gestor de paquetes

## ✨ Características

- ✅ **API RESTful** - Endpoints siguiendo principios REST
- ✅ **CRUD completo** - Operaciones Create, Read, Update, Delete
- ✅ **Serialización de datos** - Django REST Framework serializers
- ✅ **ORM de Django** - Gestión de base de datos
- ✅ **Validación de datos** - Validadores integrados
- ✅ **Paginación** - Manejo eficiente de grandes conjuntos de datos
- ✅ **Documentación automática** - Browsable API

## 🏗️ Estructura del Proyecto

```
CursoPython_SebastianMiranda/
├── api/                    # Aplicación principal
│   ├── migrations/         # Migraciones de base de datos
│   ├── models.py          # Modelos de datos
│   ├── serializers.py     # Serializadores DRF
│   ├── views.py           # Vistas/Controladores
│   ├── urls.py            # Rutas de la API
│   └── admin.py           # Panel de administración
├── proyecto/              # Configuración del proyecto
│   ├── settings.py        # Configuración Django
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # WSGI para deployment
├── manage.py              # Script de gestión Django
├── requirements.txt       # Dependencias Python
└── README.md
```

## 📡 API Endpoints

### Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/` | Lista de recursos |
| `GET` | `/api/{id}/` | Obtener recurso por ID |
| `POST` | `/api/` | Crear nuevo recurso |
| `PUT` | `/api/{id}/` | Actualizar recurso completo |
| `PATCH` | `/api/{id}/` | Actualizar recurso parcial |
| `DELETE` | `/api/{id}/` | Eliminar recurso |

### Ejemplo de Request (POST)

```bash
curl -X POST http://localhost:8000/api/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Ejemplo",
    "descripcion": "Descripción del recurso"
  }'
```

### Ejemplo de Response

```json
{
  "id": 1,
  "nombre": "Ejemplo",
  "descripcion": "Descripción del recurso",
  "fecha_creacion": "2024-10-07T10:30:00Z",
  "fecha_actualizacion": "2024-10-07T10:30:00Z"
}
```

---

## 🔧 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes)
- Virtualenv (recomendado)

### 1. Clonar el repositorio

```bash
git clone https://github.com/sebamiranda/CursoPython_SebastianMiranda.git
cd CursoPython_SebastianMiranda
```

### 2. Crear entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### 6. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

La API estará disponible en: **http://localhost:8000**

Panel de administración: **http://localhost:8000/admin**

---



### Probar la API con cURL

```bash
# Listar todos los recursos
curl http://localhost:8000/api/

# Obtener recurso específico
curl http://localhost:8000/api/1/

# Crear nuevo recurso
curl -X POST http://localhost:8000/api/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Test", "descripcion": "Prueba"}'

# Actualizar recurso
curl -X PUT http://localhost:8000/api/1/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Actualizado", "descripcion": "Nueva descripción"}'

# Eliminar recurso
curl -X DELETE http://localhost:8000/api/1/
```

---

## 📚 Django REST Framework - Browsable API

Django REST Framework proporciona una interfaz web interactiva para explorar la API:

1. Navega a http://localhost:8000/api/
2. Explora los endpoints disponibles
3. Prueba requests directamente desde el navegador
4. Visualiza respuestas formateadas

---

## 🔐 Configuración de Base de Datos

### SQLite (Desarrollo - Por defecto)

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### PostgreSQL (Producción)

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📦 Dependencias Principales

```
Django>=4.0
djangorestframework>=3.14
django-cors-headers>=3.13
python-decouple>=3.6
```

---

## 🛠️ Comandos Útiles

```bash
# Crear nueva aplicación
python manage.py startapp nombre_app

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar shell de Django
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic

# Ejecutar servidor
python manage.py runserver

# Ejecutar en puerto específico
python manage.py runserver 8080
```

---

## 🚀 Deploy en Producción

### Variables de Entorno

Crea un archivo `.env`:

```env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_URL=postgresql://usuario:password@localhost:5432/dbname
```

### Deploy en Heroku

```bash
# Instalar Heroku CLI y login
heroku login

# Crear aplicación
heroku create nombre-app

# Agregar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main

# Migrar base de datos
heroku run python manage.py migrate

# Crear superusuario
heroku run python manage.py createsuperuser
```

### Deploy en Railway / Render

1. Conecta tu repositorio GitHub
2. Configura las variables de entorno
3. Railway/Render detectará automáticamente Django
4. Deploy automático en cada push

---

## 📖 Recursos de Aprendizaje

Este proyecto fue desarrollado como parte de un curso de Python/Django e incluye:

- Implementación de API REST con Django REST Framework
- Patrones de diseño MVC
- Serialización y deserialización de datos
- Validación de modelos
- Gestión de base de datos con ORM
- Buenas prácticas de desarrollo Django

---

## 🔄 Próximas Mejoras

- [ ] Implementar autenticación JWT
- [ ] Agregar tests unitarios y de integración
- [ ] Documentación con Swagger/OpenAPI
- [ ] Sistema de permisos y roles
- [ ] Filtros y búsqueda avanzada
- [ ] Paginación customizada
- [ ] Caché con Redis
- [ ] Rate limiting
- [ ] Versionado de API
- [ ] Dockerización del proyecto

---

## 📝 Aprendizajes del Proyecto

- Desarrollo de APIs REST con Django
- Django REST Framework y serializers
- Modelos y migraciones de Django
- ORM y queries a base de datos
- Validación y manejo de errores
- Panel de administración de Django
- Buenas prácticas en Python

---

## 👨‍💻 Autor

**Sebastián Miranda**
- GitHub: [@sebamiranda](https://github.com/sebamiranda)
- LinkedIn: [https://www.linkedin.com/in/sebastian-miranda-/]

---



⭐ **Si este proyecto te sirvió de referencia para aprender Django, dale una estrella!**
