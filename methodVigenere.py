# CIFRADO DE VIGENERE BY BALTO

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
mensaje = input("Ingresa el mensaje: ").upper()
clave = input("Ingrese la clave: ").upper()
aux = 0
dif = 0
addClave = ""
newClave = ""


def descifrar(cifrado, clave):
    encryp = cifrado
    key = clave
    ite = 0
    descifrado = ""
    while ite < len(encryp):
        Ci = alfabeto.index(encryp[ite])
        Ki = alfabeto.index(key[ite])
        Mi = (Ci - Ki) % len(alfabeto)
        descifrado += alfabeto[Mi]
        ite += 1
    return descifrado


def cifrar(mensaje, clave):
    msj = mensaje
    key = clave
    ite = 0
    cifrado = ""
    while ite < len(msj):
        Mi = alfabeto.index(msj[ite])
        Ki = alfabeto.index(key[ite])
        Ci = (Mi + Ki) % len(alfabeto)
        cifrado += alfabeto[Ci]
        ite += 1
    return cifrado


if len(mensaje) != len(clave):
    dif = len(mensaje) - len(clave)
    while aux < dif:
        addClave += clave[aux]
        aux += 1
        if aux >= len(clave):
            aux = 0

        if len(addClave) == len(mensaje):
            aux = dif

    newClave = clave + addClave
    cifrar(mensaje, newClave)
    textoCifrado = cifrar(mensaje, newClave)
    textoDescifrado = descifrar(textoCifrado, newClave)
    print(textoCifrado)
    print(textoDescifrado)
else:
    textoCifrado = cifrar(mensaje, clave)
    textoDescifrado = descifrar(textoCifrado, clave)

    print(textoCifrado)
    print(textoDescifrado)
