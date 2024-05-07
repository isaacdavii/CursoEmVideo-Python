from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'rt') #read text
        a.close()
        
    except FileNotFoundError:
        #print('Arquivo não encontrado!')
        #print('Criando arquivo...')
        a = open(nome, 'wt+') #write text '+' para criar o arquivo
        print('Arquivo criado com sucesso!')
        
    #else:
        #print('Arquivo encontrado com sucesso!')
        
    finally:
        a.close()
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()
        
def listarPessoas(arq):
    try:
        a = open(arq, 'rt')
        
    except:
        print('Erro ao ler o arquivo!')
        
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            
    finally:
        a.close()

def cadastrarPessoa(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at') #append text
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
            
