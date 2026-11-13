# Simple Quantum vs Classical Comparison

A beginner-friendly example that shows the difference between classical randomness and quantum superposition.

## The High-Level Algorithm

**Goal:** Generate many random 0s and 1s and count them.

### Classical version (normal Python)
1. Flip a fair coin many times.
2. Count how many times you get heads (1) and tails (0).

### Quantum version (Qiskit)
1. Create one qubit (it starts in the state |0⟩).
2. Apply a **Hadamard gate**. This puts the qubit into superposition — it is simultaneously 0 and 1 until measured.
3. Measure the qubit many times (each measurement is called a “shot”).
4. Count how many times we got 0 and how many times we got 1.

Both should give roughly 50/50 results, but the quantum version is using true quantum superposition instead of classical random numbers.

---

## Files

- `classical_random.py` – pure Python version
- `superposition.py` – Qiskit version

## How to run the Qiskit version

```bash
pip install qiskit qiskit-aer
python superposition.py
```
