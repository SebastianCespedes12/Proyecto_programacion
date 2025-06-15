import random  
import tkinter
import json
from tkinter import messagebox

def menu_principal():
  def nivel_dificultad(n): #Se declara la funcion nivel_dificultad con el parametro n
    global dificultad #Se declara la variable global dificultad
    dificultad = n    #Se asigna a la variable global dificultad el valor de n
  ventana_menu = tkinter.Tk()  #Se crea una ventana
  ventana_menu.title("dificultad") #Se le asigna un titulo a la ventana
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
  
def añadir_palabras(tamaño_matriz):
  def agregar_palabra(): 
    palabra = Entrada_añadir.get() #Se obtiene la palabra ingresada por el usuario
    if len(palabra) > 0: #Si la cadena no esta vacia
      palabras.append(palabra) #Se añade la palabra a la lista de palabras
      Entrada_añadir.delete(0, tkinter.END) #Se borra la palabra ingresada por el usuario
  def finalizar():
    if len(palabras) >= tamaño_matriz: #Si la cantidad de palabras ingresadas es mayor o igual al tamaño de la matriz
      ventana_añadir.destroy() #  Se cierra la ventana
    else: #Si la cantidad de palabras ingresadas es menor al tamaño de la matriz
      tkinter.messagebox.showwarning("Error", f"Debe ingresar al menos {tamaño_matriz} palabras.")  #Se muestra un mensaje de error

  palabras = [] #Se crea una lista vacia para almacenar las palabras
  ventana_añadir = tkinter.Tk() 
  ventana_añadir.geometry("400x400")
  ventana_añadir.title("Añadir Palabras")
  Etiqueta_añadir = tkinter.Label(ventana_añadir, text=f"Ingrese {tamaño_matriz} palabras:", font=("Arial", 14))
  Etiqueta_añadir.pack(pady=20)
  Entrada_añadir = tkinter.Entry(ventana_añadir, font=("Arial", 14)) #Se crea una entrada para que el usuario ingrese la palabra
  Entrada_añadir.pack(pady=10)
  boton_agregar = tkinter.Button(ventana_añadir, text="Agregar", command=agregar_palabra) #Se crea un boton y se le asigna la funcion agregar_palabra
  boton_agregar.pack(pady=10)
  boton_finalizar = tkinter.Button(ventana_añadir, text="Finalizar", command=finalizar) #Se crea un boton y se le asigna la funcion finalizar
  boton_finalizar.pack(pady=10)
  ventana_añadir.mainloop()
  return palabras # Se retorna la lista de palabras

def mostrar_matriz(matriz, ventana, matriz_label, opcion): 
  for i in range(len(matriz)): #Se recorre la matriz
    fila = matriz[i] #Se asigna a fila la fila i de la matriz
    for j in range(len(fila)): #Se recorre la fila
      letra = fila[j] #Se asigna a letra la letra de la fila j
      if opcion == 1: #Si la opcion es 1
        Etiqueta = tkinter.Label(ventana, text=letra, font=("Courier", 20), width=2, borderwidth=1, bg="white", relief="solid") #Se crea una etiqueta con la letra
      elif opcion == 2: #Si la opcion es 2
        Etiqueta = tkinter.Label(ventana, text=letra, font=("Courier", 15), width=2, borderwidth=1, bg="white", relief="solid") #Se crea una etiqueta con la letra
      elif opcion == 3: #Si la opcion es 3
        Etiqueta = tkinter.Label(ventana, text=letra, font=("Courier", 10), width=2, borderwidth=1, bg="white", relief="solid") #Se crea una etiqueta con la letra
      Etiqueta.grid(row=i, column=j, padx=1, pady=1) #Se pone la etiqueta en la ventana
      matriz_label[(i, j)] = Etiqueta # Guardamos las posiciones en el diccionario

def cuenta_atras(texto, tiempo, ventana):
    def actualizar_timer():
        nonlocal tiempo  #Permite modificar la variable tiempo dentro de la funcion
        if tiempo >= 0:  
            minutos = tiempo // 60
            segundos = tiempo % 60
            texto.config(text=f"{minutos:02}:{segundos:02}")
            tiempo -= 1
            ventana.after(1000, actualizar_timer)  # Programa la SIGUIENTE actualización
        else:
            messagebox.showinfo("Perdiste", "Se acabo el tiempo") #Se muestra un mensaje de que se acabo el tiempo
            ventana.after(2000, ventana.destroy) #Se cierra la ventana despues de 2 segundos
    actualizar_timer()  # Inicia el timer 

