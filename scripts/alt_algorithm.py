import time
from graph import Graph, load_graph_from_json, generate_random_graph
from dijkstra import shortest_path


def bellman_ford(graph: Graph, source: str, target: str):
    """
    Thuat toan Bellman-Ford tim duong di ngan nhat tu source -> target.

    Input:
        graph  : doi tuong Graph (tu graph.py)
        source : dinh xuat phat
        target : dinh dich
    Output:
        (path, total_cost)
        - path: list cac dinh tu source -> target
        - total_cost: tong trong so (float)
        - Neu KHONG co duong di: return (None, float('inf'))

    Ghi chu: khac Dijkstra (tham lam, dung priority queue), Bellman-Ford
    "relax" TAT CA cac canh, lap (so_dinh - 1) lan. Cham hon Dijkstra
    (O(V*E) so voi O(E log V)) nhung xu ly duoc canh am (Dijkstra thi khong).
    """
    vertices = graph.vertices()

    # Xay danh sach canh (u, v, w) tu adjacency list
    edges = []
    for u in vertices:
        for v, w in graph.neighbors(u):
            edges.append((u, v, w))

    dist = {v: float("inf") for v in vertices}
    dist[source] = 0
    prev = {}

    # Relax tat ca canh, lap (V-1) lan
    for _ in range(max(len(vertices) - 1, 0)):
        updated = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break  # da hoi tu, khong can lap them

    # Kiem tra chu trinh am (lap them 1 lan, neu con giam duoc nghia la co)
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            raise ValueError("Do thi co chu trinh am — Bellman-Ford khong ap dung duoc.")

    if dist.get(target, float("inf")) == float("inf"):
        return None, float("inf")

    # Truy vet lai duong di tu prev
    path = [target]
    cur = target
    while cur != source:
        cur = prev[cur]
        path.append(cur)
    path.reverse()

    return path, dist[target]


def compare_algorithms(graph: Graph, source: str, target: str, verbose: bool = True):
    """
    Chay Dijkstra va Bellman-Ford tren cung 1 graph/source/target,
    do thoi gian chay va doi chieu ket qua.

    Output: dict chua ket qua + thoi gian cua ca 2 thuat toan, vi du:
        {
          "dijkstra":      {"path": [...], "cost": 13, "time_sec": 0.0001},
          "bellman_ford":  {"path": [...], "cost": 13, "time_sec": 0.0003},
          "match": True
        }
    """
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
            print(f"=> Bellman-Ford cham hon Dijkstra khoang {ratio:.2f} lan (tren do thi nay).")

    return result


def benchmark_scaling(sizes=(10, 30, 60, 100), edge_factor: int = 3, verbose: bool = True):
    """
    Do hieu nang Dijkstra vs Bellman-Ford tren cac do thi ngau nhien
    co kich thuoc tang dan, de minh hoa ro do phuc tap:
        Dijkstra:     O(E log V)
        Bellman-Ford: O(V * E)

    Input:
        sizes       : danh sach so luong dinh muon test, vi du (10, 30, 60, 100)
        edge_factor : so canh sinh ra ~ edge_factor * so_dinh
    Output:
        list[dict], moi phan tu la ket qua benchmark cho 1 kich thuoc do thi:
        {"num_vertices": ..., "time_dijkstra": ..., "time_bellman_ford": ...}
    """
    results = []
    if verbose:
        print("\n=== BENCHMARK: Dijkstra vs Bellman-Ford theo kich thuoc do thi ===")
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

    # Test truong hop khong co duong di
    g.add_vertex("Z_co_lap")
    print("\n=== TEST: khong co duong di (Bellman-Ford) ===")
    print(bellman_ford(g, "Kho_Tong", "Z_co_lap"))  # ky vong (None, inf)

    # Benchmark tren cac do thi ngau nhien lon dan (can graph.py da implement
    # ham generate_random_graph)
    try:
        benchmark_scaling()
    except NotImplementedError:
        print("\n(Bo qua benchmark_scaling: generate_random_graph() chua duoc implement trong graph.py)")
