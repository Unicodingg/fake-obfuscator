#   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
#   Author: xxh0
#   Developer: grave @mydeadlypassion
#   Discord: @xxh0
#   zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
import os
import sys
import random
import base64
import marshal
import zlib
import math
from colorama import init, Fore, Style
import shutil
import platform
init(autoreset=True)

class Obfuscator:
    def __init__(self):
        self.math_funcs = ["tan", "cos", "sin", "log", "log10", "sqrt", "fabs", "floor", "ceil", "trunc", "tanh", "exp", "pow"]
        self.defined_vars = set()
        self.console_width = shutil.get_terminal_size().columns
        self.current_user = os.getenv('USER', 'user')
        self.hostname = platform.node().split('.')[0]
       
    def rgb_to_ansi(self, r, g, b, background=False):
        """Convert RGB to ANSI escape code"""
        return f'\033[{48 if background else 38};2;{r};{g};{b}m'
   
    def gradient_color(self, start_rgb, end_rgb, steps, step):
        """Calculate gradient color between start and end"""
        if steps <= 1:
            return start_rgb
       
        r1, g1, b1 = start_rgb
        r2, g2, b2 = end_rgb
       
        ratio = step / (steps - 1)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
       
        return (r, g, b)
   
    def print_gradient_text(self, text, start_rgb=(255, 0, 0), end_rgb=(255, 255, 255)):
        """Print text with character-by-character gradient"""
        lines = text.split('\n')
       
        for line_idx, line in enumerate(lines):
            if not line.strip():
                print()
                continue
           
            gradient_chars = []
            for char_idx, char in enumerate(line):
                total_chars = sum(len(l) for l in lines)
                current_char = sum(len(lines[i]) for i in range(line_idx)) + char_idx
               
                rgb = self.gradient_color(start_rgb, end_rgb, total_chars, current_char)
                ansi_color = self.rgb_to_ansi(*rgb)
                gradient_chars.append(f"{ansi_color}{char}")
           
            print(''.join(gradient_chars) + Style.RESET_ALL)
   
    def print_gradient_line(self, text, start_rgb=(255, 0, 0), end_rgb=(255, 255, 255)):
        """Print a single line with character gradient"""
        gradient_chars = []
        for i, char in enumerate(text):
            rgb = self.gradient_color(start_rgb, end_rgb, len(text), i)
            ansi_color = self.rgb_to_ansi(*rgb)
            gradient_chars.append(f"{ansi_color}{char}")
        print(''.join(gradient_chars) + Style.RESET_ALL)
   
    def print_welcome_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == 'nt':
            os.system('mode con: cols=91 lines=25')
       
        skull_art = [
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢿⣧⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⡀⠀⠀⢀⡴⠛⠁⠀⠘⣿⡄⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⣤⡴⠋⠀⠀⠀⠀⠀⢿⣇⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⣿⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠈⣿⡀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢏⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⡇",
            "⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢿⡇",
            "⠀⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⢸⡇",
            "⠀⠀⠀⠀⠀⠀⢠⡞⠁⢹⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⠀",
            "⠀⠀⠀⠀⠀⣠⠟⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢸⠀",
            "⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀",
            "⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀",
            "⢀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀",
            "⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠃",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        ]
       
        total_chars = sum(len(l) for l in skull_art)
       
        for i, line in enumerate(skull_art):
            start_rgb = (255, 0, 0)
            end_rgb = (255, 255, 255)
           
            gradient_line = ""
            for j, char in enumerate(line):
                if char == '⠀':
                    gradient_line += char
                    continue
                   
                current_pos = (i * len(line) + j) / total_chars
               
                r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * current_pos)
                g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * current_pos)
                b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * current_pos)
               
                ansi_color = self.rgb_to_ansi(r, g, b)
                gradient_line += f"{ansi_color}{char}"
           
            print(gradient_line + Style.RESET_ALL, end='')
           
            if i == 14:
                print(" " * 10 + f"{self.rgb_to_ansi(255, 150, 150)}hello, {self.hostname}{Style.RESET_ALL}")
            elif i == 15:
                print(" " * 10 + f"{self.rgb_to_ansi(255, 180, 180)}type \"help\" to see all{Style.RESET_ALL}")
            else:
                print()
   
    def print_prompt(self):
        prompt_text = f"{self.hostname}@root:~$ "
        gradient_chars = []
        for i, char in enumerate(prompt_text):
            rgb = self.gradient_color((255, 150, 150), (255, 230, 230), len(prompt_text), i)
            ansi_color = self.rgb_to_ansi(*rgb)
            gradient_chars.append(f"{ansi_color}{char}")
        print(''.join(gradient_chars) + Style.RESET_ALL, end='', flush=True)
       
    def print_success(self, text):
        success_text = f" → {text}"
        self.print_gradient_line(success_text, start_rgb=(0, 255, 0), end_rgb=(200, 255, 200))
       
    def print_error(self, text):
        error_text = f" → {text}"
        self.print_gradient_line(error_text, start_rgb=(255, 50, 50), end_rgb=(255, 150, 150))
       
    def print_warning(self, text):
        warning_text = f" → {text}"
        self.print_gradient_line(warning_text, start_rgb=(255, 200, 0), end_rgb=(255, 255, 150))
       
    def print_info(self, text):
        info_text = f" → {text}"
        self.print_gradient_line(info_text, start_rgb=(255, 150, 150), end_rgb=(255, 230, 230))
   
    def get_input_with_prompt(self, prompt_text=""):
        if prompt_text:
            gradient_chars = []
            for i, char in enumerate(prompt_text):
                rgb = self.gradient_color((255, 150, 150), (255, 230, 230), len(prompt_text), i)
                ansi_color = self.rgb_to_ansi(*rgb)
                gradient_chars.append(f"{ansi_color}{char}")
            print(''.join(gradient_chars) + Style.RESET_ALL, end='', flush=True)
       
        sys.stdout.flush()
        try:
            user_input = input()
            return user_input
        except (EOFError, KeyboardInterrupt):
            return ""
   
    def show_help(self):
        os.system('cls' if os.name == 'nt' else 'clear')
       
        small_skull = [
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢿⣧⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⡀⠀⠀⢀⡴⠛⠁⠀⠘⣿⡄⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⣤⡴⠋⠀⠀⠀⠀⠀⢿⣇⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⣿⠀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠈⣿⡀",
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢏⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⡇",
            "⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢿⡇",
            "⠀⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⢸⡇",
            "⠀⠀⠀⠀⠀⠀⢠⡞⠁⢹⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⠀",
            "⠀⠀⠀⠀⠀⣠⠟⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢸⠀",
        ]
       
        for line in small_skull:
            self.print_gradient_line(line, start_rgb=(255, 0, 0), end_rgb=(255, 200, 200))
       
        help_box = """
╔══════════════════════════════════════════════════════════════════════╗
║                           AVAILABLE COMMANDS                         ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║    1. Obfuscate Python Code                                          ║
║       • Protect your Python scripts with advanced obfuscation        ║
║                                                                      ║
║    2. Clear                                                          ║
║       • Clear the screen                                             ║
║                                                                      ║
║    3. Help                                                           ║
║       • Show this help menu                                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        self.print_gradient_text(help_box, start_rgb=(255, 50, 50), end_rgb=(255, 255, 255))
        print("\n" + " " * 30 + "Press Enter to continue...", end="")
        input()
   
    def generate_random_name(self, prefix="obf"):
        patterns = [f"{prefix}_{random.randint(10000, 99999)}"]
        special_names = [
            "m_Ln_Jh_Z", "Y_uzOVUH", "t_Vg_POq", "HO_EuoOIVZ",
            "j_gRITo", "I_kG_k_y", "p_A_G_s_TY", "CSVzXGKl_j",
            "MTqh_cL", "IMe_f_G_w", "module_inst", "calli_ptr"
        ]
        name = random.choice(special_names + patterns)
        self.defined_vars.add(name)
        return name
   
    def generate_math_func_definitions(self):
        lines = []
       
        lines.append("def __calli__(func_type, value, func_ptr):")
        lines.append("    try:")
        lines.append("        if 'Int32' in str(func_type):")
        lines.append("            return int(value)")
        lines.append("        elif 'Double' in str(func_type):")
        lines.append("            return float(value)")
        lines.append("        else:")
        lines.append("            return value")
        lines.append("    except:")
        lines.append("        return 0")
       
        lines.append("def __ldftn__(func_name):")
        lines.append("    import math")
        lines.append("    func_map = {")
        lines.append("        'ToInt32': lambda x: int(x),")
        for func in self.math_funcs:
            lines.append(f"        '{func.capitalize()}': math.{func},")
        lines.append("    }")
        lines.append("    return func_map.get(func_name, lambda x: x)")
       
        lines.append("calli = __calli__")
        lines.append("ldftn = __ldftn__")
       
        return "\n".join(lines)
   
    def generate_math_expr(self, max_depth=2, current_depth=0):
        if current_depth >= max_depth or random.random() < 0.3:
            num = random.uniform(1.0, 10000000.0)
            return f"{num:.10f}"
       
        func = random.choice(self.math_funcs)
        func_cap = func.capitalize()
       
        if random.choice([True, False]):
            inner = self.generate_math_expr(max_depth, current_depth + 1)
            return f"calli('System.Double(System.Double)', {inner}, ldftn('{func_cap}'))"
        else:
            left = self.generate_math_expr(max_depth, current_depth + 1)
            right = self.generate_math_expr(max_depth, current_depth + 1)
            op = random.choice(["+", "-", "*", "/"])
            return f"{left} {op} {right}"
   
    def generate_call_int32(self):
        inner = self.generate_math_expr(max_depth=1)
        return f"calli('System.Int32(System.Double)', {inner}, ldftn('ToInt32'))"
   
    def generate_safe_variable_assignment(self):
        var_name = self.generate_random_name("var")
        value = random.choice([
            self.generate_call_int32(),
            f"{random.randint(1, 1000)}",
            f"0x{random.randint(0x1000, 0xFFFF):04X}",
            f"\"{base64.b85encode(os.urandom(10)).decode()[:15]}\""
        ])
        return f"{var_name} = {value}"
   
    def generate_condition(self, max_parts=3):
        parts = []
        for _ in range(random.randint(2, max_parts)):
            parts.append(self.generate_call_int32())
       
        operators = ["^", "|", "&"]
        condition_parts = []
       
        for i in range(len(parts) - 1):
            condition_parts.append(parts[i])
            condition_parts.append(random.choice(operators))
        condition_parts.append(parts[-1])
       
        condition = " ".join(condition_parts)
       
        compare_op = random.choice(["==", "!=", "<", ">", "<=", ">="])
        compare_to = self.generate_call_int32()
       
        return f"({condition}) {compare_op} {compare_to}"
   
    def generate_control_block(self, indent=4):
        lines = []
        indent_str = " " * indent
       
        for _ in range(random.randint(3, 8)):
            lines.append(f"{indent_str}{self.generate_safe_variable_assignment()}")
       
        if random.random() < 0.7:
            condition = self.generate_condition(max_parts=2)
            lines.append(f"{indent_str}if {condition}:")
            inner_indent = " " * (indent + 4)
            for _ in range(random.randint(2, 5)):
                lines.append(f"{inner_indent}{self.generate_safe_variable_assignment()}")
       
        if random.random() < 0.6:
            loop_type = random.choice(["for", "while"])
            if loop_type == "for":
                loop_var = self.generate_random_name("i")
                lines.append(f"{indent_str}for {loop_var} in range({random.randint(1, 10)}):")
                inner_indent = " " * (indent + 4)
                lines.append(f"{inner_indent}pass")
            else:
                lines.append(f"{indent_str}while False:")
                inner_indent = " " * (indent + 4)
                lines.append(f"{inner_indent}break")
       
        if random.random() < 0.4:
            lines.append(f"{indent_str}try:")
            inner_indent = " " * (indent + 4)
            temp_var = self.generate_random_name("temp")
            lines.append(f"{inner_indent}{temp_var} = {random.randint(1, 1000)}")
            lines.append(f"{indent_str}except:")
            lines.append(f"{inner_indent}pass")
       
        return "\n".join(lines)
   
    def encrypt_code(self, code):
        try:
            code_obj = compile(code, '<obfuscated>', 'exec')
            bytecode = marshal.dumps(code_obj)
            compressed = zlib.compress(bytecode, level=9)
            encrypted = base64.b85encode(compressed).decode()
           
            chunk_size = random.randint(40, 60)
            chunks = [encrypted[i:i+chunk_size] for i in range(0, len(encrypted), chunk_size)]
           
            return chunks
        except:
            encrypted = base64.b85encode(code.encode()).decode()
            chunk_size = 50
            chunks = [encrypted[i:i+chunk_size] for i in range(0, len(encrypted), chunk_size)]
            return chunks

    def generate_dead_code(self, indent=4):
        lines = []
        indent_str = " " * indent
       
        for _ in range(random.randint(2, 5)):
            var_name = self.generate_random_name("dead")
            value = random.choice([
                f"{random.randint(1, 1000)}",
                f"0x{random.randint(0x1000, 0xFFFF):04X}",
                f"'{base64.b85encode(os.urandom(5)).decode()}'",
                f"{random.uniform(1.0, 100.0):.4f}"
            ])
            lines.append(f"{indent_str}{var_name} = {value}")
       
        if random.random() < 0.7:
            condition = "False"
            lines.append(f"{indent_str}if {condition}:")
            inner_indent = " " * (indent + 4)
            for _ in range(random.randint(1, 3)):
                var_name = self.generate_random_name("dead_if")
                value = random.randint(1, 100)
                lines.append(f"{inner_indent}{var_name} = {value}")
       
        if random.random() < 0.5:
            lines.append(f"{indent_str}while False:")
            inner_indent = " " * (indent + 4)
            lines.append(f"{inner_indent}pass")
       
        return "\n".join(lines)

    def generate_main_function(self, func_name, encrypted_chunks):
        self.defined_vars.clear()
        lines = []
        lines.append(f"def {func_name}(*args, **kwargs):")
        lines.append(self.generate_dead_code(indent=4))
        for _ in range(random.randint(5, 10)):
            lines.append(f"    {self.generate_safe_variable_assignment()}")
       
        for i in range(random.randint(10, 20)):
            block = self.generate_control_block(indent=4)
            lines.append(block)
        lines.append("    import base64, zlib, marshal")
        lines.append("    try:")
       
        chunk_vars = []
        for i, chunk in enumerate(encrypted_chunks):
            var_name = f"__c{i:03d}"
            chunk_vars.append(var_name)
            lines.append(f"        {var_name} = \"{chunk}\"")
       
        lines.append(f"        __data = ''.join([{', '.join(chunk_vars)}])")
        lines.append("        __decoded = base64.b85decode(__data)")
        lines.append("        __decompressed = zlib.decompress(__decoded)")
        lines.append("        __code = marshal.loads(__decompressed)")
        lines.append("        exec(__code, globals())")
        lines.append("    except Exception as e:")
        lines.append("        try:")
        lines.append("            __data2 = ''.join([globals().get(var, '') for var in [{}]])".format(", ".join([f"'{v}'" for v in chunk_vars])))
        lines.append("            __decoded2 = base64.b85decode(__data2)")
        lines.append("            exec(__decoded2.decode(), globals())")
        lines.append("        except:")
        lines.append("            pass")
       
        lines.append("    return 0")
       
        return "\n".join(lines)

    def obfuscate_file(self, input_path, output_path, main_func_name):
        self.print_info(f"Reading {input_path}...")
        with open(input_path, 'r', encoding='utf-8') as f:
            original_code = f.read()
       
        self.print_info("Encrypting code...")
        encrypted_chunks = self.encrypt_code(original_code)
       
        obfuscated = []
       
        obfuscated.append(self.generate_math_func_definitions())
        obfuscated.append("")
       
        fake_modules = ['sys', 'os', 'math', 'random', 'time', 'datetime']
        for _ in range(random.randint(5, 10)):
            module = random.choice(fake_modules)
            obfuscated.append(f"import {module}")
       
        obfuscated.append("")
       
        for i in range(random.randint(15, 30)):
            var_name = self.generate_random_name()
            value = random.choice([
                f"{self.generate_call_int32()}",
                f"{random.randint(-1000000, 1000000)}",
                f"\"{'x' * random.randint(10, 50)}\""
            ])
            obfuscated.append(f"{var_name} = {value}")
       
        obfuscated.append("")
       
        self.print_info("Generating complex control flow...")
        main_func = self.generate_main_function(main_func_name, encrypted_chunks)
        obfuscated.append(main_func)
       
        for _ in range(random.randint(2, 5)):
            func_name = self.generate_random_name("func")
            fake_chunks = [base64.b85encode(os.urandom(30)).decode() for _ in range(random.randint(3, 6))]
            fake_func = self.generate_main_function(func_name, fake_chunks)
            obfuscated.append("")
            obfuscated.append(fake_func)
       
        obfuscated.append("")
        obfuscated.append("if __name__ == \"__main__\":")
       
        for _ in range(random.randint(2, 5)):
            var_name = self.generate_random_name("init")
            value = f"{random.randint(1, 100)}"
            obfuscated.append(f"    {var_name} = {value}")
       
        obfuscated.append(f"    {main_func_name}()")
       
        output_code = "\n".join(obfuscated)
       
        # ────────────────────────────────────────────────
        header = [
            "# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            "# Protected by grave",
            "#  zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            ""
        ]
        final_output = "\n".join(header) + output_code
        # ────────────────────────────────────────────────
       
        self.print_info(f"Writing to {output_path}...")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_output)
       
        original_lines = len(original_code.split('\n'))
        obfuscated_lines = len(final_output.split('\n'))
       
        return original_lines, obfuscated_lines
   
    def run_obfuscation(self):
        os.system('cls' if os.name == 'nt' else 'clear')
       
        start_box = """╔══════════════════════════════════════════════════════════════════════╗
