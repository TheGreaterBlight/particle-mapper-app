import heapq
#aQui guardo mis algoritmos para mis grafos
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Rango
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False
class Graph:
    def __init__(self, particulas):
        self.particulas = particulas
        self.num_particles = len(particulas)
    
    def calculate_distance(self, p1, p2):
        return ((p1.origen_x - p2.origen_x) ** 2 + (p1.origen_y - p2.origen_y) ** 2) ** 0.5

    def prims_algorithm(self):
        # Arbitrario
        arista_del_mst = [] 
        visited = [False] * self.num_particles
        min_heap = [(0, 0, -1)] 
        while min_heap:
            weight, to, frm = heapq.heappop(min_heap)
            if visited[to]:
                continue
            visited[to] = True

            if frm != -1:
                arista_del_mst.append((frm, to, weight))
            for next_particle in range(self.num_particles):
                if not visited[next_particle]:
                    distance = self.calculate_distance(self.particulas[to], self.particulas[next_particle])
                    heapq.heappush(min_heap, (distance, next_particle, to))
        return arista_del_mst