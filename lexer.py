import re

# Lista de palabras clave soportadas
KEYWORDS = {
    "int", "float", "double", "char", "boolean", "String", "if", "else", "while", "for", "return", "class", "public", "static", "void", "new"
}

# Definición de tokens
TOKEN_SPEC = [
    ('NUMBER',   r'\d+(\.\d+)?'),             # Números
    ('STRING',   r'"[^"\n]*"'),               # Cadenas entre comillas dobles
    ('ID',       r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identificadores
    ('OP',       r'==|!=|<=|>=|[+\-*/=<>]'),  # Operadores
    ('BRACE',    r'[{}()\[\];,]'),            # Símbolos especiales
    ('SKIP',     r'[ \t]+'),                  # Espacios y tabulaciones
    ('NEWLINE',  r'\n'),                      # Saltos de línea
    ('MISMATCH', r'.'),                       # Cualquier otro carácter
]

# Compila la expresión regular general
token_re = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC))

def tokenize(code):
    tokens = []
    line_num = 1

    for match in token_re.finditer(code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'NEWLINE':
            line_num += 1
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Carácter inesperado '{value}' en la línea {line_num}")
        elif kind == 'ID' and value in KEYWORDS:
            tokens.append(('KEYWORD', value))
        else:
            tokens.append((kind, value))

    return tokens

# Ejemplo de uso del lexer
# Puedes probar el lexer con un fragmento de código Java o similar
# if __name__ == "__main__":
#     code = '''
#     public class Main {
#         public static void main(String[] args) {
#             int x = 10;
#             if (x > 5) {
#                 System.out.println("Mayor a 5");
#             }
#         }
#     }
#     '''
#     for token in tokenize(code):
#         print(token)