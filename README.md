# Đề tài: Tìm đường đi ngắn nhất trong hệ thống giao hàng

## Cấu trúc thư mục

| File | Phụ trách | Mô tả |
|---|---|---|
| `data.json` | TV2 | Dữ liệu đồ thị mẫu (đỉnh, cạnh, trọng số) |
| `graph.py` | TV2 | Class `Graph` + đọc dữ liệu từ JSON |
| `dijkstra.py` | TV3 | Thuật toán Dijkstra — hàm chính `shortest_path()` |
| `alt_algorithm.py` | TV4 | Bellman-Ford để đối chiếu + đo hiệu năng |
| `multi_delivery.py` | TV5 | Bài toán giao nhiều điểm (heuristic nearest neighbor) |
| `visualize.py` | TV6 | Vẽ đồ thị + highlight tuyến đường bằng networkx/matplotlib |
| `main.py` | Trưởng nhóm | Tích hợp toàn bộ, chạy demo, test |

## Thứ tự triển khai 

1. **TV2 làm trước tiên** — hoàn thành `graph.py` + `data.json`, gửi ngay cho cả nhóm (mọi file khác đều `import` từ đây).
2. **TV3, TV4, TV5, TV6 code song song** sau khi có `graph.py`.
   - TV5 cần `dijkstra.py` của TV3 hoàn thành trước khi test được `multi_delivery.py`.
   - TV6 cần `dijkstra.py` của TV3 để có `path` mà vẽ.
3. **Trưởng nhóm ghép `main.py`** cuối buổi, chạy toàn bộ, fix lỗi tích hợp.

## Cài đặt môi trường

```bash
pip install networkx matplotlib
```

## Cách chạy demo

```bash
python main.py
```

Kết quả mong đợi:
- In ra đường đi ngắn nhất, tổng chi phí.
- Bảng so sánh Dijkstra vs Bellman-Ford (thời gian chạy + kiểm tra khớp kết quả).
- Thứ tự giao hàng tối ưu cho nhiều điểm + tổng quãng đường.
- 2 file ảnh: `route.png` (1 điểm đến) và `multi_route.png` (nhiều điểm đến).
- Test case đồ thị không liên thông chạy PASS.

## Quy ước chung khi code

- Mọi hàm trả về đường đi đều dùng chung định dạng: `(path: list[str] | None, cost: float)`.
- Đặt tên đỉnh dạng chuỗi (string), khớp với `data.json`.
- Nếu sửa `data.json`, báo ngay cho cả nhóm vì mọi người dùng chung 1 bộ dữ liệu để test.
- Mỗi file có thể chạy độc lập (`python <file>.py`) để tự test trước khi ghép vào `main.py`.
