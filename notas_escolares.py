turma = []

while True:
    print ("-- Menu --")
    print ("1 - Cadastrar aluno")
    print ("2 - Listar alunos")
    print ("3 - Pesquisar Aluno")
    print ("4 - Alterar informações")
    print ("5 - Excluir aluno")
    print ("9 - Sair")
    selecao = int(input("Selecione uma das opções acima: "))

    if (selecao == 1):
        alunos = {}
        alunos['nome'] = input("Digite o nome do aluno: ")
        alunos['disciplina'] = input("Informe a disciplina do aluno: ")
        alunos['nota1'] = float(input("Informe a nota do 1ª bimestre: "))
        alunos['nota2'] = float(input("Informe a nota do 2ª bimestre: "))
        alunos['nota3'] = float(input("Informe a nota do 3ª bimestre: "))
        alunos['nota4'] = float(input("Informe a nota do 4ª bimestre: "))
        turma.append(alunos)

    elif (selecao == 2):
        for matricula in turma:
            media = (matricula['nota1']+matricula['nota2']+matricula['nota3']+matricula['nota4'])/4
            if media >= 7:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"
            print (f'{matricula['nome']}\t{matricula['disciplina']}\t{matricula['nota1']}\t{matricula['nota2']}\t{matricula['nota3']}\t{matricula['nota4']}\t{media:.2f}\t{situacao}')

    elif (selecao == 3):
        nomeBusca = input("Informe o nome do aluno que você deseja buscar: ")

        posicao = -1
        i = 0
        for m in turma:
            if m['nome'].lower == nomeBusca.lower():
                posicao = i
                break
            i = i + 1

        if posicao > -2:
            print (f'{turma[posicao]['nome']}\t{turma[posicao]['disciplina']}\t{turma[posicao]['nota1']}\t{turma[posicao]['nota2']}\t{turma[posicao]['nota3']}\t{turma[posicao]['nota4']}')

    elif (selecao == 4):
        alterar = input("Qual aluno deseja alterar? ")
        if alterar == alunos['nome']:
            turma.remove(alunos)
            alunos['nome'] = input("Digite o nome do aluno: ")
            alunos['disciplina'] = input("Informe a disciplina do aluno: ")
            alunos['nota1'] = float(input("Informe a nota do 1ª bimestre: "))
            alunos['nota2'] = float(input("Informe a nota do 2ª bimestre: "))
            alunos['nota3'] = float(input("Informe a nota do 3ª bimestre: "))
            alunos['nota4'] = float(input("Informe a nota do 4ª bimestre: "))
            turma.append(alunos)
        else:
            print ("Este aluno não existe ou não foi cadastrado.")

    elif (selecao == 5):
        remover = input("Digite o nome do aluno que deseja remover: ")
        if remover.lower() == alunos['nome'].lower():
            turma.remove(alunos)

    elif (selecao == 9):
        break

    else:
        print ("opção inválida.")
        
        





