
from django.urls import path

from .views import (login, logout, private, refresh, register, reset_password,
                    resetpasssord, test)

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('private/', private),
    path('refresh/', refresh),
    path('reset/<str:token>/<int:userId>/', reset_password),
    path('resetPassword/', resetpasssord),
    path('logout/', logout),
    path('test/<int:testNo>/', test),
]
