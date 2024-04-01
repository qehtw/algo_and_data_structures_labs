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


def flood_fill(screen, m, n, x, y, prev_color, new_color):
    queue = [[x, y]]
    screen[x][y] = new_color

    while queue:
        curr_pixel = queue.pop(0)
        pos_x = curr_pixel[0]
        pos_y = curr_pixel[1]

        if is_valid(screen, m, n, pos_x + 1, pos_y, prev_color, new_color):
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


def read_input(input_filename):
    file = open(input_filename, "r")
    m, n = map(int, file.readline().split(","))
    x, y = map(int, file.readline().split(","))
    new_color = file.readline().strip().replace("'", "")
    screen = [
        list(line.strip().replace("'", "").replace("[", "").replace("]", "").split(","))
        for line in file.readlines()
    ]
    file.close()
    return m, n, x, y, new_color, screen


def create_output(output_filename, filled_screen):
    file = open(output_filename, "w")
    for row in filled_screen:
        file.write("['{}']".format("', '".join(row)))
        file.write("\n")
    file.close()


input_filename = "input.txt"
output_filename = "output.txt"


m, n, x, y, new_color, screen = read_input(input_filename)
prev_color = screen[x][y]
filled_screen = flood_fill(screen, m, n, x, y, prev_color, new_color)
create_output(output_filename, filled_screen)
