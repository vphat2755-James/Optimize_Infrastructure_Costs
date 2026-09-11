import time
from graph import Graph, load_graph_from_json, generate_random_graph
from dijkstra import shortest_path
 
 
def bellman_ford(graph: Graph, source: str, target: str):
    vertices = graph.vertices()
 
    edges = []
    for u in vertices:
        for v, w in graph.neighbors(u):
            edges.append((u, v, w))
 
    dist = {v: float("inf") for v in vertices}
    dist[source] = 0
    prev = {}
 
    for _ in range(max(len(vertices) - 1, 0)):
        updated = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break
 
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            raise ValueError("Do thi co chu trinh am")
 
    if dist.get(target, float("inf")) == float("inf"):
        return None, float("inf")
 
    path = [target]
    cur = target
    while cur != source:
        cur = prev[cur]
        path.append(cur)
    path.reverse()
 
    return path, dist[target]
 
 
def compare_algorithms(graph: Graph, source: str, target: str, verbose: bool = True):
    t0 = time.perf_counter()
    path_dij, cost_dij = shortest_path(graph, source, target)
    time_dij = time.perf_counter() - t0
 
    t0 = time.perf_counter()
    path_bf, cost_bf = bellman_ford(graph, source, target)
    time_bf = time.perf_counter() - t0
 
    match = (cost_dij == cost_bf)
 
    result = {
        "dijkstra": {"path": path_dij, "cost": cost_dij, "time_sec": time_dij},
        "bellman_ford": {"path": path_bf, "cost": cost_bf, "time_sec": time_bf},
        "match": match,
    }
 
    if verbose:
        print(f"\nTu {source} den {target}:")
        print("-" * 60)
        print(f"{'Thuat toan':<15}{'Chi phi':<12}{'Thoi gian (s)':<18}{'Duong di'}")
        print("-" * 60)
        print(f"{'Dijkstra':<15}{str(cost_dij):<12}{time_dij:<18.8f}{path_dij}")
        print(f"{'Bellman-Ford':<15}{str(cost_bf):<12}{time_bf:<18.8f}{path_bf}")
        print("-" * 60)
        if match:
            print("=> Ket qua KHOP giua 2 thuat toan.")
        else:
            print("=> CANH BAO: Ket qua KHONG khop giua 2 thuat toan!")
 
        if time_bf > 0 and time_dij > 0:
            ratio = time_bf / time_dij
            print(f"=> Bellman-Ford cham hon Dijkstra khoang {ratio:.2f} lan.")
 
    return result
 
 
def benchmark_scaling(sizes=(10, 30, 60, 100), edge_factor: int = 3, verbose: bool = True):
    results = []
    if verbose:
        print("\n=== BENCHMARK: Dijkstra vs Bellman-Ford ===")
        print(f"{'So dinh':<12}{'Thoi gian Dijkstra (s)':<26}{'Thoi gian Bellman-Ford (s)':<28}")
 
    for n in sizes:
        g = generate_random_graph(num_vertices=n, num_edges=n * edge_factor, seed=42)
        verts = g.vertices()
        if not verts:
            continue
        source = verts[0]
        target = verts[-1]
 
        t0 = time.perf_counter()
        shortest_path(g, source, target)
        time_dij = time.perf_counter() - t0
 
        t0 = time.perf_counter()
        bellman_ford(g, source, target)
        time_bf = time.perf_counter() - t0
 
        results.append({
            "num_vertices": n,
            "time_dijkstra": time_dij,
            "time_bellman_ford": time_bf,
        })
 
        if verbose:
            print(f"{n:<12}{time_dij:<26.8f}{time_bf:<28.8f}")
 
    return results
 
 
if __name__ == "__main__":
    g = load_graph_from_json("data.json")
    compare_algorithms(g, "Kho_Tong", "G")
 
    g.add_vertex("Z_co_lap")
    print("\n=== TEST: khong co duong di (Bellman-Ford) ===")
    print(bellman_ford(g, "Kho_Tong", "Z_co_lap"))
 
    try:
        benchmark_scaling()
    except NotImplementedError:
        print("\n(Bo qua benchmark_scaling: generate_random_graph() chua duoc implement)")