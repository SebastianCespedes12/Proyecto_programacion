def verf_vacios_hor(A:list,x:int,y:int,d:int) ->bool: #Se añaden los parametros de la matriz, la fila, la columna y la longitud de la palabra
  Vacios = False  #Se asigna a Vacios el valor de False
  for i in range(y,y+d): #Se recorre la fila por la longitud de la palabra
    if A[x][i] != "": #Si la matriz en la fila x y la columna i es diferente de vacio
      Vacios=True  #Se asigna a Vacios el valor de True y se rompe el ciclo
      break
  return Vacios

def verf_vacios_ver(A:list,x:int,y:int,d:int)->bool:
  Vacios = False #Se asigna a Vacios el valor de False
  for i in range(x,x+d): #Se recorre la columna por la longitud de la palabra
    if A[i][y] != "": #Si la matriz en la fila i y la columna y es diferente de vacio
      Vacios=True  #Se asigna a Vacios el valor de True y se rompe el ciclo
      break
  return Vacios 