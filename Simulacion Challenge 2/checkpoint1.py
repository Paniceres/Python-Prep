def ordenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario_par: Diccionario a ordenar.
        clave: Clave del diccionario recibido, por la cual ordenar.
        descendente: Un valor booleano, que al ser verdadero indica ordenamiento descendente y 
                     ascendente si es falso. Por defecto es True.
    Si el parámetro diccionario_par no es un diccionario o el parámetro clave no se encuentra 
    entre las claves del diccionario, debe devolver None.
    Ejemplo:
        dicc = {'clave1': ['c', 'a', 'b'],
                'clave2': ['casa', 'auto', 'barco'],
                'clave3': [1, 2, 3]}
        ordenarDiccionario(dicc, 'clave1')          debe retornar {'clave1': ['a', 'b', 'c'],
                                                                'clave2': ['auto', 'barco', 'casa'],
                                                                'clave3': [2, 3, 1]}
        ordenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1': ['b', 'a', 'c'],
                                                                'clave2': ['barco', 'auto', 'casa'],
                                                                'clave3': [1, 2, 3]}
    '''
    if not isinstance(diccionario_par, dict) or clave not in diccionario_par:
        return None
    
    valores_clave = diccionario_par[clave]
    pares_clave_valor = zip(valores_clave, *diccionario_par.values())
    pares_ordenados = sorted(pares_clave_valor, key=lambda x: x[0], reverse=descendente)
    indices_ordenados = [i for i, _ in pares_ordenados]

    diccionario_ordenado = {}
    for clave_actual, valores in diccionario_par.items():
        diccionario_ordenado[clave_actual] = [valores[i] for i in indices_ordenados]

    return diccionario_ordenado