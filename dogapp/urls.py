from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DogList, DogDetail, BreedList, BreedDetail


#Uncomment from between here to EOF to enable the viewset approach
#from .views import DogViewSet, BreedViewSet
# router = DefaultRouter()
# router.register(r'dogs', DogViewSet)
# router.register(r'breeds', BreedViewSet)

# urlpatterns = [
#     path('',include(router.urls))
# ]

########EOF####################


urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('breeds/', BreedList.as_view(), name='breed-list'),
    path('breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
]