def verificar_palabra(consola,dentro,puntaje_label, puntos, ventana, matriz_label, posiciones):
  palabra = consola.get().upper() #Se obtiene la palabra ingresada por el usuario y se convierte a mayusculas
  if palabra in dentro: #Si la palabra esta en la lista de palabras dentro
    dentro.remove(palabra)	#Se remueve la palabra de la lista de palabras dentro
    messagebox.showinfo("Correcto", "Palabra correcta") #Se muestra un mensaje de que la palabra es correcta
    puntos[0] += puntaje(len(palabra)) #Se suma el puntaje de acuerdo a la longitud de la palabra al puntaje total
    for pos in posiciones[palabra]: #Se recorre la lista de posiciones de la palabra
        matriz_label[pos].config(bg="light blue") # Cambia de color las letras encontradas
  else: #Si la palabra no esta en la lista de palabras dentro
    messagebox.showinfo("Error", "Palabra incorrecta")  #Se muestra un mensaje de que la palabra es incorrecta
  consola.delete(0, tkinter.END) #Se borra la palabra ingresada por el usuario
  puntaje_label.config(text=f"Puntaje: {puntos[0]}", font=("Arial", 30)) #Se actualiza el puntaje
  if len(dentro)==0: #Si la lista de palabras dentro esta vacia
    messagebox.showinfo("Felicidades", "Encontraste todas las palabras") #Se muestra un mensaje de que se encontraron todas las palabras
    ventana.after(2000, ventana.destroy) #Se cierra la ventana despues de 2 segundos

def puntaje(longitud): 
  if longitud >= 20: #Si la longitud de la palabra es mayor o igual a 20
   return 60 #Se retorna 60
  elif longitud >= 15: #Si la longitud de la palabra es mayor o igual a 15
    return 50 #Se retorna 50
  elif longitud >= 10:
    return 40
  elif longitud >= 4:
   return 30
  else:
    return 20

def crear_ventana(tiempo, dentro, matriz, posiciones, opcion):
  puntos = [0] #Se crea una lista con un entero 0
  ventana = tkinter.Tk() #Se crea una ventana
  ventana.title("Sopa de letras")
  matriz_label = {} #Se crea un diccionario vacio
  

  mostrar_matriz(matriz, ventana, matriz_label,opcion) #Se muestra la matriz en la ventana

  texto = tkinter.Label(ventana, text="", font=("Arial", 48)) #Se crea un texto vacio
  texto.grid(row=len(matriz) + 1, columnspan=len(matriz)) #Se pone el texto en la ventana

  consola = tkinter.Entry(ventana, font=("Arial", 25)) #Se crea una entrada para que el usuario ingrese la palabra
  consola.grid(row=len(matriz) + 2, columnspan=len(matriz)) #Se pone la entrada en la ventana

  etiqueta_puntaje = tkinter.Label(ventana, text="Puntaje: 0", font=("Arial", 30)) #Se crea una etiqueta con el puntaje
  etiqueta_puntaje.grid(row=len(matriz) + 3, columnspan=len(matriz)) #Se pone el puntaje en la ventana

  etiqueta_palabras_restantes = tkinter.Label(ventana, text=f"Palabras restantes: {len(dentro)}", font=("Arial", 20)) #Se crea una etiqueta con las palabras restantes
  etiqueta_palabras_restantes.grid(row=len(matriz) + 4, columnspan=len(matriz)) #Se pone la etiqueta en la ventana

  boton_consola = tkinter.Button(ventana, text="SUBIR", command=lambda: verificar_palabra(consola, dentro, etiqueta_puntaje, puntos, ventana, matriz_label, posiciones)) #Se crea un boton y se le asigna la funcion verificar_palabra
  boton_consola.grid(row=len(matriz) + 5, columnspan=len(matriz)) #Se pone el boton en la ventana

  boton_cerrar = tkinter.Button(ventana, text="SALIR", command=ventana.destroy) #Se crea un boton y se le asigna la funcion de cerrar la ventana
  boton_cerrar.grid(row=len(matriz) + 6, columnspan=len(matriz)) #Se pone el boton en la ventana

  cuenta_atras(texto, tiempo, ventana) #Se llama a la funcion cuenta_atras con los parametros texto, tiempo y ventana
  ventana.mainloop() 

def crear_matriz(n: int) -> list:
    # Crea una matriz n x n donde cada elemento es una cadena vacía
    return [["" for i in range(n)] for i in range(n)]

