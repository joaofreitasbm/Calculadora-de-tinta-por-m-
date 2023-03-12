import re
import numpy as np


print('Bem vindo!\n')

# consulta parede
nomeParede =[]
corParede = []
qntParede = []
listaParede = [[nomeParede], [corParede], [qntParede]]
nplistaParede = np.array(listaParede)

# consulta ceramica
nomeSala =[]
ceramSala = []
qntSala = []
listaSala = [[nomeSala], [ceramSala], [qntSala]]
nplistaSala = np.array(listaSala)


while True:
    print('Para calcular:')
    print('Tinta necessária para parede, digite 1')
    print('Cerâmica necessária para piso, digite 2\n')
    print('Ver relatório de calculos já gerados, digite 3\n')
    modo = input('Insira aqui o que você deseja: ')

        # parametros parede
    if modo == '1':
        print('Por gentileza, insira os dados solicitados abaixo.')
        nomeParede.append(input('Nome da parede: '))
        largParede = float(input('Largura da parede em metros: '))
        altParede = float(input('Altura da parede em metros: '))
        corParede.append(input('Cor da tinta a ser usada: '))
        cobertura = float(input('Cobertura por m² informada pelo fabricante da tinta. '))
        tamLata = float(input('Tamanho em litros da lata de tinta que você pretende usar. '))

        areaParede = largParede * altParede
        lataTinta = areaParede / (cobertura * tamLata) 
        qntParede.append(areaParede / (cobertura * tamLata))

        # resultado 
        print('\nA tinta que você escolheu cobre', round(cobertura * tamLata), 'm² por lata.')
        print('Sua parede tem', areaParede, 'm²')
        print('Você precisará de', round((lataTinta) + 0.49), 'lata(s) para cobrir a area de', areaParede, 'm²\n')        

        # parametros piso
    elif modo == '2':
        print('Por gentileza, insira os dados solicitados abaixo.')
        nomeSala.append(input('Nome da sala: '))
        largPiso = float(input('Largura do piso em metros: '))
        compPiso = float(input('Comprimento do piso em metros: '))
        tamPeça = (input('Tamanho da peça de cerâmica (ex. 60x60, 120x120, etc): '))
        ceramSala.append(input('Nome da cerâmica: '))
        peça = re.split('[Xx]', tamPeça)
        areaPeça = (float(peça[0]) * float(peça[1]))/10000
        qntCaixa = float(input('Quantas peças vem por caixa. '))
        areaPiso = float(largPiso) * float(compPiso)
        areaCaixa = round(float(areaPeça) * float(qntCaixa), 2)
        qntSala.append(round(float(areaPiso) / float(areaCaixa) + 0.49))

        # resultado 
        print('\nA cerâmica que você escolheu cobre', areaCaixa, 'm² por caixa.')
        print('Seu piso tem', areaPiso, 'm²')
        print('Você precisará de', round(float(areaPiso) / float(areaCaixa) + 0.49), 'caixa(s) para cobrir a area de', areaPiso, 'm²\n')
    
    elif modo == '3': 
        resultParede = np.transpose(listaParede)
        print('\nDados da parede:')
        print("'nome'","'cor'", "'qnt'")
        for i in resultParede:
            print(*i)
        resultSala = np.transpose(listaSala)
        print('\nDados da sala:')
        print("'nome'","'cor'", "'qnt'")
        for j in resultSala:
            print(*j)
    
    elif modo != '1' or '2' or '3':
        print('Codigo incorreto. Tente novamente.')
    else:
        break