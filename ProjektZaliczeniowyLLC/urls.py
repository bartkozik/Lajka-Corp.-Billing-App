from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from lajkacorp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('accounts/', include('accounts.urls')),
    path('lajkacorp/', include('lajkacorp.urls')),
]
