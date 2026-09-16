from graph import load_graph_from_json
from dijkstra import shortest_path
from alt_algorithm import compare_algorithms, benchmark_scaling, bellman_ford
from multi_delivery import build_full_route, print_route_report
from visualize import draw_route, draw_multi_route

DATA_FILE = "data.json"
KHO_XUAT_PHAT = "A"
DIEM_DEN_DON = "L"
DIEM_GIAO_NHIEU = ["C", "F", "L"]


def demo_1_diem_den():
    print("\n" + "=" * 60)
    print("DEMO 1: Tim duong di ngan nhat 1 diem den")
    print("=" * 60)
    g = load_graph_from_json(DATA_FILE)

    path, cost = shortest_path(g, KHO_XUAT_PHAT, DIEM_DEN_DON)
    print(f"Duong di ngan nhat tu {KHO_XUAT_PHAT} den {DIEM_DEN_DON}: {path}")
    print(f"Tong chi phi: {cost}")

    draw_route(
        g, path,
        filename="route.png",
        title=f"{KHO_XUAT_PHAT} -> {DIEM_DEN_DON} (chi phi = {cost})",
    )
    print("Da xuat anh: route.png")


def demo_2_so_sanh_thuat_toan():
    print("\n" + "=" * 60)
    print("DEMO 2: So sanh Dijkstra vs Bellman-Ford")
    print("=" * 60)
    g = load_graph_from_json(DATA_FILE)
    compare_algorithms(g, KHO_XUAT_PHAT, DIEM_DEN_DON)

    print("\n--- Benchmark hieu nang theo kich thuoc do thi ---")
    benchmark_scaling(sizes=(10, 30, 60, 100))


def demo_3_giao_nhieu_diem():
    print("\n" + "=" * 60)
    print("DEMO 3: Giao hang nhieu diem (mo rong dang TSP)")
    print("=" * 60)
    g = load_graph_from_json(DATA_FILE)

    full_route, total_cost = build_full_route(g, KHO_XUAT_PHAT, DIEM_GIAO_NHIEU)
    print_route_report(full_route, total_cost)

    draw_multi_route(g, full_route, filename="multi_route.png")
    print("Da xuat anh: multi_route.png")


def test_khong_co_duong_di():
    print("\n" + "=" * 60)
    print("TEST: Truong hop khong ton tai duong di (dinh co lap)")
    print("=" * 60)
    g = load_graph_from_json(DATA_FILE)
    g.add_vertex("Z_co_lap")

    path, cost = shortest_path(g, KHO_XUAT_PHAT, "Z_co_lap")
    print(f"Dijkstra    -> path={path}, cost={cost}")
    assert path is None and cost == float("inf"), \
        "LOI: Dijkstra chua xu ly dung truong hop khong co duong di!"

    path_bf, cost_bf = bellman_ford(g, KHO_XUAT_PHAT, "Z_co_lap")
    print(f"Bellman-Ford -> path={path_bf}, cost={cost_bf}")
    assert path_bf is None and cost_bf == float("inf"), \
        "LOI: Bellman-Ford chua xu ly dung truong hop khong co duong di!"

    print("=> PASS: Ca 2 thuat toan deu xu ly dung do thi khong lien thong.")


def test_ket_qua_khop_giua_2_thuat_toan():
    print("\n" + "=" * 60)
    print("TEST: Dijkstra va Bellman-Ford phai cho CUNG ket qua")
    print("=" * 60)
    g = load_graph_from_json(DATA_FILE)

    # Test tren nhieu cap dinh khac nhau, khong chi 1 cap
    cap_test = [("A", "L"), ("A", "K"), ("B", "G"), ("C", "J")]
    for src, dst in cap_test:
        _, cost_dij = shortest_path(g, src, dst)
        _, cost_bf = bellman_ford(g, src, dst)
        trang_thai = "OK" if cost_dij == cost_bf else "LOI"
        print(f"{src} -> {dst}: Dijkstra={cost_dij} | Bellman-Ford={cost_bf} [{trang_thai}]")
        assert cost_dij == cost_bf, f"LOI: Ket qua khac nhau cho cap ({src}, {dst})!"

    print("=> PASS: Tat ca cac cap dinh deu cho ket qua khop nhau.")


if __name__ == "__main__":
    demo_1_diem_den()
    demo_2_so_sanh_thuat_toan()
    demo_3_giao_nhieu_diem()
    #test_Kg_di()

    print("\n" + "=" * 60)
    print("HOAN THANH DEMO TICH HOP - TAT CA MODULE HOAT DONG DUNG")
    print("=" * 60)