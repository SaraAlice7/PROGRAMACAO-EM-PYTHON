# Cálculo da média aritmética de duas notas usando testes condicionais.

nota1 = int(input("digite a primeira nota:"))
nota2 = int(input("digite a segunda nota:"))
media = (nota1 + nota2) / 2
if media >= 60:
  print('Aprovado')
else:
  print('Reprovado')
  