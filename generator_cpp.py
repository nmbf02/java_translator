def generate_cpp(ast):
    lines = []

    def walk(node, indent=0):
        space = "  " * indent

        if node["type"] == "Program":
            for stmt in node["body"]:
                walk(stmt, indent)

        elif node["type"] == "VariableDeclaration":
            c_type = map_type(node["datatype"])
            name = node["name"]
            value = generate_expression(node["value"])
            lines.append(f"{space}{c_type} {name} = {value};")

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
            lines.append(f"{space}// Nodo desconocido: {node['type']}")

    def map_type(java_type):
        mapping = {
            "int": "int",
            "float": "float",
            "double": "double",
            "String": "std::string",
            "boolean": "bool"
        }
        return mapping.get(java_type, "auto")

    def generate_expression(expr):
        if expr["type"] == "Literal":
            val = expr["value"]
            if val.startswith('"') and val.endswith('"'):
                return val
            elif val.isdigit():
                return val
            else:
                try:
                    float(val)
                    return val
                except:
                    return f'"{val}"'
        elif expr["type"] == "Identifier":
            return expr["value"]
        else:
            return "/*expr*/"

    walk(ast)
    return "\n".join(lines)

#     print(js_code)
# if __name__ == "__main__":
#     from lexer import tokenize
#     from parser import Parser

#     code = '''
#     int edad = 20;
#     String nombre = "Nathaly";
#     edad = 25;
#     if (edad) {
#         nombre = "Berroa";
#     }
#     '''

#     tokens = tokenize(code)
#     parser = Parser(tokens)
#     ast = parser.parse()

#     from generator_cpp import generate_cpp
#     cpp_code = generate_cpp(ast)
#     print(cpp_code)