║                    STARTING OBFUSCATION PROCESS                      ║
╚══════════════════════════════════════════════════════════════════════╝"""
        self.print_gradient_text(start_box, start_rgb=(255, 50, 50), end_rgb=(255, 255, 255))
       
        while True:
            input_path = self.get_input_with_prompt(" → Enter Python file path to obfuscate: ")
           
            if os.path.exists(input_path):
                break
            error_msg = f"File not found: {input_path}"
            self.print_error(error_msg)
            print()
       
        func_name = self.get_input_with_prompt(" → Enter main function name (Enter for random): ")
       
        if not func_name:
            func_name = f"obf_{random.randint(10000, 99999)}"
       
        default_output = f"{os.path.splitext(input_path)[0]}_protected.py"
        output_path = self.get_input_with_prompt(f" → Enter output path (Enter for {default_output}): ")
       
        if not output_path:
            output_path = default_output
       
        print()
        config_box = """╔══════════════════════════════════════════════════════════════════════╗
║                         CONFIGURATION                                ║
╚══════════════════════════════════════════════════════════════════════╝"""
        self.print_gradient_text(config_box, start_rgb=(255, 50, 50), end_rgb=(255, 255, 255))
       
        info_lines = [
            f"Input:    {input_path}",
            f"Output:   {output_path}",
            f"Function: {func_name}",
            "╚══════════════════════════════════════════════════════════════════════╝"
        ]
       
        for i, line in enumerate(info_lines):
            if i < 3:
                self.print_gradient_line(line, start_rgb=(255, 50, 50), end_rgb=(255, 230, 230))
            else:
                self.print_gradient_line(line, start_rgb=(255, 50, 50), end_rgb=(255, 255, 255))
       
        confirm = self.get_input_with_prompt(" → Start obfuscation? (y/n): ")
       
        if confirm.lower() != 'y':
            self.print_error("Operation cancelled")
            return
       
        print()
        process_box = """╔══════════════════════════════════════════════════════════════════════╗
