import random
import copy
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
        self.fitness = np.array([1 for _ in self.population])

    def create_initial_population(self):
        self.population = []

        for _ in range(self.population_size):
            self.population.append(NeuralNet(INPUT_SIZE, OUTPUT_SIZE, HIDDEN_LAYERS))

    def mutate(self, network):
        variance = 0.5
        num = np.random.uniform(-variance, variance)
        network.update_random_weight(num)
        return network

    def mutate_chromosome(self, chromosome):
        if np.random.choice([True, False], p=[self.mutation_rate,1.0 - self.mutation_rate]):
            return self.mutate(chromosome)
        else:
            return chromosome

    def crossover(self, n1, n2):
        new_a = copy.deepcopy(n1)
        new_b = copy.deepcopy(n2)

        for layer_i, both_layers in enumerate(zip(n1.layers, n2.layers)):
            n1_layer, n2_layer = both_layers
            # iterate through rows and columns
            row_i = len(n1_layer)
            column_i = len(n1_layer[0])

            for r in range(row_i):
                for c in range(column_i):
                    # random number lol
                    if np.random.choice([True, False], p=[0.5,0.5]):
                    # switch over individual weights
                        a_weight = n1.get_weight(layer_i, r, c)
                        b_weight = n2.get_weight(layer_i, r, c)
                        new_a.update_weight(layer_i, r, c, b_weight)
                        new_b.update_weight(layer_i, r, c, a_weight)

        return new_a, new_b

    def crossover_chromosome(self, chromosome_a, chromosome_b):
        if np.random.choice([True, False], p=[self.crossover_rate,1.0 - self.crossover_rate]):
            return self.crossover(chromosome_a, chromosome_b)
        else:
            return chromosome_a, chromosome_b

    def roulette_select(self):
        normalized_fitness = self.fitness / np.sum(self.fitness)
        return np.random.choice(self.population, len(self.population), p=normalized_fitness, replace=False)

    def fitness(self, percent_solved_fn):
        pass

    def generate_new_population(self):
        new_population = []

        ordered_selection = self.roulette_select()

        # pairwise zipping
        iterable = iter(ordered_selection)
        for a,b in zip(iterable, iterable):
            a_new, b_new = self.crossover_chromosome(a,b)
            a_mutated, b_mutated = self.mutate(a_new), self.mutate(b_new)
            new_population.append(a_mutated)
            new_population.append(b_mutated)

    def run(self):
        pass

g = GeneticAlgorithm(20, 0.7, 0.03)
g.generate_new_population()
