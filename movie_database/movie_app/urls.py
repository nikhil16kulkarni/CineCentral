from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('read/', read_data, name='read_movies'), 
    path('update/<str:movie_id>/', update_movie, name='update_movie'),
    path('update-record/', update_movie_record, name='update_movie_record'),
    path('create/', create_movie, name='create_movie'),
    
    path('delete/', delete_movie, name='delete_movie'),
    #path('read/', genre_movie_view, name='genre_movie_view'),

    path('signup/', signup_view, name="signup_view"),

    path('login/', auth_views.LoginView.as_view(template_name = 'login_signup.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},  name = 'logout'),

    # path('login/', login_view, name='login'),
    # path('signup/', signup_view, name='signup'),
]

