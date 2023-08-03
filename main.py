#primer archivo pyton
#Ejercicio 1:
'''
print('Hola Mundo.')
'''
#Ejercicio 2: 
Mensaje= 'hola mundo.'
print(Mensaje)

#ejercico 3:
nombre=imput('Escribe tu nombre:')
print("hola "+nombre+"!")

#ejercico 4:
print(((3+2)/(2+5))**2)

#ejercici 5:
horas=float(input("Escriba la cantidad de horas:"))
costo=float(input("Escribe valor por hora:"))
pago=horas*costo
print("tu pago es: ",pago)'''
#Ejercicio 6:
n= int(input("entero positivo:"))
suma= n*(n+1)/2
print("la suma del entero es :,suma")'''
#Ejercicio 7:
peso=input("digita tu peso en kg: ")
estatura=input("digita tu estatura en M: ")
imc=round(float(peso)/float(estatura)**2,2)
print("tu indice de masa corporal es: ",imc)
#ejercicio 8:
N=int(input("introduce el primer numero entero (N): "))
M=int(input("introduce el segundo numero entero (M): "))

C= N // M
R= N % M
print(f"la divicion de (N) entre (M) da un cociente C = (C) y un resto R = (R)")
#Ejercicio 9:

cantidad_invertir= float(imput("introduce la cantidad a ivenrtir: "))
interes_anual= float(imput("introdusca el interes anual(%): "))
numero_años= float(imput("introdusca el numero de años: "))

interes_decimal= interes_anual/100
capital_obtenido=cantidad_invertir * (1 + interes_decimal) ** numero_años

print(f"el capital obtenido despues de (numero_años) años sera: { capital_obtenido:.2 f }")

#Ejercicio 10:
num_payasos= int(imput("introduce el numero de payasos vendido:"))
num_muñecas= int(imput("introduce el numero de muñecas vendidas:"))

peso_payaso= 112 #g
peso_muñeca= 75  #g

peso_total=(num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)

print(f"el peso total del paquete que sera enviado es: {peso_total} g")
