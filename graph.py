import csv
import json
import random
from typing import Dict, List, Optional, Tuple


class Graph:
    def __init__(self):
        self._vertices: List[str] = []                      # đổi tên: vertices -> _vertices
        self.vertex_indices: Dict[str, int] = {}
        self.adj_list: Dict[str, List[Tuple[str, float]]] = {}
        self.adj_matrix: List[List[Optional[float]]] = []

    def add_vertex(self, vertex: str) -> None:
        vertex = str(vertex).strip()
        if vertex in self.vertex_indices:
            return
        idx = len(self._vertices)
        self.vertex_indices[vertex] = idx
        self._vertices.append(vertex)
        self.adj_list[vertex] = []
        for row in self.adj_matrix:
            row.append(None)
        self.adj_matrix.append([None] * len(self._vertices))

    def add_edge(self, u: str, v: str, weight: float) -> None:
        u, v = str(u).strip(), str(v).strip()
        weight = float(weight)
        if u not in self.vertex_indices:
            self.add_vertex(u)
        if v not in self.vertex_indices:
            self.add_vertex(v)
        self.adj_list[u].append((v, weight))
        u_idx = self.vertex_indices[u]
        v_idx = self.vertex_indices[v]
        self.adj_matrix[u_idx][v_idx] = weight

    def load_from_json(self, filepath: str) -> None:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for v in data.get("vertices", []):
            self.add_vertex(v)
        for edge in data.get("edges", []):
            self.add_edge(edge["source"], edge["target"], edge["weight"])

    def load_from_csv(self, filepath: str) -> None:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_edge(row["source"], row["target"], float(row["weight"]))

    @classmethod
    def generate_random(
        cls,
        num_vertices: int = 15,
        edge_prob: float = 0.25,
        min_weight: float = 1.0,
        max_weight: float = 10.0,
    ) -> "Graph":
        g = cls()
        vertex_names = [f"V{i}" for i in range(1, num_vertices + 1)]
        for v in vertex_names:
            g.add_vertex(v)
        for u in vertex_names:
            for v in vertex_names:
                if u != v and random.random() < edge_prob:
                    w = round(random.uniform(min_weight, max_weight), 1)
                    g.add_edge(u, v, w)
        return g

    # ===== 2 HÀM THÊM MỚI để tương thích với dijkstra.py, alt_algorithm.py,
    # multi_delivery.py, visualize.py — các file này đều gọi graph.vertices()
    # và graph.neighbors(u) dưới dạng HÀM (có dấu ngoặc), không phải thuộc tính. =====

    def vertices(self) -> List[str]:
        """Trả về danh sách tất cả các đỉnh trong đồ thị."""
        return self._vertices

    def neighbors(self, u: str) -> List[Tuple[str, float]]:
        """Trả về danh sách (đỉnh_kề, trọng_số) của đỉnh u."""
        return self.adj_list.get(u, [])

    def print_adj_list(self) -> None:
        print("\n--- DANH SÁCH KỀ (ADJACENCY LIST) ---")
        for u in self._vertices:
            edges = [f"-> {v} ({w})" for v, w in self.adj_list[u]]
            print(f"{u}: {', '.join(edges) if edges else '(không có đỉnh kề)'}")

    def print_adj_matrix(self) -> None:
        print("\n--- MA TRẬN KỀ (ADJACENCY MATRIX) ---")
        header = f"{'':>5}" + "".join([f"{v:>7}" for v in self._vertices])
        print(header)
        for i, u in enumerate(self._vertices):
            row_vals = []
            for val in self.adj_matrix[i]:
                row_vals.append(f"{val:>7.1f}" if val is not None else f"{'·':>7}")
            print(f"{u:>5}" + "".join(row_vals))


# ===== HÀM CẤP MODULE 
#     from graph import Graph, load_graph_from_json
def load_graph_from_json(filepath: str) -> Graph:
    g = Graph()
    g.load_from_json(filepath)
    return g


if __name__ == "__main__":
    g1 = Graph()
    try:
        g1.load_from_json("data.json")
        g1.print_adj_list()
        g1.print_adj_matrix()
    except FileNotFoundError:
        print("Lỗi: Chưa tìm thấy data.json, kiểm tra lại file!")
