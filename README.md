# Projecto_programacion

### Definición de alternativa

### Diagrama preliminar
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
  AN-->|No|AO[Se recorre la matriz 'A']
  AO-->AP[Se añade una letra al azar a posiciones vacias]
  AP-->AR(Fin)
  M{Se selecciona al azar un numero de 1 a 3}-->N[Opción 1]
  N-->H[Se seleccionan dos números al azar 'x','y desde 0 hasta 7']
  H-->L[Se selecciona la posicion x,y]
  L-->I[Se calcula la distancia horizontal 'h' hasta el fin de la fila]
  I-->F[Se selecciona un número 'n' al azar entre 3 y 'h']
  F-->J{Se verifica que no haya ningun elemento en 'n' distancia}
  J-->|No|K[Se busca una palabra en el arreglo 'b' que tenga 'n' cantidad de caracteres]
  J-->|Si|M
  K-->AF[Se añade cada caracter de la palabra desde x,y hasta 'n' distancia a la matriz]
  M-->O[Opción 2]
  O-->P[Se seleccionan dos números al azar 'x','y' desde 0 hasta 7]
  P-->R[Se selecciona la posicion x,y]
  R-->S[Se calcula la distancia vertical 'v' hasta el fin de la columna]
  S-->AJ[Se selecciona un número 'n' al azar entre 3 y 'v']
  AJ-->J
  M-->V[Opción 3]
  V-->Q[Se seleccionan dos números al azar 'x','y' desde 0 hasta 7]
  Q-->AA[Se selecciona la posicion x,y]
  AA-->AB[Se calcula la distancia diagonal 'd' hasta el fin de la matriz]
  AB-->AK[Se selecciona un número 'n' al azar entre 3 y 'd']
  AK-->J
  AF-->AQ[i-=1]
  AQ-->AN 
```

### Solución preliminar

