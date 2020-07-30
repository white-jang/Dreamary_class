from django.contrib import admin
from django.urls import path
import page.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home, name='home'),
    path('introduce/', page.views.introduce, name="introduce"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
