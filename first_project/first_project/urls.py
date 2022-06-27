from django.contrib import admin
from django.urls import path

from first_app.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view),
]
