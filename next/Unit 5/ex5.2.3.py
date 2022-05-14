import itertools


def find_100_sum():
    """
    The function finds all the possible combinations that add up to a 100
    :return: a set of tuples, where each tuple is a different possible combination
    :rtype: set
    """
    possible_combs = 0
    money = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    for i in range(5, len(money) + 1):
        combs_set = set(itertools.combinations(money, i))
        for comb in combs_set:
            if sum(comb) == 100:
                print(comb)
                possible_combs += 1
    return possible_combs


def main():
    possible_combinations = find_100_sum()
    print(possible_combinations)


if __name__ == "__main__":
    main()
