def sumar(a,b):
    return a + b 
def resta(a, b)
    return a - b 
def multiplicacion(a, b )
    return a*b 
def division(a, b)
    if b == 0
    return "Error division por cero"
return a/b 

def mostrar_menu(): 
    print("Calculadora Basica Laura y Christopher")
    print("1.Sumar")
    print("2.Resta")  
    print("3. Multiplicar") 
    print("4.Division") 
    print("5.Salir")

def calculadora(): 
    while True:
        mostrar_menu()
        opcion = input("selecciona una opcion (1-5): ")
        if opcion == "5"
                    print("saliendo de la calculadora. !Hasta luego ¡")
                    break 
        if opcion in ["1","2","3","4"]:
            num1 = float(input("introduce el primer numero: "))
            num2 = float(input("introduce el segundo numero: "))
            if opcion == "1" :
                resultado = sumar(num1,num2)
                print(f"el resultado de {num1}+{num2} es : {Resultado}")
                elif opcion =="2" 
resultado = resta (num1,num2)
print(f"El resultado de {num1}+{num2} es : {resultado}")
elif opcion == "3" 
resultado multiplicacion(num1,num2)
print(f"El resultado de {num1*{num2} es : {resultado}")
elif opcion == "4"
resultado=dividir(num1,num2)
print(f"El resultado de {num1}/{num2} es :{resultado}") 
else: 
    print("opcion ni valida. por favor, selecciona una opcion del 1
          
                