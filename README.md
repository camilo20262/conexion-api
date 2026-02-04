# Proyecto Gemini API – Python

Este proyecto muestra cómo configurar un entorno virtual en Python y realizar una primera conexión con la API de **Gemini** utilizando variables de entorno para proteger credenciales sensibles.

---

## 📌 Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

* Python **3.9 o superior**
* Git (opcional, para clonar el repositorio)
* Acceso a una **API Key de Gemini**

Puedes verificar tu versión de Python con:

```bash
python --version
```

---

## 📂 Estructura del proyecto

```
GEMINI/
├── app_gemini.py          # Script principal de conexión con Gemini
├── prueba_entorno.py      # Script de verificación de entorno y conectividad
├── requirements.txt       # Dependencias del proyecto
├── .gitignore             # Archivos ignorados por Git
├── .env.example           # Ejemplo de variables de entorno
```

> ⚠️ El archivo `.env` y la carpeta `venv/` **no se suben al repositorio** por seguridad.

---

## ⚙️ Configuración del entorno virtual

### 1️⃣ Crear el entorno virtual

Desde la carpeta del proyecto, ejecuta:

```bash
python -m venv venv
```

### 2️⃣ Activar el entorno virtual

* **Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

* **Windows (CMD):**

```cmd
venv\Scripts\activate
```

* **Linux / macOS:**

```bash
source venv/bin/activate
```

Cuando el entorno esté activo, verás `(venv)` al inicio de la terminal.

---

## 📦 Instalación de dependencias

Con el entorno virtual activo, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración de variables de entorno

1️⃣ Crea un archivo `.env` a partir del ejemplo:

```bash
cp .env.example .env
```

2️⃣ Abre el archivo `.env` y agrega tu clave de Gemini:

```env
GEMINI_API_KEY=tu_api_key_aqui
```

---

## ▶️ Ejecución del proyecto

### Verificar el entorno virtual y la conexión a internet

```bash
python prueba_entorno.py
```

Salida esperada:

* Confirmación de entorno virtual activo
* Ruta del ejecutable de Python
* Conexión a internet exitosa

---

### Ejecutar la consulta a Gemini

```bash
python app_gemini.py
```

Salida esperada:

* Mensaje de conexión al motor Gemini
* Respuesta generada por el modelo

---

## 🧪 Notas importantes

* No compartas tu archivo `.env` ni tu API key
* Si el entorno falla, verifica que `(venv)` esté activo
* Para salir del entorno virtual:

```bash
deactivate
```

---

## 👨‍💻 Autor

Proyecto académico para prácticas de **Desarrollo de aplicaciones con IA**.

---

✅ Proyecto listo para ejecución y versionado en GitHub.
