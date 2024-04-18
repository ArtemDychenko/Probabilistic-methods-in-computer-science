
import random

def generate_uniform_number(a=50, b=150):
    u = random.random()  # Losuje liczbę z rozkładu jednostajnego [0, 1]
    return 100 * u + 50  # Transformacja odwrotna do dystrybuanty


def generate_number_with_probabilities():
    u = random.random()  # Losuje liczbę z rozkładu jednostajnego [0, 1]
    if u < 0.20:
        return 1
    elif u < 0.50:
        return 2
    elif u < 0.90:
        return 3
    else:
        return 4



if __name__ == '__main__':
    generated_numbers = [generate_uniform_number() for _ in range(10)]
    print(generated_numbers)

    # Generowanie 10 liczb z określonymi prawdopodobieństwami
    generated_numbers = [generate_number_with_probabilities() for _ in range(10)]
    print(generated_numbers)