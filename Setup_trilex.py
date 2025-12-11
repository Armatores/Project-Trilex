import os

# Определение структуры папок и файлов с их содержимым
# Мы используем последние отлаженные версии скриптов

structure = {
    "src": {
        "__init__.py": "",
        "core": {
            "__init__.py": "",
            # ALU: Арифметика физики (Движение = Умножение)
            "alu.py": """
import math

class TrilexALU:
    def __init__(self):
        # Карта операндов: Базис пространства
        self.basis_map = {'+x': 2, '-x': 0.5, 
                          '+y': 3, '-y': (1/3), 
                          '+z': 5, '-z': 0.2}
        
    def move(self, signature, axis):
        multiplier = self.basis_map.get(axis, 1)
        new_sig = signature * multiplier
        return int(new_sig) if new_sig.is_integer() else new_sig

    def merge_objects(self, sig_a, sig_b):
        return sig_a * sig_b

    def get_distance_metric(self, sig_a, sig_b):
        return math.gcd(sig_a, sig_b)
""",
        },
        "physics": {
            "__init__.py": "",
            # COLLIDER: Гравитация через НОД
            "collider.py": """
import random
import math
from collections import defaultdict

class TrilexCollider:
    def __init__(self, num_particles=200, max_val=1000):
        self.particles = [random.randint(2, max_val) for _ in range(num_particles)]
        self.particles.append(2310) # 2*3*5*7*11 (Massive object)
        self.connections = defaultdict(list)

    def run_cycle(self):
        print(f"--- [SYSTEM]: COLLIDER STARTED. Particles: {len(self.particles)} ---")
        interaction_count = 0
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                p_a = self.particles[i]
                p_b = self.particles[j]
                if math.gcd(p_a, p_b) > 1:
                    self.connections[p_a].append(p_b)
                    self.connections[p_b].append(p_a)
                    interaction_count += 1
        print(f"--- [SYSTEM]: CYCLE COMPLETE. Interactions: {interaction_count} ---")
        return self.connections
""",
        },
        "semantics": {
            "__init__.py": "",
            # MIND: Семантический процессор (Король/Королева)
            "mind.py": """
import math

class VectorMind:
    def __init__(self):
        self.basis = {
            'LIVING': 2, 'HUMAN': 3, 'MALE': 5, 
            'FEMALE': 7, 'POWER': 11, 'YOUNG': 13
        }
        self.dictionary = {}
        self.reverse_dict = {}
        
        # Init Concepts
        self.learn("Young", ['YOUNG'])
        self.learn("Man", ['LIVING', 'HUMAN', 'MALE'])
        self.learn("Woman", ['LIVING', 'HUMAN', 'FEMALE'])
        self.learn("King", ['LIVING', 'HUMAN', 'MALE', 'POWER'])
        self.learn("Queen", ['LIVING', 'HUMAN', 'FEMALE', 'POWER'])
        self.learn("Prince", ['LIVING', 'HUMAN', 'MALE', 'POWER', 'YOUNG'])
        self.learn("Princess", ['LIVING', 'HUMAN', 'FEMALE', 'POWER', 'YOUNG'])

    def learn(self, word, components):
        signature = 1
        for comp in components:
            if comp in self.basis: signature *= self.basis[comp]
        self.dictionary[word] = signature
        self.reverse_dict[signature] = word

    def think(self, equation_str):
        # Format: "A / B * C"
        try:
            tokens = equation_str.split()
            val_a = self.dictionary[tokens[0]]
            val_b = self.dictionary[tokens[2]]
            val_c = self.dictionary[tokens[4]]
            
            result_sig = (val_a / val_b) * val_c
            
            if result_sig.is_integer():
                word = self.reverse_dict.get(int(result_sig), "UNKNOWN")
                return f"RESULT: {word} (Sig: {int(result_sig)})"
            else:
                return f"PARADOX: Fractional Result ({result_sig:.2f})"
        except Exception as e:
            return f"ERROR: {e}"
""",
        }
    },
    "requirements.txt": "numpy\n"
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        
        if isinstance(content, dict):
            # Это папка
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"[+] Created directory: {path}")
            create_structure(path, content)
        else:
            # Это файл
            with open(path, "w", encoding="utf-8") as f:
                f.write(content.strip())
            print(f"[+] Created file: {path}")

if __name__ == "__main__":
    print("--- Trilex Project Architect ---")
    create_structure(".", structure)
    print("\n[SUCCESS] Project structure deployed.")
    print("Now run: pip install -r requirements.txt")
