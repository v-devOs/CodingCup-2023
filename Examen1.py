
salida = "{:>43s}AUTOS LINCE \n{:>40s}REPORTE MENSUAL\n".format("","")

salida = salida + "{}{:>20s}{:>30s}{:>20s}{:>25s}\n".format("NOMBRE", "CODIGO", "TOTAL VENTAS($)" , "COMISION($)", "COMISION A PAGAR")
totalVendedores = int(input("Ingrese el numero de vendedores: "))

ventasVenCod1 = 0
ventasVenCod2 = 0

for i in range( totalVendedores ):
  comision = 0
  comisionPagar = 0
  
  nombre = input("Ingrese el nombre del vendedor: ")
  codigo = input("Ingrese el codigo del vendedor: ")
  ventas = float(input("Ingrese el total de ventas del vendedor: "))


  if( codigo == "1"):
    ventasVenCod1 += ventas
    comision = ventas * 0.03
    if( comision > 10000):
      comisionPagar = comision
  elif( codigo == "2"):
    ventasVenCod2 += ventas
    comision = ventas * 0.05
    if( comision > 7500):
      comisionPagar = comision
  

  salida += "{}{:>20s}{:32f}{:22f}{:22f}\n".format(nombre, codigo, ventas, comision,comisionPagar)

salida += "\nTOTAL VENTAS VENDEDORES 1 ${}\nTOTAL VENTAS VENDEDORES 2 ${}".format(ventasVenCod1, ventasVenCod2)

print(salida)
