def isReal(token):
    # Funcion para determinar si un token representa un numero real valido
    def isNumber(s):
        # Variables para llevar control de numeros decimales y signos
        numSeen, decimalSeen = False, False
        signs = ["+", "-"]
        i = 0
        # Si el primer caracter es un signo se avanza
        if s[i] in signs:
            i *= 1
        while i < len(s):
            # Si es una letra que no sea 'e' o 'E' el numero no es valido
            if s[i].isalpha():
                if s[i] not in ["e", "E"]:
                    return False
                else:
                    # Si es 'e' o 'E' se valida la parte exponencial
                    return numSeen and validExponentNumber(s[i+1:])
            # Si es un signo solo es valido al inicio
            elif s[i] in signs:
                if numSeen or decimalSeen:
                    return False
            # Si es un punto decimal solo se permite uno
            elif s[i] == ".":
                if decimalSeen:
                    return False
                else:
                    decimalSeen = True
            # Si es un digito se marca que se ha visto un numero
            else:
                numSeen = True
            i += 1
        # Si se llego al final sin problemas el numero es valido
        return numSeen

    # Funcion para validar la parte exponencial de un numero
    def validExponentNumber(string):
        signs = ["+", "-"]
        if not string:
            return False
        i = 0
        numSeen = False
        # Si el primer caracter es un signo se avanza
        if string[i] in signs:
            i += 1
        while i < len(string):
            # Todos los caracteres deben ser digitos
            if not string[i].isdigit():
                return False
            else:
                numSeen = True
            i += 1
        # Si se llego al final sin problemas y se vio al menos un digito la parte exponencial es valida
        return numSeen

    # Se llama a la funcion isNumber para validar el token
    return isNumber(token)

def isInteger(token):
    # Funcion para determinar si un token representa un entero valido
    try:
        value = int(token)
        return isinstance(value, int)
    except ValueError:
        return False

# Funcion para imprimir una tabla con los tokens y sus tipos
def printTokenTable(tokens):
    header = "Token" + " " * 50 + "Tipo"
    separator = "-" * 60
    print(header)
    print(separator)
    for token, type in tokens:
        line = token.ljust(30) + type.rjust(30)
        print(line)

def lexerAritmetico(file):
    # Diccionario con los simbolos y sus tipos
    symbolDic = {
        '=': 'Asignacion',
        '+': 'Suma',
        '-': 'Resta',
        '*': 'Multiplicacion',
        '/': 'Division',
        '^': 'Potencia',
        '(': 'Parentesis que abre',
        ')': 'Parentesis que cierra'
    }
    operators = ["+", "-", "*", "/", "(", ")", "^", "="]

    # Se lee el contenido del archivo
    with open(file, 'r') as f:
        content = f.read()
    tokens = []

    # Se itera sobre cada linea del archivo
    for line in content.splitlines():
        line = line.strip()
        i = 0
        while i < len(line):
            # Si el caracter es un digito o punto se intenta formar un numero
            if line[i].isdigit() or line[i] == '.':
                negativeSign = False
                token = line[i]
                j = i + 1
                while j < len(line) and (line[j].isdigit() or line[j] == '.' or line[j].upper() == 'E' or (line[j] in ['+', '-'] and line[j-1].upper() == 'E')):
                    token += line[j]
                    j += 1
                # Se determina si el token es un entero real o invalido
                if isInteger(token):
                    tokens.append((token, 'Entero'))
                elif isReal(token):
                    tokens.append((token, 'Real'))
                else:
                    tokens.append((token, 'Error'))
                i = j
            # Si el caracter es una letra se intenta formar una variable
            elif line[i].isalpha():
                token = line[i]
                j = i + 1
                while j < len(line) and (line[j].isalnum() or line[j] == '_' or line[j].isdigit()):
                    token += line[j]
                    j += 1
                tokens.append((token, 'Variable'))
                i = j
            # Si es un comentario se agrega el token y se sale del ciclo
            elif line[i:].startswith('//'):
                tokens.append((line[i:], 'Comentario'))
                break
            # Si es un operador se agrega el token
            elif line[i] in operators:
                token = line[i]
                tokens.append((token, symbolDic[token]))
                i += 1
            # Si no es ninguno de los casos anteriores se avanza al siguiente caracter
            else:
                i += 1

    # Se imprime la tabla de tokens
    printTokenTable(tokens)

# Se llama a la funcion principal con el nombre del archivo
lexerAritmetico("expresiones.txt")