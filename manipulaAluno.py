def cadastrar (turma):

    alunos = {}
    alunos['nome'] = input("Digite o nome do aluno: ")
    alunos['disciplina'] = input("Informe a disciplina do aluno: ")
    alunos['nota1'] = float(input("Informe a nota do 1ª bimestre: "))
    alunos['nota2'] = float(input("Informe a nota do 2ª bimestre: "))
    alunos['nota3'] = float(input("Informe a nota do 3ª bimestre: "))
    alunos['nota4'] = float(input("Informe a nota do 4ª bimestre: "))
    turma.append(alunos)

def listar (turma):
    for matricula in turma:
        
        media = (matricula['nota1']+matricula['nota2']+matricula['nota3']+matricula['nota4'])/4
        
        if media >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        
        print (f'{matricula['nome']}\t{matricula['disciplina']}\t{matricula['nota1']}\t{matricula['nota2']}\t{matricula['nota3']}\t{matricula['nota4']}\t{media:.2f}\t{situacao}')

def buscar(turma):
    nomeBusca = input("Informe o nome do aluno que você deseja buscar: ")

    posicao = -1
    i = 0
    for m in turma:
        if m['nome'].lower == nomeBusca.lower():
            posicao = i
            break
        i = i + 1
    return posicao

def alterar_aluno(turma, posicao):
    if posicao > -1:
        turma[posicao]['nome'] = input("Informe o nome do aluno: ")
        turma[posicao]['disciplina'] = input("Informe a disciplina do aluno: ")
        turma[posicao]['1ª bimestre'] = input("Informe a nota do 1ª bimestre do aluno")
        turma[posicao]['2º bimestre'] = input("Informe a nota do 2ª do aluno: ")
        turma[posicao]['3º bimestre'] = input("Informe a nota do 3º bimestre do aluno: ")
        turma[posicao]['4º bimestre'] = input("Informe a nota do 4º bimestre do aluno: ")

    else: 
        print ("Este aluno não existe ou não foi cadastrado.")

def exibir (turma, posicao):
    if posicao > -2:
        print (f'{turma[posicao]['nome']}\t{turma[posicao]['disciplina']}\t{turma[posicao]['nota1']}\t{turma[posicao]['nota2']}\t{turma[posicao]['nota3']}\t{turma[posicao]['nota4']}')
    else:
        print ("Este aluno não existe ou não foi cadastrado.")

def excluir (turma, posicao):
    if posicao > -1:
        turma.pop(posicao)
    else:
        print ("Este aluno não existe ou não foi cadastrado.")
