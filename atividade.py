def coletar_valores(mensagem, valores_possiveis):
    while True:
        valor = input(mensagem).upper()
        if valor in valores_possiveis:
            return valor
        else:
            print('Valor digitado inválido!')

lista = []

while True:
    
    elevador = coletar_valores('Informe o elevador mais utilizado: (A, B ou C): ', ['A', 'B', 'C'])
    periodo = coletar_valores('Informe o período mais utilizado: (M, V ou N): ', ['M', 'V', 'N'])
        
    lista.append([elevador, periodo])    
    
    if (coletar_valores('Deseja continuar? (S/N): ', ['S', 'N']) == "N"):
        break


quantElevadorA = 0;
quantPeriodoMElevadorA = 0
quantPeriodoVElevadorA = 0
quantPeriodoNElevadorA = 0

quantElevadorB = 0;
quantPeriodoMElevadorB = 0
quantPeriodoVElevadorB = 0
quantPeriodoNElevadorB = 0

quantElevadorC = 0;
quantPeriodoMElevadorC = 0
quantPeriodoVElevadorC = 0
quantPeriodoNElevadorC = 0

for item in lista:
    if item[0] =='A':
        quantElevadorA += 1
        if item[1] == 'M':
            quantPeriodoMElevadorA += 1
        if item[1] == 'V':
            quantPeriodoVElevadorA += 1
        if item[1] == 'N':
            quantPeriodoNElevadorA += 1
    if item[0] =='B':
        quantElevadorB += 1
    if item[0] =='C':
        quantElevadorC += 1


if (quantElevadorA >= quantElevadorB) and (quantElevadorA >= quantElevadorC):
    print('Elevador mais utilizado é o A')
    if (quantPeriodoMElevadorA >= quantPeriodoVElevadorA) and (quantPeriodoMElevadorA >= quantPeriodoNElevadorA):
        print('O período mais utilizado do elevador A é Matutino')
    elif (quantPeriodoVElevadorA >= quantPeriodoMElevadorA) and (quantPeriodoVElevadorA >= quantPeriodoNElevadorA):
        print('O período mais utilizado do elevador A é Vespertino')
    elif (quantPeriodoNElevadorA >= quantPeriodoVElevadorA) and (quantPeriodoNElevadorA >= quantPeriodoMElevadorA):
        print('O período mais utilizado do elevador A é Noturno')
elif (quantElevadorB >= quantElevadorA) and (quantElevadorB >= quantElevadorC):
    print('Elevador mais utilizado é o B')
elif (quantElevadorC >= quantElevadorA) and (quantElevadorC >= quantElevadorB):
    print('Elevador mais utilizado é o C')

print('A: ',quantElevadorA)
print('B: ',quantElevadorB)
print('C: ',quantElevadorC)