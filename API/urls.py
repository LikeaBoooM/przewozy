"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

import API.views
from .views import Przewozy, PrzewozID, PrzewozyView, PrzewozyCreateView, PrzewozyDetailView, KartyID, Karty, \
    PrzewozyUpdateView, DeletePrzewoz, CardCreateView, CardDeleteView, ResetPaliwo, CarsNG, DeleteCar, RateCar, Popular, AvgRates

urlpatterns = [
    path('api/przewozy/', Przewozy.as_view(), name='przewozy'),
    path('api/przewozy/<int:id>/', PrzewozID.as_view(), name='przewozy-id'),
    path('api/karty/', Karty.as_view(), name='karty'),
    path('api/karty/<int:id>/', KartyID.as_view(), name='karty-id'),
    path('api/karty/<str:pk>/fuel', ResetPaliwo.as_view(), name='karty-id-reset'),
    path('view/przewozy/', PrzewozyView.as_view(), name='przewozy-view'),
    path('view/przewozy/<int:pk>/', PrzewozyUpdateView.as_view(), name='przewozy-view'),
    path('view/przewozy/create/', PrzewozyCreateView.as_view(), name='przewozy-view-create'),
    path('view/przewozy/delete/<int:pk>', DeletePrzewoz.as_view(), name='przewozy-view-delete'),
    path('view/przewozy/detail/<int:pk>/', PrzewozyDetailView.as_view(), name='przewozy-view-detail'),
    path('view/karty/update/', API.views.managekarty, name='karty-update'),
    path('view/karty/create/', CardCreateView.as_view(), name='karty-create'),
    path('view/karty/delete/<int:pk>', CardDeleteView.as_view(), name='karty-delete'),
    path('ng/cars/', CarsNG.as_view(), name='cars-ng'),
    path('ng/cars/<int:id>/', DeleteCar.as_view(), name='cars-ng-delete'),
    path('ng/rates/', RateCar.as_view(), name='cars-ng-rate-car'),
    path('ng/popular/', Popular.as_view(), name='cars-ng-popular'),
    path('ng/carsavg/', AvgRates.as_view(), name='cars-ng-avg-rates'),


]
