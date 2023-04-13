from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index, name='home'),
    path('test/', views.Test, name='test'),
    path('my_ajax_view/', views.my_ajax_view, name='my_ajax_view'),
    path('you/', views.Account_REDIR, name='you'),
    path('signup/', views.Reg_page, name='signup'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('settings/', views.Settings, name='edit'),
    path('top/', views.Top, name='top'),
    path('competition/', views.Competitions, name='competitions'),
    path('competition/<int:id>/', views.Сurrent_competition, name='сompetition'),
    path('competition/<int:id>/<int:taskid>/', views.Competition_now, name='competition_task'),
    path('createcompetition/', views.CreateCompetition, name='ccc'),
    path('user/<str:username>/', views.Profile, name='account'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