def filtrar(a: list)->dict:
  A ={} #Se crea un diccionario vacio
  for cadena in a: #Se recorre la lista de palabras
    ctn = len(cadena) #Se asigna a ctn la longitud de la palabra
    if ctn in A: #Si la longitud de la palabra esta en el diccionario
       A[ctn].append(cadena.upper()) #Se añade la palabra a la lista de palabras de esa longitud
    if ctn not in A: # Si la longitud de la palabra no esta en el diccionario
      A[ctn] = [cadena.upper()] #Se añade la longitud de la palabra al diccionario y se añade la palabra a la lista de palabras de esa longitud
  return A  

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

      
if __name__ == "__main__":
 
  with open('palabras.json', 'r', encoding='utf-8') as archivo:
    todas_las_palabras = json.load(archivo)


  #Usuario selecciona nivel de dificultad 
  tamaño_matriz= menu_principal() 
  if tamaño_matriz == 10:
    dificultad = 1
  elif tamaño_matriz == 15:
    dificultad = 2  
  else:
    dificultad = 3
 
  A = crear_matriz(tamaño_matriz) #Se crea la matriz dependiendo de la dificultad seleccionada por el usuario
  
  #Se seleccionan la cantidad de palabras que se van a añadir a la matriz
  cantidad_de_palabras :int = tamaño_matriz // 2

  if tamaño_matriz == 30:
    tiempo_inicial = 480
  elif tamaño_matriz == 15:
    tiempo_inicial = 360
  elif tamaño_matriz == 10:
    tiempo_inicial = 180
  
  #Se crea un diccionario vacio para guardar las posiciones de las palabras
  posiciones = {}
  
  #Se crea una lista vacia para guardar las palabras que se añaden a la matriz final
  palabras_dentro = []


  if modos_de_juego() == False: # Si el usuario selecciona la opcion de jugar con palabras predefinidas
    #Se crea un diccionario con las palabras filtradas
    palabras_filtradas :dict = filtrar(todas_las_palabras)
    #Se añaden las palabras a la matriz
    while cantidad_de_palabras > 0: #Mientras la cantidad de palabras sea mayor a 0
      opciones = random.randint(1,3)  #Se selecciona una opcion aleatoria
      if opciones == 1: #Si la opcion es 1, la palabra se añade horizontalmente
        #Se asignan los valores de la funcion palabra_horizontal a las variables A, cantidad_de_palabras, palabras_filtradas y palabras_dentro
        (A,cantidad_de_palabras, palabras_filtradas, palabras_dentro) = palabra_horizontal(A,tamaño_matriz,cantidad_de_palabras,palabras_filtradas,palabras_dentro) 

      elif opciones == 2: #Si la opcion es 2, la palabra se añade verticalmente
        #Se asignan los valores de la funcion palabra_vertical a las variables A, cantidad_de_palabras, palabras_filtradas y palabras_dentro
        (A,cantidad_de_palabras, palabras_filtradas, palabras_dentro) = palabra_vertical(A,tamaño_matriz,cantidad_de_palabras,palabras_filtradas,palabras_dentro) 

      else: #Se añade una palabra digonalmente
        #Se asignan los valores de la funcion palabra_diagonal a las variables A, cantidad_de_palabras, palabras_filtradas y palabras_dentro
        (A,cantidad_de_palabras, palabras_filtradas, palabras_dentro) = palabra_diagonal(A,tamaño_matriz,cantidad_de_palabras,palabras_filtradas,palabras_dentro) 
    #Se remplazan letras aleatorias por los espacios vacios
    for i in range(len(A)): #Se recorren las filas
      for j in range(len(A[i])): #Se recorren las columnas
        if A[i][j] == "" : #Si la matriz en la fila i y la columna j es igual a una cadena vacia
          A[i][j] = chr(random.randint(65,90)) #Se selecciona una letra aleatoria de el codigo ASCII de las mayusculas y se añade a la matriz
    crear_ventana(tiempo_inicial, palabras_dentro, A,posiciones,dificultad)
  
  else: #Si el usuario selecciona la opcion de jugar con palabras añadidas por el
    todas_las_palabras = añadir_palabras(tamaño_matriz)
    #Se crea un diccionario con las palabras filtradas
    palabras_filtradas :dict = filtrar(todas_las_palabras)
    #Se añaden las palabras a la matriz
    while cantidad_de_palabras > 0: #Mientras la cantidad de palabras sea mayor a 0
      opciones = random.randint(1,3)  #Se selecciona una opcion aleatoria
      if opciones == 1: #Si la opcion es 1, la palabra se añade horizontalmente
        #Se asignan los valores de la funcion palabra_horizontal a las variables A, cantidad_de_palabras, palabras_filtradas y palabras_dentro
        (A,cantidad_de_palabras, palabras_filtradas, palabras_dentro) = palabra_horizontal(A,tamaño_matriz,cantidad_de_palabras,palabras_filtradas,palabras_dentro) 

      elif opciones == 2: #Si la opcion es 2, la palabra se añade verticalmente
        #Se asignan los valores de la funcion palabra_vertical a las variables A, cantidad_de_palabras, palabras_filtradas y palabras_dentro
        (A,cantidad_de_palabras, palabras_filtradas, palabras_dentro) = palabra_vertical(A,tamaño_matriz,cantidad_de_palabras,palabras_filtradas,palabras_dentro) 
        do = 1

      else: #Se añade una palabra digonalmente
        #Se asignan los valores de la funcion palabra_diagonal a las variables A, cantidad_de_palabras, palabras_filtradas y palabras_dentro
        (A,cantidad_de_palabras, palabras_filtradas, palabras_dentro) = palabra_diagonal(A,tamaño_matriz,cantidad_de_palabras,palabras_filtradas,palabras_dentro) 
    #Se remplazan letras aleatorias por los espacios vacios
    for i in range(len(A)): #Se recorren las filas
      for j in range(len(A[i])): #Se recorren las columnas
        if A[i][j] == "" : #Si la matriz en la fila i y la columna j es igual a una cadena vacia
          A[i][j] = chr(random.randint(65,90)) #Se selecciona una letra aleatoria de el codigo ASCII de las mayusculas y se añade a la matriz
    crear_ventana(tiempo_inicial, palabras_dentro, A,posiciones,dificultad)