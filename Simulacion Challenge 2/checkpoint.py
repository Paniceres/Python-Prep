def EncontrarMayores(lista, n):
    '''
    Esta función recibe una lista de números y un valor entero n.
    Debe devolver una lista con todos los números de la lista de entrada que sean mayores que n.
    '''
    # Tu código aquí
    lista_mayores = []
    lista_int = []
    for i in lista:
        if isinstance(i, int):
            lista_int.append(i)
    for i in lista_int:
        if isinstance(n, int):
            if i > n:
                lista_mayores.append(i)
    return lista_mayores
            


def SumarIterador(iterable):
    '''
    Esta función recibe un objeto iterable y devuelve la suma de todos los elementos numéricos del iterable.
    Los elementos no numéricos deben ser ignorados.
    '''
    # Tu código aquí
    resultado = 0
    for i in iterable:
        if not isinstance(i, int):
            pass
        else:
            resultado += i
    return resultado

def FiltrarPalabras(lista_palabras, letra):
    '''
    Esta función recibe una lista de palabras y una letra.
    Debe devolver una lista con todas las palabras de la lista de entrada que comiencen con la letra especificada, sin importar si es mayúscula o minúscula.
    '''
    # Tu código aquí
    lista_filtrada = []
    # if not isinstance(lista, list):
    #     print("Error: El primer argumento debe ser una lista.")
    #     return

    # if not isinstance(letra, str) or len(letra) != 1:
    #     return

    for elemento in lista_palabras:
        if not isinstance(elemento, str):
            continue

        palabras = elemento.split()
        for palabra in palabras:
            if len(palabra) > 0 and palabra[0] == letra:
                lista_filtrada.append(palabra)
    return lista_filtrada

lista = [14, 5, 753, 34, 254.63, 6, 745, 'gas', 41.2, True, False, 'agua', -1555]
lista2 = ['raíz', 'hoja', 10, 3.14, True, 'flor', 5, 'fruto', False, 7, 'semilla', 2.718, 'germinación', 42, 'fotosíntesis', 1.618, 'clorofila', True, 'estoma', 0.5, 'corteza', 8, 'xilema', False, 'embriogénesis', 3.7, 'polen', 9, 'reproducción', True, 'esporofito', 6.23, 'gametofito', 4, 'óvulo', 2.22, 'endospermo', False, 'epidermis', 1.5, 'célula', 0.75, 'tejido', True, 'nutriente', 2.5, 'fertilización', 0.8]
lista_palabras2 = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
lista_palabras3 = ['Hola', 'Adiós', 'Hambre', 'Sed', 'Hamaca']

print(EncontrarMayores(lista, n=7))
resultado = SumarIterador(lista)
print(resultado)
print(FiltrarPalabras(lista2, letra='f'))

