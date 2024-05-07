Interactive Help: help()
		Manual de ajuda no Python
		help(print)

Docstrings:
		abrir aspas duplas três vezes 
		""" 
		Manual utilizado de ajuda interativa feito pelo próprio usuário
		Assunto que quero tratar
		"""

Argumentos/parâmetros opcionais:
	def somar(a = 0, b = 0, c = 0): 
	#deste modo, quando não possuo valor para alguma variável, ele recebe 0
		s = a + b + c
		print(f'A soma vale {s}')
		
	somar(3, 2, 5)
	somar(b = 8, c = 4)
	somar()

Escopo de variáveis: 
	def teste():
		x = 8 #variável local
		#se quiser que x se torne global
		# global x
		print(f'Na função teste, n vale {n}')
		print(f'Na função teste, x vale {x}')
			
	n = 2
	print(f'No programa principal, n vale {n}')
	teste()
	print(f'No programa principal, x vale {x}')


Retorno de valores/resultados:
	def somar(a = 0, b = 0, c = 0): 
	#deste modo, quando não possuo valor para alguma variável, ele recebe 0
		s = a + b + c
		return s
		
	print(f'A soma é {somar(3, 2, 5)}')