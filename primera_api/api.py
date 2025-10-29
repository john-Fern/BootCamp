import requests

# 1️⃣ Enviar solicitud GET a una API pública
response = requests.get("https://randomuser.me/api/?results=1")

# 2️⃣ Convertir la respuesta a JSON (diccionario Python)
data = response.json()

# 3️⃣ Acceder a los datos
user = data["results"][0]
print("Nombre:", user["name"]["first"])
print("Apellido:", user["name"]["last"])
print("País:", user["location"]["country"])