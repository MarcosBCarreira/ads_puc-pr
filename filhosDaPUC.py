'''
Nome: Marcos Barbosa Carreira
Curso: Tecnologia em Análise e Desenvenvolvimento de Sistemas - EAD Modular
'''
import json


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
            2. Área do professor
            3. Área da disciplina            
            4. Área de turmas
            5. Área de matrícula
            9. Sair do Sistema\n''')


def menu_de_operacoes(f_name, areasys):
    '''
    Imprime o menu principal na tela para o usuário fazer sua escolha:\n
    :param f_name: nome do arquivo
    :param areasys: nome da area no sistema
    :return: None
    '''
    while True:
        print(" \n"*3)
        print("\n", "*" * 60, "\n")
        print(f"    #FILHOS DA PUC -- AREA de {areasys.upper()}")
        print("\n", "*" * 60, "\n")
        print("1 - Fazer Um Novo Registro\n2 - Consultar Registros\n3 - Alterar um Registro\n4 - Excluir um Registro\n9 - Voltar ao Menu Principal")
        print("\n", "*" * 30, "\n")
        try:
            menu_opcao = int(input("Digite 1, 2, 3, 4 ou 9, conforme opção desejada: "))
            if menu_opcao == 1:
                if areasys == "estudante" or areasys == "professor":
                    criar_registro(f_name, areasys)
                else:
                    criar_registro(f_name, areasys)
            elif menu_opcao == 2:
                consultar_registros(f_name, areasys)
                input("Pressione qualquer tecla!!!")
            elif menu_opcao == 3:
                resultado_da_op = editar_registro(f_name, areasys)
                #print(resultado_da_funcao(resultado_da_op))
            elif menu_opcao == 4:
                excluir_registro(f_name, areasys)
            elif menu_opcao == 9:
                print("\nVocê escolheu a VOLTAR AO MENU PRINCIPAL")
                print()
                return
            else:
                input("\n\n opção inválida. Tente novamente!\n\n Pressione ENTER para continuar")
        except ValueError:
            print("\n\nValor inválido")
        except:
            print("\n\nOutro tipo de erro ocorreu!")

def resultado_da_funcao(resultado):
    '''
    Imprime o resultado da função, se houver sucesso ou insucesso...
    :param resultado: Boolean
    :return: uma string.
    '''
    if resultado == False:
        return "\n\n\n\n\t [  Operação NÃO realizada ou Registro não encontrado!!! ]"
    else:
        return "\n\n\n\n\t[  Operação Realizada com Sucesso!!!  ]"


def criar_registro(f_name, areasys):
    '''
    Solicita e cria um novo registro/cadastro
    :param f_name: nome do arquivo
    :param areasys: nome da area no sistema
    :return:
    '''

    registro_new = []
    registros_modulo_lidosJSON = ler_arquivo(f_name)
    if f_name == "professores" or f_name == "estudantes":
        print(f"Informe os dados do novo {areasys}: ")
        codigo = int(input(f"Informe o Código do {areasys}: "))
        jaexiste_rotina = list_registro(registros_modulo_lidosJSON, codigo, areasys)
        if jaexiste_rotina == False:            
            nome = input(f"Digite o nome do {areasys}: ")
            cpf = input("e seu CPF: ")        
            registro_new = {
                "codigo": codigo,
                "nome": nome,
                "CPF": cpf
            }
        else:
            print("Registro já cadastrado!!!")
    elif f_name == "disciplinas":
        codigo = int(input(f"Digite o código da {areasys}: "))
        jaexiste_rotina = list_registro(registros_modulo_lidosJSON, codigo, areasys)
        if jaexiste_rotina == False:            
            nome = input("Digite o nome da disciplina: ")
            registro_new = {
                "codigo": codigo,
                "nome": nome
            }
        else:
            print("\n\n Disciplina já cadastrada!!!\n")
            
    elif f_name == "turmas":
        codigo = int(input(f"Digite o código da {areasys}: "))
        jaexiste_rotina = list_registro(registros_modulo_lidosJSON, codigo, areasys)
        if jaexiste_rotina == False:
            consultar_registros("professores", "professor")
            print("\nEscolha um PROFESSOR na lista acima para sua nova turma!\n")
            codProf = int(input("Digite o código do Professor: "))
            consultar_registros("disciplinas", "disciplina")
            print("\nEscolha uma DISCIPLINA na lista acima para sua nova turma!\n")
            codDisciplina = int(input("Digite o código da Disciplina: "))
            registro_new = {
                "codigo": codigo,
                "codprof": codProf,
                "coddisciplina": codDisciplina
            }
        else:
            print("Turma já cadastrada! Opte por Alterar turma!!!")
    elif f_name == "matriculas":
        consultar_registros("turmas", "turma")
        print("\n\033[31m Escolha uma TURMA na lista acima p/ nova matrícula!\033[m\n")
        codTurma = int(input("Digite o código da Turma: "))
        consultar_registros("estudantes", "estudante")
        print("\n\033[31mEscolha uma ESTUDANTE na lista acima p/ nova matrícula!\033[m\n")
        codEstudante = int(input("Digite o código do Estudante: "))
        #jaexiste_rotina (aqui tem uma rotina específica, pq turma não tem código!)
        for item in registros_modulo_lidosJSON:
            if item["codTurma"] == codTurma and item["codEstudante"] == codEstudante:
                print("Matrícula já cadastrada!!!")
                break
        registro_new = {
            "codTurma": codTurma,
            "codEstudante": codEstudante
        }
    else:
        return False
    #Rotina de gravação dos dados no arquivo.
    if len(registro_new) == 0:
        return 
    else:
        registros_modulo_lidosJSON.append(registro_new)
        print(resultado_da_funcao(gravar_registro(registros_modulo_lidosJSON, f_name)))


def ler_arquivo(f_name=None):
    """
    Lê o arquivo solicitado e guardo numa variável de retorno

    :Tipo de entidade relativa aos dados do sistema: estudantes, professor, alunos
    :return: Retorna uma lista de discionários com os dados lidos.
       """
    registros_modulo_lidosJSON = []
    try:
        with open(f_name+".json", "r") as f:
            registros_modulo_lidosJSON = json.load(f)
            f.close()
    except FileNotFoundError:
        gravar_registro(registros_modulo_lidosJSON, f_name)

    return registros_modulo_lidosJSON

def consultar_registros(f_name, areasys):
    '''

    :param f_name: nome do arquivo
    :param areasys: nome da area no sistema
    :return: Retorna uma lista de discionários com os dados lidos.
    '''

    registros_modulo_lidosJSON = ler_arquivo(f_name) #carrega arquivo cadastro na memória
    if registros_modulo_lidosJSON == []:
        print()
        print(f"    Não há {f_name} cadastrados/as!")
        input("\n\nPressione ENTER para continuar")
    elif areasys == "estudante" or areasys == "professor":
        registro_order = 1
        print("-------------- L  I  S  T  A  G  E  M -------------------")
        print("Ord - Código -    Nome              -   CPF  ")
        print("---------------------------------------------------------")
        for registro in registros_modulo_lidosJSON:
            print(registro_order, "  - ", registro["codigo"], "-", registro["nome"], "   -", f'{registro["CPF"]:>10}')
            registro_order += 1
        #input("\n\nPressione ENTER para continuar")
    else:
        registro_order = 1
        print("-------------- L  I  S  T  A  G  E  M -------------------")
        print(f"\t\t\t* Registros  de  {areasys.upper()}S *")
        print("---------------------------------------------------------")
        for registro in registros_modulo_lidosJSON:
            print(registro_order, registro)
            registro_order += 1
        #input("\n\nPressione ENTER para continuar")

def list_registro(registros_modulo_lidosJSON, codigo, areasys:None):#REFAZER
    '''
    Essa função procura um registro específico a partir de uma lista recebida no 1º parâmetro.
    :param registros_modulo_lidosJSON: lista de dados com dicionários de registros/cadastros
    :param codigo: o código a ser buscado
    :param areasys: opcional (area do sistema)
    :return:
    '''

    for item in registros_modulo_lidosJSON:
        for chave, valor in item.items():
            if codigo == valor:
                return True
    return False


def editar_registro(f_name, areasys):
    '''

    :param f_name:
    :param areasys:
    :return: Se efetivado, retorna nada, mas se não efetivo retorna False
    '''
    registros_modulo_lidosJSON = ler_arquivo(f_name)
    if areasys == "matrícula":
        consultar_registros(f_name, areasys)
        input("\n\nContulte a Matrícula que deseja editar e pressionte ENTER!\n\n")
        print(f"\nInforme os dados a serem ALTERADOS relativos a {areasys}! ")
        codTurma = int(input(f"Digite o código da TURMA: "))
        codEstudante = int(input(f"Digite o código Estudante: "))
        for item in registros_modulo_lidosJSON:
            if item["codTurma"] == codTurma and item["codEstudante"] == codEstudante:
                item["codTurma"] = int(input("Novo Código da Turma: "))
                item["codEstudante"] = int(input("Novo Código do Estudante: "))
                break
    else:
        print(f"\nInforme os dados a serem ALTERADOS relativos a {areasys}! ")
        registro_especifico = int(input(f"Digite o código do/a {areasys} a ser editado/a: "))
        if f_name == "estudantes" or f_name == "professores":
            for item in registros_modulo_lidosJSON:
                if item["codigo"] == registro_especifico:
                    item["nome"] = input("Novo Nome: ")
                    item["CPF"] = input("Novo CPF: ")
                    break
            else:
                return False
        elif f_name == "disciplinas":
            #codigo = int(input(f"Digite o código da {areasys}: "))
            for item in registros_modulo_lidosJSON:
                if item["codigo"] == registro_especifico:
                    item["codigo"] = int(input("Digite o Novo Código: "))
                    item["nome"] = input("Novo Nome: ")
                    break
        elif f_name == "turmas":
            for item in registros_modulo_lidosJSON:
                if item["codigo"] == registro_especifico:
                    item["codigo"] = int(input("Novo Código da Turma: "))
                    item["codprof"] = int(input("Novo Código do Professor da Turma: "))
                    item["coddisciplina"] = int(input("Novo Código da Disciplina: "))
                    break
        else:
            return False

    print(resultado_da_funcao(gravar_registro(registros_modulo_lidosJSON, f_name)))

def excluir_registro(f_name, areasys):
    '''
    Exclui um registro de cadastro (estudante, professor, disciplina, turma, matrícula)
    :param f_name:
    :param areasys:
    :return: None
    '''
    registros_modulo_lidosJSON = ler_arquivo(f_name)

    if areasys != "matricula":
        codigo_reg = int(input(f"Digite o código do/a {areasys} a ser excluido/a: "))
        for item in registros_modulo_lidosJSON:
            if item["codigo"] == codigo_reg:
                registros_modulo_lidosJSON.remove(item)
                print(resultado_da_funcao(gravar_registro(registros_modulo_lidosJSON, f_name)))
                break
        else:
            print("\n\n\n\t [  Registro não encontrado  ]")
    else: #exclusão de matrículas
        codTurma = int(input(f"Digite o código da Turma: "))
        codEstudante = int(input(f"Digite o código do/a Estudante: "))
        for item in registros_modulo_lidosJSON:
            if item["codTurma"] == codTurma and item["codEstudante"] == codEstudante:
                registros_modulo_lidosJSON.remove(item)
                print(resultado_da_funcao(gravar_registro(registros_modulo_lidosJSON, f_name)))
                break
        else:
            print("\n\n\n\t [  Registro não encontrado  ]")


def gravar_registro(registro, f_name):
    '''
    Grava uma lista de registros(dict) em um arquivo JSON.
    :param registro:
    :param f_name:
    :return: Boolean
    '''
    try:
        with open(f_name+".json", "w+") as f:
            json.dump(registro, f)
            return True
    except:
        return False


# * * * * fim_funções * * * *
#---------------------------------------------------------------#
#main
#abaixo nome dos arquivos de cada área do sistemas
nome_arq_prof = "professores"
nome_arq_estudante = "estudantes"
nome_arq_disciplina = "disciplinas"
nome_arq_turma = "turmas"
nome_arq_matric = "matriculas"
while True:  # menu principal junto a este while
    menu_principal()#imprime na tela o MENU PRINCIPAL
    try:
        opcao_mp = int(input("Digite 1, 2, 3, 4, 5 ou 9, conforme opção desejada: "))  # opcao_mp é "opção do menu principal"
        # tratando as opções do usuário
        if opcao_mp == 1:
            menu_de_operacoes(nome_arq_estudante, "estudante")
        elif opcao_mp == 2:
            menu_de_operacoes(nome_arq_prof, "professor")
        elif opcao_mp == 3:
            menu_de_operacoes(nome_arq_disciplina, "disciplina")
        elif opcao_mp == 4:
            menu_de_operacoes(nome_arq_turma, "turma")
        elif opcao_mp == 5:
            menu_de_operacoes(nome_arq_matric, "matrícula")
        elif opcao_mp == 9:
            print("\n\n Saindo...")
            break
        else:
            print("\n\nOpção Inválida!!")
    except ValueError:
        print("\n\nValor inválido")
    except:
        print("\n\nOutro tipo de erro ocorreu!")

