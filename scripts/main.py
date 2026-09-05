from graph import load_graph_from_json
from dijkstra import shortest_path
from alt_algorithm import compare_algorithms
from multi_delivery import build_full_route, print_route_report
from visualize import draw_route, draw_multi_route


def demo_1_diem_den():
    print("\n=== DEMO 1: Tim duong di ngan nhat 1 diem den ===")
    g = load_graph_from_json("data.json")
    source, target = "Kho_Tong", "G"

    path, cost = shortest_path(g, source, target)
    print(f"Duong di ngan nhat tu {source} den {target}: {path}")
    print(f"Tong chi phi: {cost}")

    draw_route(g, path, filename="route.png", title=f"{source} -> {target} (chi phi={cost})")
    print("Da xuat anh: route.png")


def demo_2_so_sanh_thuat_toan():
    print("\n=== DEMO 2: So sanh Dijkstra vs Bellman-Ford ===")
    g = load_graph_from_json("data.json")
    compare_algorithms(g, "Kho_Tong", "G")


def demo_3_giao_nhieu_diem():
    print("\n=== DEMO 3: Giao hang nhieu diem (mo rong TSP) ===")
    g = load_graph_from_json("data.json")
    diem_giao = ["C", "F", "G"]

    full_route, total_cost = build_full_route(g, "Kho_Tong", diem_giao)
    print_route_report(full_route, total_cost)

    draw_multi_route(g, full_route, filename="multi_route.png")
    print("Da xuat anh: multi_route.png")


def test_khong_co_duong_di():
    print("\n=== TEST: Truong hop khong ton tai duong di ===")
    g = load_graph_from_json("data.json")
    g.add_vertex("Z_co_lap")  # dinh khong co canh noi toi/lui
    path, cost = shortest_path(g, "Kho_Tong", "Z_co_lap")
    print(f"Ket qua (ky vong None, inf): path={path}, cost={cost}")
    assert path is None and cost == float("inf"), "Loi: chua xu ly dung truong hop khong co duong di!"
    print("=> PASS")


if __name__ == "__main__":
    demo_1_diem_den()
    demo_2_so_sanh_thuat_toan()
    demo_3_giao_nhieu_diem()
    test_khong_co_duong_di()

    print("\n=== HOAN THANH DEMO TICH HOP ===")