def build_atomaton(needle_value: str) -> list:
    table = [{} for _ in range(len(needle_value) + 1)]
    for i in range(len(needle_value)):
        char = needle_value[i]
        for state in range(i + 1):
            if char not in table[state]:
                table[state][char] = i + 1
            else:
                table[state][char] = max(table[state][char], i + 1)
    return table


def search(needle_value: str, haystack_value: str) -> list:
    transition_table = build_atomaton(needle_value)
    current_state = 0
    indices = []

    for i, char in enumerate(haystack_value):
        if char in transition_table[current_state]:
            current_state = transition_table[current_state][char]
        else:
            current_state = 0
        if current_state == len(needle_value):
            indices.append(i - len(needle_value) + 1)  
            current_state = transition_table[current_state - 1].get(needle_value[-1], 0)  

    indices = [index for index in indices if index >= 0]
    return indices
