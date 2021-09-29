
from django.contrib import admin
from django.urls import path,include
from student_register import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student_register.urls')),
    path('getToken',views.createToken.as_view(),name='api-data'),
    path('getRoute',views.getRoute.as_view(),name='api-view'),
    path('logout',views.logoutView.as_view(),name='api-logout'),

]
