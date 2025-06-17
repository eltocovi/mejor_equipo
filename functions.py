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
            telefono = int(input("ingrese su numero celular de 8 digitos"))
            if len(telefono) == 8: 
                telefonos.append(telefono)
                print("numero telefonico ingresado correctamente")
                break
            else:
                ("numero invalido")            
        except:
            print("el numero de telefono debe ser numerico")
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
    
     