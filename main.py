import menus 

def datos():
  #f = open("datos.txt")
  #print(f.read())
  #print("#######################")
  f = open("datos.txt")
  list=[linea.split() for linea in f]
  return list

#print(datos())

menus.menu_principal(datos())