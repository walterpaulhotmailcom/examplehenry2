print("Bienvenidos a la calculadora")

while True:  
    try:

        op1=int(input("ingresa el primer numero: "))
        op2=int(input("ingresa el segundo numero: "))
        op=input("ingresa la operacion a realizar: ")
        break
    except ValueError:
        print("el numero ingresado no es valido")

if op=="suma":
    print("El resultado de la suma es:"+str(op1+op2))

elif op=="resta":
    print("El resultado de la resta es:"+str(op1-op2))

elif op=="multiplicacion":
    print("El resultado de la multiplicacion es:"+str(op1*op2))

elif op=="division":
    try:
        resultado=op1/op2
        print("El resultado de la division es:"+str(resultado))

    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        print("Operacion erronea")


else:
    print("La operacion ingresada es erronea")

print("fin de la calculadora")



