from lib.interface import *
from lib.arquivo import *

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(
        ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"]
    )
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        listarPessoas(arq)
        
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrarPessoa(arq, nome, idade)
        
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho("Saindo do sistema... Até logo!")
        break
    
    else:
        print("\033[31mERRO: Digite uma opção válida!\033[m")
