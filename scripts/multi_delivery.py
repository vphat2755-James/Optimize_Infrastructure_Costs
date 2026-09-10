from graph import Graph, load_graph_from_json
from dijkstra import shortest_path


def nearest_neighbor_order(graph: Graph, source: str, destinations: list):
    remaining = destinations.copy()
    current = source

    order = []
    while remaining:
        best_point = None          
        best_cost = float("inf")   
        for candidate in remaining:
            _, cost = shortest_path(graph, current, candidate)
            if cost < best_cost:
                best_cost = cost
                best_point = candidate
        if best_point is None:
            print(
                f"[Canh bao] Khong the tim duong di den cac diem con lai "
                f"{remaining} tu '{current}'. Dung heuristic tai day."
            )
            break
        order.append(best_point)          
        remaining.remove(best_point)      
        current = best_point              
    return order


def build_full_route(graph: Graph, source: str, destinations: list):
    order = nearest_neighbor_order(graph, source, destinations)

    current = source        
    full_route = []         
    total_cost = 0          

    for next_point in order:
        path, cost = shortest_path(graph, current, next_point)
        full_route.append((current, next_point, path, cost))
        total_cost += cost
        current = next_point

    return full_route, total_cost


def print_route_report(full_route, total_cost):
    for i, (start, end, path, cost) in enumerate(full_route, start=1):
        path_str = " -> ".join(path) if path else "Khong co duong di"
        print(f"Chang {i}: {start} -> {end} | Duong di: {path_str} | Chi phi: {cost}")

    print("-" * 43)
    print(f"TONG QUANG DUONG CA HANH TRINH: {total_cost}")


if __name__ == "__main__":
    g = load_graph_from_json("data.json")
    diem_giao = ["C", "F", "L"]
    full_route, total_cost = build_full_route(g, "A", diem_giao)
    print_route_report(full_route, total_cost)
