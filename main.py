import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import token

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

    def perform_lexical_analysis(self, code):
        """
        Simula el análisis léxico, identificando tokens únicos y
        ordenándolos por tipo: Variables, Signos, Símbolos, Números.
        """
        if not code:
            return "No hay código para analizar"

        # 1. Definición de Tipos y Grupos de Tokens
        KEYWORDS = {"return", "int", "float", "void", "boolean", "double"}
        # CAMBIO CLAVE: Usamos un diccionario para mapear el SIGNO a su NOMBRE
        OPERATORS_MAP = {
            "+": "ADICIÓN",
            "-": "SUSTRACCIÓN",
            "*": "PRODUCTO",
            "/": "COCIENTE",
            "^": "ACENTO CIRCUNFLEJO",
        }
        OPERATORS = set(OPERATORS_MAP.keys()) # Creamos el conjunto de signos a partir de las claves del diccionario        
        INDIVIDUAL_SIMBOLS = {"="}
        
        AGRUPATION_TOKEN = "()"
        AGRUPATION_NAME = "AGRUPACIÓN"

        code = code.replace("{", " ") # Reemplazamos llaves de apertura con espacio (para ignorarlas)
        code = code.replace("}", " ") # Reemplazamos llaves de cierre con espacio (para ignorarlas)
        code = code.replace("()", f" {AGRUPATION_TOKEN} ")
        
        # 2. Preprocesamiento: Separar los tokens por espacios.
        # Se reemplazan operadores/símbolos con espacios para que la función split los separe.
        for op in OPERATORS | INDIVIDUAL_SIMBOLS: # Usamos UNION (|) de sets para los reemplazos
            code = code.replace(op, f" {op} ")
            
        # Usamos split() para obtener los lexemas (tokens) reales.
        tokens = [part.strip() for part in code.split() if part.strip()]

        # 3. Clasificación de Tokens y Eliminación de Duplicados
        # Usaremos un diccionario para almacenar los tokens únicos, agrupados por su tipo.
        # El orden en las llaves es el orden de impresión deseado.
        classified_tokens = {
            'VARIABLE': set(),
            'SIGNO': set(),
            'SIMBOLO': set(),
            'NUMERO': set()
        }

        for token in tokens:

            if token in KEYWORDS:
                continue

            token_type = ""
            
            if token in KEYWORDS: # Las palabras clave se consideran PALABRA_CLAVE, pero las agruparemos con VARIABLES
                token_type = "VARIABLE"
            elif token in OPERATORS:
                token_type = "SIGNO"
                classified_tokens[token_type].add((token, OPERATORS_MAP[token]))
                continue
            elif token == AGRUPATION_TOKEN:
                token_type = "SIMBOLO"
                classified_tokens[token_type].add((token, AGRUPATION_NAME))
                continue
            elif token in INDIVIDUAL_SIMBOLS:
                token_type = "SIMBOLO"
                classified_tokens[token_type].add((token, token.upper()))
                continue
            elif token.replace('.', '', 1).isdigit():
                # Verificación robusta para números (enteros o flotantes)
                token_type = "NUMERO"
            elif token.isalpha() or (token[0].isalpha() and token.isalnum()):
                # Identificadores (Variables)
                token_type = "VARIABLE"
            else:
                # No clasificado (ej: cadena de texto, error léxico)
                token_type = "OTROS"
            
            # Agregamos el token a su conjunto correspondiente (esto elimina duplicados automáticamente)
            if token_type in classified_tokens:
                classified_tokens[token_type].add(token)

        # 4. Generación de la Salida Ordenada
        output_lines = ["--- RESULTADO DEL ANÁLISIS LÉXICO ---"]

        # Definimos el orden de impresión explícitamente
        print_order = ['VARIABLE', 'SIGNO', 'SIMBOLO', 'NUMERO']

        for type_name in print_order:
        
            if type_name == 'SIGNO':
                # MANEJO ESPECIAL PARA SIGNOS (Tuplas de 2 elementos: signo, nombre)
                tokens_list = sorted(list(classified_tokens[type_name]), key=lambda x: x[0])
            elif type_name == 'SIMBOLO':
                # MANEJO ESPECIAL PARA SÍMBOLOS (Tuplas de 2 elementos: simbolo, nombre)
                tokens_list = sorted(list(classified_tokens[type_name]), key=lambda x: x[0])
            else:
                # MANEJO ESTÁNDAR para otros tipos (Variables y Números)
                tokens_list = sorted(list(classified_tokens[type_name]))
                
            if tokens_list:
                output_lines.append(f"\n[{type_name.upper()}]:")
                
                for token_item in tokens_list:
                    if type_name in ('SIGNO', 'SIMBOLO'):
                        # Desempaquetar la tupla (token, nombre)
                        token, nombre = token_item
                        output_lines.append(f"{token} Tipo: {type_name.capitalize()} ({nombre.capitalize()})")
                    else:
                        # Formato para Variables y Números
                        output_lines.append(f"{token_item} Tipo: {type_name.capitalize()}")

        return '\n'.join(output_lines)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ventanaPrincipal(root)
    root.mainloop()