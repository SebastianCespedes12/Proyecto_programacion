# Proyecto Programación
## **Infinity Bit Team (∞BT)**
* Juan Diego Cárdenas Olarte
* Sebastián Céspedes Rico
* Alejandra Landines Sanabria

[![logo.jpg](https://i.postimg.cc/pdcVKPsT/logo.jpg)](https://postimg.cc/JyJWLCVV)

-------------
## Definición de alternativa
Optamos por la alternativa número 1, que consiste en crear una sopa de letras. Elegimos esta opción porque consideramos que programar este juego representa un reto para nosotros, que nos permite evaluar nuestro aprendizaje en la asignatura de Programación de Computadores, ya que para realizarlo es necesario hacer uso de los conceptos aprendidos; operaciones, condicionales, funciones, bucles, listas, matrices, strings y tuplas. 

El algoritmo primero solicita al usuario que seleccione un nivel de dificultad, y en función de esta elección, se genera una matriz de diferente tamaño. Luego, se añaden palabras seleccionadas aleatoriamente de una lista a la matriz, letra por letra, y en distintas direcciones: horizontal, vertical y diagonal. Una vez ubicadas las palabras correspondientes al nivel de dificultad, se completan las posiciones vacías de la matriz con letras aleatorias. La interacción con el usuario se realiza mediante la consola, donde el usuario debe escribir la palabra que encuentra, y, esta se subraya automáticamente en la matriz. Además, planeamos agregar un sistema de puntuación y tiempo al juego.

## Diagrama preliminar
```mermaid
flowchart TD
  A(inicio)-->B[Se crea arreglo 's' con todas las palabras]
  B-->C{Se elige el tamaño de la matriz 'A'}
  C-->Z[10x10]
  C-->Y[20x20]
  C-->X[30x30]
  Z-->AH[variable 't' igual a la cantidad de filas de A]
  AH-->AI[Se crea arreglo vacio 'b']
  AI-->D[Recorre arreglo 's']
  Y-->AH
  X-->AH
  D-->E[Fitra por tamaño de palabra menor o igual a 't' ]
  E-->G[Se añaden las palabras al arreglo 'b'] 
  G-->AM[Variable 'i' igual a 't'/2]
  AM-->AN{i>0?}
  AN-->|si|M{Se selecciona al azar un numero de 1 a 3}
  AN-->|no|AO[Se recorre la matriz 'A']
  AO-->AP[Se añade una letra al azar a posiciones vacias]
  AP-->AR(Fin)
  M{Se selecciona al azar un numero de 1 a 3}-->N[Opción 1]
  N-->H[Se seleccionan dos números al azar 'x','y' desde 0 hasta t-3']
  H-->L[Se selecciona la posicion x,y]
  L-->I[Se calcula la distancia horizontal 'h' hasta el fin de la fila]
  I-->F[Se selecciona un número 'n' al azar entre 3 y 'h']
  F-->J{Se verifica que no haya ningun elemento en 'n' distancia}
  J-->|No|K[Se busca una palabra en el arreglo 'b' que tenga 'n' cantidad de caracteres]
  J-->|Si|M
  K-->AF[Se añade cada caracter de la palabra desde x,y hasta 'n' distancia a la matriz]
  M-->O[Opción 2]
  O-->P[Se seleccionan dos números al azar 'x','y' desde 0 hasta t-3]
  P-->R[Se selecciona la posicion x,y]
  R-->S[Se calcula la distancia vertical 'v' hasta el fin de la columna]
  S-->AJ[Se selecciona un número 'n' al azar entre 3 y 'v']
  AJ-->J
  M-->V[Opción 3]
  V-->Q[Se seleccionan dos números al azar 'x','y' desde 0 hasta t-3]
  Q-->AA[Se selecciona la posicion x,y]
  AA-->AB[Se calcula la distancia diagonal 'd' hasta el fin de la matriz]
  AB-->AK[Se selecciona un número 'n' al azar entre 3 y 'd']
  AK-->J
  AF-->AQ[i-=1]
  AQ-->AN 
```

## Funciones de funcionalidad
Primero, se crearon 11 funciones principales antes de realizar un codigo general. La primera función consiste en crear una matriz con cualquier tamaño.
```python
def crear_matriz(n: int) -> list:
    # Crea una matriz n x n donde cada elemento es una cadena vacía
    return [["" for i in range(n)] for i in range(n)]
```
La segunda función filtra y añade a un diccionario todas las palabras, la clave es la longitud de la palabra y el valor una lista con todas las palabras de esa longitud .
```python
def filtrar(a: list)->dict:
  A ={} #Se crea un diccionario vacio
  for cadena in a: #Se recorre la lista de palabras
    ctn = len(cadena) #Se asigna a ctn la longitud de la palabra
    if ctn in A: #Si la longitud de la palabra esta en el diccionario
       A[ctn].append(cadena.upper()) #Se añade la palabra a la lista de palabras de esa longitud
    if ctn not in A: # Si la longitud de la palabra no esta en el diccionario
      A[ctn] = [cadena.upper()] #Se añade la longitud de la palabra al diccionario y se añade la palabra a la lista de palabras de esa longitud
  return A  
```
La tercera, cuarta y quinta función verifican si hay algún objeto distinto de una cadena vacía en un rango dentro de una fila o columna. Esto para saber si se puede añadir una palabra.
```python
def verf_vacios_hor(A:list,x:int,y:int,d:int) ->bool: #Se añaden los parametros de la matriz, la fila, la columna y la longitud de la palabra
  Vacios = False  #Se asigna a Vacios el valor de False
  for i in range(y,y+d): #Se recorre la fila por la longitud de la palabra
    if A[x][i] != "": #Si la matriz en la fila x y la columna i es diferente a una cadena vacia
      Vacios=True  #Se asigna a Vacios el valor de True y se rompe el ciclo
      break
  return Vacios

def verf_vacios_ver(A:list,x:int,y:int,d:int)->bool:
  Vacios = False #Se asigna a Vacios el valor de False
  for i in range(x,x+d): #Se recorre la columna por la longitud de la palabra
    if A[i][y] != "": #Si la matriz en la fila i y la columna y es diferente a una cadena vacia
      Vacios=True  #Se asigna a Vacios el valor de True y se rompe el ciclo
      break
  return Vacios 

def verf_vacios_diag(A:list,x:int,y:int,d:int)->bool:
  Vacios = False #Se asigna a Vacios el valor de False
  for i in range(x,x+d): #Se recorre la columna por la longitud de la palabra
    for j in range(y,y+d): #Se recorre la fila por la longitud de la palabra
      if i-j == x-y: #Si la resta de i-j es igual a la resta de x-y
        if A[i][j] != "": #Si la matriz en la fila i y la columna j es diferente a una cadena vacia
          Vacios=True #Se asigna a Vacios el valor de True y se rompe el ciclo
          break
  return Vacios
```
La sexta,septima y octava función añaden una cadena, caracter por caracter, a un rango dentro de una fila o columna.
```python
def añadir_palabra_horz(A:list,s:str,fila:int,columna:int)->list: #Se añaden como parametros la matriz, la palabra, la fila y la columna
    i = fila #Se asigna a i el valor de la fila, ya que la fila no cambia
    pos = []
    for k in range(columna,columna + len(s)):  #Se recorre la palabra y la fila.
        A[i][k] = s[k-columna] #Se asigna a la matriz la letra de la palabra en la posicion k-columna
        pos.append((i, k)) #Se añade la posicion a la lista de posiciones
    posiciones[s] = pos
    return A

def añadir_palabra_ver(A:list,s:str,fila:int,columna:int)->list:
  i = columna #Se asigna a i el valor de la columna, ya que la columna no cambia
  pos = []
  for k in range(fila,fila + len(s)):  #Se recorre la palabra y la columna.
    A[k][i] = s[k - fila] #Se asigna a la matriz la letra de la palabra en la posicion k-fila
    pos.append((k, i)) #Se añade la posicion a la lista de posiciones
  posiciones[s] = pos
  return A  

def añadir_palabra_diag(A:list,s:str,fila:int,columna:int)->list:
  pos = []
  for i in range(fila,fila+len(s)): #Se recorre la palabra y la fila
    for j in range(columna,columna+len(s)): #Se recorre la palabra y la columna
      if i-j == fila-columna: #Si la resta de i-j es igual a la resta de fila-columna
        A[i][j]=s.upper()[i-fila] #Se asigna a la matriz la letra de la palabra en la posicion i-fila
        pos.append((i, j)) #Se añade la posicion a la lista de posiciones
  posiciones[s] = pos
  return A
```
La novena, decima y undecima función colocan una palabra aleatoria de un diccionario en una posicion aleatoria, asegurándose de que haya suficiente espacio disponible y actualizando las listas y contadores.
```python
def palabra_horizontal(A:list,tamaño_mtr:int,palabras:int,filtradas:dict,dentro:list):
  coordenada_x = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada x aleatoria
  coordenada_y = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada y aleatoria

  distancia_x = tamaño_mtr - coordenada_y  #Se calcula la distancia en x hasta el final de la fila
  N_letras = random.randint(3,distancia_x) #Se selecciona un numero aleatorio de letras entre 3 y la distancia en x
  Vacio = verf_vacios_hor(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra   
  if Vacio == False and (filtradas.get(N_letras) != None): #Si hay espacio y la lista de palabras filtradas no esta vacia  
    if len(filtradas.get(N_letras)) > 0:
      Palabra_seleccionada = random.choice(filtradas.get(N_letras)) #Se selecciona una palabra aleatoria
      dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
      filtradas.get(N_letras).remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
      añadir_palabra_horz(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna  
      palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz
  return A, palabras, filtradas, dentro

def palabra_vertical(A:list,tamaño_mtr:int,palabras:int,filtradas:dict,dentro:list): 
  coordenada_x = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada x aleatoria
  coordenada_y = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada y aleatoria

  distancia_y= tamaño_mtr-coordenada_x #Se calcula la distancia en y hasta el final de la columna
  N_letras= random.randint(3,distancia_y) #Se selecciona un numero aleatorio de letras entre 3 y la distancia en y
  Vacio = verf_vacios_ver(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra
  if Vacio == False and (filtradas.get(N_letras) != None): #Si hay espacio y la lista de palabras filtradas no esta vacia
    if len(filtradas.get(N_letras)) > 0 :
      Palabra_seleccionada = random.choice(filtradas.get(N_letras)) #Se selecciona una palabra aleatoria
      dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
      (Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
      filtradas.get(N_letras).remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
      añadir_palabra_ver(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna 
      palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz
  return A, palabras, filtradas, dentro

def palabra_diagonal(A:list,tamaño_mtr:int,palabras:int,filtradas:dict,dentro:list):
  coordenada_x = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada x aleatoria
  coordenada_y = random.randint(0,tamaño_mtr-3) #Se selecciona una coordenada y aleatoria
  
  distancia_x = tamaño_mtr - coordenada_y #Se calcula la distancia en x hasta el final de la fila
  distancia_y = tamaño_mtr - coordenada_x #Se calcula la distancia en y hasta el final de la columna
  distancia_diag =  min(distancia_x,distancia_y) #Se calcula la distancia en y hasta el final de la fila o columna
  N_letras= random.randint(3,distancia_diag) #Se selecciona un numero aleatorio de letras entre 3 y la distancia diagonal
  
  Vacio = verf_vacios_diag(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra
  if Vacio == False and (filtradas.get(N_letras) != None): #Si hay espacio y la lista de palabras filtradas no esta vacia:
    if len(filtradas.get(N_letras)) > 0 :  
      Palabra_seleccionada = random.choice(filtradas.get(N_letras)) #Se selecciona una palabra aleatoria
      dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
      filtradas.get(N_letras).remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
      añadir_palabra_diag(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna         
      palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz
  return A, palabras, filtradas, dentro
```
### Funciones de interfaz
Primero, la función crea una ventana con tres botones para seleccionar la dificultad, retorna el tamaño de matriz escogido.
```python
def menu_principal():
  def nivel_dificultad(n): #Se declara la funcion nivel_dificultad con el parametro n
    global dificultad #Se declara la variable global dificultad
    dificultad = n    #Se asigna a la variable global dificultad el valor de n
  ventana_menu = tkinter.Tk()  #Se crea una ventana
  ventana_menu.title("Dificultad") #Se le asigna un titulo a la ventana
  ventana_menu.geometry("400x400") #Se le asigna un tamaño a la ventana
  etiqueta = tkinter.Label(ventana_menu, text="Seleccione dificultad", font=("Arial", 20)) #Se crea una etiqueta y se le asigna un texto y un tamaño de letra
  etiqueta.pack() #Se pone la etiqueta en la ventana
  boton_facil = tkinter.Button(ventana_menu, text="1. Facil 10x10 ", command=lambda: (ventana_menu.destroy(), nivel_dificultad(10))) #Se crea un boton y se le asigna la funcion nivel_dificultad con el parametro 10
  boton_facil.pack(pady=20) #Se pone el boton en la ventana
  boton_medio = tkinter.Button(ventana_menu, text="2. Medio 15x15", command=lambda:(ventana_menu.destroy(), nivel_dificultad(15)))  
  boton_medio.pack(pady=20)
  boton_dificil = tkinter.Button(ventana_menu, text="3. Dificil 30x30", command=lambda: ((ventana_menu.destroy(), nivel_dificultad(30))))
  boton_dificil.pack(pady=20)
  ventana_menu.mainloop() 
  return dificultad #Se retorna la variable global dificultad
```
La función crea una ventana con dos botones para seleccionar el modo de juego, añadiendo palabras o utilizando las predeterminadas, retorna True si el usuario elige añadir palabras y False si el usuario elige predeterminadas.
```python
def modos_de_juego():  
  ventana_modos = tkinter.Tk() #Se crea una ventana
  ventana_modos.title("Modos de juego") #Se le asigna un titulo a la ventana
  ventana_modos.geometry("400x400")  #Se le asigna un tamaño a la ventana
  
  # Variable to store the user's choice
  eleccion_usuario = [] #Se crea una lista vacia para almacenar la eleccion del usuario

  etiqueta = tkinter.Label(ventana_modos, text="Desea añadir palabras \n o jugar con las palabras \n predeterminadas?", font=("Arial", 20))
  etiqueta.pack()
  
  def en_añadir():  
    eleccion_usuario.append("añadir") #Se añade a la lista la palabra "añadir"
    ventana_modos.destroy() #Se cierra la ventana

  def en_predeterminado(): 
    eleccion_usuario.append("predeterminado") #Se añade a la lista la palabra "predeterminado"
    ventana_modos.destroy() #Se cierra la ventana
   
  boton_añadir = tkinter.Button(ventana_modos, text="1. Añadir palabras", command=en_añadir) #Se crea un boton y se le asigna la funcion en_añadir
  boton_añadir.pack(pady=30 )

  boton_predeterminado = tkinter.Button(ventana_modos, text="2. Palabras predeterminadas", command=en_predeterminado) #Se crea un boton y se le asigna la funcion en_predeterminado
  boton_predeterminado.pack(pady=30)
  
  ventana_modos.mainloop()
  if "añadir" in eleccion_usuario: #Si la palabra "añadir" esta en la lista eleccion_usuario
    return True    #Se retorna True
  elif "predeterminado" in eleccion_usuario: #Si la palabra "predeterminado" esta en la lista eleccion_usuario
    return False   #Se retorna False
```
La función crea una ventana que permite al usuario ingresar un numero de palabras, asegurando que haya un minimo para crear la sopa de letras, retorna una lista con todas las palabras del usuario.
```python
def añadir_palabras(Tamaño_matriz):
  def agregar_palabra(): 
    palabra = Entrada_añadir.get() #Se obtiene la palabra ingresada por el usuario
    if len(palabra) > 0: #Si la cadena no esta vacia
      palabras.append(palabra) #Se añade la palabra a la lista de palabras
      Entrada_añadir.delete(0, tkinter.END) #Se borra la palabra ingresada por el usuario
  def finalizar():
    if len(palabras) >= Tamaño_matriz: #Si la cantidad de palabras ingresadas es mayor o igual al tamaño de la matriz
      ventana_añadir.destroy() #  Se cierra la ventana
    else: #Si la cantidad de palabras ingresadas es menor al tamaño de la matriz
      tkinter.messagebox.showwarning("Error", f"Debe ingresar al menos {Tamaño_matriz} palabras.")  #Se muestra un mensaje de error

  palabras = [] #Se crea una lista vacia para almacenar las palabras
  ventana_añadir = tkinter.Tk() 
  ventana_añadir.geometry("400x400")
  ventana_añadir.title("Añadir Palabras")
  Etiqueta_añadir = tkinter.Label(ventana_añadir, text=f"Ingrese {Tamaño_matriz} palabras:", font=("Arial", 14))
  Etiqueta_añadir.pack(pady=20)
  Entrada_añadir = tkinter.Entry(ventana_añadir, font=("Arial", 14)) #Se crea una entrada para que el usuario ingrese la palabra
  Entrada_añadir.pack(pady=10)
  boton_agregar = tkinter.Button(ventana_añadir, text="Agregar", command=agregar_palabra) #Se crea un boton y se le asigna la funcion agregar_palabra
  boton_agregar.pack(pady=10)
  boton_finalizar = tkinter.Button(ventana_añadir, text="Finalizar", command=finalizar) #Se crea un boton y se le asigna la funcion finalizar
  boton_finalizar.pack(pady=10)
  ventana_añadir.mainloop()
  return palabras # Se retorna la lista de palabras
```

Después se añadieron todas las funciones a un codigo principal.
### Se declaran las variables
```python
if __name__ == "__main__":
  #Usuario selecciona nivel de dificultad
  Tamaño_matriz= menu_principal() 
  if Tamaño_matriz == 10:
    Dificultad = 1
  elif Tamaño_matriz == 15:
    Dificultad = 2  
  else:
    Dificultad = 30
 
  A = crear_matriz(Tamaño_matriz) #Se crea la matriz dependiendo de la dificultad seleccionada por el usuario
  
  #Se seleccionan la cantidad de palabras que se van a añadir a la matriz
  Cantidad_de_palabras :int = Tamaño_matriz // 2

  if Tamaño_matriz == 30:
    tiempo_inicial = 480
  elif Tamaño_matriz ==15:
    tiempo_inicial = 360
  elif Tamaño_matriz ==10:
    tiempo_inicial = 180

  #Se crea un diccionario vacio para guardar las posiciones de las palabras
  posiciones = {}
  
  #Se crea una lista vacia para guardar las palabras que se añaden a la matriz final
  Palabras_dentro = []
```
### Se selecciona el modo de juego
Si el usuario selecciona la opcion de jugar con palabras predefinidas
```python
  if modos_de_juego() == False: # Si el usuario selecciona la opcion de jugar con palabras predefinidas
    #Se crea un diccionario con las palabras filtradas
    Palabras_filtradas :dict = filtrar(Todas_las_palabras)
    #Se añaden las palabras a la matriz
    while Cantidad_de_palabras > 0: #Mientras la cantidad de palabras sea mayor a 0
      Opciones = random.randint(1,3)  #Se selecciona una opcion aleatoria
      if Opciones == 1: #Si la opcion es 1, la palabra se añade horizontalmente
        #Se asignan los valores de la funcion palabra_horizontal a las variables A, Cantidad_de_palabras, Palabras_filtradas y Palabras_dentro
        (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_horizontal(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 

      elif Opciones == 2: #Si la opcion es 2, la palabra se añade verticalmente
        #Se asignan los valores de la funcion palabra_vertical a las variables A, Cantidad_de_palabras, Palabras_filtradas y Palabras_dentro
        (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_vertical(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 

      else: #Se añade una palabra digonalmente
        #Se asignan los valores de la funcion palabra_diagonal a las variables A, Cantidad_de_palabras, Palabras_filtradas y Palabras_dentro
        (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_diagonal(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 
    #Se remplazan letras aleatorias por los espacios vacios
    for i in range(len(A)): #Se recorren las filas
      for j in range(len(A[i])): #Se recorren las columnas
        if A[i][j] == "" : #Si la matriz en la fila i y la columna j es igual a una cadena vacia
          A[i][j] = chr(random.randint(65,90)) #Se selecciona una letra aleatoria de el codigo ASCII de las mayusculas y se añade a la matriz
    crear_ventana(tiempo_inicial, Palabras_dentro, A,posiciones,Dificultad)
```
Si el usuario selecciona la opcion de jugar con palabras añadidas por el
```python
  else: #Si el usuario selecciona la opcion de jugar con palabras añadidas por el
    Todas_las_palabras = añadir_palabras(Tamaño_matriz)
    #Se crea un diccionario con las palabras filtradas
    Palabras_filtradas :dict = filtrar(Todas_las_palabras)
    #Se añaden las palabras a la matriz
    while Cantidad_de_palabras > 0: #Mientras la cantidad de palabras sea mayor a 0
      Opciones = random.randint(1,3)  #Se selecciona una opcion aleatoria
      if Opciones == 1: #Si la opcion es 1, la palabra se añade horizontalmente
        #Se asignan los valores de la funcion palabra_horizontal a las variables A, Cantidad_de_palabras, Palabras_filtradas y Palabras_dentro
        (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_horizontal(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 

      elif Opciones == 2: #Si la opcion es 2, la palabra se añade verticalmente
        #Se asignan los valores de la funcion palabra_vertical a las variables A, Cantidad_de_palabras, Palabras_filtradas y Palabras_dentro
        (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_vertical(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 
        do = 1

      else: #Se añade una palabra digonalmente
        #Se asignan los valores de la funcion palabra_diagonal a las variables A, Cantidad_de_palabras, Palabras_filtradas y Palabras_dentro
        (A,Cantidad_de_palabras, Palabras_filtradas, Palabras_dentro) = palabra_diagonal(A,Tamaño_matriz,Cantidad_de_palabras,Palabras_filtradas,Palabras_dentro) 
    #Se remplazan letras aleatorias por los espacios vacios
    for i in range(len(A)): #Se recorren las filas
      for j in range(len(A[i])): #Se recorren las columnas
        if A[i][j] == "" : #Si la matriz en la fila i y la columna j es igual a una cadena vacia
          A[i][j] = chr(random.randint(65,90)) #Se selecciona una letra aleatoria de el codigo ASCII de las mayusculas y se añade a la matriz
    crear_ventana(tiempo_inicial, Palabras_dentro, A,posiciones,Dificultad)
```

