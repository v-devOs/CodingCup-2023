tElementos = int(input())
nOperaciones = int(input());


numIniciales = input();

arrNums = numIniciales.split(" ")
arrNums.sort()

for i in range( nOperaciones ):
  entrada = input()
  entradaSplited = entrada.split(" ")

  if(entradaSplited[0] == "2"):
    total = 0
    rangeMin = entradaSplited[1]
    rangeMax = entradaSplited[2]

    for a in arrNums:
      if( a >= rangeMin and a <= rangeMax ):
        total += 1
    
    print( total )
  else:
    if( arrNums.__contains__(entradaSplited[1]) == False):
      if( min(arrNums) < entradaSplited[1]):

        index = 0
        seInserto = False

        while( seInserto == False and index < arrNums.__len__()):
          if( arrNums[index] > entradaSplited[1]):
            arrNums[index] = entradaSplited[1]
            seInserto = True
          else:
            index += 1

        





