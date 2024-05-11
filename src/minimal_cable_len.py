def find_root(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find_root(parent, parent[vertex])


def merge_sets(parent, rank, vertex_1, vertex_2):
    root_1 = find_root(parent, vertex_1)
    root_2 = find_root(parent, vertex_2)
    if rank[root_1] < rank[root_2]:
        parent[root_1] = root_2
    elif rank[root_1] > rank[root_2]:
        parent[root_2] = root_1
    else:
        parent[root_2] = root_1
        rank[root_1] += 1


def find_mst_length(matrix):
    number_of_vertex = len(matrix)
    edges = []
    for v1, v2 in ((v1, v2) for v1 in range(number_of_vertex) for v2 in range(number_of_vertex)):
        if matrix[v1][v2] != 0:
            edges.append((matrix[v1][v2], v1, v2))
    edges.sort()
    parent = [v1 for v1 in range(number_of_vertex)]
    rank = [0] * number_of_vertex
    mst_len = 0
    for edge in edges:
        cost, vertex_1, vertex_2 = edge
        root_vertex_1 = find_root(parent, vertex_1)
        root_vertex_2 = find_root(parent, vertex_2)
        if root_vertex_1 != root_vertex_2:
            merge_sets(parent, rank, root_vertex_1, root_vertex_2)
            mst_len += cost
    return mst_len


def read_input(input_filename):
    adjacency_matrix = []
    file = open(input_filename, "r")
    for line in file:
        row = [int(val) for val in line.strip().split(",")]
        adjacency_matrix.append(row)
    file.close()
    return adjacency_matrix


def create_output(output_filename, content):
    file = open(output_filename, "w")
    file.write(str(content))
    file.close()


adjacency_matrix = read_input("islands.csv")
mst_weight = find_mst_length(adjacency_matrix)
output_filename = "islands.out"
create_output(output_filename, mst_weight)
