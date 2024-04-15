from priority_queue import PriorityQueue

INF = float('inf')

def find_shortest_path(graph, start_p, clients):
    dist = {node: INF for node in graph}
    dist[start_p] = 0
    visited_nodes = set()
    pq = PriorityQueue()
    pq.enqueue(start_p, 0)

    while not pq.is_empty():
        vertex, current_dist = pq.dequeue()
        if vertex is None:
            break
        if vertex in visited_nodes:
            continue
        visited_nodes.add(vertex)

        neighbors = graph.get(vertex, [])
        for next_v, latency in neighbors:
            if current_dist is None:
                new_dist = latency
            else:
                new_dist = current_dist + latency
            if new_dist < dist[next_v]:
                dist[next_v] = new_dist
                pq.enqueue(next_v, new_dist)

    return dist


def find_min_max_latency(M, N, clients, connections):
    if N and M and clients:
        routers = set(range(1, N+1)) - clients
        graph = {node: [] for node in range(1, N+1)}
        for startnode, endnode, latency in connections:
            graph[startnode].append((endnode, latency))
            graph[endnode].append((startnode, latency))
        min_max_latency = INF
        for router in routers:
            distances = find_shortest_path(graph, router, clients)
            max_latency = max(distances[client] for client in clients)
            min_max_latency = min(min_max_latency, max_latency)
        return min_max_latency


def read_input(input_filename):
    file = open(input_filename, "r")
    N, M = map(int, file.readline().split(" "))
    clients = set(map(int, file.readline().split(" ")))
    connections = []
    for _ in range(M):
        startnode, endnode, latency = map(int, file.readline().split())
        connections.append((startnode, endnode, latency))
    file.close()
    return N, M, clients, connections

def create_output(latency, output_filename):
    file = open(output_filename, "w")
    if latency == INF:
        file.write(str(-1))
    else:
        file.write(str(latency))
    file.close()

input_filename = "gamsrv.in"
output_filename = "gamsrv.out"

N, M, clients, connections = read_input(input_filename)
latency = find_min_max_latency(M, N, clients, connections)
create_output(latency, output_filename)
