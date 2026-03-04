def coletar_valores(mensagem, valores_possiveis):
    while True:
        valor = input(mensagem).upper()
        if valor in valores_possiveis:
            return valor
        else:
            print('Valor digitado inválido!')

def calcular_quantidade_elevador(lista, elevador):
    quant = 0
    for item in lista:
        if item[0] == elevador:
            quant += 1
    
    return quant

def verificar_elevador_mais_utilizado(lista):
    quantElevadorA = calcular_quantidade_elevador(lista, 'A');
    quantElevadorB = calcular_quantidade_elevador(lista, 'B');
    quantElevadorC = calcular_quantidade_elevador(lista, 'C');
    if (quantElevadorA >= quantElevadorB) and (quantElevadorA >= quantElevadorC):
        return 'A'
    elif (quantElevadorB >= quantElevadorA) and (quantElevadorB >= quantElevadorC):
      return 'B'
    elif (quantElevadorC >= quantElevadorA) and (quantElevadorC >= quantElevadorB):
       return 'C'

def calcular_quantidade_turno(lista, elevador, turno):
    quant = 0
    for item in lista:
        if ((item[0] == elevador) or (elevador == None)) and (item[1] == turno):
            quant += 1
        
    return quant
        
def verificar_turno_mais_utilizado(lista, elevador):
    quantMatutino = calcular_quantidade_turno(lista, elevador, 'M');
    quantVespertino = calcular_quantidade_turno(lista, elevador, 'V');
    quantNoturno = calcular_quantidade_turno(lista, elevador, 'N');
    
    if (quantMatutino >= quantVespertino) and (quantMatutino >= quantNoturno):
        return 'M'
    elif (quantVespertino >= quantMatutino) and (quantVespertino >= quantNoturno):
        return 'V'
    elif (quantNoturno >= quantMatutino) and (quantNoturno >= quantVespertino):
        return 'N'

lista = []

while True:
    
    elevador = coletar_valores('Informe o elevador mais utilizado: (A, B ou C): ', ['A', 'B', 'C'])
    periodo = coletar_valores('Informe o período mais utilizado: (M, V ou N): ', ['M', 'V', 'N'])
        
    lista.append([elevador, periodo])    
    
    if (coletar_valores('Deseja continuar? (S/N): ', ['S', 'N']) == "N"):
        break


elevador_mais_utilizado = verificar_elevador_mais_utilizado(lista);
print('Elevador mais utilizado é o ' + elevador_mais_utilizado)
turno_mais_utilizado_elevador = verificar_turno_mais_utilizado(lista, elevador_mais_utilizado);
print('O turno mais utilizado do elevador ' + elevador_mais_utilizado + ' é o ' + turno_mais_utilizado_elevador)

periodo_mais_utilizado = verificar_turno_mais_utilizado(lista, None)
print('Turno mais utilizado: ' + periodo_mais_utilizado)



