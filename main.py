import tkinter as tk
from tkinter import messagebox, scrolledtext

from lexer import tokenize
from parser import Parser
from generator_js import generate_js
from generator_cpp import generate_cpp

class JavaTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traductor de Java a JS o C++")
        self.root.geometry("800x600")

        # Entrada de código Java
        self.input_label = tk.Label(root, text="Código Java de entrada:")
        self.input_label.pack(pady=(10, 0))

        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
        self.input_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Selección de lenguaje de salida
        self.output_language = tk.StringVar(value="JavaScript")
        self.language_frame = tk.Frame(root)
        self.language_frame.pack(pady=5)

        tk.Label(self.language_frame, text="Traducir a:").pack(side=tk.LEFT)
        tk.Radiobutton(self.language_frame, text="JavaScript", variable=self.output_language, value="JavaScript").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(self.language_frame, text="C++", variable=self.output_language, value="C++").pack(side=tk.LEFT)

        # Botón de traducción
        self.translate_button = tk.Button(root, text="Traducir", command=self.translate_code)
        self.translate_button.pack(pady=10)

        # Área de resultado
        self.output_label = tk.Label(root, text="Código traducido:")
        self.output_label.pack()

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, bg="#f4f4f4")
        self.output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    def translate_code(self):
        java_code = self.input_text.get("1.0", tk.END).strip()
        target_language = self.output_language.get()

        if not java_code:
            messagebox.showwarning("Advertencia", "Por favor ingresa código Java para traducir.")
            return

        try:
            # Fase 1: Tokenización
            tokens = tokenize(java_code)

            # Fase 2: Parsing
            parser = Parser(tokens)
            ast = parser.parse()

            # Fase 3: Generación de código
            if target_language == "JavaScript":
                translated_code = generate_js(ast)
            elif target_language == "C++":
                translated_code = generate_cpp(ast)
            else:
                translated_code = "// Lenguaje no soportado."

            # Mostrar resultado
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated_code)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante la traducción:\n\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = JavaTranslatorApp(root)
    root.mainloop()