║                   PROCESSING YOUR CODE                               ║
╚══════════════════════════════════════════════════════════════════════╝"""
        self.print_gradient_text(process_box, start_rgb=(255, 50, 50), end_rgb=(255, 255, 255))
       
        self.print_warning("Generating complex control flow...")
       
        try:
            orig_lines, obf_lines = self.obfuscate_file(
                input_path, output_path, func_name
            )
           
            print()
            success_box = """╔══════════════════════════════════════════════════════════════════════╗
║              OBFUSCATION COMPLETED SUCCESSFULLY!                   ║
╚══════════════════════════════════════════════════════════════════════╝"""
            self.print_gradient_text(success_box, start_rgb=(0, 255, 0), end_rgb=(200, 255, 200))
           
            result_lines = [
                f"Original:    {orig_lines} lines",
                f"Obfuscated:  {obf_lines} lines",
                f"Expansion:   {obf_lines/orig_lines:.1f}x",
                f"Saved to:    {output_path}",
                "╚══════════════════════════════════════════════════════════════════════╝"
            ]
           
            for i, line in enumerate(result_lines):
                if i < 4:
                    self.print_gradient_line(line, start_rgb=(255, 150, 150), end_rgb=(255, 230, 230))
                else:
                    self.print_gradient_line(line, start_rgb=(255, 150, 150), end_rgb=(255, 255, 255))
           
            print()
            run_cmd = f"Run with: python {output_path}"
            self.print_success(run_cmd)
           
        except Exception as e:
            self.print_error(f"Error: {e}")
            return
       
        print()
        self.print_gradient_line("Press Enter to continue...", start_rgb=(255, 150, 150), end_rgb=(255, 230, 230))
        input()
   
    def main_menu(self):
        self.print_welcome_screen()
       
        while True:
            self.print_prompt()
            try:
                command = input().strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                break
           
            if command == "help" or command == "3":
                self.show_help()
                self.print_welcome_screen()
            elif command == "1":
                self.run_obfuscation()
                self.print_welcome_screen()
            elif command == "clear" or command == "2" or command == "cls":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_welcome_screen()
            elif command == "":
                continue
            else:
                self.print_error(f"Unknown command: {command}")
                self.print_info('Type "help" to see available commands')
                print()

def main():
    try:
        obfuscator = Obfuscator()
        obfuscator.main_menu()
    except KeyboardInterrupt:
        print()
        interrupt_msg = "Interrupted by user"
        ansi_color = obfuscator.rgb_to_ansi(255, 100, 100)
        print(f"{ansi_color}{interrupt_msg}{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print()
        error_msg = f"Unexpected error: {e}"
        ansi_color = obfuscator.rgb_to_ansi(255, 50, 50)
        print(f"{ansi_color}{error_msg}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()