import heapq
import os
from typing import Dict, List, Optional, Tuple
from graph import Graph, load_graph_from_json


def shortest_path(
    graph: Graph, source: str, target: str
) -> Tuple[Optional[List[str]], float]:
    """
    Tìm đường đi ngắn nhất từ source -> target bằng Dijkstra (heapq).
    Output:
        (path, total_cost)
        - path: list các đỉnh [source, ..., target]
        - total_cost: tổng trọng số (float)
        - Nếu không có đường đi: trả về (None, float('inf'))
    """
    all_v = graph.vertices()
    if source not in all_v or target not in all_v:
        return (None, float("inf"))

    dist: Dict[str, float] = {v: float("inf") for v in all_v}
    dist[source] = 0.0
    prev: Dict[str, Optional[str]] = {}
    pq: List[Tuple[float, str]] = [(0.0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if u == target:
            break

        if d > dist[u]:
            continue

        for v, w in graph.neighbors(u):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    if dist[target] == float("inf"):
        return (None, float("inf"))

    # Truy vết đường đi từ target về source
    path: List[str] = []
    curr: Optional[str] = target
    while curr is not None:
        path.append(curr)
        curr = prev.get(curr)

    path.reverse()
    return (path, dist[target])


def shortest_path_all(
    graph: Graph, source: str
) -> Dict[str, Tuple[List[str], float]]:
    """
    Dijkstra từ 1 nguồn đến tất cả các đỉnh còn lại (hỗ trợ Thành viên 5).
    Output: dict {dinh: (path, cost)}
    """
    all_v = graph.vertices()
    if source not in all_v:
        return {}

    dist: Dict[str, float] = {v: float("inf") for v in all_v}
    dist[source] = 0.0
    prev: Dict[str, Optional[str]] = {}
    pq: List[Tuple[float, str]] = [(0.0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph.neighbors(u):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    result: Dict[str, Tuple[List[str], float]] = {}
    for node in all_v:
        if dist[node] == float("inf"):
            continue

        path: List[str] = []
        curr: Optional[str] = node
        while curr is not None:
            path.append(curr)
            curr = prev.get(curr)
        path.reverse()
        result[node] = (path, dist[node])

    return result


if __name__ == "__main__":
    # Tự động tìm đường dẫn chính xác tới data.json
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(curr_dir, "data.json")
    if not os.path.exists(data_path):
        data_path = os.path.join(curr_dir, "..", "data.json")

    g = load_graph_from_json(data_path)

    # Lấy đỉnh bắt đầu và đỉnh đích theo file data.json mẫu (A -> L)
    src = "A"
    dst = "L"

    path, cost = shortest_path(g, src, dst)
    print("Duong di ngan nhat:", path)
    print("Tong chi phi:", cost)

    # Test trường hợp không tồn tại đường đi (đỉnh Z cô lập)
    g.add_vertex("Z")
    print("Test dinh khong den duoc (Z):", shortest_path(g, src, "Z"))