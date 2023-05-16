# Dicionário com os vinhos disponíveis e seus preços
vinhos = {
    'Cabernet Franc': 70,
    'Syrah': 80,
    'Grenache': 60,
    'Cabernet Sauvignon': 100,
    'Pinot Noir': 120,
    'Tinto Malbec': 80,
    'Tinto Merlot': 90,
    'Tinto Syrah': 100,
    'Chardonnay': 80,
    'Sauvignon Blanc': 70,
    'Riesling': 90,
    'Pinot Grigio': 60
}

carrinho = []  # Lista para armazenar os itens do carrinho
#imprime a listas de vinhos
def listar_vinhos():
    print("\nVINHOS DISPONÍVEIS:\n")
    print("\tCATEGORIA: ROSÉS\n")

    for vinho, preco in vinhos.items():

        if vinho in ['Cabernet Franc', 'Syrah', 'Grenache']:
            print(f"{vinho} - R${preco}")

    print("\n\tCATEGORIA: TINTOS\n")

    for vinho, preco in vinhos.items():
        if vinho in ['Cabernet Sauvignon', 'Pinot Noir', 'Tinto Malbec', 'Tinto Merlot', 'Tinto Syrah']:
            print(f"{vinho} - R${preco}")
    print("\n\tCATEGORIA: BRANCOS\n")

    for vinho, preco in vinhos.items():
        if vinho in ['Chardonnay', 'Sauvignon Blanc', 'Riesling', 'Pinot Grigio']:
            print(f"{vinho} - R${preco}")

    print('\n')
    comprar_vinhos()


def comprar_vinhos():

    vinho = input("Digite o nome do vinho que deseja comprar: \t")
    quantidade = int(input("Digite a quantidade desejada: \t"))

    if vinho in vinhos:
        preco_total = vinhos[vinho] * quantidade
        carrinho.append((vinho, quantidade, preco_total))
        print('________________________________________')
        print("Item adicionado ao carrinho com sucesso!")
        print('________________________________________')
    else:
        print("Vinho indisponível.")
    
    opcaos()
    


def visualizar_carrinho():

    print('_____________________')
    print("CARRINHO DE COMPRAS:")
    print('_____________________')
    print('\n')

    total_compra = 0
    for item in carrinho:
        vinho, quantidade, preco_total = item
        print(f"{vinho} - Quantidade: {quantidade} - Preço total: R${preco_total}")
        total_compra += preco_total

    if len(carrinho) > 0:
        #aplicar_desconto(total_compra)
        """ 
        • Na compra de 3 garrafas,o cliente receberá um desconto de 10%. 
        • Na compra de 4 garrafas,o cliente receberá um desconto de 20%.
        • Na compra de 5 ou mais garrafas,o cliente receberá um descontode 30%.

        """
        if len(carrinho) >= 5:
            total_compra *= 0.7
        elif len(carrinho) >= 4:
            total_compra *= 0.8
        elif len(carrinho) >= 3:
            total_compra *= 0.9
        print(f"Valor total com desconto: R${total_compra:.2f}")
    opcao = int(input('Selecione uma opção: \n \t (1)finalizar compra \t(2)listar vinhos \nOpção: '))

    # Verifica a opção escolhida
    if opcao == 1:
        finalizar_compra()
    elif opcao == 2:
        listar_vinhos()

# def aplicar_desconto(total_compra):
def finalizar_compra():
    print('_____________________')
    print("FINALIZAR COMPRA:")
    print('_____________________')
    nome = input("Digite o nome completo: ")
    email = input("Digite o email: ")
    cpf = input("Digite o CPF: ")
    data_nascimento = input("Digite ano da data de nascimento ")
    endereco = input("Digite o endereço (rua, número, complemento): ")
    print('COMPRA FINALIZADA!')
    #for data_nacimento in range(0,18):
       # print('IDADE MENOR')
        #break
def opcaos():
    print('\n')
    opcao = int(input('Selecione uma opção: \n \t (1)comprar_vinhos \t(2)visualizar_carrinho \nOpcao:'))

    # Verifica a opção ecolhida
    match opcao:
        case 1:
            comprar_vinhos()
        case 2: 
            visualizar_carrinho()
        case _:                 # default
            print('Opção Inválida')
print('\n\tSeja bem vindo a VINHERIA AGNELLO\n')
listar_vinhos()