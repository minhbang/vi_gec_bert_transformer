# Tự động trích xuất văn bản từ website 

## RUN

- Mặc định: tải 2 ngày, bao gồm hôm nay và lùi lại 1 ngày
    - ```scrapy crawl tuoitre_vn --nolog```
- Tham số: tải 10 ngày, bắt đầu từ **13/6/2019** lùi lại đến ngày **4/6/2019**
    - ```scrapy crawl tuoitre_vn -a start_date=13-6-2019 -a days=10 --nolog```
    
## Todo
- Chuyển các xử lý pipelines thành lib bên ngoài để dùng lại code
- Cho phép option chuyển cả câu thành chữ thường trước khi lưu: ```-a lower=True```