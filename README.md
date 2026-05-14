# Django Computer Store

## Thông tin sinh viên

* Họ tên: Nguyễn Minh Toàn
* Email: toannm190984@sv-onuni.edu.vn

* SĐT: 0907045210

## Mô tả project

Website bán linh kiện máy tính xây dựng bằng Django.

## Chức năng chính

* Hiển thị danh sách sản phẩm
* Thêm sản phẩm vào giỏ hàng
* Xóa sản phẩm khỏi giỏ hàng
* Lọc sản phẩm theo danh mục

## Công nghệ sử dụng

* Python
* Django
* HTML, CSS
Hướng dẫn cài đặt
1️⃣ Clone project
git clone https://github.com/your-username/computer-store.git
cd computer-store
2️⃣ Tạo môi trường ảo
python -m venv venv
Kích hoạt môi trường
Windows
venv\Scripts\activate
Linux / MacOS
source venv/bin/activate
3️⃣ Cài đặt Django
pip install django
4️⃣ Migration database
python manage.py makemigrations
python manage.py migrate
5️⃣ Tạo tài khoản admin
python manage.py createsuperuser
6️⃣ Chạy server
python manage.py runserver

Mở trình duyệt:

http://127.0.0.1:8000/
🔐 Trang quản trị Django Admin

Truy cập:

http://127.0.0.1:8000/admin/

Đăng nhập bằng tài khoản admin đã tạo.

🛒 Chức năng giỏ hàng

Hệ thống sử dụng Django Session để lưu giỏ hàng tạm thời.

Các chức năng gồm:

Thêm sản phẩm vào giỏ
Cập nhật số lượng
Xóa sản phẩm
Tính tổng tiền
Thanh toán đơn hàng
📷 Giao diện hệ thống

Website được thiết kế theo phong cách thương mại điện tử hiện đại:

Responsive
Dễ sử dụng
Tối ưu trải nghiệm người dùng
Giao diện sáng, trực quan
📚 Kiến thức áp dụng

Trong quá trình thực hiện dự án, đã áp dụng:

Django MTV Architecture
Django ORM
Django Session
Authentication System
Template Engine
CRUD Operations
Bootstrap UI Design
🎯 Mục tiêu dự án
Xây dựng website bán hàng bằng Django
Thực hành thiết kế database
Áp dụng CRUD và Authentication
Hiểu quy trình triển khai hệ thống web
Nâng cao kỹ năng lập trình Python Django

📄 License

Dự án được sử dụng cho mục đích học tập và nghiên cứu.

❤️ Cảm ơn

Cảm ơn thầy/cô và mọi người đã xem dự án TechShop.
