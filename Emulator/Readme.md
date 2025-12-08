# Trilex Logic Emulator (MVP)

### 🔮 Concept: Beyond Binary AI
This script demonstrates the core logic of the **Project Trilex** architecture. It compares two approaches to computing "meaning" in artificial intelligence:

1.  **Legacy AI (Standard Neuron):**
    * **Logic:** `Dot Product + Sigmoid Activation`.
    * **Problem:** It calculates *everything*, even noise. It consumes energy to process mismatched vectors, producing a "fuzzy" activation (e.g., 0.48) that leads to hallucinations.
    * **Physics:** Equivalent to pushing electrons through a resistor (Heat).

2.  **Trilex AI (Resonance Gate):**
    * **Logic:** `Geometric Synchronization (Input ∩ Memory ∩ Context)`.
    * **Solution:** It uses a "Gate" mechanism. If the geometric phase of the input does not resonate with the context, the gate stays **physically closed**.
    * **Result:** `Output = 0.0` (Absolute Silence). No energy wasted on noise. No hallucinations.
    * **Physics:** Equivalent to optical interference. Constructive = Signal, Destructive = Silence.

---

### 🚀 How to Run

Requirements: `numpy`

```bash
pip install numpy
python trilex_emulator.py

```

📊 Understanding the Output
When you run the script, you will see a comparison:
 * [Legacy AI] Output: You will often see values like 0.45 or 0.55. This is "doubt." In a massive LLM, these accumulating doubts cause the model to lie or hallucinate facts.
 * [Simureality AI] Output: You will likely see 0.0 (Gate Closed) or a high value (Gate Open).
   * Gate Closed: The system detected that the Input Vector does not match the Context Vector. It blocked the signal before processing it deeply.
   * Efficiency: In a hardware implementation (Optical/Spintronic), a "Closed Gate" consumes ZERO energy and generates ZERO heat.
🛠 Under the Hood
The trizistor_gate function implements the 3-Channel Resonance Protocol:
 * Channel A (Input): The incoming data pattern.
 * Channel B (Memory): The stored weight/pattern.
 * Channel C (Context): The global intent or subject matter.
The signal propagates ONLY if all three vectors align in the high-dimensional phase space.
# The Core Logic
total_resonance = abs(resonance_1 * resonance_2) * phase_lock

License: GNU GPLv3
Copyright © 2025 Pavel Popov

***


