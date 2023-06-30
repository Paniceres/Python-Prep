
def comparar_letras(lista, letra):
    if not isinstance(lista, list):
        print("Error: El primer argumento debe ser una lista.")
        return

    if not isinstance(letra, str) or len(letra) != 1:
        return

    for elemento in lista:
        if not isinstance(elemento, str):
            continue

        palabras = elemento.split()
        for palabra in palabras:
            if len(palabra) > 0 and palabra[0] == letra:
                print(f"La letra '{letra}' es la primera letra de la palabra '{palabra}'")


lista2 = ['raíz', 'hoja', 10, 3.14, True, 'flor', 5, 'fruto', False, 7, 'semilla', 2.718, 'germinación', 42, 'fotosíntesis', 1.618, 'clorofila', True, 'estoma', 0.5, 'corteza', 8, 'xilema', False, 'embriogénesis', 3.7, 'polen', 9, 'reproducción', True, 'esporofito', 6.23, 'gametofito', 4, 'óvulo', 2.22, 'endospermo', False, 'epidermis', 1.5, 'célula', 0.75, 'tejido', True, 'nutriente', 2.5, 'fertilización', 0.8]

print(comparar_letras(lista2, letra='f'))