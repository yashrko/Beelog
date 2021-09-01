from blog.views import Home_view,Blog_detailview,Blog_createview,Blog_updateview,Blog_deleteview
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', Home_view.as_view(),name="home-view"),
    path('home/<int:pk>/', Blog_detailview.as_view(),name="detail-view"),
    path('home/create/', Blog_createview.as_view(),name="create-view"),
    path('home/<int:pk>/update/', Blog_updateview.as_view(),name="blog-update-view"),
    path('home/<int:pk>/delete/', Blog_deleteview.as_view(),name="blog-delete-view"),
]

if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)