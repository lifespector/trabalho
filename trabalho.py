class Agenda_Manoel_Ellen_Jaine:
    def __init__(self, nome, email, telefone, idade, endereço):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade
        self.endereço = endereço

    def capitalizar_nome(self):
        self.nome = self.nome.title()

    def pegar_numero(self):
        aux = self.endereço.split()
        numero = int(aux[-1])
        return numero

    def imprimir(self):
        print("===================")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereço}")


agendas = []

def menu():
    print("Programa Agenda - v.1.0")
    print("==============================")
    print("1 - Cadastrar")
    print("2 - Buscar por nome")
    print("3 - Buscar por E-mail")
    print("4 - Buscar por Telefone")
    print("5 - Listar em ordem por Nome")
    print("6 - Listar em ordem por Email")
    print("7 - Listar Maiores de Idade (>18)")
    print("8 - Sair")

def cadastrar():
    nome = input("Informe o nome: ")
    email = input("Informe o E-mail: ")
    telefone = input("Informe o telefone: ")
    idade = input("Informa a idade: ")
    endereço = input("Informe o endereço: ")
    while "@" not in email:
        print("Email inválido.")
        email = input("Informe novamente um email: ")

    agendas.append(Agenda_Manoel_Ellen_Jaine(nome, email, telefone, idade, endereço))
    print("Cadastro realizado.")

def buscar_por_nome():
    achou = False
    nom = input("Digite o nome que procura: ")
    for pessoa in agendas:
        if nom == pessoa.nome:
            pessoa.imprimir()
            achou = True
            break
        if not achou:
            print("Esta pessoa não foi encontrada ou não está cadastrada.")

def buscar_por_email():
    achou = False
    email = input("Digite o E-mail que procura: ")
    for pessoa in agendas:
        if email == pessoa.email:
            pessoa.imprimir()
            achou = True
            break
        if not achou:
            print("Esta pessoa não foi encontrada ou não está cadastrada.")

def buscar_por_endereço():
    achou = False
    end = input("Digite o endereço que procura: ")
    for pessoa in agendas:
        if end == pessoa.endereço:
            pessoa.imprimir()
            achou = True
            break
        if not achou:
            print("Esta pessoa não foi encontrada ou não está cadastrada.")

def listar_em_ordem_por_nome():
    cont = 0
    for pessoa in sorted(agendas, key=lambda pessoa: pessoa.nome):
        cont = cont + 1
        print(f"{cont} - {pessoa.nome}")


def listar_em_ordem_por_email():
    cont = 0
    for pessoa in sorted(agendas, key=lambda pessoa: pessoa.email):
        cont = cont + 1
        print(f"{cont} - {pessoa.email}")

def listar_maiores_de_idade():
    cont = 0
    for pessoa in sorted(agendas, key=lambda pessoa: pessoa.nome):
        if pessoa.idade > 18:
            cont = cont + 1
            print(f"{cont} - {pessoa.nome}")


while True:
    menu()
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        buscar_por_nome()
    elif opcao == 3:
        buscar_por_email()
    elif opcao == 4:
        buscar_por_endereço()
    elif opcao == 5:
        listar_em_ordem_por_nome()
    elif opcao == 6:
        listar_em_ordem_por_email()
    elif opcao == 7:
        listar_maiores_de_idade()
    elif opcao == 8:
        print("Saindo do programa.")
    elif opcao >= 9:
        print("Opção inválida.")


