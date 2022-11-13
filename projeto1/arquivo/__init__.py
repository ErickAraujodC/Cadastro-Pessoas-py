from projeto1.interface import *


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
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO AO CRIAR ARQUIVO')
    else:
        print(f'Arquivo {nome}, criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO LER ARQUIVO.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<15}{dado[1]:<} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO NA ABERTURA DO ARQUIVO.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO AO CADASTRAR PESSOA')
        else:
            print(f'{nome}, cadastrado com sucesso.')
            a.close()
