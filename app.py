    # O programa poderia permitir:
    # Cadastrar pedido
    # Listar pedidos
    # Buscar pedido
    # Alterar status
    # Excluir pedido
    # Sair


from time import sleep

print('Sistema de Gerenciamento doceria')
sleep(1)

# função que mostra menu de escolhas
def menu():
    print('''Escolha uma das opcões abaixo: 
        1 - Cadastrar pedido
        2 - Listar pedidos
        3 - Buscar pedido
        4 - Altera/Atualizar status
        5 - Excluir pedido
        6 - Sair --(0)--
        \n
    ''')

class Pedidos:
    def __init__(self, Nome, Quantidade, Sabor):
        self.nome = Nome
        self.quantidade = Quantidade
        self.sabor = Sabor

# - - lista dos pedidos onde ficará armazenado as instancias dos objetos - - 
lista_de_pedidos = []

# - - função cadastrar pedidos - -
def cadastrar_pedido():
    nome = input('digite o nome do pedido: ') 
    quantidade = input('Digite a quantidade de doces do pedido: ')
    sabor = input('digite o sabor do pedido: ')
    print('\n Pedido cadastrado com sucesso! \n')
    sleep(1)

    pedido = Pedidos(nome, quantidade, sabor)
    lista_de_pedidos.append(pedido)

# - - função que lista os produtos - -
def listar_produtos():

    if lista_de_pedidos:
        for i, p in enumerate(lista_de_pedidos, 1):
            print(f'''
            pedido: {i}
            Nome: {p.nome}
            Quantidade: {p.quantidade}
            Sabor: {p.sabor} 
            \n''')
            sleep(0.8)
    else:
        print('Não existe pedidos para listar! \n')
        sleep(1)
        

# - - loop de escolha do usuário - - 
while True:
    menu()
    escolha_usuario = int(input('Digite a opção que deseja: '))
    match escolha_usuario:
        case 1:
            cadastrar_pedido()
        case 2:
            listar_produtos()
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case 0:
            print('Você escolheu sair! ')
            sleep(1)
            break


#







