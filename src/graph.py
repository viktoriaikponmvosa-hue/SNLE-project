from heap import MinHeap

class Graph:
    def __init__(self):
        self.adj = {}
        self.packages = []
        self.dp_cache = {}

    # -----------------------
    # Add edge (DIRECTED)
    # -----------------------
    def add_edge(self, u, v, distance, time, risk):
        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append((v, distance, time, risk))

    # -----------------------
    # Load network file 
    # -----------------------
    def load_network(self, filename):
        mode = None

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if line == "NODES":
                    mode = "nodes"
                    continue
                elif line == "EDGES":
                    mode = "edges"
                    continue
                elif line == "PACKAGES":
                    mode = "packages"
                    continue

                parts = line.split()

                if mode == "nodes":
                    for node in parts:
                        if node not in self.adj:
                            self.adj[node] = []

                elif mode == "edges":
                    if len(parts) < 5:
                        continue

                    u = parts[0]
                    v = parts[1]
                    d = int(parts[2])
                    t = int(parts[3])
                    r = int(parts[4])

                    self.add_edge(u, v, d, t, r)

                elif mode == "packages":
                    if len(parts) < 4:
                        continue

                    pkg_id = parts[0]
                    priority = int(parts[1])
                    dest = parts[2]
                    weight = float(parts[3])

                    self.packages.append((priority, pkg_id, dest, weight))

    # -----------------------
    # Network Summary
    # -----------------------
    def summary(self):
        nodes = len(self.adj)
        edges = sum(len(v) for v in self.adj.values())

        print("\n=== Network Summary ===")
        print(f"Total Nodes: {nodes}")
        print(f"Total Edges: {edges}")

    # -----------------------
    # Get neighbors
    # -----------------------
    def get_neighbors(self, node):
        return self.adj.get(node, [])

    # -----------------------
    # Select weight
    # -----------------------
    def get_weight(self, distance, time, risk, mode):
        if mode == "distance":
            return distance
        elif mode == "time":
            return time
        else:
            return risk

    # -----------------------
    # Dijkstra algorithm
    # -----------------------
    def dijkstra(self, start, mode):
        distances = {}
        previous = {}

        heap = MinHeap()

        for node in self.adj:
            distances[node] = float('inf')
            previous[node] = None

        distances[start] = 0
        heap.push((0, start))

        while not heap.is_empty():
            current_dist, current_node = heap.pop()

            for neighbor, d, t, r in self.get_neighbors(current_node):
                weight = self.get_weight(d, t, r, mode)
                new_distance = current_dist + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node
                    heap.push((new_distance, neighbor))

        return distances, previous

    # -----------------------
    # DP: All-pairs shortest paths 
    # -----------------------
    def all_pairs_shortest_paths(self, mode):
        if mode in self.dp_cache:
            return self.dp_cache[mode]

        print("\nBuilding DP cache...")

        dp = {}

        for node in self.adj:
            distances, previous = self.dijkstra(node, mode)
            dp[node] = (distances, previous)

        self.dp_cache[mode] = dp
        return dp

    # -----------------------
    # Build path
    # -----------------------
    def build_path(self, previous, end):
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path

    # -----------------------
    # Shortest path 
    # -----------------------
    def shortest_path(self, start, end, mode):
        dp = self.all_pairs_shortest_paths(mode)

        distances, previous = dp[start]
        path = self.build_path(previous, end)

        return path, distances[end]

    # -----------------------
    # Cycle detection (DFS)
    # -----------------------
    def detect_cycle(self):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {node: WHITE for node in self.adj}

        def dfs(node):
            if color[node] == GRAY:
                return True
            if color[node] == BLACK:
                return False

            color[node] = GRAY

            for neighbor, _, _, _ in self.adj[node]:
                if dfs(neighbor):
                    return True

            color[node] = BLACK
            return False

        for node in self.adj:
            if color[node] == WHITE:
                if dfs(node):
                    return True

        return False

    # -----------------------
    # ASCII Visualization 
    # -----------------------
    def visualize_ascii(self):
        print("\n" + "=" * 45)
        print("        SMART NETWORK VISUALIZATION")
        print("=" * 45)

        for node in self.adj:
            print(f"\n[{node}]")

            if not self.adj[node]:
                print("   └── (no outgoing edges)")
                continue

            for i, (neighbor, d, t, r) in enumerate(self.adj[node]):
                connector = "├──>" if i < len(self.adj[node]) - 1 else "└──>"

                print(f"   {connector} {neighbor}")
                print(f"   │     distance: {d}")
                print(f"   │     time:     {t}")
                print(f"   │     risk:     {r}")

        print("\n" + "=" * 45)