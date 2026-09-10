import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph, load_graph_from_json
from dijkstra import shortest_path

def build_nx_graph(graph: Graph) -> nx.DiGraph:
    """
    Chuyen doi tuong Graph (cua TV2) thanh nx.DiGraph de ve.
    Duyet qua graph.vertices() va graph.neighbors(u) de add_node/add_edge
    vao doi tuong nx.DiGraph, giu lai trong so (weight) lam thuoc tinh canh.
    """
    G = nx.DiGraph()
    G.add_nodes_from(graph.vertices())

    for source in graph.vertices():
        for target, weight in graph.neighbors(source):
            G.add_edge(source, target, weight=weight)

    return G

def draw_route(graph: Graph, path: list, filename: str = "route.png", title: str = "Duong di ngan nhat"):
    G = build_nx_graph(graph)
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=900)
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="lightgray",
        arrows=True,
        arrowsize=18,
        connectionstyle="arc3,rad=0.05",
    )
    nx.draw_networkx_labels(G, pos, font_size=9)

    path = path or []
    route_nodes = [node for node in path if node in G]
    route_edges = [
        (path[index], path[index + 1])
        for index in range(len(path) - 1)
        if G.has_edge(path[index], path[index + 1])
    ]
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=route_nodes,
        node_color="tomato",
        node_size=950,
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=route_edges,
        edge_color="crimson",
        width=3,
        arrows=True,
        arrowsize=22,
        connectionstyle="arc3,rad=0.05",
    )

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()

def draw_multi_route(graph: Graph, full_route, filename: str = "multi_route.png"):
    G = build_nx_graph(graph)
    pos = nx.spring_layout(G, seed=42)
    colors = ["crimson", "darkorange", "seagreen", "royalblue", "darkviolet"]

    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=900)
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="lightgray",
        arrows=True,
        arrowsize=18,
        connectionstyle="arc3,rad=0.05",
    )
    nx.draw_networkx_labels(G, pos, font_size=9)

    for index, segment in enumerate(full_route or []):
        if len(segment) < 3:
            continue
        path = segment[2] or []
        route_edges = [
            (path[path_index], path[path_index + 1])
            for path_index in range(len(path) - 1)
            if G.has_edge(path[path_index], path[path_index + 1])
        ]
        color = colors[index % len(colors)]
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=[node for node in path if node in G],
            node_color=color,
            node_size=950,
        )
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=route_edges,
            edge_color=color,
            width=3,
            arrows=True,
            arrowsize=22,
            connectionstyle="arc3,rad=0.05",
        )
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Lo trinh giao hang nhieu diem")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()
if __name__ == "__main__":
    from multi_delivery import build_full_route, print_route_report
    
    g = load_graph_from_json("data.json")
    path, cost = shortest_path(g, "Kho_Tong", "G")
    print("Duong di:", path, "| Chi phi:", cost)
    draw_route(g, path, filename="route.png", title=f"Kho_Tong -> G (chi phi = {cost})")
    print("Da xuat anh: route.png")

    diem_giao = ["C", "F", "G"]
    full_route, total_cost = build_full_route(g, "Kho_Tong", diem_giao)
    print_route_report(full_route, total_cost)
    draw_multi_route(g, full_route, filename="multi_route.png")
    print("Da xuat anh: multi_route.png")