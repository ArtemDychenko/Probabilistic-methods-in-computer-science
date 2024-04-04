import random
import math


def generate_permutations(n):
    def backtrack(permutation):
        if len(permutation) == n:
            permutations.append(permutation[:])
        else:
            for i in range(0, n):
                if i not in permutation:
                    permutation.append(i)
                    backtrack(permutation)
                    permutation.pop()

    permutations = []
    backtrack([])
    return permutations


def generate_combinations(m, n):
    perm = generate_permutations(n)
    comb = []
    for p in perm:
        if p[:m] not in comb:
            comb.append(p[:m])

    return comb

def calculate_length(point1, point2):
    d = math.sqrt(((point2["Longitude"] - point1["Longitude"])**2) + ((point2["Latitude"] - point1["Latitude"])**2))
    return d

def calculate_population(cities, comb):
    pop = 0
    for i in comb:
        pop = pop + cities[i]["Population"]
    return pop


def find_the_best_root(cities, N):
    best_root_length = 0
    d = 0
    best_option = 0
    perm = generate_permutations(N)
    for i in perm:
        punkt1 = cities[i[0]]
        d = 0
        for c in i[1:]:
            punkt2 = cities[c]
            d = d + calculate_length(punkt1, punkt2)
            punkt1 = punkt2
        if best_root_length == 0 or best_root_length > d:
            best_root_length = d
            best_option = i

    return best_option, best_root_length


def find_the_best_population_combination(cities, K, N):
    total_population = 0
    cities_comb_n = list(range(0, N))
    total_population = calculate_population(cities, cities_comb_n)
    closest_combination_population = 0
    half_total_population = total_population / 2
    closest_combination = None
    closest_diff = float('inf')


    for combination in generate_combinations(K, N):
        current_population = calculate_population(cities, combination)
        current_diff = abs(half_total_population - current_population)


        if current_diff < closest_diff:
            closest_diff = current_diff
            closest_combination = combination
            closest_combination_population = current_population

    return closest_combination, closest_combination_population

cities_data = []
with open("france.txt", "r") as file:
    next(file)  # Pomijamy pierwszą linię z nagłówkami
    for line in file:
        data = line.split()  # Dzielimy linię na kolumny
        city_id = int(data[0])
        town = data[1]
        population = int(data[2])
        latitude = float(data[3])
        longitude = float(data[4])
        city_info = {'Town': town, 'Population': population, 'Latitude': latitude, 'Longitude': longitude}
        cities_data.append(city_info)


# f=0
# comb = generate_permutations(5)
# for i in comb:
#     f=f+1
#     print(f, " ", i)


# wynik = find_the_best_root(cities_data, 5)
# print(wynik[0])
# print(wynik[1])

wynik = find_the_best_population_combination(cities_data, 4, 10)
print(wynik[0])
print(wynik[1])
