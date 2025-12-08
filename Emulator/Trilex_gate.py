# Project Trilex: Vector Resonance Logic Emulator
# Copyright (C) 2025 Pavel Popov
# Licensed under GNU GPLv3

import numpy as np
import math

class SimurealityDemo:
    def __init__(self):
        print("--- INITIALIZING TRIZISTOR EMULATION ---")
        
    def generate_vector(self, dim=3):
        """Создает случайный 3D-вектор (Трилекс)"""
        v = np.random.randn(dim)
        return v / np.linalg.norm(v)  # Нормализация (делаем длину = 1)

    # --- ПОДХОД 1: КЛАССИЧЕСКАЯ НЕЙРОСЕТЬ (МАТЕМАТИКА) ---
    def standard_neuron(self, input_vec, weight_vec):
        """
        Классический подход: Умножаем и складываем.
        Требует много вычислений, результат - просто число.
        """
        # Скалярное произведение (Dot Product)
        activation = np.dot(input_vec, weight_vec)
        # Сигмоида (Activation Function)
        output = 1 / (1 + math.exp(-activation))
        return output

    # --- ПОДХОД 2: ТРИЗИСТОРНАЯ ЛОГИКА (ГЕОМЕТРИЯ) ---
    def trizistor_gate(self, input_vec, memory_vec, context_vec):
        """
        Подход Simureality: TRI_LOCK.
        Сравниваем ГЕОМЕТРИЮ трех каналов.
        Выход открывается только при тройном резонансе.
        """
        # Канал 1: Проверка Адреса (Вход vs Память)
        resonance_1 = np.dot(input_vec, memory_vec)
        
        # Канал 2: Проверка Контекста (Вход vs Контекст)
        resonance_2 = np.dot(input_vec, context_vec)
        
        # Канал 3: Спин/Фаза (Синхронизация)
        # В симуляции это просто проверка, совпадают ли знаки проекций
        phase_lock = 1.0 if (resonance_1 * resonance_2) > 0 else 0.0
        
        # ИТОГОВЫЙ ГЕЙТ: Работает только если есть Фаза и Резонанс
        # Это не умножение, это физическое "совпадение"
        total_resonance = abs(resonance_1 * resonance_2) * phase_lock
        
        return total_resonance

# --- ЗАПУСК СИМУЛЯЦИИ ---
sim = SimurealityDemo()

# Данные
input_signal = sim.generate_vector()  # Входящий сигнал (например, слово "Кот")
neuron_weight = sim.generate_vector() # Память нейрона (понятие "Животное")
context_signal = sim.generate_vector() # Контекст (например, тема "Зоология")

print(f"\nVector Input: {input_signal}")

# 1. Классический тест
std_out = sim.standard_neuron(input_signal, neuron_weight)
print(f"\n[Legacy AI] Output: {std_out:.4f}")
print("-> Просто число. Нет понимания 'почему'. Трата энергии на вычисления.")

# 2. Тризисторный тест
tri_out = sim.trizistor_gate(input_signal, neuron_weight, context_signal)
print(f"\n[Simureality AI] Output: {tri_out:.4f}")
print("-> Геометрический резонанс. Если 0 - ток не идет (0 энергии).")
print("-> Учитывает КОНТЕКСТ аппаратно, без лишних циклов.")

if tri_out > 0.5:
    print("\nRESULT: GATE OPEN (Смысл совпал!)")
else:
    print("\nRESULT: GATE CLOSED (Шум отфильтрован аппаратно)")
