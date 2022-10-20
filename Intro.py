numero1 = int(input('digite o numero 1:'))
numero2 = int(input('digite o numero 2:'))
numero3 = int(input('digite o numero 3:'))
if numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
  exit( ) 
if numero1 > numero2 and numero1 > numero3:
  print('o primeiro numero é o maior')
if numero2 > numero1 and numero2 > numero3:
  print('o segundo numero é o maior')
if numero3 > numero1 and numero3 > numero2:
  print('o terceiro numero é o maior')
