# Optimize_Infrastructure_Costs — Shortest Path Delivery System

## Thông tin dự án
- **Project Code:** Optimize_Infrastructure_Costs
- **Project Name:** Shortest Path Delivery System (Tìm đường đi ngắn nhất trong hệ thống giao hàng)
- **Môn học:** [Điền tên môn học]

## Thành viên nhóm
|      Họ và tên      |     MSSV     |      GitHub             |                Vai trò                  |
|----------------------|--------------|------------------------|------------------------------------------|
| Võ Thanh Phát        | 087205017625 | vphat2755-James        | Trưởng nhóm, Mô tả bài toán, Tích hợp & Test |
| Nguyễn Thị Ngọc Hân  | 087306013212 | hanntn3212@ut.edu.vn   | Xây dựng đồ thị & đọc dữ liệu đầu vào (graph.py) |
| Nguyễn Thị Mỹ Hương  | 060306002632 | huongntm2632@ut.edu.vn | Thuật toán Dijkstra (dijkstra.py)         |
| Nguyễn Ngọc Tùng     | 079205036628 | tungnn6628@ut.edu.vn   | Thuật toán đối chiếu Bellman-Ford & đo hiệu năng(alt_algorithm.py)|
| Võ Duy Khang         | 083206000919 | KBOT-1                 | Bài toán giao nhiều điểm (multi_delivery.py) |
| Nguyễn Gia Khiêm     | 040206013248 | khiemng3248@ut.edu.vn  | Trực quan hóa kết quả (visualize.py)      |

## Proposal

### What we want to do
Xây dựng một hệ thống mô phỏng bài toán **tìm đường đi ngắn nhất trong
mạng lưới giao hàng nội đô**, lấy bối cảnh thực tế của công ty chuyển
phát nhanh FastShip tại q1, Thành phố Hồ Chí Minh. Hệ thống mô hình hóa
mạng lưới đường (giao lộ, kho hàng, điểm giao) bằng đồ thị có hướng,
có trọng số, từ đó tính toán lộ trình tối ưu cho shipper nhằm giảm thời
gian giao hàng và chi phí vận hành.

### What features we aim to complete
- Xây dựng cấu trúc dữ liệu đồ thị có hướng, có trọng số (danh sách kề), đọc dữ liệu từ file JSON hoặc sinh dữ liệu mô phỏng
- Cài đặt thuật toán Dijkstra tìm đường đi ngắn nhất giữa 2 điểm bất kỳ, dùng hàng đợi ưu tiên (heapq)
- Cài đặt thuật toán Bellman-Ford để đối chiếu kết quả với Dijkstra, đo và so sánh thời gian chạy giữa 2 thuật toán
- Mở rộng bài toán sang nhiều điểm giao hàng cùng lúc (heuristic Nearest Neighbor, tiệm cận bài toán TSP/VRP đơn giản hóa)
- Trực quan hóa đồ thị và highlight tuyến đường tìm được bằng networkx/matplotlib, xuất ra file ảnh
- Xử lý các ràng buộc thực tế: đường một chiều (đồ thị có hướng), trường hợp không tồn tại đường đi giữa 2 điểm (đồ thị không liên thông)
- Tích hợp toàn bộ pipeline (đọc dữ liệu → tính toán → trực quan hóa) qua 1 script chạy demo duy nhất, kèm test case kiểm tra tính đúng đắn

### What stack we are using
- **Language:** Python 3
- **Graph & Algorithm:** cấu trúc dữ liệu tự cài đặt (adjacency list), thư viện chuẩn `heapq`
- **Data Format:** JSON (đồ thị mẫu, danh sách điểm giao hàng)
- **Visualization:** `networkx`, `matplotlib`
- **Testing:** `assert` / test case thủ công trong `main.py`
- **IDE:** Visual Studio Code

### What will be achieved as final
Một bộ chương trình Python hoàn chỉnh, có thể chạy bằng một lệnh
(`python main.py`), thực hiện: (1) đọc dữ liệu mạng lưới giao hàng mô
phỏng, (2) tìm đường đi ngắn nhất giữa kho và 1 điểm giao bằng
Dijkstra, (3) đối chiếu kết quả với Bellman-Ford kèm bảng so sánh thời
gian chạy, (4) xác định thứ tự giao hàng tối ưu khi có nhiều điểm cần
giao, (5) xuất ra hình ảnh trực quan hóa tuyến đường. Kết quả demo và
số liệu đo hiệu năng sẽ được đưa vào báo cáo cuối kỳ.

