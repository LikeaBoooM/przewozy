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

from django.urls import path, include

import API.views
from . views import Przewozy, PrzewozID, PrzewozyView, PrzewozyCreateView, PrzewozyDetailView, KartyID, Karty, PrzewozyUpdateView, DeletePrzewoz

urlpatterns = [
    path('api/przewozy/', Przewozy.as_view(), name='przewozy'),
    path('api/przewozy/<int:id>/', PrzewozID.as_view(), name='przewozy-id'),
    path('api/karty/', Karty.as_view(), name='karty'),
    path('api/karty/<int:id>/', KartyID.as_view(), name='karty-id'),
    path('view/karty/update/', API.views.managekarty, name='karty-update'),
    path('view/przewozy/', PrzewozyView.as_view(), name='przewozy-view'),
    path('view/przewozy/<int:pk>/', PrzewozyUpdateView.as_view(), name='przewozy-view'),
    path('view/przewozy/create/', PrzewozyCreateView.as_view(), name='przewozy-view-create'),
    path('view/przewozy/delete/<int:pk>', DeletePrzewoz.as_view(), name='przewozy-view-delete'),
    path('view/przewozy/detail/<int:pk>/', PrzewozyDetailView.as_view(), name='przewozy-view-detail'),

]
