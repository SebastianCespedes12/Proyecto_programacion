def crear_matriz(n: int) -> list:
    # Crea una matriz n x n donde cada elemento es una cadena vacía
    return [["" for i in range(n)] for i in range(n)]

def filtrar_palabras(Todas:list,tamaño_mtr:int)->list: #Se añaden como parametros la lista de palabras y el tamaño de la matriz
  filtradas = []  #Se crea una lista vacia para guardar las palabras filtradas
  for i in Todas: #Se recorre la lista de palabras
    if len(i) <= tamaño_mtr: #Si la longitud de la palabra es menor o igual al tamaño de la matriz
      filtradas.append(i) #Se añade la palabra a la lista filtradas
  return filtradas 


