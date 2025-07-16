def generate_js(ast):
    lines = []

    def walk(node, indent=0):
        space = "  " * indent

        if node["type"] == "Program":
            for stmt in node["body"]:
                walk(stmt, indent)

        elif node["type"] == "VariableDeclaration":
            name = node["name"]
            value = generate_expression(node["value"])
            lines.append(f"{space}let {name} = {value};")

        elif node["type"] == "Assignment":
            name = node["name"]
            value = generate_expression(node["value"])
            lines.append(f"{space}{name} = {value};")

        elif node["type"] == "IfStatement":
            condition = generate_expression(node["condition"])
            lines.append(f"{space}if ({condition}) {{")
            for stmt in node["body"]:
                walk(stmt, indent + 1)
            lines.append(f"{space}}}")

        else:
            lines.append(f"{space}// No se reconoce el nodo: {node['type']}")

    def generate_expression(expr):
        if expr["type"] == "Literal":
            return expr["value"]
        elif expr["type"] == "Identifier":
            return expr["value"]
        else:
            return "undefined"

    walk(ast)
    return "\n".join(lines)

# if __name__ == "__main__":
#     from lexer import tokenize
#     from parser import Parser

#     java_code = '''
#     int x = 10;
#     String mensaje = "Hola";
#     x = 5;
#     if (x) {
#         mensaje = "Mundo";
#     }
#     '''

#     tokens = tokenize(java_code)
#     parser = Parser(tokens)
#     ast = parser.parse()
    
#     from generator_js import generate_js
#     js_code = generate_js(ast)
#     print(js_code)
