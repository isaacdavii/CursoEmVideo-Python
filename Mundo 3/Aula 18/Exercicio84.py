lista = []
principal = []
maior = menor = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    
    if len(principal) == 0:
        maior = menor = lista[1]
    elif lista[1] > maior:
        maior = lista[1]
    elif lista[1] < menor:
        menor = lista[1]
    
    principal.append(lista[:])
    lista.clear()

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == "N":
        break
    while continuar not in 'SN':
        print("Opção Inválida! Tente novamente!")
        continuar = input("Quer continuar? [S/N]: ").upper().strip()

print("=-" * 30)
print(f"Os dados foram: {principal}")
print(f"Ao todo, você cadastrou {len(principal)} pessoas.")
print(f'O maior peso foi de {maior} Kgs. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f"[{p[0]}] ", end='')
print(f'\nO menor peso foi de {menor} Kgs. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f"[{p[0]}] ", end='')


