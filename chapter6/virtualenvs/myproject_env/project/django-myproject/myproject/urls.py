"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

from utils.views import render_js

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bulletins/', include('bulletin_board.urls')),
    path('cv/', include('cv.urls')),
    path('email/', include('email_messages.urls')),
    path('like/', include('likes.urls')),
    path('locations/', include('locations.urls')),
    path('movies/', include('movies.urls')),
    path('products/', include('products.urls')),
    path('quotes/', include('quotes.urls')),
]

urlpatterns += i18n_patterns(
    path('search/', include('haystack.urls')),
    path("js-settings/", render_js,
         {"template_name": "settings.js"},
         name="js_settings"),
)
