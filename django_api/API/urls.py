from .views import CreateArticleCars, LoginView, AllArticleCars, CreateProfile, CreateCar, CreateFuel, UpdateArticle,\
    UpdateProfile

from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('create_articles/', CreateArticleCars.as_view(), name='create_articles'),
    path('all_articles/', AllArticleCars.as_view(), name='all_articles'),
    path('create_profile/', CreateProfile.as_view(), name='create-profile'),
    path('create_car/', CreateCar.as_view(), name='create-car'),
    path('create_fuel/', CreateFuel.as_view(), name='create-fuel'),
    path('update_profile/<int:pk>/', UpdateProfile.as_view(), name='update-profile'),
    path('update_article/<int:pk>/', UpdateArticle.as_view(), name='update-article'),
]