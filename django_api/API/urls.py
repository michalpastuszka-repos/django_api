from .views import CreateArticleCars, LoginView, AllArticleCars, CreateProfile, CreateCar, CreateFuel, UpdateArticle,\
    UpdateProfile, AllUserProfiles, AllCarModels, AllFuelTypes, UpdateCar, UpdateFuelType


from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('all_articles/', AllArticleCars.as_view(), name='all_articles'),
    path('all_users/', AllUserProfiles.as_view(), name='all_users'),
    path('all_cars/', AllCarModels.as_view(), name='all_cars'),
    path('all_fuels/', AllFuelTypes.as_view(), name='all_fuels'),
    path('create_article/', CreateArticleCars.as_view(), name='create_article'),
    path('create_profile/', CreateProfile.as_view(), name='create-profile'),
    path('create_car/', CreateCar.as_view(), name='create-car'),
    path('create_fuel/', CreateFuel.as_view(), name='create-fuel'),
    path('update_profile/<int:pk>/', UpdateProfile.as_view(), name='update-profile'),
    path('update_article/<int:pk>/', UpdateArticle.as_view(), name='update-article'),
    path('update_car/<int:pk>/', UpdateCar.as_view(), name='update-car'),
    path('update_fuel/<int:pk>/', UpdateFuelType.as_view(), name='update-fuel'),
]