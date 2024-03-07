lista = []

while True:
    numero = float(input("Digite um número: "))
    if numero not in lista:
        lista.append(numero)
        print("Número adicionado com sucesso.")
    else:
        print("Número já existe na lista.")
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if continuar == "N":
        break
    while continuar not in 'SN':
        print("Opção Inválida! Tente novamente!")
        continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()
print("=-" * 30)
print(f"Os números digitados foram: {sorted(lista)}")
