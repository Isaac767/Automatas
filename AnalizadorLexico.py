import re

# Palabras reservadas 
palabras_reservadas = {
    "if_", "else_", "for_", "proc_", "func_", "return_", "FALSE", "TRUE",
    "main_", "print_", "input_", "num_", "string_", "boolean_"
}

# Operadores
operadores_aritmeticos = {"+", "-", "*", "/"}
operadores_relacionales = {"<", ">", "<=", ">=", "=", "!=", "=="}

# Separadores y símbolos
simbolos = {"(", ")", "{", "}", "[", "]", "\"", "\'"}

# Regex para tokens
regex_token = {
    "identificador": r"^[a-zA-Z_][a-zA-Z_0-9]*$",
    "numero": r"^\d+(\.\d+)?$",
    "cadena": r"^\".*\"$|^'.*'$"
}

def clasificar_token(token):
    if token in palabras_reservadas:
        return "Palabra reservada"
    elif token in operadores_aritmeticos:
        return "Operador aritmetico"
    elif token in operadores_relacionales:
        return "Operador relacional"
    elif token in simbolos:
        return "Simbolo"
    elif re.match(regex_token["numero"], token):
        return "Numero"
    elif re.match(regex_token["cadena"], token):
        return "Cadena"
    elif re.match(regex_token["identificador"], token):
        return "Identificador"
    else:
        return "Error lexico"

def analizar_archivo(ruta): 
    with open(ruta, 'r') as archivo:
        linea_n = 0
        for linea in archivo:
            linea_n += 1
            tokens = re.findall(r"[a-zA-Z_][a-zA-Z_0-9]*|\d+\.\d+|\d+|\".*?\"|'.*?'|==|!=|<=|>=|[^\s]", linea)
            print(f"\nLínea {linea_n}: {linea.strip()}")
            for token in tokens:
                tipo = clasificar_token(token)
                if tipo != "Error lexico":
                    print(f"  Es válido: {token} ➜ {tipo}")
                else:
                    print(f"  Error lexico: {token}")


archivo_fuente = r"C:/Users/User\Desktop/RepositorioIntegrador/ingweb/oli/Prueba.txt"

analizar_archivo(archivo_fuente)