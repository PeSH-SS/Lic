produtos = ['salgado','refrigerante','suco','brigadeiro','sorvete','cafe','capuccino','bolinho do zudinho','dadinho']
precos = [4.0,4.50,5.0,0.0,6.0,4.0,6.0,4.50,0.50]

def cantina(produto):
    nomeProduto = produto.lower().strip()
    
    for i in range(len(produtos)):
        if produtos[i] == nomeProduto:
            return precos[i]    

def armazenaFila():
    pessoas = []
    pedidos = []

    contador = 1

    while contador != 8:
        iPessoa = input('seu nome meu patrao, vc ta em {}  na fila: '.format(contador)).strip()
        iPedido = input('numero {} da fila amanda o pedido: '.format(contador)).lower().strip()

        if iPedido in produtos:
            pessoas.append(iPessoa)
            pedidos.append(iPedido)

        

            contador +=1
        else:
            print('nao vende meu chegado')
            
    return [pessoas,pedidos]


def final ():
    fila = armazenaFila()
    listaPessoas = fila[0]
    listaProdutos = fila[1]
    listaPrecos = []
    soma = 0
    
    for i in range(len(listaPessoas)):
        valorProduto = cantina(listaProdutos[i])
        listaPrecos.append(valorProduto)
        soma += valorProduto
        
        
            
        print('{} {} {}'.format(listaPessoas[i],listaProdutos[i],listaPrecos[i]))
    print('Valor final em caixa: {}'.format(soma))

    


        
cabo()
