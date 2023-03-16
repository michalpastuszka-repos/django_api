from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import generics
from .models import UserProfile, CarModel, ArticleCars, FuelType
from .serializers import UserProfileSerializer, ArticleCarsSerializer, CarModelSerializer, FuelTypeSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
#endpoint to log in by user
class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

#private endpoint (only for superusers) to create entry with nested objects
class CreateArticleCars(generics.CreateAPIView):
    serializer_class = ArticleCarsSerializer
    permission_classes = [IsAdminUser]

class CreateProfile(generics.CreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]

class CreateCar(generics.CreateAPIView):
    serializer_class = CarModelSerializer
    permission_classes = [IsAdminUser]

class CreateFuel(generics.CreateAPIView):
    serializer_class = FuelTypeSerializer
    permission_classes = [IsAdminUser]

#public endpoint to serve data from your models with all related objects
class AllArticleCars(generics.ListAPIView):
    serializer_class = ArticleCarsSerializer
    queryset = ArticleCars.objects.all()

class AllUserProfiles(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class AllCarModels(generics.ListAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()

class AllFuelTypes(generics.ListAPIView):
    serializer_class = FuelTypeSerializer
    queryset = FuelType.objects.all()


#private endpoint (only for owners) to update entry with nested objects
class UpdateProfile(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class UpdateArticle(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleCarsSerializer
    queryset = ArticleCars.objects.all()

class UpdateCar(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()

class UpdateFuelType(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarModelSerializer
    queryset = FuelType.objects.all()


