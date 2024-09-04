import random  
import crear as cr
import verificación as verf
import añadir as an

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


# #Usuario selecciona nivel de dificultad y se crea la matriz
print("Seleccione nivel de dificultad:\n 1.Facil 10x10 \n 2.Medio 20x20 \n 3.Dificil 30x30")  #Se le pide al usuario que seleccione el nivel de dificultad
Dificultad: int =int(input("Escriba 1, 2 , 3: ")) #Se guarda la respuesta del usuario en la variable Dificultad
A = cr.crear_matriz(Dificultad * 10) #Se crea la matriz dependiendo de la dificultad seleccionada por el usuario

Tamaño_matriz = len(A) #Se guarda el tamaño de la matriz en la variable Tamaño_matriz

#Se crea una lista con las palabras filtradas
Palabras_filtradas = cr.filtrar_palabras(Todas_las_palabras,Tamaño_matriz)

#Se seleccionan la cantidad de palabras que se van a añadir a la matriz
Cantidad_de_palabras:int = Tamaño_matriz // 2

#Se crea una lista vacia para guardar las palabras que se añaden a la matriz final
Palabras_dentro = []

#Se añaden las palabras a la matriz
while Cantidad_de_palabras > 0: #Mientras la cantidad de palabras sea mayor a 0
  Opciones = random.randint(1,3)  #Se selecciona una opcion aleatoria
  if Opciones == 1: #Si la opcion es 1, la palabra se añade horizontalmente
    coordenada_x = random.randint(0,Tamaño_matriz-3) #Se selecciona una coordenada x aleatoria
    coordenada_y = random.randint(0,Tamaño_matriz-3) #Se selecciona una coordenada y aleatoria

    distancia_x = Tamaño_matriz - coordenada_y  #Se calcula la distancia en x hasta el final de la fila
    N_letras = random.randint(3,distancia_x) #Se selecciona un numero aleatorio de letras entre 3 y la distancia en x
    Vacio = verf.verf_vacios_hor(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra
    
    if Vacio == False: #Si hay espacio:
      Palabra_seleccionada = ""  #Se crea una cadena vacia para guardar la palabra seleccionada
      Palabra_seleccionada = random.choice(Palabras_filtradas) #Se selecciona una palabra aleatoria
      if len(Palabra_seleccionada) == N_letras:  #Si la longitud de la palabra seleccionada es igual a un numero aleatorio N_letras
        Palabras_dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
        Palabras_filtradas.remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
        an.añadir_palabra_horz(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna  
        Cantidad_de_palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz


  elif Opciones == 2: #Si la opcion es 2, la palabra se añade verticalmente
    coordenada_x = random.randint(0,Tamaño_matriz-3) #Se selecciona una coordenada x aleatoria
    coordenada_y = random.randint(0,Tamaño_matriz-3) #Se selecciona una coordenada y aleatoria

    distancia_y= Tamaño_matriz-coordenada_x #Se calcula la distancia en y hasta el final de la columna
    N_letras= random.randint(3,distancia_y) #Se selecciona un numero aleatorio de letras entre 3 y la distancia en y
    Vacio = verf.verf_vacios_ver(A,coordenada_x,coordenada_y,N_letras) #Se verifica si hay espacio para añadir la palabra
    if Vacio == False: #Si hay espacio:
      Palabra_seleccionada = "" #Se crea una cadena vacia para guardar la palabra seleccionada
      Palabra_seleccionada = random.choice(Palabras_filtradas) #Se selecciona una palabra aleatoria
      if len(Palabra_seleccionada) == N_letras: #Si la longitud de la palabra seleccionada es igual a un numero aleatorio N_letras
        Palabras_dentro.append(Palabra_seleccionada) #Se añade la palabra a la lista de palabras dentro
        Palabras_filtradas.remove(Palabra_seleccionada) #Se remueve la palabra de la lista de palabras filtradas
        an.añadir_palabra_ver(A,Palabra_seleccionada,coordenada_x,coordenada_y) #Se añade la palabra a la matriz usando como parametros la matriz, la palabra, la fila y la columna 
        Cantidad_de_palabras-=1 #Se resta 1 a la cantidad de palabras que se van a añadir a la matriz

#Se remplazan letras aleatorias por los espacios vacios
for i in range(len(A)): #Se recorren las filas
  for j in range(len(A[i])): #Se recorren las columnas
    if A[i][j] == "": #Si la matriz en la fila i y la columna j es igual a una cadena vacia
      A[i][j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #Se selecciona una letra aleatoria y se añade a la matriz

#Se imprime la matriz
for i in range(len(A)):#Se recorren las filas
  print(A[i]) #Se imprime cada fila

while len(Palabras_dentro) > 0: #Mientras la longitud de la lista de palabras dentro de la matriz sea mayor a 0
    Intento = input("Ingrese la palabra que encuentre: ") #Se le pide al usuario que ingrese una palabra
    if Intento.upper() in Palabras_dentro: #Si la palabra ingresada por el usuario esta en la lista de palabras dentro
      print("Palabra correcta") #Se imprime que la palabra es correcta
      Palabras_dentro.remove(Intento.upper()) #Se remueve la palabra de la lista de palabras dentro
if len(Palabras_dentro) == 0: #Si la longitud de la lista de palabras dentro es igual a 0
  print("Se han encontrado todas las palabras") #Se imprime que se han encontrado todas las palabras
      