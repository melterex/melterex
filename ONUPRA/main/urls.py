from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index, name='home'),
    path('you/', views.Account_REDIR, name='accountREDIR'),
    path('signup/', views.Reg_page, name='signup'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('edit/', views.Account_REDIR, name='edit'),
    path('top/', views.Rating, name='top'),
    path('competitions/', views.Competitions, name='competitions'),
    path('competition/<int:id>/', views.Сurrent_competition, name='сompetition'),
    path('competition/<int:id>/<int:taskid>/', views.Competition_task, name='competition_task'),
    path('createcompetition/', views.CreateCompetition, name='ccc'),
    path('user/<slug:slug>/', views.Profile, name='account'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
