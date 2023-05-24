import math

costoAlmace = 0.05 * 12

# con math.sqrt calculamos la raiz cuadrada de un numero
l1 = math.sqrt( (2*20000/1) * (300/costoAlmace))
nLotes1 = 20000/l1
t1 = (365*l1)/20000


numCasos = int(input( "Digite el numero de casos: "))
aux = 0

while aux < numCasos:

  demandaAnual2 = int(input("Ingrese la demanda anual: "))
  costoPrepaLote = int(input("Ingrese el costo de preparacion por lote: "))

  l2 = math.sqrt( (2*demandaAnual2/ 1) * (costoPrepaLote/costoAlmace) )
  t2 = (365*l2)/demandaAnual2

  nLotes2 = demandaAnual2/l1

  if( l1 > l2 ):
    print("La segunda propuesta es mas barata con cargas de {} litros cada {} dias".format(nLotes2, t2))
  else:
    print("La primer propuesta es mas barata con cargas de {} litros cada {} dias".format(nLotes1, t1))

  
  aux += 1
