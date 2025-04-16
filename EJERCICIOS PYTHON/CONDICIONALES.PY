'''
hacer un algoritmo en el cual proporcione 
el divisor y tiene que darme como resultado si 
multiplo o no de ese numero
================================
entrada ::> numero a evaluar
divisor ::> numero de divisor
'''
'''
num = int(input("Ingrese Numero: "))
div = int(input("Ingrese Divisor: "))

if (num % div == 0) :
    print("El Numero ",num, "Es multiplo de ",div)
else:
    print("El Numero ",num,"NO es Multiplo de", div)'''

# ejercicio de indice de masa corpotral formula
'''
 BAJO_PESO =2
 PESO_NORMAL = 1
 SOBBRE_PESO = 0
 OBESIDAD = 2

'''


totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0
while totpacientes<5:
    totpacientes = totpacientes + 1 
    print("---------------")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        cBajoPeso = cBajoPeso + 1
    elif 18.5 <= imc < 24.9:
        cPesoNormal = cPesoNormal + 1
    elif 25 <= imc < 29.9:
        cSobrePeso = cSobrePeso + 1
    else:
        cObesidad = cObesidad + 1
    
print("Pacientes Bajo de Peso : ",cBajoPeso)
print("Pacientes Peso Normal : ",cPesoNormal)
print("Pacientes Con SobrePeso : ",cSobrePeso)
print("Pacientes Con Obesidad : ",cObesidad)