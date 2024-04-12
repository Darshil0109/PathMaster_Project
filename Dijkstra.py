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
    def main(self):
        # adjacency_list = {
        #     'S': {'T': 10, 'Y': 5},
        #     'T': {'Y': 2, 'X': 1},
        #     'X': {'Z': 4},
        #     'Y': {'T': 3, 'X': 9, 'Z': 2},
        #     'Z': {'S': 7, 'X': 6},
        # }
        adjacency_list = {
            '1': {'2': 10, '6': 30},
            '2': {'3': 20},
            '3': {'4': 15, '5': 5},
            '4': {'5': 12, '7': 20, '1': 25},
            '5': {'7': 7},
            '6': {'7': 35},
            '7': {},
        }

        g = DijkstraAlgo(adjacency_list)
        g.dijkstra('1')
# obj=DijkstraSolver()
# obj.main()