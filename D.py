def main():
  entradaIni = input()

  tDatos = entradaIni.split(" ")[0]
  tope = int( entradaIni.split(" ")[1])

  numsIni = input().split(" ")
  arrNums = []

  for a in numsIni:
    arrNums.append( int(a) )

  arrNums.sort()

  for i in range(tope):
    op = input().split(" ")

    if op[0] == "2":
      total = 0
      rangeMin =int( op[1])
      rangeMax =int( op[2])
      
      for a in arrNums:
        if( a >= rangeMin and a <= rangeMax ):
          total += 1

      print(total)
    elif( op[0] == "1"):
      numAdd = int(op[1])

      if( min(arrNums) < numAdd ):

        index = 0
        seAgrego = False

        while index < arrNums.__len__() and seAgrego == False:
          if( arrNums[index] > numAdd ):
            seAgrego = True
            arrNums[index] = numAdd
          else:
            index += 1


if __name__ == "__main__":
  main()