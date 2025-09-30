"""
URL Configuration for clinic_management project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language  # Import view set_language

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),
    
    # URL cho chức năng chuyển đổi ngôn ngữ
    path('i18n/setlang/', set_language, name='set_language'),
]

# i18n patterns for translatable URLs
urlpatterns += i18n_patterns(
    # Home app - trang chủ và giới thiệu
    path('', include('app_home.urls')),
    
    # Authentication app - đăng nhập, đăng xuất
    path('auth/', include('app_auth.urls')),
    
    # Booking app - đặt lịch khám
    path('booking/', include('app_booking.urls')),
    
    # Patient app - quản lý bệnh nhân
    path('patients/', include('app_patient.urls')),
    
    # Staff app - quản lý nhân viên và bác sĩ
    path('staff/', include('app_staff.urls')),
    
    prefix_default_language=True
)

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)