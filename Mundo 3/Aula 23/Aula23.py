"""try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b
	
except Exception as erro:
	print(f'Infelizmente tivemos um problema chamado {erro.__class__}')
	
else:	
	print(f'O resultado é {r:.1f}')

finally:
	print('Volte sempre!')"""
 
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
	
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
          
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
    
except Exception as erro:
    print(f'Infelizmente tivemos um problema chamado {erro.__class__}.')
	
else:	
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre!')
