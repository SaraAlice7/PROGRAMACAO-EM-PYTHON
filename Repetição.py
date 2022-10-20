nome  = input("Nome: ")
tempo = float(input("Tempo (em s): "))

nome_melhor  = nome
tempo_melhor = tempo
nome_pior    = nome
tempo_pior   = tempo

soma_tempo   = tempo
tempo_entre12e15 = 0

if tempo >= 12 and tempo <= 15:
    tempo_entre12e15 += 1

for x in range(6):
    nome  = input("Nome: ")
    tempo = float(input("Tempo (em s): "))
    if tempo < tempo_melhor:
        tempo_melhor = tempo
        nome_melhor  = nome

    if tempo > tempo_pior:
        tempo_pior = tempo
        nome_pior  = nome

    if tempo >= 12 and tempo <= 15:
        tempo_entre12e15 += 1

    soma_tempo += tempo
print(f"\nMelhor nadador é {nome_melhor} com o tempo {tempo_melhor}s")
print(f"Pior nadador é {nome_pior} com o tempo {tempo_pior}s")
media_tempo = soma_tempo / 7
print(F"Média dos tempos é {media_tempo:.2f}")
print(F"Qtde de nadadores com o tempo no intervalo [12, 15] é {tempo_entre12e15}")
