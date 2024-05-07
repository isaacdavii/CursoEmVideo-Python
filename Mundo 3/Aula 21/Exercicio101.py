def voto():
    from datetime import date
    nasc = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - nasc
    if idade < 16:
        return f'Você tem {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos: VOTO OPCIONAL'
    else:
        return f'Você tem {idade} anos: VOTO OBRIGATÓRIO'

print(voto())