from projeto1.interface import *
from projeto1.arquivo import  *
from time import sleep

arq = ('cursoemvideo.txt')
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    sleep(1)
    resposta = menu(['CADASTRAR PESSOA', 'VISUALISAR CADASTROS', 'SAIR'])
    if resposta == 1:
        nome = input('Nome: ')
        idade = verificanumint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('SAINDO DO SISTEMA, ATÉ LOGO.')
        break
    else:
        cabeçalho('ERRO, OPÇÃO INVÁLIDA, TENTE NOVAMENTE')



