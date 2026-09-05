import heapq
from graph import Graph, load_graph_from_json


def shortest_path(graph: Graph, source: str, target: str):
    """
    TODO (TV3):
    Input:
        graph  : doi tuong Graph (tu graph.py)
        source : dinh xuat phat
        target : dinh dich
    Output:
        (path, total_cost)
        - path: list cac dinh tu source -> target, vi du ["Kho_Tong", "B", "A"]
        - total_cost: tong trong so cua duong di do (float)
        - Neu KHONG co duong di: return (None, float('inf'))

    Goi y thuat toan:
        dist = {v: float('inf') for v in graph.vertices()}
        dist[source] = 0
        prev = {}  # de truy vet lai duong di
        pq = [(0, source)]  # (khoang_cach, dinh)

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

        # Truy vet duong di tu prev, dao nguoc lai
        # Neu dist[target] == inf -> khong co duong di
    """
    pass


def shortest_path_all(graph: Graph, source: str):
    """
    TODO (TV3 - tuy chon nhung nen lam):
    Dijkstra tu 1 nguon den TAT CA cac dinh con lai (single-source).
    Output: dict {dinh: (path, cost)} cho tat ca cac dinh co the den duoc.
    Ham nay giup Thanh vien 5 khong phai goi shortest_path() nhieu lan
    rieng le (toi uu hon).
    """
    pass


if __name__ == "__main__":
    g = load_graph_from_json("data.json")
    path, cost = shortest_path(g, "Kho_Tong", "G")
    print("Duong di ngan nhat:", path)
    print("Tong chi phi:", cost)

    # Test truong hop khong co duong di (tu tao 1 dinh co lap de thu)
    # g.add_vertex("Z")
    # print(shortest_path(g, "Kho_Tong", "Z"))  # ky vong (None, inf)