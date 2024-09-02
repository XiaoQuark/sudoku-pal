# import itertools library
import itertools

    # receive 2 integers: sum to obtain and length of combinations (optional)
def find_combinations(target_sum, length = None):
    # define list of integers that can be used: 1-9 only
    digits = range(1, 10)

    # condition for combination length
    if length:
        # return all combinations in the list of digits for a given length
        combinations = itertools.combinations(digits, length)
    else:
        # find all combinations in a range of lengths from 1 to 9
        combinations = (comb for range in range(1, 10) for comb in itertools.combinations(digits, range))

    # filter combinations by target sum
    results = [comb for comb in combinations if sum(comb) == target_sum]

    print(results, "results")

    


find_combinations(15, 4)
find_combinations(15)
