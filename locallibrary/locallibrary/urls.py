from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import include
from django.urls import path
urlpatterns += [
     path('catalog/', include('catalog.urls')),
]
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)