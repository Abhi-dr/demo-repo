from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('suryanshbhaikijai/', admin.site.urls),

    path("", include("home.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

