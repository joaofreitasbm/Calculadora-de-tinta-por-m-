from decimal import *
import re

print('Bem vindo!\n')

def loop():
    print('Para calcular:')
    print('Tinta necessária para parede, digite 1')
    print('Cerâmica necessária para piso, digite 2\n')
    modo = input('Insira aqui o que você deseja: ')

    if modo == '1':
        print('Por gentileza, insira os dados solicitados abaixo. Use apenas numeros.')

        # parametros parede
        largParede = float(input('Largura da parede em metros: '))
        altParede = float(input('Altura da parede em metros: '))
        cobertura = float(input('Cobertura por m² informada pelo fabricante da tinta. '))
        tamLata = float(input('Tamanho em litros da lata de tinta que você pretende usar. '))

        areaParede = largParede * altParede
        lataTinta = areaParede / (cobertura * tamLata)

        # resultado corrigido
        print('\nA tinta que você escolheu cobre', round(cobertura * tamLata), 'm² por lata.')
        print('Sua parede tem', areaParede, 'm²')
        print('Você precisará de', round((lataTinta) + 0.5), 'lata (s) para cobrir a area de', areaParede, 'm²\n')

    elif modo == '2':
        print('Por gentileza, insira os dados solicitados abaixo. Use apenas numeros.')

        # parametros piso
        largPiso = Decimal(input('Largura do piso em metros: '))
        compPiso = Decimal(input('Comprimento do piso em metros: '))
        tamPeça = (input('Tamanho da peça de cerâmica (ex. 60x60, 120x120, etc): '))
        peça = re.split('[Xx]', tamPeça)
        areaPeça = (Decimal(peça[0]) * Decimal(peça[1]))/10000
        qntCaixa = Decimal(input('Quantas peças vem por caixa. '))
        areaPiso = Decimal(largPiso) * Decimal(compPiso)
        areaCaixa = round(float(areaPeça) * float(qntCaixa), 2)

        # resultado corrigido
        print('\nA cerâmica que você escolheu cobre', areaCaixa, 'm² por caixa.')
        print('Seu piso tem', areaPiso, 'm²')
        print('Você precisará de', round(float(areaPiso) / float(areaCaixa) + 0.5), 'caixas (s) para cobrir a area de', areaPiso, 'm²\n')

    elif modo != '1' or '2':
        print('Codigo incorreto. Tente novamente.')
while True:
    loop()