def añadir_palabra_horz(A:list,s:str,fila:int,columna:int)->list: #Se añaden como parametros la matriz, la palabra, la fila y la columna
    i = fila #Se asigna a i el valor de la fila, ya que la fila no cambia
    for k in range(columna,columna + len(s)):  #Se recorre la palabra y la fila.
        A[i][k] = s[k-columna] #Se asigna a la matriz la letra de la palabra en la posicion k-columna
    return A

def añadir_palabra_ver(A:list,s:str,fila:int,columna:int)->list:
  i = columna #Se asigna a i el valor de la columna, ya que la columna no cambia
  for k in range(fila,fila + len(s)):  #Se recorre la palabra y la columna.
    A[k][i] = s[k - fila] #Se asigna a la matriz la letra de la palabra en la posicion k-fila
  return A  