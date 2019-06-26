from neurons import Neuron, InputNeuron, OutputNeuron

i1 = InputNeuron(0)
i2 = InputNeuron(1)
i3 = InputNeuron(0)

# learning rate, thresholds of connected neurons, connected neurons, initial connection weights
h1 = Neuron(0.1, 0.5, [i1], [1])
h2 = Neuron(0.1, 0.3, [i2], [1])
h3 = Neuron(0.1, 0.8, [i3], [1])

h4 = Neuron(0.1, 0.6, [h1, h2, h3], [0.3, -0.4, 0.7])

o = OutputNeuron(0.1, [h4], [0.3])

print(o.fire())

for _ in range(100):
    h4.calc_error_delta_rule(1, 1)

print(o.fire())
