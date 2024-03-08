lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == "N":
        break
    while continuar not in 'SN':
        print("Opção Inválida! Tente novamente!")
        continuar = input("Quer continuar? [S/N]: ").upper().strip()
print("=-" * 30)
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)    
print(f"Os números digitados foram: {lista}")

if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não faz parte da lista!')