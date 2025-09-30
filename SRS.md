# 📄 Software Requirements Specification (SRS)
**Dự án:** Quản lý phòng mạch tư nhân – Private Clinic Management System  
**Ngày:** 2025-09-16  
**Ngôn ngữ:** Song ngữ (Việt – Anh)  
**Framework:** Django  

---

## 1. Giới thiệu
### 1.1. Mục tiêu
- Xây dựng hệ thống quản lý phòng mạch tư nhân cho các bác sĩ tự mở phòng khám tại Việt Nam.  
- Cho phép bệnh nhân đặt lịch khám, quản lý hồ sơ bệnh án, bác sĩ quản lý thông tin bệnh nhân và lịch khám.  
- Hệ thống **mã nguồn mở** và miễn phí cho cộng đồng.  

### 1.2. Người dùng hệ thống
- **Bệnh nhân (Patient):** Đặt lịch khám, tra cứu hồ sơ bệnh án bằng số điện thoại.  
- **Bác sĩ & nhân viên y tế (Doctor/Staff):** Đăng nhập, quản lý hồ sơ bệnh nhân, lịch khám.  
- **Admin:** Quản trị toàn hệ thống.  

---

## 2. Yêu cầu hệ thống
### 2.1. Chức năng chính
- **Trang chủ (Home):** Giới thiệu dự án, chọn ngôn ngữ (Việt/Anh), đặt lịch khám, đăng nhập.  
- **Booking App:** Đặt lịch khám cho bệnh nhân.  
- **Patient App:** Quản lý thông tin bệnh nhân (tên, số điện thoại, tiền sử bệnh, lịch sử khám).  
- **Staff App:** Quản lý bác sĩ, điều dưỡng, y tá (thông tin cá nhân, chuyên môn, lịch làm việc).  
- **Login App:**  
  - Bác sĩ/nhân viên đăng nhập bằng tài khoản mật khẩu.  
  - Bệnh nhân dùng số điện thoại để tra cứu và đặt lịch.  
- **About Page:** Giới thiệu dự án, cung cấp link tải source code.  

### 2.2. Yêu cầu phi chức năng
- **Đơn giản, dễ dùng:** Giao diện HTML + Bootstrap.  
- **Song ngữ:** Dùng Django i18n cho đa ngôn ngữ.  
- **CSDL:** SQLite (khởi đầu), có thể nâng cấp PostgreSQL/MySQL.  
- **Phân quyền:**  
  - Bệnh nhân: đặt lịch, xem hồ sơ.  
  - Bác sĩ/nhân viên: quản lý bệnh nhân & lịch khám.  
  - Admin: quản lý toàn bộ.  

---

## 3. Kiến trúc Django
- `app_home`: Trang chủ + giới thiệu.  
- `app_booking`: Quản lý lịch khám.  
- `app_patient`: Quản lý bệnh nhân.  
- `app_staff`: Quản lý bác sĩ/nhân viên.  
- `app_auth`: Đăng nhập & phân quyền.  

---

## 4. Mô hình dữ liệu (ERD sơ bộ)

```
+----------------+        +-----------------+        +----------------+
|   Patient      |        |  Appointment    |        |    Staff       |
+----------------+        +-----------------+        +----------------+
| id (PK)        |<--+    | id (PK)         |        | id (PK)        |
| name           |   |    | patient_id (FK) |        | name           |
| phone (unique) |   +----| doctor_name     |        | role           |
| medical_history|        | appointment_date|        | specialization |
+----------------+        | note            |        | schedule       |
                          +-----------------+        +----------------+
```

---

## 5. Luồng người dùng
### 5.1. Bệnh nhân
1. Vào trang chủ → chọn “Đặt lịch khám”.  
2. Nhập tên + số điện thoại → chọn bác sĩ, ngày giờ → lưu vào hệ thống.  
3. Có thể tra cứu hồ sơ khám bằng số điện thoại.  

### 5.2. Bác sĩ/nhân viên
1. Đăng nhập bằng username/password.  
2. Xem danh sách bệnh nhân.  
3. Cập nhật tiền sử bệnh, kết quả khám.  
4. Quản lý lịch khám của mình.  

### 5.3. Admin
- Thêm/sửa/xóa bác sĩ, nhân viên.  
- Quản lý toàn bộ bệnh nhân và lịch khám.  

---

## 6. Ví dụ code Django (đơn giản)
### 6.1. `models.py` – app_patient
```python
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)   # Họ tên bệnh nhân
    phone = models.CharField(max_length=15, unique=True)  # Số điện thoại (dùng tra cứu)
    medical_history = models.TextField(blank=True, null=True)  # Tiền sử bệnh

    def __str__(self):
        return f"{self.name} - {self.phone}"
```

### 6.2. `models.py` – app_booking
```python
from django.db import models
from app_patient.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Liên kết bệnh nhân
    doctor_name = models.CharField(max_length=100)  # Tên bác sĩ (đơn giản)
    appointment_date = models.DateTimeField()  # Ngày giờ khám
    note = models.TextField(blank=True, null=True)  # Ghi chú

    def __str__(self):
        return f"{self.patient.name} - {self.doctor_name} - {self.appointment_date}"
```

### 6.3. `views.py` – app_booking
```python
from django.shortcuts import render, redirect
from .models import Appointment
from app_patient.models import Patient

def book_appointment(request):
    if request.method == "POST":
        name = request.POST.get("name")   # Tên bệnh nhân
        phone = request.POST.get("phone") # Số điện thoại
        doctor = request.POST.get("doctor") # Bác sĩ
        date = request.POST.get("date")   # Ngày giờ

        # Tìm hoặc tạo bệnh nhân
        patient, created = Patient.objects.get_or_create(phone=phone, defaults={"name": name})

        # Tạo lịch khám
        Appointment.objects.create(
            patient=patient,
            doctor_name=doctor,
            appointment_date=date
        )
        return redirect("success")  # Trang báo thành công

    return render(request, "booking.html")
```

---

## 7. Kế hoạch mở rộng
- Thêm chức năng gửi SMS/email nhắc lịch.  
- Tích hợp API tra cứu hồ sơ bệnh án.  
- Thêm dashboard cho bác sĩ (thống kê số bệnh nhân, lịch khám).  
