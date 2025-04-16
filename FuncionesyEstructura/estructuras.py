#print("hola amor")
#estructur de datos dinamicas
#lista
#tuplas
#conjuntos
#dicionaros

''''
nombres = ["alberto","angela","alejandro", "alejandro", "alicia","carla"]

for  nombre in nombres:
    print(nombre)
'''
'''
datos =[15,13,9,True,False, "Maria ROsario",14]
for data in datos :
    print(data)

print("----despues del  ejecucison")
datos.append("rene jose")
for data in datos :
    print(data)
'''

'''
#tuplas

coordenadas =(4545454.45454,754454)
for punto in coordenadas:
    print(punto)

print("----despues del  ejecucison")
for punto in coordenadas:
    print(punto)
    '''

#listar 
datos =[15,13,9,True,False, "Maria ROsario",14,15,13,9,True,False, "Maria ROsario",14,15,13,9,True,False, "Maria ROsario","oso"]

#print(datos[1])
#print(datos[4])

print("==========================")

cantidadelementos = len(datos)
#dato = datos[cantidadelementos - 1]

print("la cantidada elementos", cantidadelementos)

print("==========================")
datos.remove("maria Rosario") # pensar tarea 

cantidadelementosNuevos = len(datos)

print("El ultimo dato es ",cantidadelementosNuevos)
#datos.insert(5+30,"Francisco")
#datos.append("francisco")

for lis in datos:
    print(lis)


#datosdupla = [15,13,9,True,False, "Maria ROsario",14]
#datosdupla.append("francisco")

