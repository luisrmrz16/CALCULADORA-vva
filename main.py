import  os

def SUMA():
  n1 = float(input("Escribe el primer valor de la suma: "))
  n2 = float(input("Ingresa el segundo valor de la suma: "))
  suma = n1 + n2
  print("La suma es: ", suma)

def RESTA():
  n1 = float(input("Escribe el primer valor de la resta: "))
  n2 = float(input("Ingresa el segundo valor de la resta: "))
  resta = n1 - n2
  print("La resta es: ", resta)

def MULTIPLICACION():
  n1 = float(input("Escribe el primer valor de la multiplicación: "))
  n2 = float(input("Ingresa el segundo valor de la multiplicación: "))
  multi = n1 * n2
  print("La multiplicación es: ", multi)

def DIVISION():
  n1 = float(input("Escribe el primer valor de la división: "))
  n2 = float(input("Ingresa el segundo valor de la división: "))
  division = n1 / n2
  print("La división es: ", division)

def PAUSA():
    input("Presione <ENTER> para continuar...")

def MENU():
  print("¿Que operación desea realizar?")
  print("     SUMA --> +")
  print("     RESTA --> -")
  print("     MULTIPLICACIÓN --> *")
  print("     DIVISIÓN --> /")
  print("Escriba el simbolo correspondiente en su teclado: ")
  op = str(input())
  if op == str("+"):
    SUMA()
    print("Para realizar otra operación escriba 'otra'")
    option1 = input("")
    if option1 == ("otra"):
      MENU()
    else:
      os.system("clear")
      print("GRACIAS POR USAR LA CALCULADORA VVA")
  elif op == str("-"):
    RESTA()
    print("Para realizar otra operación escriba 'otra'")
    option1 = input("")
    if option1 == ("otra"):
      MENU()
    else:
      os.system("clear")
      print("GRACIAS POR USAR LA CALCULADORA VVA")
  elif op == str("*"):
    MULTIPLICACION()
    print("Para realizar otra operación escriba 'otra'")
    option1 = input("")
    if option1 == ("otra"):
      MENU()
    else:
      os.system("clear")
      print("GRACIAS POR USAR LA CALCULADORA VVA")
  elif op == str("/"):
    DIVISION()
    print("Para realizar otra operación escriba 'otra'")
    option1 = input("")
    if option1 == ("otra"):
      MENU()
    else:
      os.system("clear")
      print("GRACIAS POR USAR LA CALCULADORA VVA")
  else:
    print("Por favor, ingrese un operador valido, escriba 'regresar' para volver al menu de operaciones")
    option2 = input("")
    if option2 == ("regresar"):
      os.system("clear")
      MENU()
    else:
      print("¡ERROR!")

print(" === CALCULADORA vva V1.0 ===")
print("     *** BIENVENIDO *** ")
PAUSA()
os.system ("clear")

MENU()