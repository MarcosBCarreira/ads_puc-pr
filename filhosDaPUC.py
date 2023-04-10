'''
Nome: Marcos Barbosa Carreira
Curso: Tecnologia em Análise e Desenvenvolvimento de Sistemas - EAD Modular
'''
# módulos
import json

# variáveis
# estudante = {}
estudante_base = []  #lista para guardar os estudantes cadastrados - vazia

def sistema_puc():
    while True:  # menu principal junto a este while
        menu_principal()  #imprime menu principal
        # como vi o "try" na lição, tentei usar para controlar a entrada do usuário e não saír do programa por conta de uma entrada inválida...
        try:
            opcao_mp = int(
                input("Digite 1, 2, 3, 4, 5 ou 9, conforme opção desejada: "))  # opcao_mp é "opção do menu principal"
            # tratando as opções do usuário
            if opcao_mp == 1:
                print("\n", "Você escolheu ACESSAR A ÁREA DE ESTUDANTES \n")
                while True:  # submenu operações com estudantes
                    menu_estudante() #imprime menu estudante
                    # tratando as opções do menu do estudante, controlar escolha do user.
                    try:
                        opcao = int(input("Digite 1, 2, 3, 4 ou 9, conforme opção desejada: "))
                        if opcao == 1: #Incluir estudantes
                            print("\n", "Você escolheu a CRIAR um registro de Estudante\n")
                            criar_registro_estudante("estudante")  # chama função para criar o registro do estudante.
                        elif opcao == 2: #Listar estudantes
                            print("\n", "Você escolheu a LISTAR Estudantes\n")
                            listar_registro_estudante("estudante")  # chama a função de listagem dos estudantes.
                        elif opcao == 3: #editar estudantes
                            print()
                            print("Você escolheu a ALTERAR um registro de Estudante\n")
                            editar_registro("estudante") # chama a função de edição dos estudantes
                            input("\n\nPressione ENTER para continuar")
                        elif opcao == 4: #excluir estudantes
                            print("\nVocê escolheu a EXCLUIR um registro de Estudante\n")
                            excluir_estudante()  # chama a função de exclusão dos estudantes
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
                # gravar_estudante(estudante_base)
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


def menu_principal():
    """
    Imprime o menu principal na tela para o usuário fazer sua escolha:\n
    sem parâmetros e sem retorno.
    """
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

def menu_estudante():
    """
    Imprime o menu principal na tela para o usuário fazer sua escolha:\n
    sem parâmetros e sem retorno.
    """
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

def criar_registro_estudante(tipo=None):
    estudante_base = ler_arquivo(tipo)
    """
    Solicita e salva registros informados pelo usuários.

    :sem parâmetros
    :return: Sem retorno
    """
    print("Informe os dados do novo estudante!")
    codigo = int(input("Informe o Código do Estudante: "))
    nome = input("Nome do Estudante: ")
    cpf = input("e CPF: ")
    estudante = {
        "código": codigo,
        "nome": nome,
        "CPF": cpf
    }
    #with open("filhosdapuc_estudantes.json", "r") as f:
    #    estudante_base = json.load(f)
    estudante_base.append(estudante)
    gravar = gravar_registro(estudante_base)
    if gravar == True:
        print("Estudante Cadastrado! ")


def ler_arquivo(tipo=None):
    """
    Lê o arquivo solicitado e guardo numa variável de retorno

    :Tipo de entidade relativa aos dados do sistema: estudantes, professor, alunos
    :return: Retorna uma lista de discionários com os dados lidos.
       """
    if tipo == "estudante":
        try:
            with open("filhosdapuc_estudantes.json", "r") as f:
                estudante_base = json.load(f)
        except IOError:
            return False
    return estudante_base

def listar_registro_estudante(tipo=None):
    """
    Lista na tela dados solicitados a partir da leitura de arquivos da base do sistema

    :Tipo de entidade relativa aos dados do sistema: estudantes, professor, alunos
    :return: Retorna uma lista de discionários com os dados lidos.
    """
    # ler estudantes na base json
    estudante_base = ler_arquivo(tipo)
    if estudante_base == []:
        print()
        print("    Não há estudantes cadastrados!")
        input("\n\nPressione ENTER para continuar")
    elif estudante_base == False:
        print("Arquivo de Cadastros Inexistente. Faça um primeiro cadastro!!!")
    else:
        student_order = 1
        print("-------------- L  I  S  T  A  G  E  M -------------------")
        print("Ord - Código -    Nome              -   CPF  ")
        print("---------------------------------------------------------")
        for estudante in estudante_base:
            print(student_order, "  - ", estudante["código"], "-", estudante["nome"], "   -", f'{estudante["CPF"]:>10}')
            student_order += 1
    input("\n\nPressione ENTER para continuar")


def listar_estudante_especifico(estudante_base):
    estudante_a_listar = int(input("Informe o nome ou código do estudante: "))
    for estudante in estudante_base:
        for chave, valor in estudante.items():
            if estudante_a_listar == valor:
                # return(estudante["código"], "-", estudante["nome"], "CPF:", estudante["CPF"])
                return (estudante)


def editar_registro(tipo=None):
    estudante_base = ler_arquivo(tipo)
    estudante_listado = listar_estudante_especifico(estudante_base)
    student_key = estudante_listado["código"]
    print("Informe novos dado parao estude de código ", student_key)
    nome = input("Novo Nome:")
    cpf = input("Novo CPF:")
    # editando estudante:
    estudante_new = {"código": student_key, "nome": nome, "CPF": cpf}
    index_estudante = estudante_base.index(estudante_listado)
    estudante_base[index_estudante] = estudante_new
    # estudante_base.append(estudante_new)
    gravar_registro(estudante_base)


def excluir_estudante():
    estudante_base = ler_arquivo()
    estudante_listado = listar_estudante_especifico(estudante_base)
    estudante_base.remove(estudante_listado)
    gravar_registro(estudante_base)


def gravar_registro(registro):

    with open("filhosdapuc_estudantes.json", "w+") as f:
        json.dump(registro, f)
        for item in registro:
            f.write(item + "\n")
    return True

# * * * * fim_funções * * * *

#chamando o programa

sistema_puc()
