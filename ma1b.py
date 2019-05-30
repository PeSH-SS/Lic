with open('ma1b.csv', 'r',encoding='utf-8') as file:
    listamaiorqsete=[]

    for line in file.readlines():
        separado= line.split(',')
        if separado[1]!='nome':
            if separado[6]>='7':
                print('Tirou mais q sete: ',separado[1])
                listamaiorqsete.append(separado[1])


print(listamaiorqsete)

            
        
