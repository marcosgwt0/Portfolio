maquina = [['Produtos Disponiveis: '],
[1,'Coca Cola',3.75,2],
[2,'Pepsi',3.67,5],
[3,'Monster',9.96,1],
[4,'Café',1.25,100],
[5,'Redbull',13.99,2]]

def calcTroco(preço,valorComprador):
    cedulas = [200, 100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    troco = valorComprador - preço
    print('Seu troco será composto por: ')
    print('-'*15)
    for x in cedulas:
        qntdCedulas = 0
        if troco >= x:
            qntdCedulas += 1
            print(qntdCedulas,"cedula(s) de:",x)
            print('-'*15)
            troco -= x
    for y in moedas:
        qntdMoedas = 0
        if troco >= y:
            qntdMoedas += 1
            print(qntdMoedas,'moeda(s) de:',y)
            print('-'*15)
            troco -= y
    print('Quantidade do produto restante no estoque: {}'.format(maquina[pedido][3] - 1))
    print('-'*20)

for x in maquina:
    print(x)

print('-'*50)
pedido = int(input('Selecione um produto que deseja comprar: '))
while True:
    if pedido > 0 and pedido < 6 and maquina[pedido][3] >0:
        print('-'*50)
        print('Produto =', maquina[pedido][1],'| Preço =', maquina[pedido][2], '| Quantidade em estoque =', maquina[pedido][3])
        print('-'*50)
        valorComprador = float(input('Digite o valor para adquirir o produto: '))
        if valorComprador < maquina[pedido][2]:
            print('-'*50)
            print("valor insuficiente para comprar o produto.")
            print('-'*50)
        else:
            calcTroco(maquina[pedido][2],valorComprador)
            maquina[pedido][3]-=1
        pedido = int(input('Digite 0 para terminar ou selecione um produto que deseja comprar: '))
        print('-'*20)
    elif pedido == 0:
        break
    else:
        pedido = int(input('Digite um valor valido ou o estoque acabou: '))