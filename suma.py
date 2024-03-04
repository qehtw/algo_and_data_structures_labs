def suma(new_arr, goal):
    new_arr.sort()
    n = len(new_arr)

    if n < 3 or n > 1000:
        raise ValueError(f'Розмір масиву має бути в межах від 3 до 1000.')

    for num in new_arr:
        if num < 1 or num > 10 ** 9:
            raise ValueError(f'Елементи масиву мають бути в межах від 1 до 10^9.')

    if goal < 1 or goal > 3 * 10 ** 9:
        raise ValueError(f'Число P має бути в межах від 1 до 3*10^9.')

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = new_arr[i] + new_arr[left] + new_arr[right]
            if current_sum == goal:
                return True
            elif current_sum < goal:
                left += 1
            else:
                right -= 1
    return False


# Приклад використання
new_arr = [1, 2, 3, 6]
goal = 6
print(suma(new_arr, goal))
