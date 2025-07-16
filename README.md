# 🧠 Traductor de Código Java a JavaScript/C++

Este proyecto es un traductor interactivo que convierte código fuente escrito en Java a su equivalente en **JavaScript** o **C++**, utilizando análisis léxico, sintáctico y generación de código desde cero. Incluye una interfaz gráfica amigable construida con **Tkinter (Python)**.

---

## 🚀 Características

✅ Lexer: análisis léxico del código fuente Java  
✅ Parser: construcción de árbol sintáctico abstracto (AST)  
✅ Generadores: conversión a JavaScript o C++  
✅ GUI: interfaz de escritorio con Tkinter  
✅ Documentación técnica incluida  
✅ Código modular y limpio

---

## 🖥️ Captura de la Interfaz (opcional)

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/12e48e7b-d1bf-440a-aaa0-6b7752a1bd7f" />

---

## 📂 Estructura del Proyecto

```

traductor-java/
├── main.py                  # Interfaz gráfica
├── lexer.py                 # Análisis léxico
├── parser.py                # Parser: AST desde tokens
├── generator\_js.py          # Generador de código JS
├── generator\_cpp.py         # Generador de código C++
├── utils.py                 # (Opcional) funciones auxiliares
├── docs/
│   └── language\_spec.md     # Documentación del lenguaje soportado
├── examples/
│   └── hello\_world.java     # Código de prueba en Java
└── README.md                # Este archivo

````

---

## 🧪 Funcionalidad Soportada

El traductor reconoce:

- Declaraciones de variables (`int`, `float`, `String`, etc.)
- Asignaciones (`x = 5;`)
- Condicionales `if (...) { ... }` sin `else` (por ahora)
- Literales (`10`, `"texto"`)
- Identificadores

---

## 🛠️ Tecnologías Utilizadas

- Python 3.9+
- Tkinter (interfaz gráfica)
- Expresiones regulares (`re`) para análisis léxico
- Árboles y estructuras anidadas para parser
- Generadores de código independientes

---

## ▶️ Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/traductor-java.git
cd traductor-java
````

### 2. Ejecutar la interfaz

```bash
python main.py
```

> 💡 Asegúrate de tener **Python 3.9 o superior** instalado en tu sistema.

---

## 💡 Cómo Usar

1. Escribe o pega código Java en la caja superior.
2. Selecciona el lenguaje de salida: **JavaScript** o **C++**
3. Haz clic en **Traducir**
4. El resultado se mostrará en la caja inferior.

---

## 📄 Documentación

Puedes encontrar la documentación detallada del lenguaje soportado en:

```
docs/language_spec.md
```

Incluye ejemplos, equivalencias entre lenguajes y limitaciones actuales.

---

## 🧱 Posibles Mejoras Futuras

* Soporte para `else`, `while`, `for`
* Funciones y clases
* Exportación automática a archivos `.js` o `.cpp`
* Validación semántica
* Empaquetado como ejecutable `.exe` (con PyInstaller)

---

## ✨ Autor

Desarrollado por **Nathaly Michel Berroa Fermín**
📧 [nathalyberroaf@gmail.com](mailto:nathalyberroaf@gmail.com)
