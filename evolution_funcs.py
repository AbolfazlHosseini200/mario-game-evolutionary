import math
import random


def random_chromosome(length):
    chromosome = ''
    for i in range(length):
        chromosome += str(random.randint(0, 2))
    return chromosome


def creating_first_population(n, length):
    population = []
    for i in range(n):
        population.append(random_chromosome(length))
    return population


def fitness(actions, game_instance):
    Done, steps, game_environment = game_instance.get_score(actions)
    fitness_score = Done * 10 + steps * 2 + game_environment
    return fitness_score


def choose_best_chromosome(chromosomes, fitness_scores, new_population_number):
    new_population = []
    temp = sorted(fitness_scores, reverse=True)
    for i in range(new_population_number):
        new_population.append(chromosomes[fitness_scores.index(temp[i])])
    return new_population


def roulette_wheel(chromosomes, fitness_scores, new_population_number):
    summation = sum(fitness_scores)
    new_population = []
    for i in range(new_population_number):
        random_number = random.randint(0, math.floor(summation) - 1)
        selected = None
        cur = 0
        for j in fitness_scores:
            cur += j
            if random_number < cur:
                selected = j
                break
        new_population.append(chromosomes[fitness_scores.index(selected)])
    return new_population


def sus(chromosomes, fitness_scores, new_population_number):
    summation = sum(fitness_scores)
    maximum = summation // new_population_number
    random_number = random.randint(0, maximum - 1)
    new_population = []
    for i in range(new_population_number):
        selected = None
        cur = 0
        for j in fitness_scores:
            cur += j
            if random_number < cur:
                selected = j
                break
        new_population.append(chromosomes[fitness_scores.index(selected)])
        random_number += maximum
    return new_population


def roulette_wheel_for_parents(chromosomes, fitness_scores):
    summation = sum(fitness_scores)
    new_population = []
    for i in range(2):
        random_number = random.randint(0, math.floor(summation) - 1)
        selected = None
        cur = 0
        for j in fitness_scores:
            cur += j
            if random_number < cur:
                selected = j
                break
        new_population.append(chromosomes[fitness_scores.index(selected)])
    return new_population


def recombination(chromosome1, chromosome2, double_point=False):
    new_chromosome1 = ''
    new_chromosome2 = ''
    # recombination_point = random.randint(1, len(chromosome1))
    if double_point:
        recombination_point = len(chromosome1) // 3
        recombination_point2 = recombination_point
        recombination_point2 *= 2
        # while recombination_point2 == recombination_point:
        #     recombination_point2 = random.randint(1, len(chromosome1))
    else:
        recombination_point = len(chromosome1) // 2
        recombination_point2 = recombination_point
    flag = True
    for i in range(len(chromosome1)):
        if recombination_point == i or recombination_point2 == i:
            flag = not flag
        if flag:
            new_chromosome1 += chromosome1[i]
            new_chromosome2 += chromosome2[i]
        else:
            new_chromosome1 += chromosome2[i]
            new_chromosome2 += chromosome1[i]
    return new_chromosome1, new_chromosome2


def genetic_mutation(chromosome, probability_of_mutation=0.4):
    arr = list(chromosome)
    for i in range(len(arr)):
        random_number_for_mutation = random.randint(0, 100) / 100
        if random_number_for_mutation < probability_of_mutation:
            random_number_to_choose_mutation_action = random.randint(0, 1)
            if random_number_to_choose_mutation_action == 0:
                arr[i] = str((int(arr[i]) + 1) % 3)
            else:
                arr[i] = str((int(arr[i]) + 2) % 3)
    result = ''.join(arr)
    return result


def check_evolution_end(fitness_scores_new, fitness_scores_old, epsilon):
    avg1 = sum(fitness_scores_new) / len(fitness_scores_new)
    avg2 = sum(fitness_scores_old) / len(fitness_scores_old)
    if math.fabs(avg1 - avg2) < epsilon:
        return True
    else:
        return False


def check_results(chromosomes, fitness_scores, game_instance, level_number):
    temp = sorted(fitness_scores, reverse=True)[:5]
    print("_________Level" + str(level_number + 1) + "__________")
    for i in temp:
        print(game_instance.get_score(chromosomes[fitness_scores.index(i)]))
    return


def level_generator(n):
    level = ''
    for i in range(n):
        temp = random.randint(0, 3)
        if temp == 0:
            level += '_'
        elif temp == 1:
            level += 'M'
        elif temp == 2:
            level += 'L'
        elif temp == 3:
            level += 'G'
    return level
