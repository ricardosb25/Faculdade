escolha = ['1', '2', '3', '4']  # opções do menu


def menu():
    print('\n\nMenu do sistema')
    print('1 - Cadastrar um novo aluno')
    print('2 - Listar todos os alunos cadastrados')
    print('3 - Buscar um aluno cadastrado')
    print('4 - Excluir um aluno cadastrado\n')
    op = input('Escolha uma das opções:')
    # validando a escolha do usuário
    while op not in escolha:
        op = input('Escolha uma opção válida:')
    return op


def cadastro(nome, email, curso):
    arquivo = open('cadastro_aluno.txt', 'a+')
    arquivo.write(str(nome+';'+email+';'+curso+'\n'))
    print("Cadastrado com sucesso!!\n\n")
    arquivo.close()


def listar():
    arquivo = open('cadastro_aluno.txt', 'r', encoding='utf-8')
    dados = arquivo.readlines()
    # repetição para retirar o \n do texto
    for i in range(len(dados)):
        dados[i] = dados[i].strip('\n')
    arquivo.close()
    return dados


def buscar(dado):
    resp = 0
    arquivo = open('cadastro_aluno.txt', 'r', encoding='utf-8')
    dados = arquivo.readlines()
    for aluno in dados:
        nome, email, curso = aluno.split(';')
        if dado.lower() == nome.lower():
            arquivo.close()
            return (nome, email, curso)
    arquivo.close()
    return resp


def deletar(dado):
    resp = 0
    # encoding='utf-8' é só para trazer o texto com acentuação
    arquivo = open('cadastro_aluno.txt', 'r', encoding='utf-8')
    dados = arquivo.readlines()
    arquivo.close()
    arquivo = open('cadastro_aluno.txt', 'w', encoding='utf-8')
    for aluno in dados:
        nome, email, curso = aluno.split(';')
        # lower() é para deixar todos os caracteres minúsculos
        if dado.lower() != nome.lower():
            arquivo.write(aluno)
        else:
            resp = 1
    arquivo.close()
    return resp


continua = 's'  # só para entrar no while
while continua == 's' or continua == 'S':
    # chama a função menu que retorna a escolha do usuário
    resp = menu()
    if resp == '1':
        nome = input('Digite o nome do aluno:')
        email = input('Digite o email do aluno:')
        curso = input('Digite o curso do aluno:')
        # chama a função cadastro passando o nome, email e curso como parâmetros
        cadastro(nome, email, curso)
    elif resp == '2':
        resultado = listar()
        for aluno in resultado:
            nome_aluno, email_aluno, curso_aluno = aluno.split(';')
            print('Nome: '+nome_aluno+' - E-mail: ' +
                  email_aluno+' - Curso: '+curso_aluno)
    elif resp == '3':
        nome = input('Digite o nome do aluno:')
        # chama a função buscar passando o nome como parâmetro
        resposta = buscar(nome)
        if resposta == 0:
            print('Aluno não encontrado!!\n')
        else:
            # print('Aluno encontrado\n')
            nome_aluno, email_aluno, curso_aluno = resposta
            print('Nome: '+nome_aluno+' - E-mail: ' +
                  email_aluno+' - Curso: '+curso_aluno)
    elif resp == '4':
        nome = input('Digite o nome do aluno:')
        # chama a função deletar passando o nome como parâmetro
        resposta = deletar(nome)
        if resposta == 1:
            print('Aluno '+nome.upper()+' excluído com sucesso!!\n')
        else:
            print('Aluno não encontrado!!\n')

    continua = input('Deseja continuar executando o programa?[S/N]:')
    # validando a escolha do usuário
    while continua != 's' and continua != 'S' and continua != 'n' and continua != 'N':
        continua = input('Deseja continuar executando o programa?[S/N]:')
