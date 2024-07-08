import re
# Categorías léxicas de Python
categories = {
    'Palabra_reservada': r'(?:(?<!\w)(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)(?!\w))',
    'Operador': r'(?:\+\+?|--?|//|\*\*?|=|=>|<=|>=|==|!=|//?|%|[|&^])',
    'Literal_numerico': r'(?:(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?|0[xX][a-fA-F0-9]+)',
    'Literal_de_cadena': r'(?:(?:"(?:\\.|[^\\"])*")|(?:\'(?:\\.|[^\\\'])*\'))',
    'FunctionCall': r'(?:\w+\()',
    'Identificador': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'Comentario': r'(?:#.*)',
    'Delimitador': r'(?:[:(){}[\],.])',
}
# Expresión regular que coincide con cualquier token
token_regex = re.compile(r'|'.join(r'(?P<%s>%s)' % (name, regex) for name, regex in categories.items()))
def highlight_python_code(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    pColors = ["#FFD700", "#af11ed", "#ed5311", "#3147d6", "#42d631", "#008000", "#000000", "#FFD700", "#00BFFF", "#008000", "#FFD700"]
    html_code = '<pre>\n'
    last_end = 0
    in_function = False
    parentesis = 0

    for match in token_regex.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        start, end = match.span()

        html_code += code[last_end:start]

        # print(token_type,token_value)
        # if (parentesis >0): print("Parentesis es: " , parentesis)

        if ("&" in token_value) or ("<" in token_value) or (">" in token_value) or ('"' in token_value) or ("'" in token_value):
                token_value = token_value.replace("&", "&amp;")
                token_value = token_value.replace("<", "&lt;")
                token_value = token_value.replace(">", "&gt;")
                token_value = token_value.replace('"', "&quot;")
                token_value = token_value.replace("'", "&apos;")

        if token_type == 'Palabra_reservada' and token_value == 'def':
            in_function = True
        elif token_type == 'Palabra_reservada':
            html_code += f'<span class="palabra_reservada">{token_value}</span>'
        elif in_function and token_type == 'FunctionCall':
            html_code += f'<span class="palabra_reservada">def</span> <span class="funcion">{token_value[:-1]}</span><span style="color:{pColors[parentesis]}">(</span>'
            in_function = False
            parentesis += 1
        elif token_type == 'Delimitador' and token_value == ')' and parentesis > 0:
            parentesis -= 1
            html_code += f'<span style="color:{pColors[parentesis]}">)</span>'
        elif token_type == 'Delimitador' and token_value == '(':
            html_code += f'<span style="color:{pColors[parentesis]}">(</span>'
            parentesis += 1
        elif token_type == 'Identificador':
            html_code += f'<span class="variable">{token_value}</span>'
        elif token_type == 'Literal_numerico':
            html_code += f'<span class="numero">{token_value}</span>'
        elif token_type == 'FunctionCall':
            html_code += f'<span class="funcion">{token_value[:-1]}</span><span style="color:{pColors[parentesis]}">(</span>'
            parentesis += 1
        else:
            html_code += f'<span class="{token_type.lower()}">{token_value}</span>'

        last_end = end

    html_code += code[last_end:]
    html_code += '\n</pre>'

    with open(output_file, 'w') as f:
        f.write('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resaltado de código Python</title>
    <style>
        .palabra_reservada { color: #7F0055; font-weight: bold; }
        .operador { color: #ff0000; }
        .literal_numerico { color: #008000; }
        .literal_de_cadena { color: #BA2121; }
        .identificador { color: #000000; }
        .comentario { color: #008000; font-style: italic; }
        .delimitador { color: #000000; }
        .funcion { color: #FFD700; font-weight: bold; }
        .variable { color: #00BFFF; }
        .numero { color: #008000; }
        .functioncall { color: #FFD700; }
        pre { background-color: #F8F8F8; padding: 10px; }
    </style>
</head>
<body>
''')
        f.write(html_code)
        f.write('</body>\n</html>')
# Ejemplo de uso
highlight_python_code('codigo.py', 'codigo_resaltado.html')
