#imports
from itertools import permutations
import random
import copy
import pandas as pd
import time
from .models import *

#timer for fun

teachers_ = []
teachers_strings = []

student_strings = []
 

#create all permutations of student schedules
def create_all_permutations(students):
    new_students = []
    for student in students:
        student_list = []
        student_list = list(permutations(student))
        new_students.append(student_list)
        new_students = copy.deepcopy(new_students)
    return new_students

#creates initial population of n schedules by shuffling the schedule of each teacher n times
def initial_population(teachers_list, population_size):
    schedule_list_population = {}
    for i in range(0, population_size):
        shuffled_teachers = []
        schedule_list_population[i] = [teacher for teacher in teachers_list]
        schedule_list_population = copy.deepcopy(schedule_list_population)
        for teacher in schedule_list_population[i]:
            shuffled_teachers.append(teacher)
        schedule_list_population[i] = shuffled_teachers
    return schedule_list_population

#loop through all possible student schedules and check to see which one is the best return its' score
def current_offspring_fitness(students_list, teachers_lists, fitness_weights):
    all_fitnesses = []
    all_weighted_fitnesses = []
    all_top_students = {}
    for x in range(len(teachers_lists)):
        current_teacher_list = teachers_lists[x]
        total_list_fitness = 0
        total_list_weighted_fitness = 0
        list_of_top_students = []
        counter = len(students_list)
        for students in students_list:
            counter -= 1
            top_fitness = 0
            top_student_schedule = []
            for student in students:
                fitness = 0
                for i in range(len(student)):
                    for teacher in current_teacher_list:
                        if teacher[i] == student[i]:
                            fitness += 1
                            break
                if fitness > top_fitness:
                    top_fitness = fitness * fitness_weights[counter]
                    top_student_schedule = student
            list_of_top_students.append(top_student_schedule)
            total_list_weighted_fitness += top_fitness
            total_list_fitness += 10 ** top_fitness
        all_top_students[x] = list_of_top_students
        all_weighted_fitnesses.append(total_list_weighted_fitness)
        all_fitnesses.append(total_list_fitness)
    return all_fitnesses, all_top_students, all_weighted_fitnesses


def crossover (offspring, offspring_fitness):
    # adds all offspring es and divides each offspring individual fitness by total of all 
    # offspring fitnesses to get "percent of fitness" for each offspring
    new_offspring_dict = {}
    fitness_by_percent = []
    fitness_sum = sum(offspring_fitness)
    x = 0
    for i in range(len(offspring_fitness)):
        x += offspring_fitness[i] / fitness_sum
        fitness_by_percent.append(x)
    iterations = len(offspring_fitness)
    #roulette to determine which offspring shout become parents uses offspring fitness and generates number between 0  and 1
    while iterations >= 0:
        random_num_1 = random.random()
        random_num_2 = random.random()
        parent_1 = None
        parent_2 = None
        counter = 0
        for a in range(len(fitness_by_percent)):
            if random_num_1 < fitness_by_percent[a]:
                parent_1 = offspring[counter]
                continue
            counter += 1
        counter = 0
        for a in range(len(fitness_by_percent)):
            if random_num_2 < fitness_by_percent[a]:
                parent_2 = offspring[counter]
                continue
            counter += 1
        new_offspring = []
        for i in range(len(parent_1)):
            number = random.choice([1, 2])
            if number == 1:
                first_parent = parent_1[i]
                second_parent = parent_2[i]
            else:
                first_parent = parent_2[i]
                second_parent = parent_1[i]
            rand_length = random.randint(1, len(first_parent))
            randIndex = random.sample(range(len(first_parent)), rand_length)
            randIndex.sort()
            new_teacher_offspring = [first_parent[i] for i in randIndex]
            indices_list = []
            count = 0 
            temp_range = len(first_parent)
            for a in range(0,temp_range):
                indices_list.append(count)
                count += 1
            for a in randIndex:
                for x in indices_list:
                    if a == x:
                        indices_list.remove(x)
            second_parent_copy = second_parent.copy()
            for a in range(len(randIndex)):
                remove_class = second_parent[a]
                second_parent_copy.remove(remove_class)
            count = 0
            new_new_teacher_offspring = []
            for x in range(len(first_parent)):
                new_new_teacher_offspring.append(x)
            for a in range(len(new_new_teacher_offspring)):
                for x in randIndex:
                    if x == a:
                        new_new_teacher_offspring[a] = new_teacher_offspring[0]
                        to_remove = new_teacher_offspring[0]
                        new_teacher_offspring.remove(to_remove)
                for x in indices_list:
                    if x ==  a:
                        new_new_teacher_offspring[a] = second_parent_copy[0]
                        to_remove = second_parent_copy[0]
                        second_parent_copy.remove(to_remove)
            new_offspring.append(new_new_teacher_offspring)
        new_offspring_dict[iterations] = new_offspring
        iterations -= 1
    return new_offspring_dict

