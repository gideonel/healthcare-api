from django.urls import path
from users.views import RegisterView, LoginView, LogoutView, UserDetailView, UserView

urlpatterns = [
    # User-related endpoints
    path('', UserView.as_view(), name='users'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='users-detail'),

]