def suma(my_arr, res):
    my_arr.sort()
    n = len(my_arr)

    if n < 3 or n > 1000:
        raise ValueError(f'Розмір масиву має бути в межах від 3 до 1000.')

    for num in my_arr:
        if num < 1 or num > 10 ** 9:
            raise ValueError(f'Елементи масиву мають бути в межах від 1 до 10^9.')

    if res < 1 or res > 3 * 10 ** 9:
        raise ValueError(f'Число P має бути в межах від 1 до 3*10^9.')

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = my_arr[i] + my_arr[left] + my_arr[right]
            if current_sum == res:
                return True
            elif current_sum < res:
                left_index, right_index = left + 1, right
                while left_index <= right_index:
                    mid = left_index + (right_index - left_index) // 2
                    if my_arr[mid] == res - my_arr[i] - my_arr[left]:
                        return True
                    elif my_arr[mid] < res - my_arr[i] - my_arr[left]:
                        left_index = mid + 1
                    else:
                        right_index = mid - 1
                left += 1
            else:
                right -= 1
    return False


my_arr = [1, 2, 3, 6]
res = 6
print(suma(my_arr, res))
