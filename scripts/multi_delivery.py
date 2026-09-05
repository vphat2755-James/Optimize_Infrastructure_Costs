from graph import Graph, load_graph_from_json
from dijkstra import shortest_path


def nearest_neighbor_order(graph: Graph, source: str, destinations: list):
    """
    TODO (TV5):
    Input:
        graph        : doi tuong Graph
        source       : diem xuat phat (kho)
        destinations : danh sach cac diem CAN GIAO (list[str])
    Output:
        thu_tu_giao : list cac diem theo THU TU nen di (khong bao gom source)

    Thuat toan Nearest Neighbor (tham lam):
        1. Bat dau tu source, coi la "diem hien tai".
        2. Trong so cac diem CHUA GIAO, tim diem GAN NHAT
           (dung shortest_path(graph, diem_hien_tai, diem_ung_vien)
           de lay chi phi, chon diem co chi phi nho nhat).
        3. Them diem do vao thu_tu_giao, cap nhat "diem hien tai" = diem do.
        4. Lap lai cho den khi giao het tat ca cac diem trong destinations.

    Luu y: day la heuristic (khong dam bao toi uu tuyet doi nhu TSP
    chinh xac), nhung du dung cho quy mo bai tap va de giai thich.
    """
    pass


def build_full_route(graph: Graph, source: str, destinations: list):
    """
    TODO (TV5):
    Input:  graph, source, destinations (giong ham tren)
    Output: (full_route, total_cost)
        - full_route: list cac buoc, moi buoc la (diem_bat_dau, diem_ket_thuc,
          path_chi_tiet, chi_phi_doan_nay)
        - total_cost: tong chi phi CA HANH TRINH (cong don tat ca doan)

    Cach lam:
        1. order = nearest_neighbor_order(graph, source, destinations)
        2. diem_hien_tai = source
        3. Voi moi diem ke tiep trong order:
             path, cost = shortest_path(graph, diem_hien_tai, diem_ke_tiep)
             them (diem_hien_tai, diem_ke_tiep, path, cost) vao full_route
             cong don cost vao total_cost
             cap nhat diem_hien_tai = diem_ke_tiep
        4. Return full_route, total_cost
    """
    pass


def print_route_report(full_route, total_cost):
    """
    TODO (TV5 - de lam bao cao/demo):
    In ra man hinh tung chang duong va tong ket, vi du:
        Chang 1: Kho_Tong -> C  | Duong di: [...]  | Chi phi: 11
        Chang 2: C -> F         | Duong di: [...]  | Chi phi: 7
        Chang 3: F -> G         | Duong di: [...]  | Chi phi: 4
        -----------------------------------------
        TONG QUANG DUONG CA HANH TRINH: 22
    """
    pass


if __name__ == "__main__":
    g = load_graph_from_json("data.json")
    diem_giao = ["C", "F", "G"]  # lay tu data.json["diem_giao_hang_mau"]

    full_route, total_cost = build_full_route(g, "Kho_Tong", diem_giao)
    print_route_report(full_route, total_cost)