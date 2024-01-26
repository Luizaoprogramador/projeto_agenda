from utils import menu
from manipulaAluno import alterar_aluno, cadastrar, excluir, exibir, listar, buscar

turma = []

while True:
    menu()
    selecao = int(input("Selecione uma das opções acima: "))

    if (selecao == 1):
        cadastrar(turma)

    elif (selecao == 2):
        listar(turma)

    elif (selecao == 3):
        posicao = buscar(turma)
        exibir (turma, posicao)
    elif (selecao == 4):
        posicao = buscar(turma)
        alterar_aluno(turma, posicao)

    elif (selecao == 5):
        posicao = buscar(turma)
        excluir (turma, posicao)

    elif (selecao == 9):
        break

    else:
        print ("opção inválida.")
        
        





