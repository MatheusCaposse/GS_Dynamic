"""
PROBLEMA:
Em busca de conciliar tecnologia com melhoria de vida, criamos um chatbot que permite aos funcionários registrarem
reclamações e sugestões de forma anônima, com o objetivo de melhorar a saúde mental
e o ambiente corporativo.

ENTRADAS:
- Tipo de registro (reclamação ou sugestão);
- Texto digitado pelo usuário.

SAÍDAS:
- Mensagens de confirmação no console;
- Registros salvos no arquivo 'registros.csv';
- Visualização dos registros armazenados.

OBJETIVO:
Facilitar a coleta, o armazenamento e a visualização de feedbacks dos colaboradores,
criando um canal seguro e acessível de comunicação interna.

"""


import csv
import matplotlib.pyplot as plt

def mostrarMenu():
    print("========== BEM VINDO AO CHAT ESPAÇO MENTAL DA EMPRESA FIAP===============")
    print("\n🤖 : Sou o Lyra, chatbot que esta um busca de melhorar a \nsaude mental dos nossos funcionarios\n\n🤖 : como posso te ajudar hoje?\n")
    
    while True:
        print("====================================================")
        print("\n1 - Registrar reclamação\n2 - Registrar sugestão\n3 - Verificar registros\n4 - Gerar grafico\n5 - sair")
        escolha = input("\nUser: ")
        
        if escolha=="1":
            registrar("Reclamação")
        elif escolha =="2":
            registrar("Sugestão")
        elif escolha=="3":
            mostrarRegistros()
        elif escolha=="4":
            mostrarGrafico()
        elif escolha=="5":
            print("🤖 : Até logo!👋")
            break
        else:
            print("🤖 : Escolha uma opção valida\n")
            
def registrar(tipo):
    print(f"🤖 : Certo! sua {tipo.lower()} é muito importante para nós! e ela é \ntotalmente anonima, não se preocupe\n\n🤖 : Qual {tipo.lower()} gostaria de fazer? \n")
    reclamacao = input("User: ")
    def salvarReclamacao(tipo, reclamacao):
        arquivo = "registros.csv"
        try:
            with open(arquivo, mode="a", newline="", encoding="utf-8") as file:
                escritor = csv.writer(file)
            
                escritor.writerow([tipo, reclamacao])

            print("\n🤖 : ✅ Reclamação registrada com sucesso!\n\n")
        except:
            print("\n🤖 : ❌ Erro ao salvar {e} \n")
    salvarReclamacao(tipo, reclamacao)

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x[0] <= pivo[0]]
    maiores = [x for x in lista[1:] if x[0] > pivo[0]]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


def mostrarRegistros():
    arquivo = "registros.csv"
    try:
        with open(arquivo, mode="r", encoding="utf-8") as file:
            leitor = csv.reader(file)
            registros = [linha for linha in leitor if linha]

            if not registros:
                print("🤖 : Nenhum registro encontrado ainda.")
                return

            registros_ordenados = quick_sort(registros)

            print("\n========== REGISTROS ORDENADOS ==========")
            for tipo, texto in registros_ordenados:
                print(f"- {tipo}: {texto}")

    except FileNotFoundError:
        print("🤖 : Nenhum registro encontrado. O arquivo ainda não existe.")
    except Exception as e:
        print(f"🤖 :❌ Erro ao ler os registros: {e}")
        
def mostrarGrafico():
    arquivo = "registros.csv"
    try:
        with open(arquivo, mode="r", encoding="utf-8") as file:
            leitor = csv.reader(file)
            registros = [linha for linha in leitor if linha]

            if not registros:
                print("🤖 : Nenhum registro encontrado ainda.")
                return

            # Conta os tipos
            total_reclamacoes = sum(1 for linha in registros if "reclama" in linha[0].lower())
            total_sugestoes = sum(1 for linha in registros if "sugest" in linha[0].lower())

            # Cria gráfico
            tipos = ["Reclamações", "Sugestões"]
            quantidades = [total_reclamacoes, total_sugestoes]

            plt.bar(tipos, quantidades, color=["red", "green"])
            plt.title("Quantidade de Registros por Tipo")
            plt.xlabel("Tipo de Registro")
            plt.ylabel("Quantidade")
            plt.show()

    except FileNotFoundError:
        print("🤖 : Nenhum registro encontrado. O arquivo ainda não existe.")
    
mostrarMenu()