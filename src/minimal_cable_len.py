def find_root_of_set(parent, i):
    if parent[i] == i:
        return i
    return find_root_of_set(parent, parent[i])


def merge_sets(parent, rank, vertex_1, vertex_2):
    root_vertex_1 = find_root_of_set(parent, vertex_1)
    root_vertex_2 = find_root_of_set(parent, vertex_2)
    if rank[root_vertex_1] < rank[root_vertex_2]:
        parent[root_vertex_1] = root_vertex_2
    elif rank[root_vertex_1] > rank[root_vertex_2]:
        parent[root_vertex_2] = root_vertex_1
    else:
        parent[root_vertex_2] = root_vertex_1
        rank[root_vertex_1] += 1


def kruskal(matrix):
    num_vertices = len(matrix)
    edges = []
    for i, j in ((i, j) for i in range(num_vertices) for j in range(num_vertices)):
        if matrix[i][j] != 0:
            edges.append((matrix[i][j], i, j))
    edges.sort()
    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices
    mst_len = 0
    for edge in edges:
        cost, vertex_1, vertex_2 = edge
        root_vertex_1 = find_root_of_set(parent, vertex_1)
        root_vertex_2 = find_root_of_set(parent, vertex_2)
        if root_vertex_1 != root_vertex_2:
            merge_sets(parent, rank, root_vertex_1, root_vertex_2)
            mst_len += cost
    return mst_len


def read_input(input_filename):
    adjacency_matrix = []
    with open(input_filename, "r") as file:
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
mst_weight = kruskal(adjacency_matrix)
output_filename = "islands.out"
create_output(output_filename, mst_weight)
