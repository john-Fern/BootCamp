contactos = []
contacto1 = {"nombre": "Ana", "telefono": "987654321", "correo": "ana@mail.com"}
contacto2 = {"nombre": "Luis", "telefono": "912345678", "correo": "luis@mail.com"}
contacto3 = {"nombre": "Sofía", "telefono": "998877665", "correo": "sofia@mail.com"}
contador = 1

contactos.append(contacto1)
contactos.append(contacto2)
contactos.append(contacto3)

print("=== Mis Contactos ===")
for i in contactos:
    print(f"{contador}. {i["nombre"]} - {i["telefono"]} - {i["correo"]}")
    contador += 1
contador = 1

tipo_contactos = ("amigos", "familia", "trabajo")
print(f"Tipos de contacto: {tipo_contactos}")

def agregar_contacto():
    contacto = {}
    contacto["nombre"] = input("Ingrese nombre: ")
    contacto["telefono"] = input("Ingrese numero: ")
    contacto["correo"] = input("Ingrese correo: ")

    contactos.append(contacto)

agregar_contacto()

for i in contactos:
    print(f"{contador}. {i["nombre"]} - {i["telefono"]} - {i["correo"]}")
    contador += 1

for i, contacto in enumerate(contactos, start=1):
    print(f"{i}. {contacto["nombre"]} - {contacto["telefono"]} - {contacto["correo"]}")