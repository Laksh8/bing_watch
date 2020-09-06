from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Videos',views.VideosViewSet)


urlpatterns = [
    path("router/",include(router.urls)),
    path('',views.home,name='home'),
    path('watch/<id>',views.watch,name='watch'),
    path('comments/watch/<title>',views.comments),
    path('add_video/',views.add_video,name='add_video'),
    path('update_profile/<id>',views.update_profile),
    path('reply/<id>',views.reply)
]

