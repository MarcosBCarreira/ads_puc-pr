'''
Nome: Marcos Barbosa Carreira
Curso: Tecnologia em Análise e Desenvenvolvimento de Sistemas - EAD Modular
'''

import json

estudante_base = []  #lista para guardar os estudantes cadastrados - vazia
#lista estudante para testes:
'''
estudante_base = [
        {'código': 23001, 'nome': 'Marcos Barbosa Carreira', 'CPF': '222.222.333-44'},
        {'código': 23002, 'nome': 'Pedro da Silva Sauro', 'CPF': '333.333.444-55'},
        {'código': 23003, 'nome': 'Leidiane Guga ', 'CPF': '414.444.555-66'},
        {'código': 23004, 'nome': 'Celia Carreira', 'CPF': '888.888.999-00'},
        {'código': 23005, 'nome': 'Felipe Santos Carreira', 'CPF': '555.444.999-00'},
        {'código': 23006, 'nome': 'Guga da Silva Sauro', 'CPF': '85.855.955-00'} ]
'''
estudante = {}

def menu():
    while True: #menu principal junto a este while
        print("\n", "*" * 60, "\n")
        print(" # F I L H O S   D A   P U C -- M E N U   P R I N C I P A L")
        print("\n", "*" * 60, "\n")
        print('''   FILHOS DA PUC - SYSTEM \n 
        1. Área do Estudante
        2. Área da disciplina
        3. Área do professor
        4. Área de turmas
        5. Área de matrícula
        9. Sair do Sistema\n''')
        #como vi o "try" na lição, tentei usar para controlar a entrada do usuário e não saír do programa por conta de uma entrada inválida...
        try:
            opcao_mp = int(input("Digite 1, 2, 3, 4, 5 ou 9, conforme opção desejada: ")) #opcao_mp é "opção do menu principal"
            # tratando as opções do usuário
            if opcao_mp == 1:
                print("\n", "Você escolheu ACESSAR A ÁREA DE ESTUDANTES \n")
                while True: #submenu operações com estudantes
                    print(" \n" * 80)
                    print("\n", "*" * 60, "\n")
                    print("    #FILHOS DA PUC -- MENU ESTUDANTES")
                    print("\n", "*" * 60, "\n")
                    print("1 - Registrar estudante")
                    print("2 - Listar estudante")
                    print("3 - Alterar estudante")
                    print("4 - Excluir estudante")
                    print("9 - Voltar ao Menu Principal")
                    print("\n", "*" * 30, "\n")
                    # tratando as opções do menu do estudante, controlar escolha do user.
                    try:
                        opcao = int(input("Digite 1, 2, 3, 4 ou 9, conforme opção desejada: "))
                        if opcao == 1:
                            print("\n", "Você escolheu a CRIAR um registro de Estudante\n")
                            criar_registro_estudante()  # chama função para criar o registro do estudante.
                        elif opcao == 2:
                            print("\n", "Você escolheu a LISTAR Estudantes\n")
                            listar_registro_estudante()   #chama a função de listagem dos estudantes.
                        elif opcao == 3:
                            print()
                            print("Você escolheu a ALTERAR um registro de Estudante\n")
                            print("EM DESENVOLVIMENTO...")
                            editar_estudante()
                            input("\n\nPressione ENTER para continuar")
                        elif opcao == 4:
                            print("\nVocê escolheu a EXCLUIR um registro de Estudante\n")
                            print("EM DESENVOLVIMENTO...")
                            excluir_estudante()
                            input("\n\nPressione ENTER para continuar")
                        elif opcao == 9:
                            print("\nVocê escolheu a VOLTAR AO MENU PRINCIPAL")
                            print()
                            break
                        else:
                            input("\n\n opção inválida. Tente novamente!\n\n Pressione ENTER para continuar")
                    except ValueError:
                        print("\n\nValor inválido")
                    except:
                        print("\n\nOutro tipo de erro ocorreu!")
            elif opcao_mp == 2:
                print("\n", "*" * 60, "\n")
                print("    #FILHOS DA PUC -- AREA DISCIPLINAS")
                print("\n", "*" * 60, "\n")
                print("\nEM DESENVOLVIMENTO...")
                input("\n\nPressione ENTER para continuar")
                pass
            elif opcao_mp == 3:
                print("\n", "*" * 60, "\n")
                print("    #FILHOS DA PUC -- AREA PROFESSOR")
                print("\n", "*" * 60, "\n")
                print("\nEM DESENVOLVIMENTO...")
                gravar_estudante(estudante_base)
                input("\n\nPressione ENTER para continuar")
                pass
            elif opcao_mp == 4:
                print("\n", "*" * 60, "\n")
                print("    #FILHOS DA PUC -- AREA TURMAS")
                print("\n", "*" * 60, "\n")
                print("\nEM DESENVOLVIMENTO...")
                input("\n\nPressione ENTER para continuar")
                pass
            elif opcao_mp == 5:
                print("\n\nAréa de MATRÍCULAS")
                print("EM DESENVOLVIMENTO...")
                input("Pressione ENTER para continuar")
                pass
            elif opcao_mp == 9:
                print("\n\n Saindo...")
                break
            else:
                print("\n\nOpção Inválida!!")
        except ValueError:
            print("\n\nValor inválido")
        except:
            print("\n\nOutro tipo de erro ocorreu!")

