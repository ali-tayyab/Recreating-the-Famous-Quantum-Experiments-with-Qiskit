import qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.visualization import plot_histogram, plot_distribution, plot_bloch_multivector
from qiskit.circuit import Parameter
from qiskit_ibm_runtime import Options, Session, SamplerV2 as Sampler, QiskitRuntimeService
from qiskit_aer import AerSimulator
from qiskit.result import marginal_distribution
from qiskit.transpiler import generate_preset_pass_manager
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from IPython.display import display
import io