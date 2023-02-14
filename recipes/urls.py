from django.urls import path

from . import views
from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),   
    path('search/', views.search, name="search"),   
    # path('recipes/<uuid:id>/', recipe),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
