def build_automaton(needle_value: str) -> list:
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
    transition_table = build_automaton(needle_value)
    current_state = 0
    indices = []
    haystack_length = len(haystack_value)

    i = 0
    while i < haystack_length:
        char = haystack_value[i]
        if char in transition_table[current_state]:
            current_state = transition_table[current_state][char]
        else:
            current_state = 0
        if current_state == len(needle_value):
            indices.append(i - len(needle_value) + 1)
            current_state = transition_table[current_state - 1].get(needle_value[-1], 0)
        i += 1

    indices = [index for index in indices if index >= 0]
    return indices

if __name__ == "__main__":
    haystack_value = str(input("Введіть <<haystack>>: "))
    needle_value = str(input("Введіть <<needle>>: "))

    result = search(needle_value, haystack_value)
    if result:
        print(f"Індекси входжень підстрічки '{needle_value}' в стрічці '{haystack_value}': {result}")
    else:
        print(f"Підстрічка '{needle_value}' не знайдена в стрічці '{haystack_value}'")
