from lexer import tokenize

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def match(self, expected_type, expected_value=None):
        token_type, token_value = self.current()
        if token_type == expected_type and (expected_value is None or token_value == expected_value):
            self.pos += 1
            return token_value
        return None

    def expect(self, expected_type, expected_value=None):
        token = self.match(expected_type, expected_value)
        if token is None:
            raise ParserError(f"Se esperaba {expected_type} {expected_value}, pero se encontró {self.current()}")
        return token

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return {"type": "Program", "body": statements}

    def parse_statement(self):
        token_type, token_value = self.current()

        if token_type == 'KEYWORD' and token_value in {"int", "float", "String"}:
            return self.parse_variable_declaration()
        elif token_type == 'KEYWORD' and token_value == "if":
            return self.parse_if_statement()
        elif token_type == 'ID':
            return self.parse_assignment()
        elif token_type == 'BRACE' and token_value == "}":
            self.pos += 1  # cerrar bloque
            return None
        else:
            raise ParserError(f"Sentencia no reconocida: {self.current()}")

    def parse_variable_declaration(self):
        var_type = self.expect('KEYWORD')
        var_name = self.expect('ID')
        self.expect('OP', '=')
        expr = self.parse_expression()
        self.expect('BRACE', ';')
        return {
            "type": "VariableDeclaration",
            "datatype": var_type,
            "name": var_name,
            "value": expr
        }

    def parse_assignment(self):
        var_name = self.expect('ID')
        self.expect('OP', '=')
        expr = self.parse_expression()
        self.expect('BRACE', ';')
        return {
            "type": "Assignment",
            "name": var_name,
            "value": expr
        }

    def parse_expression(self):
        # Soportamos solo expresiones numéricas simples por ahora: ID | NUMBER | STRING
        token_type, token_value = self.current()
        if token_type in {"NUMBER", "STRING", "ID"}:
            self.pos += 1
            return {
                "type": "Literal" if token_type != "ID" else "Identifier",
                "value": token_value
            }
        raise ParserError(f"Expresión no válida: {self.current()}")

    def parse_if_statement(self):
        self.expect('KEYWORD', 'if')
        self.expect('BRACE', '(')
        condition = self.parse_expression()
        self.expect('BRACE', ')')
        self.expect('BRACE', '{')

        body = []
        while self.current()[1] != '}':
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)

        self.expect('BRACE', '}')
        return {
            "type": "IfStatement",
            "condition": condition,
            "body": body
        }

# Ejemplo de uso del parser
# if __name__ == "__main__":
#     code = '''
#     int x = 10;
#     String nombre = "Nathaly";
#     x = 5;
#     if (x) {
#         nombre = "Hola";
#     }
#     '''
#     tokens = tokenize(code)
#     parser = Parser(tokens)
#     ast = parser.parse()
#     import json
#     print(json.dumps(ast, indent=2))
