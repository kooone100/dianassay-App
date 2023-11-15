from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('collecctions', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services",),
    path('test', views.test, name="test"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
