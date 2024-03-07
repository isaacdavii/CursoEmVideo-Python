from random import randint
vitoria = 0
while True:
    escolha = str(input("Escolhar P para 'PAR' e I para 'ÍMPAR': ")).strip().upper()
    while escolha not in 'PI': #CASO A PESSOA DIGITE ERRADO
        print("OPÇÃO INVÁLIDA! Digite novamente!")
        escolha = str(input("Escolhar P para 'PAR' e I para 'ÍMPAR': ")).strip().upper()
    jogador = int(input("Digite um valor [0 - 10]: "))
    computador = randint(0,10)
    soma = jogador + computador
    if escolha == "P": #JOGADOR ESCOLHE PAR
        if soma % 2 == 1:
            print(f"Você jogou {jogador} e eu {computador}!")
            print(f"A soma deu {soma}! O resultador é Ímpar!")
            print("Você perdeu HAHAHA")
            break
        elif soma % 2 == 0:
            print(f"Você jogou {jogador} e eu {computador}!")
            print(f"A soma deu {soma}! O resultador é Par!")
            vitoria += 1
            print("Você venceu! Parabéns!")
    elif escolha == "I": #JOGADOR ESCOLHE ÍMPAR
        if soma % 2 == 1:
            print(f"Você jogou {jogador} e eu {computador}!")
            print(f"A soma deu {soma}! O resultador é Ímpar!")
            vitoria += 1
            print("Você venceu! Parabéns!")
        elif soma % 2 == 0:
            print(f"Você jogou {jogador} e eu {computador}!")
            print(f"A soma deu {soma}! O resultador é Par!")
            print("Você perdeu HAHAHA")
            break
print(f"Você obteve \033[31m{vitoria}\033[m vitória(s)! Parabéns" if vitoria > 0 else "Você obteve \033[34mNENHUMA\033[m vitória!")
