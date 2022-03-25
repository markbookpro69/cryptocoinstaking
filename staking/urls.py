from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('live', include('livestakes.urls')),
    path('rates/', include('cryptoRates.urls')),    
    path('about-us/', include('aboutUs.urls')),
    path('contact-us/', include('contactUs.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('userProfile.urls')),
    path('withdrawals/', include('withdrawals.urls')),
    path('verification/', include('verification.urls')),
    path('settings/', include('settings.urls')),
    path('compound/', include('compound.urls')),
    path('investments/', include('investments.urls')),
    path('interests/', include('interests.urls')),
    path('affiliates/', include('affiliates.urls')),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)