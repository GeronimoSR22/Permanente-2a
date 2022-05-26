print ('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬           CONVERTIDOR DE PESOS, MEDIDAS y TEMPERATURA')
print ('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
print ('\n')
       
p = 'PESOS'
m = 'MEDIDAS'
t = 'TEMPERATURA'

print ("[p]",p,'\n','\n'"[m]",m,'\n','\n'"[t]",t,'\n')

x = input('Seleccione que desea convertir: ')
if x == 'p':
  print ('\n','▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬',p,'▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬','\n')
  kg = 'Kilogramos'
  g  = 'Gramos'
  mg = 'Miligramos'
  print ("[k]",kg,'\n','\n'"[g]",g,'\n','\n'"[m]",mg,'\n')
  Opcion_Peso1 = input('• Que unidad desea convertir: ')
  if Opcion_Peso1 == 'k':
    print ('\n')
    kilogramo = float(input("Ingrese el valor KG : ",))
    print ('\n')
    print ("[g]",g,'\n','\n'"[m]",mg,'\n')
    Opcion_Peso2 = input('a que unidad desea convetir: ')
    if Opcion_Peso2 == 'g':
      Convertidor_Kg_G = kilogramo * 1000
      print ('\n')
      print (kilogramo,"kg es equivalente a",Convertidor_Kg_G,"g")
    else:
      Convertidor_Kg_Mg = kilogramo * 1000000
      Opcion_Peso2 == 'mg'
      print ('\n')
      print (kilogramo,"kg es equivalente a",Convertidor_Kg_Mg,"mg")
  elif Opcion_Peso1 == 'g':
    print ('\n')
    gramo = float(input("Ingrese el valor G : ",))
    print ('\n')
    print ("[k]",kg,'\n','\n'"[m]",mg,'\n')
    Opcion_Peso2 = input('a que unidad desea convetir: ')
    if Opcion_Peso2 == 'k':
      Convertidor_G_Kg = gramo / 1000
      print ('\n')
      print (gramo,"g es equivalente a",Convertidor_G_Kg,"kg")
    else:
      Convertidor_G_Mg = gramo * 1000
      Opcion_Peso2 == 'mg'
      print ('\n')
      print (gramo,"g es equivalente a",Convertidor_G_Mg,"mg")
  else:
    Opcion_Peso1 == 'm'
    print ('\n')
    miligramo = float(input("Ingrese el valor Mg : ",))
    print ('\n')
    print ("[k]",kg,'\n','\n'"[g]",g,'\n')
    Opcion_Peso2 = input('a que unidad desea convetir: ')
    if Opcion_Peso2 == 'k':
      Convertidor_Mg_Kg = miligramo / 100000
      print ('\n')
      print (miligramo,"mg es equivalente a",Convertidor_Mg_Kg,"kg")
    else:
      Convertidor_Mg_G = miligramo / 1000
      Opcion_Peso2 == 'g'
      print ('\n')
      print (miligramo,"mg es equivalente a",Convertidor_Mg_G,"g")
elif x == 'm':
  print ('\n','▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬',m,'▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬','\n')
  km = 'Kilómetro'
  m  = 'Metro'
  cm = 'Centímetro'
  mm = 'Milímetro'
  print ("[k]",km,'\n','\n'"[m]",m,'\n','\n'"[c]",cm,'\n','\n'"[mm]",mm,'\n')
  Opcion_Medida1 = input('• Que unidad desea convertir: ')
  if Opcion_Medida1 == 'k':
    print ('\n')
    kilometro = float(input("Ingrese los kilómetros : ",))
    print ('\n')
    print ("[m]",m,'\n','\n'"[c]",cm,'\n','\n'"[mm]",mm,'\n')
    Opcion_Medida2 = input('a que unidad desea convetir: ')
    if Opcion_Medida2 == 'm':
      Convertidor_Km_M = kilometro * 1000    
      print ('\n')
      print (kilometro,"km es equivalente a",Convertidor_Km_M,"m")
    elif Opcion_Medida2 == 'c':
      Convertidor_Km_Cm = kilometro * 100000
      print ('\n')
      print (kilometro,"km es equivalente a",Convertidor_Km_Cm,"cm")
    else:
      Convertidor_Km_Mm = kilometro * 1000000
      Opcion_Medida2 == 'mm'
      print ('\n')
      print (kilometro,"km es equivalente a",Convertidor_Km_Mm,"mm")
  elif Opcion_Medida1 == 'm':
    print ('\n')
    metro = float(input("Ingrese los metros : ",))
    print ('\n')
    print ("[k]",km,'\n','\n'"[c]",cm,'\n','\n'"[mm]",mm,'\n')
    Opcion_Medida2 = input('a que unidad desea convetir: ')
    if Opcion_Medida2 == 'k':
      Convertidor_M_Km = metro / 1000
      print ('\n')
      print (metro,"m es equivalente a",Convertidor_M_Km,"km")
    elif Opcion_Medida2 == 'c':
      Convertidor_M_Cm = metro * 100
      print ('\n')
      print (metro,"m es equivalente a",Convertidor_M_Cm,"cm")
    else:
      Convertidor_M_Mm = metro * 1000
      Opcion_Medida2 == 'mm'
      print ('\n')
      print (metro,"m es equivalente a",Convertidor_M_Mm,"mm")
  elif Opcion_Medida1 == 'c':
    print ('\n')
    centimetro = float(input("Ingrese los centímetros : ",))
    print ('\n')
    print ("[k]",km,'\n','\n'"[m]",m,'\n','\n'"[mm]",mm,'\n')
    Opcion_Medida2 = input('a que unidad desea convetir: ')
    if Opcion_Medida2 == 'k':
      Convertidor_Cm_Km = centimetro / 100000
      print ('\n')
      print (centimetro,"cm es equivalente a",Convertidor_Cm_Km,"km")
    elif Opcion_Medida2 == 'm':
      Convertidor_Cm_M = centimetro / 100
      print ('\n')
      print (centimetro,"cm es equivalente a",Convertidor_Cm_M,"m")
    else:
      Convertidor_Cm_Mm = centimetro * 10
      Opcion_Medida2 == 'mm'
      print ('\n')
      print (centimetro,"cm es equivalente a",Convertidor_Cm_Mm,"mm")
  else:
    Opcion_Medida1 == 'mm'
    print ('\n')
    milimetro = float(input("Ingrese los milímetros : ",))
    print ('\n')
    print ("[k]",km,'\n','\n'"[m]",m,'\n','\n'"[c]",cm,'\n')
    Opcion_Medida2 = input('a que unidad desea convetir: ')
    if Opcion_Medida2 == 'k':
      Convertidor_Mm_Km = milimetro * 1000000
      print ('\n')
      print (milimetro,"mm es equivalente a",Convertidor_Mm_Km,"km")
    elif Opcion_Medida2 == 'm':
      Convertidor_Mm_M = milimetro / 1000
      print ('\n')
      print (milimetro,"mm es equivalente a",Convertidor_Mm_M,"m")
    else:
      Convertidor_Mm_Cm = milimetro / 10
      Opcion_Medida2 == 'c'
      print ('\n')
      print (milimetro,"mm es equivalente a",Convertidor_Mm_Cm,"cm")
else:
  x == 't'
  print ('\n','▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬',t,'▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬','\n')
  kv = 'Kelvin'
  cl = 'Celsius'
  fh = 'Fahrenheit'
  print ("[k]",kv,'\n','\n'"[c]",cl,'\n','\n'"[f]",fh,'\n')
  Opcion_Temp1 = input('• Que unidad desea convertir: ')
  if Opcion_Temp1 == 'k':
    print ('\n')
    kelvin = float(input("Ingrese la temperatura Kelvin : ",))
    print ('\n')
    print ("[c]",cl,'\n','\n'"[f]",fh,'\n')
    Opcion_Temp2 = input('a que unidad desea convetir: ')
    if Opcion_Temp2 == 'c':
      Convertidor_Kv_C = kelvin - 273.15
      print ('\n')
      print (kelvin,"grados kelvin es equivalente a",Convertidor_Kv_C,"grados celsius")
    else:
      Convertidor_Kv_Fh = (kelvin - 273.15)*9/5+32
      Opcion_Temp2 == 'f'
      print ('\n')
      print (kelvin,"grados kelvin es equivalente a",Convertidor_Kv_Fh,"grados fahrenheit")
  elif Opcion_Temp1 == 'c':
    print ('\n')
    celsius = float(input("Ingrese la temperatura Celsius : ",))
    print ('\n')
    print ("[k]",kv,'\n','\n'"[f]",fh,'\n')
    Opcion_Temp2 = input('a que unidad desea convetir: ')
    if Opcion_Temp2 == 'k':
      Convertidor_Cl_Kv = celsius + 273.15
      print ('\n')
      print (celsius,"grados celsius es equivalente a",Convertidor_Cl_Kv,"grados kelvin")
    else:
      Convertidor_Cl_Fh = (celsius * 9/5)+32
      Opcion_Temp2 == 'f'
      print ('\n')
      print (celsius,"grados celsius es equivalente a",Convertidor_Cl_Fh,"grados fahrenheit")
  else:
    Opcion_Temp1 == 'f'
    print ('\n')
    fahrenheit = float(input("Ingrese la temperatura Fahrenheit : ",))
    print ('\n')
    print ("[k]",kv,'\n','\n'"[c]",cl,'\n')
    Opcion_Temp2 = input('a que unidad desea convetir: ')
    if Opcion_Temp2 == 'k':
      Convertidor_Fh_Kv = (fahrenheit - 32)*5/9+273.15
      print ('\n')
      print (fahrenheit,"grados fahrenheit es equivalente a",Convertidor_Fh_Kv,"grados kelvin")
    else:
      Convertidor_Fh_Cl = (fahrenheit - 32)*5/9
      Opcion_Temp2 == 'c'
      print ('\n')
      print (fahrenheit,"grados fahrenheit es equivalente a",Convertidor_Fh_Cl,"grados celsius")