def criar_registro_estudante():
    print("Informe os dados do novo estudante!")
#SEMANA - 5
    codigo = int(input("Informe o Código do Estudante: "))
    nome = input("Nome do Estudante: ")
    cpf = input("e CPF: ")
    estudante = {
      "código": codigo,
      "nome": nome,
      "CPF": cpf
    }
    estudante_base.append(estudante)
#semana 4
    # estudante_base.append(input("Informe o Nome do Estudante: "))
    print("Estudante Cadastrado! ")

def listar_registro_estudante():

    # ler valor_pi de um arquivo json
    with open("filhosdapuc_estudantes.json", "r") as f:
        estudantes_lido = json.load(f)
        print(f'{estudantes_lido}, tipo {type(estudantes_lido)}')
    '''
    if estudante_base == []:
        print()
        print("    Não há estudantes cadastrados!")
        input("\n\nPressione ENTER para continuar")
    else:
        student_order = 1
        print("-------------- L  I  S  T  A  G  E  M -------------------")
        print("Ord - Código -    Nome              -   CPF  ")
        print("---------------------------------------------------------")
#semana4:
        # for estudante in estudante_base:
        #     print(cont, "-", estudante)
        #     cont += 1
#semana5:
        for estudante in estudante_base:
            #print(" ", student_order, "-", "Código:", estudante["código"], "-", "Nome:", estudante["nome"], "-",  "CPF:", estudante["CPF"])
            print(student_order, "  - ", estudante["código"], "-", estudante["nome"], "   -", estudante["CPF"])
            student_order += 1
'''
    input("\n\nPressione ENTER para continuar")

def listar_estudante_especifico(estudante_base):
    estudante_a_listar = int(input("Informe o nome ou código do estudante: "))
    for estudante in estudante_base:
        for chave, valor in estudante.items():
            if estudante_a_listar == valor:
                #return(estudante["código"], "-", estudante["nome"], "CPF:", estudante["CPF"])
                return(estudante)




def editar_estudante():
    estudante_listado = listar_estudante_especifico(estudante_base)
    student_key = estudante_listado["código"]

    # for estudante in estudante_base:
    #     if estudante["código"] == estudante_listado["código"]:
    print("Informe novos dado parao estude de código ", student_key)
    nome = input("Novo Nome:")
    cpf  = input("Novo CPF:")

    #editando estudante:
    estudante_new = {
        "código": student_key,
        "nome": nome,
        "CPF": cpf
    }

    index_estudante = estudante_base.index(estudante_listado)
    estudante_base[index_estudante] = estudante_new
    #estudante_base.append(estudante_new)
    gravar_estudante(estudante_base)

def excluir_estudante():
    estudante_listado = listar_estudante_especifico(estudante_base)

    estudante_base.remove(estudante_listado)

def gravar_estudante(estudantes):
    '''
    em andamento/nao funcional... pesquisar se dá pra gravar list em Json... acho q só dicionário. Pesquisei pra gravar
    arquivos json na internet... mas não consegui implementar... mas não é para esta semana!

    *****exemplo do professor Willington******
    with open("valor_pi.json", "w") as f:
    json.dump(valor_pi, f)   '''

    with open("filhosdapuc_estudantes.json", "w") as f:
        json.dump(estudantes, f)


        for estudante in estudantes:
            f.write(estudante + "\n")


def testando():
    estudante_base = [{'código': 20230001, 'nome': 'Marcos Barbosa Carreira', 'CPF': '222.222.333-44'}, {'código': 20230002, 'nome': 'Pedro da Silva Sauro', 'CPF': '333.333.444-55'}, {'código': 20230003, 'nome': 'Leidiane Guga ', 'CPF': '414.444.555-66'}, {'código': 20230004, 'nome': 'Celia Carreira', 'CPF': '888.888.999-00'}]
    #listar_registro_estudante(estudante_base)
    print(listar_estudante_especifico(estudante_base))

# * * * * fim_funções * * * *

#testando()
menu()
