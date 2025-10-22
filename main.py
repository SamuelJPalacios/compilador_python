from num2words import num2words
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

######################################################################
######################################################################
######################################################################

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

    # Función para convertir números a texto en español
    def number_to_text(self, number_str):
        """Convierte una cadena de número a palabras en español."""
        try:
            # Reemplazamos el punto decimal por 'coma' para num2words en español
            number_str = number_str.replace('.', ' punto ', 1)
            # Intentamos convertir a float, si falla, es un entero
            number = float(number_str)
            
            # num2words convierte el número a palabras en español
            text = num2words(number, lang='es').upper() 
            
            # Limpieza simple para que el formato sea solo palabras
            return text.replace('-', ' ')
        except ValueError:
            return "ERROR_CONV"
        except Exception as e:
            return f"ERROR: {e}"

    # ⭐️ FUNCIÓN AUXILIAR PARA CONVERTIR NÚMEROS A PALABRAS (Debe estar definida en la clase)
    def number_to_text(self, number_str):
        """Convierte una cadena de número a palabras en español."""
        try:
            # Reemplazamos el punto decimal por 'punto' para num2words en español
            number_str = number_str.replace('.', ' punto ', 1)
            number = float(number_str.replace(' punto ', '.'))
            text = num2words(number, lang='es').upper()
            return text.replace('-', ' ')
        except ValueError:
            return "ERROR_CONV"
        except Exception:
            return "ERROR_INTERNO"


    def perform_lexical_analysis(self, code):
        """
        Simula el análisis léxico: maneja paréntesis separados, asigna nombre a '=',
        y asegura la correcta detección de números.
        """
        if not code:
            return "No hay código para analizar"

        # 1. Definición de Tipos y Grupos de Tokens
        KEYWORDS = {"return", "int", "float", "void", "boolean", "double"}
        
        # Mapeo de Operadores para el tipo SIGNO
        OPERATORS_MAP = {
            "+": "ADICIÓN",
            "-": "SUSTRACCIÓN",
            "*": "MULTIPLICACIÓN",
            "/": "COCIENTE",
            "^": "EXPONENTE",
        }
        OPERATORS = set(OPERATORS_MAP.keys())

        # ⭐️ CAMBIO CLAVE 1: Agregamos el par de paréntesis y el '=' al mapa para darles nombre
        SIMBOLS_MAP = {
            "=": "ASIGNACIÓN", # ⭐️ SOLUCIÓN 3: Nombre descriptivo
            ";": "PUNTO_Y_COMA",
            "(": "PARÉNTESIS_APERTURA", # Los tratamos individualmente en el preproceso
            ")": "PARÉNTESIS_CIERRE",   # para poder agruparlos luego
        }
        INDIVIDUAL_SIMBOLS = set(SIMBOLS_MAP.keys())
        
        # Símbolos a IGNORAR
        IGNORE_SIMBOLS = {"{", "}"}

        # 2. Preprocesamiento: Aislar Símbolos y Operadores
        
        # ⭐️ SOLUCIÓN 1 y 2: Aislamiento flexible de todos los símbolos (incluidos paréntesis)
        for char_to_isolate in OPERATORS | INDIVIDUAL_SIMBOLS | IGNORE_SIMBOLS:
            code = code.replace(char_to_isolate, f" {char_to_isolate} ")
        
        # Eliminamos múltiples espacios y saltos de línea
        code = ' '.join(code.split())
        
        # ⭐️ Solución al problema de agrupacion y deteccion unica de parentesis:
        # Reemplazamos los paréntesis individuales por un único token si aparecen juntos.
        # Para simplificar y mantener el par único en la salida (como pedías en pasos anteriores),
        # podemos recolectar los paréntesis individuales y darles un nombre genérico "AGRUPACIÓN"
        # en la salida final usando el set para la unicidad.
        
        tokens = [part.strip() for part in code.split() if part.strip()]

        # 3. Clasificación de Tokens y Eliminación de Duplicados
        classified_tokens = {
            'VARIABLE': set(),
            'SIGNO': set(), 
            'SIMBOLO': set(),
            'NUMERO': set() 
        }

        # Conjunto temporal para registrar que ya mostramos el par '()'
        parenthesis_found = False

        for token in tokens:
            if token in KEYWORDS or token in IGNORE_SIMBOLS:
                continue
            
            token_type = ""
            
            if token in OPERATORS:
                token_type = "SIGNO"
                classified_tokens[token_type].add((token, OPERATORS_MAP[token]))
            
            elif token in INDIVIDUAL_SIMBOLS:
                token_type = "SIMBOLO"
                
                # ⭐️ CLAVE: Manejo y Agrupación de Paréntesis
                if token in ("(", ")"):
                    if not parenthesis_found:
                        # Si no hemos registrado el par, lo añadimos como token único '()'
                        classified_tokens[token_type].add(("()", "AGRUPACIÓN"))
                        parenthesis_found = True
                    continue # Ignoramos el '(' o ')' individual después de registrar el par

                # Manejo de Símbolos Individuales restantes (ej. '=' y ';')
                classified_tokens[token_type].add((token, SIMBOLS_MAP[token]))
            
            elif token.replace('.', '', 1).isdigit():
                token_type = "NUMERO"
                valor_en_letras = self.number_to_text(token)
                classified_tokens[token_type].add((token, valor_en_letras))
                
            elif token.isalpha() or (token[0].isalpha() and token.isalnum()):
                token_type = "VARIABLE"
                classified_tokens[token_type].add(token)
            
            # Nota: Si se llega aquí, se ignora la clasificación en 'OTROS', ya que solo nos interesan los definidos.


        # 4. Generación de la Salida Ordenada
        output_lines = ["--- RESULTADO DEL ANÁLISIS LÉXICO (Llaves {} y Palabras Clave Omitidas) ---"]
        print_order = ['VARIABLE', 'SIGNO', 'SIMBOLO', 'NUMERO']
        variable_counter = 1 

        for type_name in print_order:
            
            # Ordenamiento:
            tokens_list = sorted(list(classified_tokens[type_name]), key=lambda x: x[0] if isinstance(x, tuple) else x)
                
            if tokens_list:
                output_lines.append(f"\n[{type_name.upper()}]:")
                
                for token_item in tokens_list:
                    
                    if type_name == 'VARIABLE':
                        token = token_item
                        output_lines.append(f"{token} Tipo: {type_name.capitalize()} #{variable_counter}")
                        variable_counter += 1
                        
                    elif type_name in ('SIGNO', 'SIMBOLO'):
                        token, nombre = token_item
                        output_lines.append(f"{token} Tipo: {type_name.capitalize()} {nombre.capitalize()}")
                        
                    elif type_name == 'NUMERO':
                        token, valor_en_letras = token_item
                        output_lines.append(f"{token} Tipo: {type_name.capitalize()} {valor_en_letras.capitalize()}")

        return '\n'.join(output_lines)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ventanaPrincipal(root)
    root.mainloop()