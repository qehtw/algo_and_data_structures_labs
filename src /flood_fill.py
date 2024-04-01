def is_valid(screen, m, n, x, y, prev_color, new_color):
    if (
            x < 0
            or x >= m
            or y < 0
            or y >= n
            or screen[x][y] != prev_color
            or screen[x][y] == new_color
    ):
        return False
    return True


# FloodFill function
def flood_fill(screen, m, n, x, y, prev_color, new_color):
    queue = [[x, y]]
    screen[x][y] = new_color

    # While the queue is not empty i.e. the whole component having prevC color is not colored with newC color
    while queue:
        # Dequeue the front node
        curr_pixel = queue.pop(0)
        pos_x = curr_pixel[0]
        pos_y = curr_pixel[1]

        # Check if the adjacent pixels are valid
        if is_valid(screen, m, n, pos_x + 1, pos_y, prev_color, new_color):
            # Color with newC if valid and enqueue
            screen[pos_x + 1][pos_y] = new_color
            queue.append([pos_x + 1, pos_y])
        if is_valid(screen, m, n, pos_x - 1, pos_y, prev_color, new_color):
            screen[pos_x - 1][pos_y] = new_color
            queue.append([pos_x - 1, pos_y])
        if is_valid(screen, m, n, pos_x, pos_y + 1, prev_color, new_color):
            screen[pos_x][pos_y + 1] = new_color
            queue.append([pos_x, pos_y + 1])
        if is_valid(screen, m, n, pos_x, pos_y - 1, prev_color, new_color):
            screen[pos_x][pos_y - 1] = new_color
            queue.append([pos_x, pos_y - 1])

    return screen


with open("input.txt", "r") as f:
    m, n = map(int, f.readline().split(","))
    x, y = map(int, f.readline().split(","))
    new_color = f.readline().strip().replace("'", "")
    screen = [
        list(line.strip().replace("'", "").replace("[", "").replace("]", "").split(","))
        for line in f.readlines()
    ]

prev_color = screen[x][y]

filled_screen = flood_fill(screen, m, n, x, y, prev_color, new_color)

with open("output.txt", "w") as f:
    for row in filled_screen:
        f.write("['{}']".format("', '".join(row)))
        f.write("\n")
