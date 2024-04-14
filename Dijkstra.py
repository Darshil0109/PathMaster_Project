class DijkstraAlgo:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, start):
        # Initialize distances dictionary with infinite distance for all nodes
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0    # distance from start to itself is 0

        visited = []  # Array to keep track of visited vertices
        self.print_header(distances, start)

        while len(visited) < len(self.graph):
            # Find the vertex with the smallest distance
            min_vertex = self.get_min_distance_vertex(distances, visited)

            visited.append(min_vertex)   # Mark the vertex as visited
            self.print_iteration(distances, visited)

            # Update distances to its neighbors
            for neighbor, weight in self.graph[min_vertex].items():
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        print(f'\n{"-" * (8 * len(distances) + 1)}')
        return distances

    @staticmethod
    def get_min_distance_vertex(distances, visited):
        min_distance = float('inf')
        min_vertex = None
        for vertex, dist in distances.items():
            if vertex not in visited and dist < min_distance:
                min_distance = dist
                min_vertex = vertex
        return min_vertex

    @staticmethod
    def print_header(distances, start):
        n = len(distances)
        print("Shortest distances from", start, "to all vertices using Dijkstra Algorithm:")
        print(f'{"-" * (8 * n + 1)}')
        print(end='|   ')
        for node in distances.keys():
            print(f'{node}', end='   |   ')
        print(f'\n{"-" * (8 * n + 1)}', end='')

    @staticmethod
    def print_iteration(distances, visited):
        print(end='\n|')
        for dist in distances.values():
            print(f'{dist:4.0f}', end='   |')
        print(end='\t')
        print(*visited, sep=', ', end='')

class DijkstraSolver:
    def user_input(self):
        graph = {}

        # Prompt for the number of nodes
        num_nodes = int(input("Enter the number of nodes in the graph: "))

        # Prompt for each node's adjacency list
        for i in range(num_nodes):
            node = input(f"\n\n\nEnter the name of node {i + 1}: ").upper()
            num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))
            neighbors = {}
            for j in range(num_neighbors):
                neighbor = input(f"Enter name of neighbor {j + 1} of node {node}: ").upper()
                weight = float(input(f"Enter weight for edge {node}-{neighbor}: "))
                neighbors[neighbor] = weight
            graph[node] = neighbors

        # Prompt for the starting node
        start_node = input("\n\n\nEnter the starting node/source node for Dijkstra's algorithm: ")

        return graph, start_node

    def main(self):
        print("[1]. Use Default Input ")
        print("[2]. Enter Input by Self")
        choice=int(input("Enter Choice: "))
        if choice==1:
            adjacency_list = {
               'S': {'U': 10, 'Y': 5},
               'U': {'Y': 2, 'V': 1},
               'V': {'Z': 4},
               'Y': {'U': 3, 'V': 9, 'Z': 2},
               'Z': {'S': 7, 'V': 6},
            }
            start_node="U"
        elif choice==2:
            # For  taking Input From the user 
            # Get user input for graph and starting node
            adjacency_list, start_node = self.user_input()
        


        # Create an instance of DijkstraAlgo with the adjacency list
        dijkstra_algo = DijkstraAlgo(adjacency_list)

        # Run Dijkstra's algorithm
        dijkstra_algo.dijkstra(start_node)

