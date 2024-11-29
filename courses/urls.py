from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListAPIView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course_detail'),
    path('months/', views.MounthListAPIView.as_view(), name='month_list'),
    path('months/<int:pk>/', views.MounthDetailAPIView.as_view(), name='month_detail'),
    path('classes/', views.ClassAndHomeWorkListAPIView.as_view(), name='class_list'),
    path('classes/<int:pk>/', views.ClassAndHomeWorkDetailAPIView.as_view(), name='class_detail'),
    
]
