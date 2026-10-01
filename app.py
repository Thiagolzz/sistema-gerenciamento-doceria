    # O programa poderia permitir:
    # Cadastrar pedido
    # Listar pedidos
    # Buscar pedido
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
        4 - Excluir pedido
        0 - Digite (0) para sair
        \n
    ''')

# - - estrutura/esqueleto dos pedidos - -
class Pedidos:
    def __init__(self, Nome, Quantidade, Sabor):
        self.nome = Nome
        self.quantidade = Quantidade
        self.sabor = Sabor

# - - lista dos pedidos onde ficará armazenado as instancias dos objetos - - 
lista_de_pedidos = []

# - - função cadastrar pedidos (1)- -
def cadastrar_pedido():
    while True:
        nome = input('digite o nome do pedido: ')
        sleep(0.8)
        quantidade = input('Digite a quantidade de doces do pedido: ')
        sleep(0.8)
        sabor = input('digite o sabor do pedido: ')
        sleep(0.8)

        # - Atribuição do objeto pedido - 
        if not(nome == '' or quantidade == '' or sabor == ''):
            pedido = Pedidos(nome, quantidade, sabor)
            lista_de_pedidos.append(pedido)
            print('Pedido adicionado com sucesso! ')
            break
        else:
            print('Digite corretamente todos os campos!')


# - - função que lista os produtos (2)- -
def listar_produtos():

    if lista_de_pedidos:
        for i, p in enumerate(lista_de_pedidos, 1):
            print(f'''
            Codigo: {i}
            Nome: {p.nome}
            Quantidade: {p.quantidade}
            Sabor: {p.sabor} 
            \n''')
            sleep(0.8)
    else:
        print('Não existe pedidos para listar! \n')
        sleep(1)

# - - função de buscar um pedido (3)- - 
def buscar_pedido():
    while True:
        pedido_busca = input('Digite o nome do pedido para buscar ou (0) para sair: ')
        if pedido_busca == '0':
            print('Você escolheu sair!')
            break

        for p in lista_de_pedidos:
                if pedido_busca == p.nome:
                    print(f'''
                    nome do pedido: {p.nome}
                    quantidade do pedido: {p.quantidade}
                    sabor do pedido: {p.sabor}
                    ''')   
                    sleep(1)
                    break
                    
        else:
            print('Não foi possivel ')
            sleep(1)

# função de excluir pedido 
def excluir_pedido():
        if not lista_de_pedidos:
            print('Primeiro adicione algum pedido. ')
            sleep(1)
        for p in lista_de_pedidos:
            while True:
                exclusao_pedido = input('Digite o nome do pedido que deseja excluir ou (0) para sair: ')
                if exclusao_pedido == p.nome:
                    print(f'o pedido {p.nome} foi deletado! \n')
                    lista_de_pedidos.remove(p)
                    sleep(1.5)
                    break
                elif exclusao_pedido == '0':
                    print('Você escolheu sair!')
                    sleep(1)
                    break
                else:
                    print('Digite um pedido válido!')
                

        
# - - loop que roda menu e escolha usuario - - 
while True:
    menu()
    escolha_usuario = None
    while True:
        try:
            escolha_usuario = int(input('Digite a opção desejada: '))
            print('\n')
            break
        except ValueError:
            print('Por favor, digite corretamente.')
            sleep(1), print('\n')
            break
         
    match escolha_usuario:
        case 1:
            cadastrar_pedido()
        case 2:
            listar_produtos()
        case 3:
            buscar_pedido()
        case 4:
            excluir_pedido()
        case 0:
            print('Você escolheu sair! ')
            sleep(1)
            break