## Planning

### Phase 1 — Tuần 1
- Thiết lập project structure, Git repo, tạo nhánh `dev` và nhánh riêng cho từng thành viên
- Viết mô tả bài toán (bối cảnh, input/output, ràng buộc) — mục 3.1 & 3.2 báo cáo
- Thiết kế cấu trúc dữ liệu đồ thị (`Graph`) và dữ liệu mẫu (`data.json`)
- Thống nhất định dạng trả về chung giữa các module: `(path, cost)`

### Phase 2 — Tuần 2
- Hoàn thiện thuật toán Dijkstra (`dijkstra.py`) — thuật toán chính của hệ thống
- Hoàn thiện thuật toán đối chiếu Bellman-Ford và đo hiệu năng (`alt_algorithm.py`)
- Test độc lập từng module trên dữ liệu mẫu trước khi tích hợp

### Phase 3 — Tuần 3
- Hoàn thiện bài toán giao nhiều điểm (`multi_delivery.py`)
- Hoàn thiện trực quan hóa kết quả (`visualize.py`)
- Trưởng nhóm ghép toàn bộ vào `main.py`, chạy demo tích hợp, fix lỗi phát sinh

### Phase 4 — Tuần 4
- Viết báo cáo hoàn chỉnh (mô tả bài toán, thuật toán, kết quả thử nghiệm, so sánh hiệu năng)
- Chuẩn bị slide thuyết trình
- Chụp/ghi lại kết quả demo (ảnh trực quan hóa, bảng so sánh thuật toán)
- Merge nhánh `dev` vào `main`, dọn dẹp repo trước khi nộp

### Tuần 5 — Buffer (dự phòng)
- Fix bug phát sinh khi tích hợp
- Chuẩn bị thuyết trình
- Nộp bài

## Mô tả
Hệ thống mô phỏng bài toán tìm đường đi ngắn nhất trong mạng lưới giao
hàng, lấy bối cảnh công ty FastShip tại TP.HCM. Mạng lưới đường được
mô hình hóa bằng đồ thị có hướng, có trọng số; hệ thống cài đặt và so
sánh hai thuật toán kinh điển (Dijkstra, Bellman-Ford), đồng thời mở
rộng sang bài toán giao nhiều điểm và trực quan hóa kết quả.

## Cấu trúc repo
- `data.json` — Dữ liệu đồ thị mẫu (đỉnh, cạnh, trọng số)
- `graph.py` — Cấu trúc dữ liệu đồ thị + đọc dữ liệu từ JSON
- `dijkstra.py` — Thuật toán Dijkstra (thuật toán chính)
- `alt_algorithm.py` — Thuật toán Bellman-Ford để đối chiếu + đo hiệu năng
- `multi_delivery.py` — Bài toán giao nhiều điểm (heuristic Nearest Neighbor)
- `visualize.py` — Trực quan hóa đồ thị và tuyến đường
- `main.py` — Tích hợp toàn bộ pipeline, chạy demo và test

## Công nghệ sử dụng
- Python 3
- networkx
- matplotlib
- heapq (thư viện chuẩn Python)

## Hướng dẫn chạy
1. Clone repo về máy: `git clone https://github.com/vphat2755-James/Optimize_Infrastructure_Costs.git`
2. Cài đặt thư viện cần thiết: `pip install networkx matplotlib`
3. Mở thư mục project bằng Visual Studio Code
4. Chạy file demo tích hợp: `python main.py`
5. Kết quả gồm: đường đi ngắn nhất + chi phí, bảng so sánh Dijkstra vs Bellman-Ford, thứ tự giao hàng tối ưu cho nhiều điểm, và 2 file ảnh `route.png` / `multi_route.png`
6. Có thể chạy riêng từng file (`python dijkstra.py`, `python visualize.py`, ...) để test độc lập trước khi tích hợp