#importa a 
import datetime

# Dicionário com os vinhos disponíveis e seus preços
vinhos = {
    'cabernet franc': 70,
    'syrah': 80,
    'grenache': 60,
    'cabernet sauvignon': 100,
    'pinot noir': 120,
    'tinto malbec': 80,
    'tinto merlot': 90,
    'tinto syrah': 100,
    'chardonnay': 80,
    'sauvignon blanc': 70,
    'riesling': 90,
    'pinot grigio': 60
}



carrinho = []  # Lista para armazenar os itens do carrinho
#carronho.pop( [intex] ) -> remove item
#imprime a listas de vinhos
def listar_vinhos():
    print("\nVINHOS DISPONÍVEIS:\n")
    print("\tCATEGORIA: ROSÉS\n")

    for vinho, preco in vinhos.items():

        if vinho in ['cabernet franc', 'syrah', 'grenache']:
            print(f"{vinho} - R${preco}")
    
    print("\n\tCATEGORIA: TINTOS\n")

    for vinho, preco in vinhos.items():
        if vinho in ['cabernet sauvignon', 'pinot noir', 'tinto malbec', 'tinto merlot', 'tinto syrah']:
            print(f"{vinho} - R${preco}")
    print("\n\tCATEGORIA: BRANCOS\n")
    
    for vinho, preco in vinhos.items():
        if vinho in ['chardonnay', 'sauvignon blanc', 'riesling', 'pinot grigio']:
            print(f"{vinho} - R${preco}")

    print('\n')
    comprar_vinhos()


def comprar_vinhos():
    
    vinho = input("Digite o nome do vinho que deseja comprar: \t")
    vinho = vinho.lower()
    quantidade = int(input("Digite a quantidade desejada: \t"))
    if quantidade <=0:
        print("Erro: Valor inválido no arquivo!")
    else: 
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

    print('\n')
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
        q = 0
        for x in carrinho:
            q += x[1]
        if q >= 5:
          total_compra = total_compra - (total_compra * 0.3) #30%
        elif q == 4:
            total_compra *= 0.8 #20%
        elif q == 3:
            total_compra *= 0.9 #10%
            
        print(f"Valor total com desconto: R${total_compra:.2f} \n\n")
    opcao = int(input('Selecione uma opção: \n \t (1)finalizar compra \t(2)apagar carrinho \nOpção: '))

    # Verifica a opção escolhida
    if opcao == 1:
        finalizar_compra()
    elif opcao == 2:
        carrinho.clear()
        print('_________________')
        print('CARRINHO APAGADO')
        print('_________________')

        opcaos()

# def aplicar_desconto(total_compra):
def finalizar_compra():
    print('_____________________')
    print("  FINALIZAR COMPRA:")
    print('_____________________')
    print('\n') 
    nome = input("Digite o nome completo: ")
    email = input("Digite o email: ")
    cpf = input("Digite o CPF: ")
    data_nascimento_str = input("Digite sua data de nascimento (formato: DD-MM-AAAA): ")
    endereco = input("Digite o endereço (rua, número, complemento): ")
    
    data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d-%m-%Y").date()
    #data_atual = datetime.date.today()   - não deu certo com esse methodo
    data_18_anos_atras = datetime.date(2005, 1, 1)
    if data_nascimento <= data_18_anos_atras:
        print('__________________')
        print('COMPRA FINALIZADA!')
        print('__________________')
    else:
        print('\n')
        print('_____________________')
        print('  COMPRA CANCELADA!')
        print('   MENOR DE IDADE ')
        print('_____________________')
    
def opcaos():
    print('\n')
    opcao = int(input('Selecione uma opção: \n \t (1)continuar comprando \t(2)visualizar carrinho \nOpcao:'))
    print('\n')
    # Verifica a opção ecolhida
    match opcao:
        case 1:
            listar_vinhos()
        case 2: 
            visualizar_carrinho()
        case _:                 # default
            print('Opção Inválida')
print('\n\tSeja bem vindo a VINHERIA AGNELLO\n')
listar_vinhos()