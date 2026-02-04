import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# Validación básica de la API key
if not clave_api:
    raise ValueError("❌ No se encontró la variable de entorno GEMINI_API_KEY")

# 2. Inicializar el Cliente
client = genai.Client(api_key=clave_api)


def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")

    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=(
                "hola como estas "
                
            )
        )

        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")

    except Exception as e:
        print(f"❌ Error durante la consulta: {e}")


if __name__ == "__main__":
    ejecutar_consulta()
# Nota: Asegúrate de tener instaladas las dependencias necesarias:
# pip install google-genai python-dotenv