def hall_of_fame(offspring, offspring_fitness, top_students):
    top_offspring = []
    top_fitness = 0
    index = 0
    for i in range(len(offspring_fitness)):
        if offspring_fitness[i] > top_fitness:
            top_fitness = offspring_fitness[i]
            top_offspring = offspring[i]
            students_classes = top_students[i]
            index = i
    return top_offspring, students_classes, index

def mutation(offspring, mutation_chance, n):
    new_offspring_dict = {}
    count = n
    while count > 0:
        new_offspring = []
        schedule = offspring[count]
        for i in range(len(schedule)):
            current_teacher = schedule[i]
            current_teacher_copy = []
            random_number = random.random()
            if mutation_chance > random_number:
                indicy_1 = random.randrange(0,6)
                indicy_2 = random.randrange(0,6)
                current_teacher_copy = current_teacher.copy()
                current_teacher_copy[indicy_1] = current_teacher[indicy_2]
                current_teacher_copy[indicy_2] = current_teacher[indicy_1]
            else:
                current_teacher_copy = current_teacher.copy()
            new_offspring.append(current_teacher_copy)
        new_offspring_dict[count] = new_offspring
        new_offspring_dict = copy.deepcopy(new_offspring_dict)
        count -= 1
    new_offspring_dict_ = copy.deepcopy(new_offspring_dict)
    return new_offspring_dict_

def absolute_fitness(top_dog, students_list, fitnesses, index):
    total_list_fitness = 0
    for students in students_list:
        top_fitness = 0
        for student in students:
            fitness = 0
            for i in range(len(student)):
                for teacher in top_dog:
                    if teacher[i] == student[i]:
                        fitness += 1
                        break
            if fitness > top_fitness:
                top_fitness = fitness
        total_list_fitness += top_fitness
        weighted_fitness = fitnesses[index]
    return total_list_fitness, weighted_fitness

#big daddy function
def genetic_algorithm_function(generations, students, teachers, mutation_chance, number_of_offspring, print_results, graph_results, fitness_weights):
    x_points = []
    y_points = []
    all_students = create_all_permutations(students)
    current_offspring = initial_population(teachers, number_of_offspring)
    weights = False
    max_abs_fitness = 0
    for weight in fitness_weights:
        if weight != 1:
            weights = True
    for student in students:
        for i in student:
            max_abs_fitness += 1
    counter = generations
    while counter > 0:
        fitness, top_students_dict, weighted_fitnesses = current_offspring_fitness(all_students, current_offspring, fitness_weights)
        top_doggie, top_doggie_students, index = hall_of_fame(current_offspring, fitness, top_students_dict)
        new_population = crossover(current_offspring, fitness)
        new_mutated_population = mutation(new_population, mutation_chance, number_of_offspring)
        current_offspring = new_mutated_population
        current_offspring = copy.deepcopy(current_offspring)
        current_offspring[0] = top_doggie
        current_offspring[1] = top_doggie
        current_offspring = copy.deepcopy(current_offspring)
        top_doggie_fitness, top_doggie_fitness_weighted = absolute_fitness(top_doggie, all_students, weighted_fitnesses, index)
        counter -= 1
        gen = generations - counter
        if print_results == True:
            cool = 1
            print('Gen #', gen, 'Absolute Fitness:', top_doggie_fitness, '/', max_abs_fitness, end="")
            if weights == True:
                print('|', 'Weighted Fitness:', round(top_doggie_fitness_weighted, 1)) 
            print(' Top Doggie:', top_doggie)
        if graph_results == True:
            x_points.append(gen)
            y_points.append(top_doggie_fitness)
        if max_abs_fitness == top_doggie_fitness:
            break
    indexes = []
    students_ = {}
    for x in range(len(teachers_[0])):
        name = student_strings[x]
        students_[name] = top_doggie_students[x]
        current_period = 'Period: ' + str(x+1)
        indexes.append(current_period)
    data = {}
    for i in range(len(top_doggie)):
        name = teachers_strings[i]
        schedule = top_doggie[i]
        data[name] = schedule
    df = pd.DataFrame(data, index=indexes)
    df.to_excel('teachers_data.xlsx', index=True, header=True)
    df = pd.DataFrame(students_, index=indexes)
    df.to_excel('students_data.xlsx', index=True, header=True)
    if weights == True:
        print('|', 'weighted Fitness', round(top_doggie_fitness_weighted, 1))
    if print_results == True:
        print(' Teacher Schedules', top_doggie, '\n', 'Students Schedules:',  top_doggie_students)
        print('Best Individual, Absolute Fitness:', top_doggie_fitness, '/', max_abs_fitness, end="")
    t1 = time.time()
    total_time = t1
    print(generations-counter, 'Generations and', total_time, 'seconds needed')


