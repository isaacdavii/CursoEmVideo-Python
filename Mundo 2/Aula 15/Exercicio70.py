print("-"*20)
print('{:^20}'.format('LOJA DO MANÉ'))
print("-"*20)
total = totalmil = menor = quant = barato = 0 
while True:
    produto = str(input("Insira o nome do produto: "))
    preço = float(input("Insira o valor do produto: R$ "))
    if preço > 1000:
        totalmil += 1
    quant += 1
    total += preço
    if quant == 1 or preço < menor:
        menor = preço
        barato = produto
    escolha = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if escolha == 'N':
        break
    while escolha not in 'SN':
        print("Opção Inválida! Tente novamente!")
        escolha = str(input("Quer continuar? [S/N]: ")).upper().strip()
print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f"O total gasto na compra é de {total:.2f}!")
print(f"{totalmil} produtos custam mais de R$1000.00!")
print(f"O produto mais barato é o {barato } e custa R$ {menor:.2f}!")
