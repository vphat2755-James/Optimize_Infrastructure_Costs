import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph, load_graph_from_json
from dijkstra import shortest_path


def build_nx_graph(graph: Graph) -> nx.DiGraph:
    """
    TODO (TV6):
    Chuyen doi tuong Graph (cua TV2) thanh nx.DiGraph de ve.
    Duyet qua graph.vertices() va graph.neighbors(u) de add_node/add_edge
    vao doi tuong nx.DiGraph, giu lai trong so (weight) lam thuoc tinh canh.
    """
    G = nx.DiGraph()
    # TODO: G.add_node(v) cho tung dinh
    # TODO: G.add_edge(u, v, weight=w) cho tung canh
    return G


def draw_route(graph: Graph, path: list, filename: str = "route.png", title: str = "Duong di ngan nhat"):
    """
    TODO (TV6):
    Input:
        graph    : doi tuong Graph goc
        path     : danh sach dinh cua duong di can highlight, vi du ["Kho_Tong","B","A"]
        filename : ten file anh xuat ra
        title    : tieu de bieu do

    Cac buoc goi y:
        1. G = build_nx_graph(graph)
        2. pos = nx.spring_layout(G, seed=42)   # vi tri cac dinh, seed de on dinh
        3. Ve TOAN BO do thi mau xam nhat (nx.draw voi edge_color='lightgray')
        4. Tao danh sach cac canh thuoc "path": [(path[i], path[i+1]) for i in range(len(path)-1)]
        5. Ve DE LEN TREN cac canh/dinh trong path bang mau do/xanh noi bat
           (dung nx.draw_networkx_edges/nodes voi edgelist/nodelist rieng)
        6. Them nhan trong so canh: nx.draw_networkx_edge_labels(G, pos, edge_labels=...)
        7. plt.title(title); plt.savefig(filename, dpi=150); plt.close()
    """
    pass


def draw_multi_route(graph: Graph, full_route, filename: str = "multi_route.png"):
    """
    TODO (TV6 - phoi hop voi TV5):
    Tuong tu draw_route(), nhung highlight NHIEU doan duong lien tiep
    (moi doan trong full_route co the to 1 mau khac nhau de de phan biet
    thu tu giao hang: doan 1 mau do, doan 2 mau cam, doan 3 mau tim, ...).
    """
    pass


if __name__ == "__main__":
    g = load_graph_from_json("data.json")
    path, cost = shortest_path(g, "Kho_Tong", "G")
    print("Duong di:", path, "| Chi phi:", cost)
    draw_route(g, path, filename="route.png", title=f"Kho_Tong -> G (chi phi = {cost})")
    print("Da xuat anh: route.png")