from functools import partial
from random import choices, randint, randrange
import random
import time
from typing import Callable, List, Tuple
from models import *

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]

# En un genoma (un día de la semana) un 0 representa espacio vacío; un 1, un
# espacio ocupado. Espacio o 'bloque': una sección de 2 horas desde las 7 a.m.
def generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length) # returns a k-list with random elements (0, 1)

# Generación de los 5 genomas (5 días de clase de la semana)
def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

# Función fitness para calificar a un genoma. Irá restando puntos de valor
# si hay huecos entre materia (sin contar los huecos antes y después de laborar)
def fitness(genome: Genome) -> int:
    has_started = False
    last_block = False
    block_count = 0
    hole_count = 0
    bad_count = 0
    count = 0
    value = 7

    for block in genome:
        count += 1

        if block == 1:
            has_started = True
            last_block = True
            block_count += 1

        if last_block and block == 0:
            last_block = False
            hole_count += 1

        if last_block == False and block == 0:
            hole_count += 1

        if (last_block == True or count == 7) and hole_count > 0:
            bad_count += hole_count
            hole_count = 0

    return value - bad_count

# Seleccionar un par de genomas para producir uno mejor que ellos
def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    )

# Hacer un crossover de dos genomas
def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomas a y b deben tener el mismo tamanio!")
    
    length = len(a)

    if length < 2:
        return a, b

    p = randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]

# Mutar un genoma para obtener más variedad en las reproducciones
def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random.random() > probability else abs(genome[index] - 1)
    return genome

def run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int,
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = single_point_crossover,
        mutation_func: MutationFunc = mutation,
        generation_limit = 100
) -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(
            population,
            key=lambda genome: fitness_func(genome),
            reverse=True
        )

        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    population = sorted(
        population,
        key=lambda genome: fitness_func(genome),
        reverse=True
    )

    return population, i

start = time.time()
population, generations = run_evolution(
    populate_func=partial(
        generate_population, size=(5), genome_length=7
    ),
    fitness_func=partial(
        fitness
    ),
    fitness_limit=7,
    generation_limit=100
)
end = time.time()

def genome_to_list(genome: Genome) -> []: # type: ignore
    result = []
    for i in population:
        result += [i]

    return result

# TESTING FITNESS IN POPULATION
# population = generate_population(5, 7)

# for genome in population:
#     print(fitness(genome))

print(f"number of generations: {generations}")
print(f"time: {end - start}s")
print(f"best solution: {genome_to_list(population[0])}")