import random  

def crear_matriz(n: int) -> list:
    # Crea una matriz n x n donde cada elemento es una cadena vacía
    return [["" for i in range(n)] for i in range(n)]

def filtrar_palabras(Todas:list,tamaño_mtr:int)->list: #Se añaden como parametros la lista de palabras y el tamaño de la matriz
  filtradas = []  #Se crea una lista vacia para guardar las palabras filtradas
  for i in Todas: #Se recorre la lista de palabras
    if len(i) <= tamaño_mtr: #Si la longitud de la palabra es menor o igual al tamaño de la matriz
      filtradas.append(i) #Se añade la palabra a la lista filtradas
  return filtradas 

def verf_vacios_hor(A:list,x:int,y:int,d:int) ->bool:
  Vacios = False
  for i in range(y,y+d):
    if A[x][i] != "":
      Vacios=True  
      break
  return Vacios

def verf_vacios_ver(A:list,x:int,y:int,d:int)->bool:
  Vacios = False
  for i in range(x,x+d):
    if A[i][y] != "":
      Vacios=True  
      break
  return Vacios  

def verf_vacios_diag(A:list,x:int,y:int,d:int)->bool:
  Vacios = False
  for i in range(x,x+d):
    for j in range(y,y+d):
      if i-j == x-y:
        if A[i][j] != "":
          Vacios=True
          break
  return Vacios

def añadir_palabra_horz(A:list,s:str,fila:int,columna:int)->list:
    i = fila
    for k in range(columna,columna + len(s)):             
        A[i][k] = s[k-columna]
    return A

def añadir_palabra_ver(A:list,s:str,fila:int,columna:int)->list:
  i = columna
  for k in range(fila,fila + len(s)):             
    A[k][i] = s[k - fila]
  return A  

def añadir_palabra_diag(A:list,s:str,fila:int,columna:int)->list:
  for i in range(fila,fila+len(s)):
    for j in range(columna,columna+len(s)):
      if i-j==fila-columna:
        A[i][j]=s.upper()[i-fila]
  return A

