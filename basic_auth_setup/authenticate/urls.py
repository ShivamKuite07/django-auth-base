

from django.urls import path
from .views import signup, logout_view
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('signup/', view=signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='authenticate/login.html', authentication_form = LoginForm), name='login'),
    path('logout/', view=logout_view, name='logout'),  # Logout
]
