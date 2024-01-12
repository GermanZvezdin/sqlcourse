# tâche 9
def solution_9():
    original_list = [(1, 3, 4), (2, 1), (6,), (2, 2, 2, 1)]

    modified_list = [tuple(t[:-1]) if len(t) % 2 == 0 else t for t in original_list]

    print(modified_list)
# tâche 10
def solution_10():
    int_list = [2, 4, 1, 3]
    str_list = ['a', 'b', 'c', 'd']

    result_dict = {key: value * key for key, value in zip(int_list, str_list)}

    print(result_dict)

if __name__ == '__main__':
    solution_10()