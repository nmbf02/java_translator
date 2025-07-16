## ✅ Archivo: `docs/language_spec.md`

Este archivo explica:

1. Qué estructuras del lenguaje Java están soportadas.
2. Qué tipo de variables y sentencias reconoce el sistema.
3. Cómo se traducen a JavaScript y C++.
4. Ejemplos comparativos.

---

### 📄 `docs/language_spec.md`

````markdown
# Especificación del Lenguaje - Traductor Java a JS/C++

## 🧠 Introducción

Este documento detalla el subconjunto del lenguaje Java que es reconocido y traducido correctamente por el sistema. También se describen las reglas de transformación hacia JavaScript y C++.

---

## ✅ Estructuras Soportadas (Fase 1)

Actualmente se soportan:

- Declaraciones de variables
- Asignaciones
- Condicionales `if` (sin `else`)
- Literales (números, cadenas)
- Identificadores simples

---

## 📌 Tipos de Datos Reconocidos

| Tipo en Java | Tipo en JavaScript | Tipo en C++     |
|--------------|--------------------|-----------------|
| `int`        | `let` (número)     | `int`           |
| `float`      | `let` (decimal)    | `float`         |
| `double`     | `let` (decimal)    | `double`        |
| `String`     | `let` (cadena)     | `std::string`   |
| `boolean`    | `let` (true/false) | `bool`          |

---

## 📌 Sentencias Reconocidas

### 1. Declaración de Variable

**Entrada en Java:**
```java
int x = 10;
String nombre = "Nathaly";
````

**Salida en JavaScript:**

```js
let x = 10;
let nombre = "Nathaly";
```

**Salida en C++:**

```cpp
int x = 10;
std::string nombre = "Nathaly";
```

---

### 2. Asignación

**Entrada:**

```java
x = 20;
```

**JavaScript:**

```js
x = 20;
```

**C++:**

```cpp
x = 20;
```

---

### 3. Condicional `if` (sin `else` aún)

**Entrada:**

```java
if (x) {
    nombre = "Nuevo";
}
```

**JavaScript:**

```js
if (x) {
  nombre = "Nuevo";
}
```

**C++:**

```cpp
if (x) {
  nombre = "Nuevo";
}
```

---

## 🚫 Limitaciones Actuales

* No se soporta `else`, `while`, `for`, `switch`, clases ni métodos todavía.
* No hay verificación de tipos o errores semánticos.
* Solo se reconoce un archivo de entrada sin dependencias externas.

---

## 📁 Estructura esperada del código

El código Java debe cumplir con las siguientes condiciones:

* Usar punto y coma `;` correctamente.
* No incluir clases o métodos por ahora.
* Declarar y asignar variables fuera de bloques `main()` o `class`.

---

## 📅 Próximas funcionalidades planeadas

* Soporte para `else`, `while`, `for`
* Traducción de métodos simples
* Soporte para clases y objetos
* Traducción completa de archivos `.java`

---

## ✍ Autores

* Traductor desarrollado por Nathaly M. Berroa F.
* Documentación generada automáticamente como parte del sistema

---

## 📄 Versión

* v1.0 - Traducción de estructuras básicas (julio 2025)

