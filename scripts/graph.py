import json


class Graph:
    def __init__(self, directed: bool = True):
        """
        TODO (TV2):
        - self.adj: dict[str, list[tuple[str, float]]]
          vi du: {"A": [("B", 4), ("C", 2)], ...}
        - self.directed: co huong hay khong
        """
        self.directed = directed
        self.adj = {}

    def add_vertex(self, v: str):
        """TODO: them dinh v vao self.adj neu chua co."""
        pass

    def add_edge(self, u: str, v: str, weight: float):
        """
        TODO:
        - Them canh (u -> v, weight) vao self.adj.
        - Neu self.directed = False thi them ca chieu nguoc lai (v -> u).
        - Nho dam bao ca u va v deu da ton tai trong self.adj (goi add_vertex).
        """
        pass

    def neighbors(self, u: str):
        """TODO: tra ve danh sach (v, weight) ke voi u."""
        pass

    def vertices(self):
        """TODO: tra ve danh sach tat ca cac dinh."""
        pass

    def __repr__(self):
        return f"Graph(directed={self.directed}, vertices={len(self.adj)})"


def load_graph_from_json(filepath: str) -> Graph:
    """
    TODO (TV2):
    - Doc file JSON co dang giong data.json (key "vertices", "edges").
    - Tao doi tuong Graph, add_vertex cho tung dinh, add_edge cho tung canh.
    - Return doi tuong Graph da xay dung xong.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    g = Graph(directed=True)
    # TODO: duyet data["vertices"] -> g.add_vertex(...)
    # TODO: duyet data["edges"] -> g.add_edge(e["from"], e["to"], e["weight"])
    return g


def generate_random_graph(num_vertices: int = 30, num_edges: int = 60, seed: int = 42) -> Graph:
    """
    TODO (TV2 - tuy chon, phuc vu TV4 do hieu nang):
    - Sinh ngau nhien num_vertices dinh (vi du: "V0", "V1", ...).
    - Sinh ngau nhien num_edges canh co trong so duong (vi du 1-20).
    - Dung random.seed(seed) de ket qua co the lap lai.
    """
    import random
    random.seed(seed)
    g = Graph(directed=True)
    # TODO: implement
    return g


if __name__ == "__main__":
    # Test nhanh khi chay truc tiep file nay
    g = load_graph_from_json("data.json")
    print(g)
    print("Cac dinh:", g.vertices())
    print("Ke cua Kho_Tong:", g.neighbors("Kho_Tong"))