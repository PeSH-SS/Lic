def letras_favoritas(letra, frase):
    h=len(frase)
    p=0
    for i in range(0, h):
        if frase[i].lower()==letra:
         p=p+1
    print('Sua letra favorita:', letra)
    print('Uma frase importante:', frase)
    print('Sua letra favorita é a letra', letra.lower(),'e ela aparece', p,'vezes na fras', frase)

letras_favoritas(letra, frase)
    

           
       
