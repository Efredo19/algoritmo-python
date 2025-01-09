#sumar dos numeros
#n1=int(input("Ingrese el primer numero: "))# pedir el primer numero
#n2=int(input("Ingrese el segundo numero: "))# pedir el segundo numero


#print(f"{n1} + {n2} = {n1 + n2}") 



# El usuario ingresa su edad y vamos a determinar si es mayor o menor de edad
#edad = int(input("ingresa tu edad:")) 

#if(edad < 18):
#    print("Eres menor de edad")# decimos que es menor de edad

#else:
#   print("Eres mayoe de edad")

# de una lista de numeros obtener la suma de todos los valores 
#lista = [1,2,3,4,5,6,7,8,9,10]
#sumalista = 0
#for i in lista:
 #   sumalista = sumalista + i # 0 = 0 + 1 -> 1 = 1 + 2 -> 3 = 3 + 3 -> 6 = 6 + 4

#print(" Suma de la lista", sumalista)


# de una lista de numeros obtener la suma de todos los valores 
#sumalista2 = 0
#for i in range(1,101):
 #   sumalista2 = sumalista2 + i # 0 = 0 + 1 -> 1 = 1 + 2 -> 3 = 3 + 3 -> 6 = 6 + 4

#print(" Suma de la lista", sumalista2)

#while
#lista3 = [1,2,3,4]
#sumalista3 = 0
#contador = 0
#flag = True
#while flag:
#    sumalista3 += lista3[contador]# 0 = 1 -> 1 = 3
 #   contador+= 1

 #   if contador > 3:
 #       flag = False



#print(sumalista3)

#def cuadradoNumero(numero = 0):
 #   return numero * numero

#print(cuadradoNumero(5))

#biblioteca = [
 #   {
 #       "Libro1": "El principito",
 #       "descripcion": "EL PRINCIPITO DESCRIPCION"
  #  },
   # {
#      "Libro2": "la biblia",
 #       "descripcion": "la biblia DESCRIPCION"  
 #   }
#]

#print(biblioteca[0]["Libro1"])


#string
#nombre = "Jorge"
#nombre = nombre.upper()
#nombre = nombre.lower()
#nombre = nombre.capitalize()
#print(nombre)

#ARRAY
#array = [1,2,"carro",False,{"libro": "WDW3"},[1,2,3],None]
#print(array)
#array.append(23)#agrega un valor al final
#print(array)
#array.pop()#elomina el ultimo valor 
#print(array)

#array.insert(0,"Nuevo valor") # agregar valor definiendo la posicion
#print(array)

#def calcularAreaCirculo(radio):
 #   return 3.1416 * (radio * radio)

#print(calcularAreaCirculo(5))

#pedir dos numeros al usuario 

#v1 = int(input("ingrese un numero:"))
#v2 = int(input("ingrese un numero:"))

#if (v1 > v2):
#    print("este numero",v1, "es mayor que", v2) 

#else:
#    print("este numero",v2, "es mayor que", v1)


numero = int(input("ingrese un numero:"))

if (numero % 2 == 0):
    print("es par")

else:
    print("es impar")
