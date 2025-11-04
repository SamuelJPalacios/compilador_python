from num2words import num2words
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

class ventanaPrincipal:
    def __init__(self, root):
        # Configuración de la ventana
        self.root = root
        self.root.title("Proyecto Final Compilador")
        self.root.geometry("1200x700")

        # --- Interfaz (Mantenida) ---

        self.code_label = tk.Label(root, text = "Escriba su codigo aqui:")
        self.code_label.pack(pady = 10)

        self.code_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 50, height = 10, font = ("Times New Roman", 16))
        self.code_area.pack(padx = 10, pady = 10)

        self.analyze_button = tk.Button(root, text = "Iniciar Compilación", command = self.run_analysis, font = ("Arial", 14))
        self.analyze_button.pack (pady = 10)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Crear los frames de las pestañas
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

        # Inicialización de widgets de salida
        self.analisis_lexico_output = self._create_output_widget(self.analisis_lexico, "Análisis Léxico")
        self.analisis_sintactico_output = self._create_output_widget(self.analisis_sintactico, "Análisis Sintáctico")
        self.analisis_semantico_output = self._create_output_widget(self.analisis_semantico, "Análisis Semántico")
        self.codigo_intermedio_output = self._create_output_widget(self.codigo_intermedio, "Código Intermedio")
        self.optimacion_output = self._create_output_widget(self.optimacion, "Optimación")
        self.generacion_codigo_objeto_output = self._create_output_widget(self.generacion_codigo_objeto, "Generación de Código Objeto")
        self.codigo_objeto_output = self._create_output_widget(self.codigo_objeto, "Código Objeto")
        self.tabla_simbolos_output = self._create_output_widget(self.tabla_simbolos, "Tabla de Símbolos")
        self.admin_errores_output = self._create_output_widget(self.admin_errores, "Administrador de Errores")


    def _create_output_widget(self, parent_frame, label_text):
        """Función auxiliar para crear etiquetas y áreas de texto."""
        label = tk.Label(parent_frame, text=label_text)
        label.pack(pady=10)
        output_widget = scrolledtext.ScrolledText(parent_frame, wrap=tk.WORD, width=100, height=10, font=("Times New Roman", 16))
        output_widget.pack(padx=10, pady=10)
        return output_widget

    # --- Métodos Generales y Coordinación ---
    
    def clear_and_insert (self, widget, content):
        """ Función para limpiar y agregar contenido a un widget de texto """
        widget.config (state = 'normal')
        widget.delete ("1.0", tk.END)
        widget.insert (tk.END, content)
        widget.config (state = 'disabled')

    def _clear_subsequent_tabs(self, current_phase_name):
        """Limpia las pestañas de las fases posteriores a la detención."""
        phase_widgets_map = {
            "ANÁLISIS LÉXICO": [self.analisis_sintactico_output, self.analisis_semantico_output, self.codigo_intermedio_output, self.optimacion_output, self.generacion_codigo_objeto_output, self.codigo_objeto_output, self.tabla_simbolos_output],
            "ANÁLISIS SINTÁCTICO": [self.analisis_semantico_output, self.codigo_intermedio_output, self.optimacion_output, self.generacion_codigo_objeto_output, self.codigo_objeto_output], 
            "ANÁLISIS SEMÁNTICO": [self.codigo_intermedio_output, self.optimacion_output, self.generacion_codigo_objeto_output, self.codigo_objeto_output],
        }
        
        widgets_to_clear = phase_widgets_map.get(current_phase_name, [])
            
        halt_message = f"PROCESO DETENIDO. La compilación se detuvo en la fase de {current_phase_name} debido a errores."
        
        for widget in widgets_to_clear:
            self.clear_and_insert(widget, halt_message)

    def run_analysis(self):
        """ Método para el boton Iniciar Compilación - ORQUESTACIÓN """
        source_code = self.code_area.get("1.0", tk.END).strip()
        if not source_code:
            self.clear_and_insert(self.admin_errores_output, "No hay código de entrada. Por favor, ingrese código para comenzar.")
            return
        
        self.clear_and_insert(self.admin_errores_output, "")
        
        # --- 1. ⭐️ ANÁLISIS LÉXICO ---
        lexical_output, lexical_errors = self.perform_lexical_analysis(source_code)
        self.clear_and_insert(self.analisis_lexico_output, lexical_output)
        
        if lexical_errors:
            self.update_error_manager("ANÁLISIS LÉXICO", lexical_errors, full_compilation=False)
            self._clear_subsequent_tabs("ANÁLISIS LÉXICO")
            return
        
        # --- 2. ⭐️ ANÁLISIS SINTÁCTICO ---
        syntactic_output, syntactic_errors = self.perform_syntactic_analysis(source_code, None) 
        
        if syntactic_errors:
            self.update_error_manager("ANÁLISIS SINTÁCTICO", syntactic_errors, full_compilation=False)
            self._clear_subsequent_tabs("ANÁLISIS SINTÁCTICO")
            return
        
        # --- 3. ⭐️ TABLA DE SÍMBOLOS (Generación) ---
        symbol_table = self.build_symbol_table(source_code) 
        self.display_symbol_table(symbol_table)
        
        # --- 4. ⭐️ ANÁLISIS SEMÁNTICO (Verificación) ---
        semantic_errors = self.perform_semantic_analysis(source_code, symbol_table)
        
        if semantic_errors:
            self.update_error_manager("ANÁLISIS SEMÁNTICO", semantic_errors, full_compilation=False)
            self._clear_subsequent_tabs("ANÁLISIS SEMÁNTICO")
            return
        
        # Si no hay errores, el proceso continúa
        
        # --- 5. ⭐️ CÓDIGO INTERMEDIO (Generación de 3-dir) ---
        intermediate_code_lines = self.perform_intermediate_code_generation(source_code)
        
        # --- 6. ⭐️ OPTIMACIÓN ---
        optimized_code_lines = self.perform_optimization(intermediate_code_lines)
        
        # --- 7. ⭐️ GENERACIÓN CÓDIGO OBJETO ---
        self.perform_object_code_generation(optimized_code_lines)
        
        # --- 8. ⭐️ ADMINISTRADOR DE ERRORES (Resumen final) ---
        self.update_error_manager("COMPLETADO", [], full_compilation=True)


    # --- Análisis Léxico (Métodos) ---

    def number_to_text(self, number_str):
        """Convierte una cadena de número a palabras en español."""
        try:
            number_str = number_str.replace('.', ' punto ', 1)
            number = float(number_str.replace(' punto ', '.'))
            text = num2words(number, lang='es').upper()
            return text.replace('-', ' ')
        except ValueError:
            return "ERROR_CONV"
        except Exception:
            return "ERROR_INTERNO"


    def perform_lexical_analysis(self, code):
        """Simula el análisis léxico y devuelve errores léxicos."""
        if not code:
            return "No hay código para analizar", []

        KEYWORDS = {"return", "int", "float", "void", "boolean", "double"}
        OPERATORS_MAP = {"+": "ADICIÓN", "-": "SUSTRACCIÓN", "*": "MULTIPLICACIÓN", "/": "COCIENTE", "^": "EXPONENTE"}
        OPERATORS = set(OPERATORS_MAP.keys())
        SIMBOLS_MAP = {"=": "ASIGNACIÓN", ";": "PUNTO_Y_COMA", "(": "PARÉNTESIS_APERTURA", ")": "PARÉNTESIS_CIERRE", ",": "COMA"}
        INDIVIDUAL_SIMBOLS = set(SIMBOLS_MAP.keys())
        IGNORE_SIMBOLS = {"{", "}"}

        # 2. Preprocesamiento
        temp_code = code
        for char_to_isolate in OPERATORS | INDIVIDUAL_SIMBOLS | IGNORE_SIMBOLS:
            temp_code = temp_code.replace(char_to_isolate, f" {char_to_isolate} ")
        temp_code = ' '.join(temp_code.split())
        tokens = [part.strip() for part in temp_code.split() if part.strip()]

        # 3. Clasificación de Tokens
        classified_tokens = {'VARIABLE': set(), 'SIGNO': set(), 'SIMBOLO': set(), 'NUMERO': set()}
        parenthesis_found = False
        lexical_errors = [] 

        for token in tokens:
            if token in KEYWORDS or token in IGNORE_SIMBOLS:
                continue
            
            if token in OPERATORS:
                classified_tokens["SIGNO"].add((token, OPERATORS_MAP[token]))
            
            elif token in INDIVIDUAL_SIMBOLS:
                if token in ("(", ")"):
                    if not parenthesis_found:
                        classified_tokens["SIMBOLO"].add(("()", "AGRUPACIÓN"))
                        parenthesis_found = True
                    continue 
                classified_tokens["SIMBOLO"].add((token, SIMBOLS_MAP[token]))
            
            elif token.replace('.', '', 1).isdigit():
                valor_en_letras = self.number_to_text(token)
                if "ERROR_CONV" in valor_en_letras:
                    lexical_errors.append(f"ERROR Léxico: Número mal formado o imposible de convertir a texto ('{token}').")
                classified_tokens["NUMERO"].add((token, valor_en_letras))
                
            elif token.isalpha() or (token[0].isalpha() and token.isalnum()):
                classified_tokens["VARIABLE"].add(token)
            
            else:
                 if token not in ['(', ')', ',', '=', ';']: 
                     lexical_errors.append(f"ERROR Léxico: Carácter o token no reconocido ('{token}').")

        # 4. Generación de la Salida Ordenada
        output_lines = ["--- RESULTADO DEL ANÁLISIS LÉXICO (Llaves {} y Palabras Clave Omitidas) ---"]
        if lexical_errors:
             output_lines.append(f"\n⚠️ SE ENCONTRARON {len(lexical_errors)} ERRORES LÉXICOS CRÍTICOS (Ver Administrador de Errores) ⚠️")
        
        print_order = ['VARIABLE', 'SIGNO', 'SIMBOLO', 'NUMERO']
        variable_counter = 1 

        for type_name in print_order:
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
                        output_lines.append(f"{token} Tipo: {type_name.capitalize()} ({nombre.capitalize()})")
                    elif type_name == 'NUMERO':
                        token, valor_en_letras = token_item
                        output_lines.append(f"{token} Tipo: {type_name.capitalize()} ({valor_en_letras.capitalize()})")

        return '\n'.join(output_lines), lexical_errors


    # --- Análisis Sintáctico (Métodos) ---

    def _get_clean_lexemes(self, code):
        """Función auxiliar para obtener una lista limpia de lexemas (tokens) del código."""
        OPERATORS = {"+", "-", "*", "/", "^"}
        SIMBOLS = {"=", ";", "(", ")", "{", "}", ","} 
        
        # Tokenización unificada (misma lógica que Léxico) 
        temp_code = code
        for char_to_isolate in OPERATORS | SIMBOLS:
            temp_code = temp_code.replace(char_to_isolate, f" {char_to_isolate} ")
        
        temp_code = ' '.join(temp_code.split())
        tokens = [part.strip() for part in temp_code.split() if part.strip()]
        
        # Excluir palabras clave (ya que el análisis se centra en la expresión/asignación)
        keywords_to_ignore = {'int', 'double', 'float', 'void', 'main', '{', '}', 'return', 'boolean'}
        return [t for t in tokens if t not in keywords_to_ignore]


    def infix_to_postfix_simulation(self, tokens):
        """Genera Notación Postfija (N.P.) para una expresión, incluyendo la asignación (=)."""
        if not tokens:
            return ""

        precedence = {'=': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4}
        output = []
        operator_stack = []

        for token in tokens:
            if token.replace('.', '', 1).isdigit() or token.isalpha():
                output.append(token)
            elif token in precedence:
                
                while (operator_stack and 
                    operator_stack[-1] != '(' and 
                    precedence.get(operator_stack[-1], 0) >= precedence[token]):
                    
                    if token == '=' and precedence.get(operator_stack[-1], 0) == precedence[token]:
                        break 
                        
                    output.append(operator_stack.pop())
                
                operator_stack.append(token)
                
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
        
        while operator_stack:
            output.append(operator_stack.pop())
            
        return " ".join(output)
            
    def _simulate_parse_tree(self, tokens):
        """Simula una estructura de Árbol de Sintaxis Abstracta (AST) para ASIGNACIONES."""
        
        if '=' not in tokens:
            return "Árbol no generado (No es una asignación simple)."

        try:
            root_index = tokens.index('=')
            variable_node = tokens[root_index - 1]
            # Mantenemos la remoción de paréntesis simples (aunque un parser real los usaría para precedencia)
            expression_tokens = [t for t in tokens[root_index + 1:] if t not in ['(', ')']] 
        except (ValueError, IndexError):
            return "Error al identificar la asignación en los tokens."
        
        tree = f"|-- =\n"
        # Lado Izquierdo de '=' (Variable objetivo)
        tree += f"    |-- {variable_node} (Terminal)\n"
        
        # Lado Derecho de '=' (Expresión) - Llamada a la función recursiva
        if not expression_tokens:
            tree += "    |-- VACÍO\n"
        else:
            # Llama a la función recursiva con un nivel de indentación inicial de 1
            tree += self._build_expression_tree_recursive(expression_tokens, 1)

        return tree


    # ... (Mantener _get_operator_precedence, _build_expression_tree_recursive, _simulate_parse_tree)

    def perform_syntactic_analysis(self, source_code, lexical_tokens):
        """Simula el análisis sintáctico y devuelve errores sintácticos. Corregido para manejar ','."""
        if not source_code:
            self.clear_and_insert(self.analisis_sintactico_output, "No hay código para realizar el análisis sintáctico.")
            return "", []

        syntactic_output = "--- RESULTADO DEL ANÁLISIS SINTÁCTICO ---\n\n"
        output_parts = []
        operation_counter = 1
        syntactic_errors = [] 

        # ⭐️ CORRECCIÓN CLAVE: Segmentación de expresiones ⭐️
        
        # 1. Separar por ';' (sentencias completas, incluyendo declaraciones)
        sentences = source_code.split(';')
        
        # 2. Inicializar lista de expresiones limpias a analizar
        clean_expressions = []
        
        KEYWORDS = {"int", "double", "float", "void", "boolean"}

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence: continue

            # Detectar si es una línea de declaración (ej: "int a=12,b,c")
            is_declaration = any(sentence.startswith(kw) for kw in KEYWORDS)
            
            # Si es una declaración, la separamos por ',' para obtener múltiples asignaciones/variables.
            if is_declaration:
                # Quitamos la palabra clave del tipo (ej: "int ")
                type_removed = sentence.split(None, 1)[-1] 
                sub_expressions = type_removed.split(',')
            else:
                # Si no es una declaración, se considera una sola expresión (ej: "b=50/7")
                sub_expressions = [sentence]

            for expr in sub_expressions:
                expr = expr.strip()
                if expr and '=' in expr:
                    clean_expressions.append(expr)
        
        # 3. Procesar cada expresión de asignación limpia
        for expression in clean_expressions:
                
            clean_tokens = self._get_clean_lexemes(expression) 
            final_tokens = [t for t in clean_tokens if t not in [',']]
            
            # --- Verificación de error Sintáctico ---
            if '=' not in final_tokens or len(final_tokens) < 3:
                # Si llega aquí, es probablemente un token suelto (ej: "c")
                continue
            
            operators = {'+', '-', '*', '/', '^'}
            for i in range(len(final_tokens) - 1):
                if final_tokens[i] in operators and final_tokens[i+1] in operators:
                    syntactic_errors.append(f"ERROR Sintáctico: Dos operadores consecutivos ('{final_tokens[i]} {final_tokens[i+1]}') sin operando en la expresión: '{' '.join(final_tokens)}'.")
                    break
            
            if syntactic_errors:
                 continue
            
            # Generación de N.P. y AST (Lógica sin cambios)
            postfix_notation = self.infix_to_postfix_simulation(final_tokens)
            tree_simulation = self._simulate_parse_tree(final_tokens)
            
            operation_output = f"--- OPERACIÓN {operation_counter} ---\n"
            operation_output += f"EXPRESIÓN INFIJA: {' '.join(final_tokens)}\n\n"
            operation_output += f"N.P. (Notación Postfija):\n{postfix_notation}\n\n"
            operation_output += "ÁRBOL DE SINTAXIS ABSTRACTA (AST):\n"
            operation_output += tree_simulation
            operation_output += "\n"
            
            output_parts.append(operation_output)
            operation_counter += 1

        if output_parts:
            syntactic_output += "\n".join(output_parts)
        else:
            syntactic_output += "No se encontraron operaciones de asignación para analizar."
        
        if syntactic_errors:
             syntactic_output += f"\n\n⚠️ SE ENCONTRARON {len(syntactic_errors)} ERRORES SINTÁCTICOS CRÍTICOS (Ver Administrador de Errores) ⚠️"

        self.clear_and_insert(self.analisis_sintactico_output, syntactic_output)
        return syntactic_output, syntactic_errors

        if output_parts:
            syntactic_output += "\n".join(output_parts)
        else:
            syntactic_output += "No se encontraron operaciones de asignación para analizar."
        
        if syntactic_errors:
             syntactic_output += f"\n\n⚠️ SE ENCONTRARON {len(syntactic_errors)} ERRORES SINTÁCTICOS CRÍTICOS (Ver Administrador de Errores) ⚠️"

        self.clear_and_insert(self.analisis_sintactico_output, syntactic_output)
        return syntactic_output, syntactic_errors

    # --- Tabla de Símbolos y Análisis Semántico ---
    
    def get_type_size(self, var_type):
        """Simula el tamaño en bytes de los tipos de datos."""
        if var_type == 'int' or var_type == 'float':
            return 4
        elif var_type == 'double':
            return 8
        elif var_type == 'boolean':
            return 1
        return 0
    
    def _get_operator_precedence(self, op):
        """
        Precedencia de los operadores para la construcción del AST. 
        Cuanto menor el número, más BAJA la prioridad (se ejecuta AL FINAL, es la raíz).
        """
        precedence = {'=': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence.get(op, 99) # 99 para no-operadores

    def get_initial_value(self, var_type):
        """Simula el valor inicial por defecto según el tipo."""
        if var_type == 'int' or var_type == 'double' or var_type == 'float':
            return '0.0' if var_type in ['float', 'double'] else '0'
        elif var_type == 'boolean':
            return 'false'
        return 'Ø' # Símbolo vacío

    def build_symbol_table(self, source_code):
        """
        Extrae declaraciones y crea una Tabla de Símbolos simulando todas las columnas
        requeridas: Nombre, Tipo, Tamaño, Valor, Ámbito, Dir. Mem., Parámetros.
        """
        symbol_table = {}
        all_tokens = source_code.replace(',', ' , ').replace(';', ' ; ').replace('=', ' = ').replace('(', ' ( ').replace(')', ' ) ').split()
        all_tokens = [t.strip() for t in all_tokens if t.strip()]

        TYPES = {"int", "double", "float", "boolean", "void"}
        current_type = None
        mem_address_counter = 1
        
        i = 0
        while i < len(all_tokens):
            token = all_tokens[i]
            
            # Detección de tipos
            if token in TYPES:
                current_type = token
                i += 1
                continue
            
            # Detección de Declaración de Función o Variable
            if token.isalpha() and current_type:
                var_name = token
                
                # Check for Function declaration (e.g., suma(int a, float b))
                if (i + 1 < len(all_tokens) and all_tokens[i + 1] == '('):
                    
                    # Simulación de la Función como un Símbolo
                    symbol_table[var_name] = {
                        'name': var_name,
                        'type': current_type,
                        'size': self.get_type_size(current_type) if current_type != 'void' else 4, # Tamaño del puntero o valor de retorno
                        'value': self.get_initial_value(current_type),
                        'scope': 'main', # Asumimos que las funciones se declaran en main (global)
                        'mem_addr': f'@{mem_address_counter}',
                        'params_in': [],
                        'params_out': [],
                        'kind': 'function'
                    }
                    mem_address_counter += 1
                    
                    # ⭐️ Simulación de Parámetros de Entrada ⭐️
                    i += 2 # Saltar 'nombre('
                    params = []
                    while i < len(all_tokens) and all_tokens[i] != ')':
                        if all_tokens[i] in TYPES:
                            p_type = all_tokens[i]
                            i += 1
                            if i < len(all_tokens) and all_tokens[i].isalpha():
                                p_name = all_tokens[i]
                                p_value = self.get_initial_value(p_type)
                                params.append({'name': p_name, 'type': p_type, 'value': p_value})
                                i += 1
                            if i < len(all_tokens) and all_tokens[i] == ',':
                                i += 1 # Saltar ','
                            else:
                                pass # No es necesario manejar ',' explícitamente si se manejan los tipos/nombres
                        else:
                             i += 1 # Saltar cualquier token inesperado dentro del paréntesis
                    
                    symbol_table[var_name]['params_in'] = params
                    
                    # Limpiamos el tipo actual si la declaración de la función terminó
                    current_type = None
                    
                # Declaración de Variable
                else:
                    if var_name not in symbol_table:
                        symbol_table[var_name] = {
                            'name': var_name,
                            'type': current_type,
                            'size': self.get_type_size(current_type),
                            'value': self.get_initial_value(current_type),
                            'scope': 'main', # Simulación: Asumimos 'main' por simplicidad si no se especifica
                            'mem_addr': f'@{mem_address_counter}',
                            'params_in': [],
                            'params_out': [],
                            'kind': 'variable'
                        }
                        mem_address_counter += 1
                    
                    # Continuar para ver si hay una asignación en la misma línea
                    i += 1
                    continue
            
            # Detección de Asignación de Valor
            elif token == '=':
                try:
                    var_name = all_tokens[i - 1]
                    # Simulación de actualización de Valor/Inicialización
                    if var_name in symbol_table and i + 1 < len(all_tokens):
                        next_token = all_tokens[i + 1]
                        
                        # Simplificación: si es un número, usamos ese número como valor (sin evaluar toda la expresión)
                        if next_token.replace('.', '', 1).isdigit():
                            symbol_table[var_name]['value'] = next_token
                            
                except:
                    pass
                i += 1
                continue
            
            # Fin de la sentencia de declaración
            elif token == ';':
                current_type = None
            
            i += 1

        # ⭐️ Post-Procesamiento: Simular el Ámbito para variables asignadas en funciones ⭐️
        # Busca tokens de función y simula que las variables inmediatamente declaradas o asignadas están en ese ámbito
        scope_tokens = [t for t in all_tokens if t.isalpha() and t in symbol_table and symbol_table[t]['kind'] == 'function']
        
        # Simple simulación de ámbito para variables
        current_scope = 'main'
        for token in all_tokens:
            if token in scope_tokens:
                 current_scope = token
            elif token in symbol_table and symbol_table[token]['kind'] == 'variable' and token not in ('main', 'suma'):
                 symbol_table[token]['scope'] = current_scope
        
        return symbol_table

    
    def display_symbol_table(self, symbol_table):
        """Muestra la tabla de símbolos en un formato de lista jerárquica simple."""
        
        output_lines = ["--- TABLA DE SÍMBOLOS (SIMULACIÓN EXTENDIDA) ---\n"]
        if not symbol_table:
            self.clear_and_insert(self.tabla_simbolos_output, output_lines[0] + "\nNo se encontraron símbolos.")
            return

        # Mapeo de Claves Internas a Nombres Legibles (para la lista)
        ATTRIBUTE_NAMES = {
            "type": "tipo",
            "size": "tamaño",
            "value": "valor",
            "scope": "ámbito",
            "mem_addr": "dir. memoria",
            "kind": "clase" # Añadimos la clase (variable/función) para claridad
        }

        # 1. Impresión de Símbolos Ordenados
        
        # Ordenar: primero funciones, luego variables
        sorted_symbols = sorted(symbol_table.items(), key=lambda item: (item[1]['kind'], item[0]))
        
        counter = 1
        for name, data in sorted_symbols:
            
            output_lines.append(f"{counter}. **{name}** ({data.get('kind', 'indefinido')})")
            
            # Imprimir atributos base
            for key_internal, key_display in ATTRIBUTE_NAMES.items():
                if key_internal != 'kind': # 'kind' ya se imprimió en el título
                    value = data.get(key_internal, 'Ø')
                    output_lines.append(f"   - {key_display.capitalize()}: {value}")
            
            # Imprimir Parámetros de Entrada (si es una función)
            params_in = data.get('params_in', [])
            if params_in:
                output_lines.append("   - **Parámetros de Entrada:**")
                for i, param in enumerate(params_in):
                    p_name = param.get('name', 'N/A')
                    p_type = param.get('type', 'N/A')
                    p_value = param.get('value', 'Ø')
                    output_lines.append(f"     - {i+1}. {p_name} (Tipo: {p_type}, Valor: {p_value})")

            # Imprimir Parámetros de Salida (Simulación)
            params_out = data.get('params_out', [])
            if params_out:
                output_lines.append("   - **Parámetros de Salida:**")
                for i, param in enumerate(params_out):
                    p_name = param.get('name', 'N/A')
                    p_type = param.get('type', 'N/A')
                    p_value = param.get('value', 'Ø')
                    output_lines.append(f"     - {i+1}. {p_name} (Tipo: {p_type}, Valor: {p_value})")
            
            output_lines.append("") # Línea en blanco para separar símbolos
            counter += 1

        self.clear_and_insert(self.tabla_simbolos_output, "\n".join(output_lines))        
    def perform_semantic_analysis(self, source_code, symbol_table):
        """Simula la verificación de tipos y el uso de variables. Se detiene en el primer error."""
        semantic_output = "--- RESULTADO DEL ANÁLISIS SEMÁNTICO ---\n\n"
        errors = []
        output_parts = []
        
        sentences = source_code.split(';')
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence: continue

            current_sentence_errors = []
            
            # 1. Chequeo de variables no declaradas/utilizadas en esta sentencia
            current_tokens = self._get_clean_lexemes(sentence)
            for lexeme in current_tokens:
                if lexeme.isalpha() and lexeme not in symbol_table and lexeme not in ["main", "if", "else", "while", "for"]:
                    current_sentence_errors.append(f"ERROR Semántico: Variable '{lexeme}' utilizada sin ser declarada (o está mal escrita).")
            
            # 2. Chequeo específico de asignación (Conflictos de Tipo)
            if '=' in sentence:
                parts = sentence.split('=')
                var_name = parts[0].strip().split()[-1]
                expression = parts[1].strip()
                
                if var_name in symbol_table:
                    target_type = symbol_table[var_name]['type']
                    
                    is_float_expression = False
                    expression_tokens = self._get_clean_lexemes(expression) 
                    
                    for token in expression_tokens:
                        # a) Chequeo de literal flotante
                        if token.replace('.', '', 1).isdigit() and '.' in token: 
                            is_float_expression = True
                            break
                        # b) Chequeo de tipo flotante de variable
                        if token in symbol_table and symbol_table.get(token, {}).get('type') in ['float', 'double']:
                            is_float_expression = True
                            break

                    # Solo error si target es INT y la expresión es EXPLICITAMENTE float.
                    if target_type == 'int' and is_float_expression:
                        current_sentence_errors.append(f"ERROR Semántico: Conflicto de tipos. Asignando un valor flotante explícito (literal o variable 'float'/'double') a la variable entera '{var_name}'.")
                    
                    # Chequeo 3: Variable NO inicializada (simple check)
                    # Esta lógica es compleja ya que debería ver si se usó *después* de su declaración/asignación. 
                    # Por simplicidad, se mantiene solo si no se ha asignado en la declaración
                    # if not symbol_table[var_name]['initialized']:
                    #     current_sentence_errors.append(f"ADVERTENCIA Semántica: La variable '{var_name}' se utiliza sin haber sido inicializada previamente.")
            
            # 3. Registrar el resultado de la sentencia
            operation_title = f"# SENTENCIA: {sentence}"
            
            if current_sentence_errors:
                output_parts.append(f"{operation_title}\n-- ❌ ERRORES ENCONTRADOS --\n- " + "\n- ".join(current_sentence_errors))
                errors.extend(current_sentence_errors)
                
                # ⭐️ DETENCIÓN INMEDIATA ⭐️
                semantic_output += "\n".join(output_parts)
                semantic_output += f"\n\n\n🛑 PROCESO DETENIDO: Se encontró un error semántico crítico. (Ver Administrador de Errores)"
                self.clear_and_insert(self.analisis_semantico_output, semantic_output)
                return errors 
                
            else:
                output_parts.append(f"{operation_title}\n-- ✅ VERIFICACIÓN SEMÁNTICA APROBADA --")

        # Si el bucle termina sin errores
        semantic_output += "\n".join(output_parts)
        semantic_output += "\n\nEl código ha pasado todas las verificaciones semánticas básicas (simulación)."
        self.clear_and_insert(self.analisis_semantico_output, semantic_output)
        return errors 
        
    # --- Código Intermedio, Optimación y Código Objeto (Simulaciones) ---
    
    def perform_intermediate_code_generation(self, source_code):
        intermediate_code_output = "--- CÓDIGO INTERMEDIO (TRES DIRECCIONES) ---\n"
        code_lines = []
        temp_counter = 0
        sentences = source_code.split(';')
        for sentence in sentences:
            sentence = sentence.strip()
            if '=' not in sentence: continue
            assignment_tokens = self._get_clean_lexemes(sentence)
            final_tokens = [t for t in assignment_tokens if t not in [',', 'int', 'double', 'float', 'void', 'boolean', 'main', '{', '}']]
            if '=' not in final_tokens or len(final_tokens) < 3: continue
            target_var = final_tokens[0]
            expression_tokens = [t for t in final_tokens[2:] if t not in ['(', ')']]
            postfix = self.infix_to_postfix_simulation(expression_tokens)
            postfix_tokens = postfix.split()
            stack = []
            instructions = []
            for token in postfix_tokens:
                if token.replace('.', '', 1).isdigit() or token.isalpha():
                    stack.append(token)
                elif token in {'+', '-', '*', '/'}:
                    if len(stack) < 2: continue
                    op2 = stack.pop()
                    op1 = stack.pop()
                    temp_var = f"T{temp_counter}"
                    instructions.append(f"{temp_var} = {op1} {token} {op2}")
                    stack.append(temp_var)
                    temp_counter += 1
            if stack and target_var != stack[0]:
                 instructions.append(f"{target_var} = {stack[0]}")
            if instructions:
                code_lines.append(f"\n# Sentencia: {sentence}")
                code_lines.extend(instructions)
        if code_lines:
            intermediate_code_output += "\n".join(code_lines)
        else:
            intermediate_code_output += "\nNo se generó código intermedio para asignaciones."
        self.clear_and_insert(self.codigo_intermedio_output, intermediate_code_output)
        return code_lines
        
    def perform_optimization(self, intermediate_code_lines):
        optimized_code_output = "--- CÓDIGO OPTIMIZADO ---\n"
        optimized_lines = []
        if not intermediate_code_lines:
            optimized_code_output += "\nNo hay código intermedio para optimizar."
            self.clear_and_insert(self.optimacion_output, optimized_code_output)
            return []
        optimization_applied = False
        for line in intermediate_code_lines:
            if line.startswith("#"):
                optimized_lines.append(line)
                continue
            if '=' in line and len(line.split('=')) == 2:
                target, expression = line.split('=', 1)
                target = target.strip()
                expr_parts = expression.strip().split()
                if len(expr_parts) == 3:
                    op1, op, op2 = expr_parts
                    if op1.replace('.', '', 1).isdigit() and op2.replace('.', '', 1).isdigit() and op in "+-*/":
                        try:
                            result = eval(f"{op1} {op} {op2}")
                            optimized_lines.append(f"{target} = {int(result) if result == int(result) else result}")
                            optimization_applied = True
                            continue
                        except:
                            pass
            optimized_lines.append(line)
        optimized_code_output += "\n"
        if optimization_applied:
            optimized_code_output += "Optimización Aplicada: Plegado de Constantes (Constant Folding).\n\n"
        else:
            optimized_code_output += "No se aplicó optimización (Plegado de Constantes).\n\n"
        optimized_code_output += "\n".join(optimized_lines)
        self.clear_and_insert(self.optimacion_output, optimized_code_output)
        return optimized_lines

    def perform_object_code_generation(self, optimized_code_lines):
        object_code_output = "--- GENERACIÓN DE CÓDIGO OBJETO (ASSEMBLY SIMULADO) ---\n"
        assembly_lines = []
        if not optimized_code_lines:
            object_code_output += "No hay código optimizado para generar código objeto."
            self.clear_and_insert(self.generacion_codigo_objeto_output, object_code_output)
            self.clear_and_insert(self.codigo_objeto_output, object_code_output)
            return

        register_map = {}
        next_register = 1
        def get_register(var):
            nonlocal next_register
            if var not in register_map:
                register_map[var] = f"R{next_register}"
                next_register += 1
            return register_map[var]

        for line in optimized_code_lines:
            if line.startswith("#"):
                assembly_lines.append(f"\n; {line[2:].strip()}")
                continue
            if '=' in line:
                target, expression = line.split('=', 1)
                target = target.strip()
                expression = expression.strip()
                expr_parts = expression.split()
                reg_target = get_register(target)
                if len(expr_parts) == 1:
                    op = expr_parts[0]
                    if op.replace('.', '', 1).isdigit():
                        assembly_lines.append(f"MOV {reg_target}, #{op} ; Cargar constante")
                    else:
                        assembly_lines.append(f"MOV {reg_target}, {op} ; Cargar valor de variable/temporal")
                elif len(expr_parts) == 3:
                    op1, op_symbol, op2 = expr_parts
                    if op1.replace('.', '', 1).isdigit():
                         assembly_lines.append(f"MOV {reg_target}, #{op1}")
                    else:
                         assembly_lines.append(f"MOV {reg_target}, {op1}")
                    if op_symbol == '+': instruction = 'ADD'
                    elif op_symbol == '-': instruction = 'SUB'
                    elif op_symbol == '*': instruction = 'MUL'
                    elif op_symbol == '/': instruction = 'DIV'
                    else: instruction = 'OP'
                    if op2.replace('.', '', 1).isdigit():
                        assembly_lines.append(f"{instruction} {reg_target}, #{op2} ; {op_symbol} constante")
                    else:
                        assembly_lines.append(f"{instruction} {reg_target}, {op2} ; {op_symbol} variable")
                assembly_lines.append(f"STR {target}, {reg_target} ; Guardar resultado en memoria")

        object_code_output += "\n".join(assembly_lines)
        self.clear_and_insert(self.generacion_codigo_objeto_output, object_code_output)
        self.clear_and_insert(self.codigo_objeto_output, object_code_output)

    # --- Administrador de Errores ---

    def update_error_manager(self, phase, errors_list, full_compilation=True):
        """Actualiza la pestaña de Administrador de Errores. Detiene si full_compilation es False."""
        error_output = "--- ADMINISTRADOR DE ERRORES (SIMULACIÓN) ---\n\n"
        
        if not full_compilation:
            error_output += f"🛑 COMPILACIÓN DETENIDA EN LA FASE DE {phase.upper()} 🛑\n\n"
            error_output += "Se encontraron los siguientes errores críticos que impiden continuar con el análisis:\n"
            error_output += "\n- " + "\n- ".join(errors_list)
        else:
            error_output += "✅ ¡Felicidades! Proceso de compilación completado (sin errores críticos de detención)."

        self.clear_and_insert(self.admin_errores_output, error_output)

    def _build_expression_tree_recursive(self, tokens, indent_level):
        """
        Construye el AST de la expresión de forma recursiva (profundidad primero).
        Utiliza la técnica de encontrar el operador de MENOR precedencia.
        """
        
        if not tokens:
            return "ERROR: Expresión vacía"
        
        # 1. Encontrar la raíz de esta sub-expresión (Operador de MENOR Precedencia)
        min_exec_precedence = 10 # Comienza con un número mayor a cualquier precedencia de operador
        root_op = None
        root_index = -1
        
        # Recorrido de IZQUIERDA a DERECHA (L-to-R) para encontrar el operador de
        # menor precedencia. Si la precedencia es IGUAL, elegir el de la DERECHA
        # (simulando la asociatividad por la izquierda de +,-,*,/ en el AST).
        for i, token in enumerate(tokens):
            precedence = self._get_operator_precedence(token)
            
            # Solo consideramos operadores infijos (precedencia > 0)
            if precedence > 0:
                # Si la precedencia es menor, se convierte en el nuevo Root
                if precedence < min_exec_precedence: 
                    min_exec_precedence = precedence
                    root_op = token
                    root_index = i
                # Si la precedencia es igual (ej: a + b + c), nos quedamos con el último (derecha), 
                # lo que garantiza que la operación de la derecha sea el nodo raíz (correcta para Left-Associativity en AST).
                elif precedence == min_exec_precedence: 
                    root_op = token
                    root_index = i
        
        indent = "    " * indent_level

        # 2. Caso Base: Es un Terminal (Variable o Literal)
        if root_op is None:
            if len(tokens) == 1:
                return f"{indent}|-- {tokens[0]} (Terminal)"
            else:
                return f"{indent}|-- ERROR_EXPR (Tokens: {' '.join(tokens)})"

        # 3. Caso Recursivo: Es un Operador (Nodo Interno)
        
        left_tokens = tokens[:root_index]
        right_tokens = tokens[root_index + 1:]
        
        tree_str = f"{indent}|-- {root_op} (Operación)"
        
        # Sub-Árbol Izquierdo
        tree_str += "\n" + self._build_expression_tree_recursive(left_tokens, indent_level + 1)
        
        # Sub-Árbol Derecho
        tree_str += "\n" + self._build_expression_tree_recursive(right_tokens, indent_level + 1)
        
        return tree_str


if __name__ == "__main__":
    root = tk.Tk()
    app = ventanaPrincipal(root)
    root.mainloop()