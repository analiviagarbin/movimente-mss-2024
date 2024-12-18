from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jogadores/', include('movimente_app.urls')),  # URLs da aplicação movimente_app
]
