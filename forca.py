from random import randint
#variaveis
erros = [ ]
letras_descobertas = [ ]
fruta = ['uva', 'banana', 'manga']
objetos= ['garfo','celular', 'escada',]
nomes = ['wesley','bruno', 'ana']

print('==== jogo da forca ====\n')

#escolha da palavra
while True:
    opcao = input('\n1- frutas\n2- objetos\n3- nomes (pessoais)\nescolha uma opção para gera a palavra:')
    if opcao == '1':
        descobrir = fruta[randint(0, 2)].strip().lower()
        print('palavra gerada, agora tente acerta!!!')
        break
    if opcao == '2':
        descobrir = objetos[randint(0, 2)].strip().lower()
        print('palavra gerada, agora tente acerta!!!')
        break
    if opcao == '3':
        descobrir = nomes[randint(0, 2)].strip().lower()
        print('palavra gerada, agora tente acerta!!!\n')
        break
   
#função print
def mostra_letras():
    for x in range(len(letras_descobertas)):
        print(letras_descobertas[x],end=" ")

tentativas = len(descobrir)

for x in range(len(descobrir)):
    letras_descobertas.append("_")

for _ in range(tentativas):
    mostra_letras()
    descoberta = False
    print(f'\nerros:{erros} tentativas:{tentativas}')
    letra = input('digite uma letra:').strip().lower()

    if len(letra) > 1:
        resposta_1 = input('você deseja chutar a palavra? [S/N]:').lower()
        if resposta_1 in ['s', 'sim']:
            resposta_2 = input(f'você ainda tem {tentativas} restnates\nvocê tem certeza que deseja chutar? [s/n]').lower()
            if resposta_2 in ['s', 'sim,', 'claro']:
                if letra == descobrir:
                    print(f'parabens você acertou a palavra era {descobrir}')
                    print('==== fim de jogo ====')
                    break
                else:
                    print('\nerrou, infelizmente você perdeu\n')
                    print('==== fim de jogo ====')
                    break
        if resposta_1 in ['n', 'nao','não']:
            continue

    if letra in erros or letra in letras_descobertas:
        print(f'\nletra {letra.upper()} ja foi dita.\n')
    
    else:
        for x in range(0, len(descobrir)):
            if letra in descobrir[x]:
                print(f'\nletra {letra.upper()} descoberta!\n')
                letras_descobertas[x] = letra
                descoberta = True

        #verificar se tem a letra
        if descoberta is False:
            print(f'\nnâo tem a letra {letra.upper()} na palavra\n')
            tentativas -= 1
            erros.append(letra)

    #vitoria
    if '_' not in letras_descobertas:
        print(f'\nparabens você venceu a palavra era {descobrir.upper()}.\n')
        break

    #derrota  
    elif tentativas == 0:
        print(f'\ninfelizmente suas chances acabaram\n')
        print('==== fim de jogo ====')
        break