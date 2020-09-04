## Tự động sinh văn bản sai chính tả
- Load file văn vản đã tải bằng crawler ==> List các câu
- Tách từ trong từng câu

## Rules
    Thực hiện ngẩu nhiên 1 hoặc kết hợp 1 số luật sau:

- Lỗi dấu hỏi/dấu ngã
- Lỗi đánh máy
    - Bỏ dấu tiếng Việt => quên gõ dấu
    - Bỏ dấu tiếng Việt + thêm ký tự (Telex) hoặc số (VNI) tương ứng => Lỗi bỏ dấu bằng bộ gõ TELEX hay VNI
    - Đảo vị trí 
    - Đảo vị trí ngẩu nhiên trong 
- Lỗi chính tả - tìm và thay thế lẫn nhau		
    - Giọng Bắc		
        - Bắt đầu với CH/TR: trăn trối => chăn chối
        - Bắt đầu với S/X: năng suất => năng xuất
        - Bắt đầu với D/GI:	dang dở => giang giở
    - Giọng Nam và Trung		
        - Bắt đầu với D/GI/V: vang danh => dang danh
        - Bắt đầu với U/H/QU: uy quyền => quy quyền
        - Phụ âm cuối C/T: hờn mát => hờn mác
        - Phụ âm cuối N/NG: khốn cùng => khốn cùn
        - Phụ âm cuối I/Y: trình bày => trình bài


- Tách từ => Danh sách các từ
     