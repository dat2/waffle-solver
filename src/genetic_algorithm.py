import numpy as np
from neural_net import NeuralNet

# we are doing a fixed topology network
#
# this is specialized for a 3x3x3 rubiks cubes
# n_input is 54, 9 colours per face * 6 faces
# 2 moves per face (Clockwise, counter clockwise) * 6 faces
#
# 54 input colours, 42 in the first hidden layer, 21 in the second hidden layer
# 12 moves as the output layer
INPUT_SIZE = 54
HIDDEN_LAYERS = [42,21]
OUTPUT_SIZE = 12

class GeneticAlgorithm:
    def __init__(self, population_size, crossover_rate, mutation_rate):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

        self.create_initial_population()

    def create_initial_population(self):
        self.population = []

        for _ in range(self.population_size):
            self.population.append(NeuralNet(INPUT_SIZE, OUTPUT_SIZE, HIDDEN_LAYERS))

    def mutate(self, network):
        variance = 0.5
        num = np.random.uniform(-variance, variance)
        network.update_random_weight(num)

    def crossover(self):
        pass

    def iterate(self):
        pass

g = GeneticAlgorithm(20, 0.7, 0.03)
g.mutate(g.population[0])
