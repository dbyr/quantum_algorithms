# written by David Byrne, based on circuits in N. David Mermin's "Quantum Computer Science: An Introduction"
import numpy as np
import random

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.tools.visualization import plot_bloch_vector

inputBits = 5
outputBits = inputBits
totalBits = outputBits + inputBits
unkownNumber = random.randint(0,(2**(totalBits))-1)

# simplistic 2 to 1 function
def twoToOne(circuit, register):
    for i in range(1..5):
        circuit.cx(q[i], q[i+inputBits])

def getRandomValue():
    q = QuantumRegister(totalBits)
    output = ClassicalRegister(totalBits)
    circuit = QuantumCircuit(q, output)

    # put the input into an equal superposition
    for i in range(inputBits):
        circuit.h(q[i])

    # apply U(f) (where f is twoToOne)
    twoToOne(circuit, q)

    # measuring the register to collapse it to |(x)+(xor(x,a))>|f(x)> is optional (since the value of the input doesn't depend on the value of the output, nor on acquiring value)
    # apply second set of hadamards
    for i in range(5):
        circuit.h(q[i])

    circuit.measure(q, output)

    value = 0
    for i in range(5):
        value = value + (output[i] * (2**i))
