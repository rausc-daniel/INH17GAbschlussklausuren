from random import randrange

class Neuron():
    weights = []

    def __init__(self, learning_rate, threshold, neurons, weights = None):
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.neurons = neurons
        if weights is None:
            for i in len(neurons):
                self.weights[i] = randrange(-1, 1)
        else:
            self.weights = weights

    def evaluate(self):
        res = 0
        for i in range(len(self.neurons)):
            res = res + self.weights[i] * self.neurons[i].fire()
        return res

    def fire(self):
        if self.evaluate() > self.threshold:
           return 1
        return 0

    # returns the learning rate * (output that was predicted - actual output of the neuron) *
    # output of the neuron in the previous layer whose weight is to be changed
    def calc_error_delta_rule(self, target_output, weight):
        self.weights[weight] += self.learning_rate * (target_output - self.fire()) * self.neurons[weight].fire()

    # calculates how the weight has to be changes via the learning rate, the output of the previous layer and the neuron in question
    def calc_error_hebb_theory(self, weight):
        self.weights[weight] += self.learning_rate * self.evaluate() * self.neurons[weight].fire()

class InputNeuron(Neuron):
    def __init__(self, intake):
        self.intake = intake
        
    def fire(self):
        return self.intake

class OutputNeuron(Neuron):
    def __init__(self, learning_rate, neurons, weights):
        super().__init__(learning_rate, 0, neurons, weights)