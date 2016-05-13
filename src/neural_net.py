import numpy as np
from scipy.special import expit

sigmoid = expit

np.random.seed(42)

# fixed topology
class NeuralNet:
    def __init__(self, n_input, m_output, hidden_layers):
        '''
        hidden_layers is an array of n for each layer
        '''
        n_per_layer = [n_input, m_output]
        n_per_layer[1:1] = hidden_layers

        layers = []
        # [layer_1, layer_2] zipped with [layer_2, layer_3]
        for layer_i, layer_j in zip( n_per_layer[:-1], n_per_layer[1:] ):
            layers.append( np.random.rand(layer_j, layer_i) )

        self.layers = layers

    def evaluate(self, x):
        result = x

        for layer in self.layers:
            result = sigmoid(np.dot( layer, result ))

        return result

net = NeuralNet(3, 2, [])
