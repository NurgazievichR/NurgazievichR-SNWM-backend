from django.urls import path
from .views import PostCreateView, PostDetailView

urlpatterns = [
    path('', PostCreateView.as_view(), name='post-create'),
    path('<int:id>/', PostDetailView.as_view(), name='post-detail'),
]