import csv
from collections import Counter


def read_lists(input_path) -> tuple[list, list]:
    list_l = []
    list_r = []
    with open(input_path, 'r') as f:
        reader = csv.reader(f, delimiter=" ")
        for row in reader:
            list_l.append(int(row[0]))
            list_r.append(int(row[-1]))

    return list_l, list_r


def get_diff(list_l: list[int], list_r: list[int]) -> int:
    """Star 1"""
    list_l.sort()
    list_r.sort()

    diff_sum = 0
    for left, right in zip(list_l, list_r):
        diff_sum += abs(left - right)

    return diff_sum


def get_similarity_score(list_l: list[int], list_r: list[int]) -> int:
    """Star 2"""
    l_counter = Counter(list_l)
    r_counter = Counter(list_r)

    similarity_score = 0
    for key, val in l_counter.items():
        similarity_score += key * val * r_counter[key]

    return similarity_score


if __name__ == "__main__":
    ll, lr = read_lists('./inputs/2024-12-01.csv')
    diff = get_diff(ll, lr)
    print(f"differences: {diff}")
    sim_score = get_similarity_score(ll, lr)
    print(f"similarity score: {sim_score}")