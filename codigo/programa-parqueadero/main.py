
def msgOpcionEntradaoSalida():
    opcion = int(input('ingresar una opcion:\n1 - para ingresar un auto\n2 - para salida de auto\n3 - salir del programa\n:'))
    return opcion
    
def msgDespedido():
    msg = 'El sistema se cerro'
    return msg

def pedirDatosAuto():
    placa = input('ingresar placa del auto: ')
    horaEntrada = input('ingresar hora de entrada (formato: hh:mm): ')
    datosEntrada = (placa, horaEntrada) 
    return datosEntrada


def main():
    encendido = True
    while encendido:
        opcion = msgOpcionEntradaoSalida()

        if opcion == 1:
            datosEntrada = pedirDatosAuto()
            print(datosEntrada)
    
        if opcion == 3:
            encendido = False
            print(msgDespedido())


if __name__ == "__main__":
    main()