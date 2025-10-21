import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

class ventanaPrincipal:
    def __init__(self, root):
        # Configuración de la ventana
        self.root = root
        self.root.title("Proyecto Final Compilador")
        self.root.geometry("1200x700")

        # Etiqueta para la caja de texto
        self.code_label = tk.Label(root, text = "Escriba su codigo aqui:")
        self.code_label.pack(pady = 10)

        # Widget de texto con scroll
        self.code_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 50, height = 10, font = ("Times New Roman", 16))
        self.code_area.pack(padx = 10, pady = 10)

        # Botón para iniciar el análisis
        self.analyze_button = tk.Button(root, text = "Iniciar Compilación", command = self.run_analysis, font = ("Arial", 14))
        self.analyze_button.pack (pady = 10)

        # Contenedor de las pestañas de los procesos (Notebook)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        #Crear los frames de las pestañas
        self.analisis_lexico = ttk.Frame(self.notebook)
        self.analisis_sintactico = ttk.Frame(self.notebook)
        self.analisis_semantico = ttk.Frame(self.notebook)
        self.codigo_intermedio = ttk.Frame(self.notebook)
        self.optimacion = ttk.Frame(self.notebook)
        self.generacion_codigo_objeto = ttk.Frame(self.notebook)
        self.codigo_objeto = ttk.Frame(self.notebook)
        self.tabla_simbolos = ttk.Frame(self.notebook)
        self.admin_errores = ttk.Frame(self.notebook)

        # Agregar las pestañas al contenedor (Notebook)
        self.notebook.add(self.analisis_lexico, text = "Análisis Léxico")
        self.notebook.add(self.analisis_sintactico, text = "Análisis Sintáctico")
        self.notebook.add(self.analisis_semantico, text = "Análisis Semántico")
        self.notebook.add(self.codigo_intermedio, text = "Código Intermedio")
        self.notebook.add(self.optimacion, text = "Optimación")
        self.notebook.add(self.generacion_codigo_objeto, text = "Generación de Código Objeto")
        self.notebook.add(self.codigo_objeto, text = "Código Objeto")
        self.notebook.add(self.tabla_simbolos, text = "Tabla de Símbolos")
        self.notebook.add(self.admin_errores, text = "Administrador de Errores")

        # Widgets de la pestana Análisis_lexico
        analisis_lexico_label = tk.Label(self.analisis_lexico, text = "Análisis Léxico")
        analisis_lexico_label.pack(pady = 10)
        self.analisis_lexico_output = scrolledtext.ScrolledText(self.analisis_lexico, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.analisis_lexico_output.pack(padx=10, pady=10)

        # Widgets de la pestaña Análisis Sintáctico
        analisis_sintactico_label = tk.Label(self.analisis_sintactico, text = "Análisis Sintáctico")
        analisis_sintactico_label.pack(pady = 10)
        self.analisis_sintactico_output = scrolledtext.ScrolledText(self.analisis_sintactico, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.analisis_sintactico_output.pack(padx=10, pady=10)

        # Widgets de la pestaña Análisis Semántico
        analisis_semantico_label = tk.Label(self.analisis_semantico, text = "Análisis Semántico")
        analisis_semantico_label.pack(pady = 10)
        self.analisis_semantico_output = scrolledtext.ScrolledText(self.analisis_semantico, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.analisis_semantico_output.pack(padx=10, pady=10)

        # Widgets de la pestañana Código Intermedio
        codigo_intermedio_label = tk.Label(self.codigo_intermedio, text="Código Intermedio")
        codigo_intermedio_label.pack(pady=10)
        self.codigo_intermedio_output = scrolledtext.ScrolledText(self.codigo_intermedio, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.codigo_intermedio_output.pack(padx=10, pady=10)

        # Widgets de la pestaña Optimación
        optimacion_label = tk.Label(self.optimacion, text = "Optimación")
        optimacion_label.pack(pady=10)
        self.optimacion_output = scrolledtext.ScrolledText(self.optimacion, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.optimacion_output.pack(padx = 10, pady = 10)

        # Widgets de la pestaña Generación de Código Objeto
        generacion_codigo_objeto_label = tk.Label(self.generacion_codigo_objeto, text="Generación de Código Objeto")
        generacion_codigo_objeto_label.pack(pady=10)
        self.generacion_codigo_objeto_output = scrolledtext.ScrolledText(self.generacion_codigo_objeto, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.generacion_codigo_objeto_output.pack(padx = 10, pady = 10)

        # Widgets de la pestaña Código Objeto
        codigo_objeto_label = tk.Label(self.codigo_objeto, text = "Código Objeto")
        codigo_objeto_label.pack(pady=10)
        self.codigo_objeto_output = scrolledtext.ScrolledText(self.codigo_objeto, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.codigo_objeto_output.pack(padx = 10, pady = 10)

        # Widgets de la pestaña Tabla de Símbolos
        tabla_simbolos_label = tk.Label(self.tabla_simbolos, text = "Tabla de Símbolos")
        tabla_simbolos_label.pack(pady = 10)
        self.tabla_simbolos_output = scrolledtext.ScrolledText(self.tabla_simbolos, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.tabla_simbolos_output.pack(padx = 10, pady = 10)

        # Widgets de la pestaña Administrador de Errores
        admin_errores_label = tk.Label(self.admin_errores, text = "Administrador de Errores")
        admin_errores_label.pack(pady = 10)
        self.admin_errores_output = scrolledtext.ScrolledText(self.admin_errores, wrap = tk.WORD, width = 100, height = 10, font = ("Times New Roman", 16))
        self.admin_errores_output.pack(padx = 10, pady = 10)

    # Métodos de análisis (placeholders)
    def clear_and_insert (self, widget, content):
        """ Función para limpiar y agregar contenido a un widget de texto """
        widget.config (state = 'normal')
        widget.delete ("1.0", tk.END)
        widget.insert (tk.END, content)
        widget.config (state = 'disabled')

    def run_analysis (self):
        """ Método para el boton Iniciar Compilación """
        source_code = self.code_area.get("1.0", tk.END).strip()
        if not source_code:
            self.clear_and_insert(self.analisis_lexico_output, "Por favor, ingrese código para analizar.")
            return
        
        # Ejecucución del Análisis Léxico
        lexical_output = self.perform_lexical_analysis(source_code)

        # Mostrar el resultado en la pestaña de Análisis Léxico
        self.clear_and_insert(self.analisis_lexico_output, lexical_output)
        self.analisis_lexico_output.config(state='normal') # Habilita la edición del widget temporalmente
        self.analisis_lexico_output.insert(tk.END, lexical_output) # Inserta el resultado del analisis léxico
        self.analisis_lexico_output.config(state='disabled') # Deshabilita la edición del widget nuevamente

    def perform_lexical_analysis(self, code):
        # Simulacion de la creacion de tokens
        if not code:
            return "No hay código para analizar"
        
        #Lista de palabras clave y Operadores
        KEYWORDS = ["return", "int", "float", "void", "boolean", "double"]
        OPERATORS = ["+", "-", "*", "/", "^"]
        SIMBOL = ["=", "(", ")"]

        # Dejar espacios entre los operadores y palabras clave
        for op in OPERATORS:
            code = code.replace(op, f' {op} ')

        # Obtener una lista de lexemas
        tokens = [part.strip() for part in code.split() if part.strip()]

        # Generar la salida del análisis léxico
        lexical_output = ""
        for token in tokens:
            if token in KEYWORDS:
                token_type = "PALABRA_CLAVE"
            elif token in OPERATORS:
                token_type = "SIGNO"
            elif token in SIMBOL:
                token_type = "SIMBOLO"
            elif token.isdigit:
                token_type = "NUMERO"
            elif token.isalpha:
                token_type = "VARIABLE"
            else:
                token_type = "DESCONOCIDO"
            lexical_output += f'Token: {token}, Tipo: {token_type}\n'

        return lexical_output

if __name__ == "__main__":
    root = tk.Tk()
    app = ventanaPrincipal(root)
    root.mainloop()