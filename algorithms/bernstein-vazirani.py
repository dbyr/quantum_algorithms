# written by David Byrne, based on circuits in N. David Mermin's "Quantum Computer Science: An Introduction"
import numpy as np
import random

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.tools.visualization import plot_bloch_vector

unkownNumber = random.randint(0,31)
q = QuantumRegister(6)
output = ClassicalRegister(6)
circuit = QuantumCircuit(q, output)

# set the circuit up in the correct state
circuit.x(q[5])
for i in range(0, 6):
    circuit.h(q[i])

# apply the oracle (which, at this point makes the algorithm pointless because it's limited by the classical process of applying the gates)
for i in range(0, 5):
    if (2 ** i) & unkownNumber:
        circuit.cx(q[i], q[5])

# reduce the phase
for i in range(0, 6):
    circuit.h(q[i])

# measure the value of a
circuit.measure(q, output)

# evaluate the value of the unkownNumber
backend = BasicAer.get_backend('statevector_simulator')
job = execute(circuit, backend, shots=2048)
result = job.result()

# display the results
qresult = 0
print("Quantum results:")
print(result.get_counts(circuit))
print("Actual value:")
print(unkownNumber)
