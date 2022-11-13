def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for i in lista:
        print(f'{cont} \t - \t {i}')
        cont += 1
    print(linha())
    opc = verificanumint('Digite uma opção: ')
    return opc


def verificanumint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('ERRO, por favor digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n




def cadastro(nome, idade):
    while True:
        try:
            nome = input(nome)
        except(ValueError, TypeError):
            print('ERRO, digite um nome válido.')
            continue
        return nome
    print(linha())

    while True:
        try:
            idade = int(input(idade))
        except(ValueError, TypeError):
            print('ERRO, digite um idade válida.')
            continue
        return idade
    linha()





