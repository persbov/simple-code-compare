"""
Simple Qiskit example: put one qubit into superposition and measure it.

High-level algorithm:
1. Create one qubit (starts as |0>)
2. Apply Hadamard gate → creates equal superposition of |0> and |1>
3. Measure the qubit many times
4. Count the results

This is the quantum version of a fair coin flip.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Create a circuit with 1 qubit and 1 classical bit to store the result
circuit = QuantumCircuit(1, 1)

# 2. Apply Hadamard gate on qubit 0
#    This puts the qubit into superposition: (|0> + |1>) / √2
circuit.h(0)

# 3. Measure the qubit and store the result in the classical bit
circuit.measure(0, 0)

# 4. Run the circuit many times on a simulator
simulator = AerSimulator()
job = simulator.run(circuit, shots=1024)
counts = job.result().get_counts()

print("Quantum superposition results:")
print(counts)
print("\n(You should see roughly equal numbers of '0' and '1')")