def palabra_horizontal(A:list,tamaño_mtr:int,palabras:int,filtradas:list,dentro:list):
  coordenada_x = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada x aleatoria
  coordenada_y = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada y aleatoria

  distancia_x = tamaño_mtr - coordenada_y  #Se calcula la distancia en x hasta el final de la fila
  N_letras = random.randint(3,distancia_x) #Se selecciona un numero aleatorio de letras entre 3 y la distancia en x
  Vacio = verf_vacios_hor(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra
    
  if Vacio == False: #Si hay espacio:
    Palabra_seleccionada = random.choice(filtradas) #Se selecciona una palabra aleatoria
    if len(Palabra_seleccionada) == N_letras:  #Si la longitud de la palabra seleccionada es igual a un numero aleatorio N_letras
      dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
      filtradas.remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
      añadir_palabra_horz(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna  
      palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz
  return A, palabras, filtradas, dentro

def palabra_vertical(A:list,tamaño_mtr:int,palabras:int,filtradas:list,dentro:list):
  coordenada_x = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada x aleatoria
  coordenada_y = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada y aleatoria

  distancia_y= tamaño_mtr-coordenada_x #Se calcula la distancia en y hasta el final de la columna
  N_letras= random.randint(3,distancia_y) #Se selecciona un numero aleatorio de letras entre 3 y la distancia en y
  Vacio = verf_vacios_ver(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra
  if Vacio == False: #Si hay espacio:
    Palabra_seleccionada = random.choice(filtradas) #Se selecciona una palabra aleatoria
    if len(Palabra_seleccionada) == N_letras: #Si la longitud de la palabra seleccionada es igual a un numero aleatorio N_letras
      dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
      filtradas.remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
      añadir_palabra_ver(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna 
      palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz
  return A, palabras, filtradas, dentro

def palabra_diagonal(A:list,tamaño_mtr:int,palabras:int,filtradas:list,dentro:list):
  coordenada_x = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada x aleatoria
  coordenada_y = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada y aleatoria
  
  distancia_x = tamaño_mtr - coordenada_y #Se calcula la distancia en x hasta el final de la fila
  distancia_y = tamaño_mtr - coordenada_x #Se calcula la distancia en y hasta el final de la columna
  distancia_diag =  min(distancia_x, distancia_y) #Se selecciona la distancia mas corta entre x y y
  N_letras= random.randint(3,distancia_diag) #Se selecciona un numero aleatorio de letras entre 3 y la distancia diagonal
  
  Vacio = verf_vacios_diag(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra
  if Vacio == False: #Si hay espacio:
    Palabra_seleccionada = random.choice(filtradas) #Se selecciona una palabra aleatoria
    if len(Palabra_seleccionada) == N_letras: #Si la longitud de la palabra seleccionada es igual a un numero aleatorio N_letras
      dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
      filtradas.remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
      añadir_palabra_diag(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna         
      palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz
  return A, palabras, filtradas, dentro


Todas_las_palabras = [
    "AMISTAD",
    "MONTAÑA",
    "NIEBLA",
    "RAPIDO",
    "FELIZ",
    "ESPEJO",
    "LUNA",
    "DULCE",
    "VIAJE",
    "JUEGO",
    "FRUTA",
    "CORAZON",
    "RIO",
    "VIENTO",
    "MESA",
    "AMOR",
    "MARIPOSA",
    "LAGO",
    "LIBRO",
    "CASA",
    "SOL"
]

if __name__ == "__main__":

  # #Usuario selecciona nivel de dificultad y se crea la matriz
  print("Seleccione nivel de dificultad:\n 1.Facil 10x10 \n 2.Medio 20x20 \n 3.Dificil 30x30")  #Se le pide al usuario que seleccione el nivel de dificultad
  Dificultad: int =int(input("Escriba 1, 2 , 3: ")) #Se guarda la respuesta del usuario en la variable Dificultad
  A = crear_matriz(Dificultad * 10) #Se crea la matriz dependiendo de la dificultad seleccionada por el usuario

  Tamaño_matriz = len(A) #Se guarda el tamaño de la matriz en la variable Tamaño_matriz

  #Se crea una lista con las palabras filtradas
  Palabras_filtradas = filtrar_palabras(Todas_las_palabras,Tamaño_matriz)

  #Se seleccionan la cantidad de palabras que se van a añadir a la matriz
  Cantidad_de_palabras:int = Tamaño_matriz // 2

  #Se crea una lista vacia para guardar las palabras que se añaden a la matriz final
  Palabras_dentro = []

  #Se añaden las palabras a la matriz
  while Cantidad_de_palabras > 0: #Mientras la cantidad de palabras sea mayor a 0
    Opciones = random.randint(1,3)  #Se selecciona una opcion aleatoria
    if Opciones == 1: #Si la opcion es 1, la palabra se añade horizontalmente
      (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_horizontal(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 

    elif Opciones == 2: #Si la opcion es 2, la palabra se añade verticalmente
      (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_vertical(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 
    
    else: #Si la opcion es 3, la palabra se añade diagonalmente
      (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_diagonal(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro)

  #Se remplazan letras aleatorias por los espacios vacios
  for i in range(len(A)): #Se recorren las filas
    for j in range(len(A[i])): #Se recorren las columnas
      if A[i][j] == "": #Si la matriz en la fila i y la columna j es igual a una cadena vacia
        A[i][j] = chr(random.randint(65,90)) #Se selecciona una letra aleatoria y se añade a la matriz

  #Se imprime la matriz
  for i in range(len(A)):#Se recorren las filas
    print(A[i]) #Se imprime cada fila

  #El usuario ingresa las palabras que encuentre
  while len(Palabras_dentro) > 0: #Mientras la longitud de la lista de palabras dentro de la matriz sea mayor a 0
      Intento = input("Ingrese la palabra que encuentre o 'salir' si desea cerrar el programa: ") #Se le pide al usuario que ingrese una palabra
      if Intento.upper() in Palabras_dentro: #Si la palabra ingresada por el usuario esta en la lista de palabras dentro
        print("Palabra correcta") #Se imprime que la palabra es correcta
        Palabras_dentro.remove(Intento.upper()) #Se remueve la palabra de la lista de palabras dentro
      if Intento.upper() == "SALIR": # Si el usuario escribe salir
        break #Se rompe el bucle
  if len(Palabras_dentro) == 0: #Si la longitud de la lista de palabras dentro es igual a 0
    print("Se han encontrado todas las palabras") #Se imprime que se han encontrado todas las palabras
        