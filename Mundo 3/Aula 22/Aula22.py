# Modularização e Pacotes
# Foco é dividir o código em partes menores para facilitar a manutenção e organização
# Pacotes são pastas que contém módulos
# Foco é aumentar a legibilidade
# Dividir um problemão em pequenos problemas
#É um arquivo .py que contém funções e classes
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')
print(f'A raíz quadrada de {num} é {uteis.raiz(num)}')
print(f'O quadrado de {num} é {uteis.quadrado(num)}')
print(f'O cubo de {num} é {uteis.cubo(num)}')
print(f'O número {num} é par? {uteis.par(num)}')
print(f'O número {num} é primo? {uteis.primo(num)}')


