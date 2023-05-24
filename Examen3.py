salida = "{:>8s}REPORTE DE ANGULOS\n".format("");

salida += "{}{:>14s}{:>10s}\n".format('ANGULO', 'CUADRANTE', 'EJE')

casos = int(input('Digite los casos de prueba: '))


for i in range(casos):
    cuadrante = "---"
    eje = "---"
    
    angulo = int(input('Digite un angulo: '))

    if angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
        if angulo == 0:
            eje = "X+"
        elif angulo == 90:
            eje = "Y+"
        elif angulo == 180:
            eje = "X-"
        elif angulo == 270:
            eje = "Y-"
        else:
            eje = "X+"
    else:
        if angulo > 1 and angulo < 89:
            cuadrante = "I"
        elif angulo > 91 and angulo < 179:
            cuadrante = "II"
        elif angulo > 181 and angulo < 269:
            cuadrante = "III"
        else:
            cuadrante = "IV"
    
    salida += "{}{:>15s}{:>15s}\n".format(angulo, cuadrante, eje)

print(salida)

        

    