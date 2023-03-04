from django.contrib import admin
from django.urls import path, include
from qna import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('qna', include('qna.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]

handler404 = 'common.views.page_not_found'