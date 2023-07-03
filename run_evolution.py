import game
import evolution_funcs as funcs
import matplotlib.pyplot as plt


def calculate_fitness_scores(population, game_instance):
    fitness_scores = []
    for chromosome in population:
        fitness_scores.append(funcs.fitness(chromosome, game_instance))
    return fitness_scores


def choose_parents_and_recombination(population_given, fitness_scores_given, number_of_new_chromosomes):
    new_born = []
    for _ in range(number_of_new_chromosomes // 2):
        parents = funcs.roulette_wheel_for_parents(population_given, fitness_scores_given)
        res = funcs.recombination(parents[0], parents[1])
        new_born.append(funcs.genetic_mutation(res[0], 0.1))
        new_born.append(funcs.genetic_mutation(res[1], 0.1))
    return new_born


evolution_loop = 100
population_number = 200
levels_directory = './levels/level'
levels = []
for i in range(1, 11):
    with open(levels_directory + str(i) + '.txt', 'r') as file:
        file_contents = file.read()
        levels.append(file_contents)
game_instance = game.Game(levels)
for cnt in range(len(levels)):
    game_instance.load_next_level()
    population = funcs.creating_first_population(population_number, len(levels[cnt]))
    fitness_scores = None
    avg_x = []
    avg_y = []
    best_x = []
    best_y = []
    worst_x = []
    worst_y = []
    for j in range(evolution_loop):
        fitness_scores = calculate_fitness_scores(population, game_instance)
        population = population + choose_parents_and_recombination(population, fitness_scores, population_number)
        fitness_scores = calculate_fitness_scores(population, game_instance)
        population = funcs.choose_best_chromosome(population, fitness_scores, population_number)
        fitness_scores = calculate_fitness_scores(population, game_instance)
        avg_x.append(j)
        avg_y.append(sum(fitness_scores) / len(fitness_scores))
        best_x.append(j)
        best_y.append(max(fitness_scores))
        worst_x.append(j)
        worst_y.append(min(fitness_scores))
    fig1, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
    ax1.plot(avg_x, avg_y)
    ax2.plot(best_x, best_y)
    ax3.plot(worst_x, worst_y)
    ax1.set_title('average fitness graph of level-' + str(cnt + 1))
    ax1.set_xlabel('Generation')
    ax1.set_ylabel('Fitness Average')
    ax2.set_title('best fitness graph of level-' + str(cnt + 1))
    ax2.set_xlabel('Generation')
    ax2.set_ylabel('Best Fitness')
    ax3.set_title('worst fitness graph of level-' + str(cnt + 1))
    ax3.set_xlabel('Generation')
    ax3.set_ylabel('Worst Fitness')
    funcs.check_results(population, fitness_scores, game_instance, cnt)
    plt.show()
