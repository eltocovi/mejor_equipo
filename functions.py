def agregar(nombres, correos, telefonos):
    while True:
        nombre = input("ingrese un nombre\n") 
        if len(nombre)>2:
            nombres.append(nombre)
            print("nombre ingresado correctamente")
            break
        else:
            print("el nombre no cumple con los requisitos")
    while True:
        try:
            telefono = (input("ingrese su numero celular de 8 digitos \n"))
            if  len(telefono) == 8: 
                telefono = int(telefono)
                telefonos.append(telefono)
                print("numero telefonico ingresado correctamente")
                break
            else:
                ("numero invalido")            
        except:
            print("el numero de telefono debe ser numerico y de 8 digitos")
    while True:
        correo = input("ingrese su correo")
        if len(correo)>4 and "@" in correo:
            correos.append(correo)
            print("correo agregado correctamente")
            break
        else:
            print("correo invalido")           
            
def mostrar(nombres, correos, telefonos):
    if len(nombres)>0:
        for x in range(len(nombres)):
            print(f"{x+1}- nombre: {nombres[x]} correo: {correos[x]} telefono: {telefonos[x]}") 
    else:
        print("no hay nada en la lista")
        
def buscar_contacto(lista):
    if len(lista)>0:
        while True:
            nombre_buscar=input("Ingrese el nombre del contacto que desea buscar \n")
            if len(nombre_buscar)>2:
                for x,contacto in enumerate(lista):
                    if nombre_buscar in contacto: 
                       print(f"{x+1}- Nombre: {contacto}")
                break
            else:
                print("El nombre debe tener mas de 2 caracteres")
    else:
        print("No se encuentran contactos registrados")

def eliminar_contacto(lista):
    if len(lista)>0:
        for x,contacto in enumerate(lista):
            print(f"{x+1}- Nombre: {contacto}")
            
        while True:
            try:
                eliminar=int(input("Que numero de contacto desea eliminar?"))
                if eliminar>0 and eliminar<=len(lista):
                    lista.pop(eliminar-1)
                    break
                else:
                    print("Numero de contacto no encontrado")
            except:
                print("Debe ingresar un valor numerico")
    else:
        print("No se encuentran contactos registrados")
           
    
def main():
    contactos = []
    emails = []
    telefonos = []

    while True:
            print("\n--- Menú de Gestión de Contactos ---")
            print("1. Agregar un contacto")
            print("2. Listar contactos")
            print("3. Buscar un contacto por nombre")
            print("4. Eliminar un contacto")
            print("5. Salir del programa")
            print("------------------------------------")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                agregar(contactos, emails, telefonos)
                               
            elif opcion == '2':
                mostrar(contactos, emails, telefonos)
            elif opcion == '3':
                buscar_contacto(contactos)
            elif opcion == '4':
                eliminar_contacto(contactos)
            elif opcion == '5':
                print("Gracias por usar el programa, ¡Hasta luego!")
                break  
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

