def build_automaton(needle_value: str) -> list:
    automaton = [{} for _ in range(len(needle_value) + 1)]
    m = len(needle_value)

    for i in range(m):
        for char in automaton[i]:
            if char == needle_value[i]:
                automaton[i][char] = i + 1
            else:
                j = i
                while j > 0:
                    j = automaton[j - 1].get(char, 0)
                    if char == needle_value[j]:
                        automaton[i][char] = j + 1
                        break
                if j == 0:
                    automaton[i][char] = 0

    return automaton


def search(needle_value: str, haystack_value: str) -> list:
    automaton = build_automaton(needle_value)
    m, n = len(needle_value), len(haystack_value)

    j = 0
    indices = []

    for i in range(n):
        while j > 0 and haystack_value[i] != needle_value[j]:
            j = automaton[j - 1].get(haystack_value[i], 0)

        if haystack_value[i] == needle_value[j]:
            j += 1

        if j == m:
            indices.append(i - m + 1)
            j = automaton[j - 1].get(haystack_value[i], 0)

    return indices
    