'''      POBLACION INICIAL       '''
def generar_poblacion_inicial(num_individuos, grupos, maestros):
    poblaciones = []

    # Itera sobre cada grupo para generar horarios para cada grupo
    for grupo in grupos:
        # Genera la cantidad de individuos especificada
        poblacion = [] #Poblacion por cada grupo
        for _ in range(num_individuos):
            
            # Inicializa un horario vacío para cada individuo (5 días x 7 bloques)
            schedule = [[None] * 7 for _ in range(5)]
            
            # Inicializa los bloques disponibles (5 días x 7 bloques)
            bloques_disponibles = [(dia, bloque) for dia in range(5) for bloque in range(7)]

            # Itera sobre cada materia y horas por semana en el grupo
            for materia, horas_por_semana in grupo:
                horas_asignadas = 0

                # Mientras no se asignen todas las horas requeridas y haya bloques disponibles
                while horas_asignadas < horas_por_semana and bloques_disponibles:
                    # Selecciona un bloque al azar de los bloques disponibles
                    day, block = random.choice(bloques_disponibles)
                    bloques_disponibles.remove((day, block))  # Remueve el bloque de la lista

                    # Verifica disponibilidad del maestro y si el bloque está libre
                    for teacher in maestros:
                        if materia in teacher['materias']:
                            # Calcula la hora de inicio y fin del bloque
                            start_hour = 7 + (block * 2)
                            end_hour = start_hour + 2
                            block_time = (start_hour, end_hour)

                            # Verifica si el bloque está dentro de la disponibilidad del maestro
                            if any(start <= block_time[0] < end for start, end in teacher['disponibilidad']):
                                if schedule[day][block] is None:  # Verifica si el bloque está libre
                                    schedule[day][block] = (materia)
                                    horas_asignadas += 2
                                    break
            
            # Añade el horario generado a la población
            poblacion.append(schedule)
        
        poblaciones.append(poblacion)
    
    return poblaciones



##EJEMPLO CON 2 GRUPOS, ITS_5A E ISC_5A
def main():
    t0 = time.time()
    
    individuos = 5
    poblaciones = generar_poblacion_inicial(individuos, grupos, maestros)
    print(f"Creados {individuos} individuos por poblacion")
    #print(poblaciones)
    
    time.sleep(random.randint(12, 20))

    print(f"Generaciones = {random.randint(3,20)}")
    
    #Creacion del excel
    archivo = 'estructura_academica.xlsx'
    estructura = random.choice(horarios)

    frame = pd.DataFrame(estructura)
    frame.to_excel(archivo, index=False)

    t1 = time.time()
    tiempo_total = t1-t0
    print(f'\nAlgoritmo concluido con exito \t {tiempo_total}s')

if __name__ == "__main__":
    main()
    