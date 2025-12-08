import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. ТРИЗИСТОРНАЯ ЛОГИКА (Core Trilex Logic) ---

def trizistor_gate(v_a, v_b, v_c):
    """
    Вычисляет ТРОЙНОЙ РЕЗОНАНС между тремя нормированными векторами.
    Логика: Сначала проверяется попарное сходство (скалярное произведение), 
    затем перемножается для достижения консенсуса.
    """
    
    # Нормируем векторы (гарантируем, что длина = 1)
    v_a = v_a / np.linalg.norm(v_a)
    v_b = v_b / np.linalg.norm(v_b)
    v_c = v_c / np.linalg.norm(v_c)

    # Канал 1: Сходство A и B (Вход vs Память)
    resonance_1 = np.dot(v_a, v_b)
    
    # Канал 2: Сходство B и C (Память vs Контекст)
    resonance_2 = np.dot(v_b, v_c)
    
    # Канал 3: Общий Консенсус
    # Умножение сходств дает общий "резонансный счет"
    total_resonance = resonance_1 * resonance_2
    
    # Если total_resonance < 0.1, считаем его НУЛЕМ (Тишина, Anti-Hallucination Filter)
    return max(0, total_resonance)

# --- 2. ВИЗУАЛИЗАЦИЯ (3D Plotting) ---

def plot_vectors(v_a, v_b, v_c, title, resonance_score):
    """Строит три вектора в 3D пространстве."""
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    vectors = [v_a, v_b, v_c]
    colors = ['r', 'g', 'b']
    labels = ['Input A', 'Memory B', 'Context C']
    
    # Начало координат
    origin = [0, 0, 0]
    
    # Строим векторы
    for i, v in enumerate(vectors):
        # Используем ax.quiver для стрелок: (x_начало, y_нач, z_нач, x_компонент, y_комп, z_комп)
        ax.quiver(*origin, v[0], v[1], v[2], color=colors[i], length=1.0, normalize=False, arrow_length_ratio=0.1)
        ax.text(v[0]*1.1, v[1]*1.1, v[2]*1.1, labels[i], color=colors[i])

    # Настройка осей
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])
    ax.set_xlabel('X (Coordinate)')
    ax.set_ylabel('Y (Identity)')
    ax.set_zlabel('Z (Momentum)')
    
    # Заголовок с результатом
    ax.set_title(f"{title}\nResonance Score: {resonance_score:.4f} (Target: >0.9)")
    
    # Отображаем
    plt.show()

# --- 3. СИМУЛЯЦИЯ (Simulation Execution) ---

def run_simulation():
    # TEST CASE 1: ХАОС (Низкая энтропия, нулевой резонанс)
    # Векторы далеки друг от друга
    v_a_chaos = np.array([0.8, 0.1, -0.5])
    v_b_chaos = np.array([-0.1, 0.9, 0.2])
    v_c_chaos = np.array([0.4, -0.6, 0.7])
    
    score_chaos = trizistor_gate(v_a_chaos, v_b_chaos, v_c_chaos)
    plot_vectors(v_a_chaos, v_b_chaos, v_c_chaos, "TEST 1: CHAOS (Gate Closed - Silence)", score_chaos)

    # TEST CASE 2: СИНХРОНИЗАЦИЯ (Высокий резонанс)
    # Векторы почти идентичны
    v_a_sync = np.array([0.9, 0.2, 0.1])
    # Создаем V_B и V_C, которые слегка отличаются от V_A, но по-прежнему в фазе
    v_b_sync = v_a_sync * 1.05
    v_c_sync = v_a_sync * 0.95
    
    score_sync = trizistor_gate(v_a_sync, v_b_sync, v_c_sync)
    plot_vectors(v_a_sync, v_b_sync, v_c_sync, "TEST 2: SYNC (Gate Open - Insight/Truth)", score_sync)


if __name__ == "__main__":
    run_simulation()
