
from django.urls import path
from . import views

urlpatterns = [
    path('delete_comments/<id>',views.delete_comments),
    path('delete_video/<id>',views.delete_video),
    path('delete_reply/<id>',views.delete_reply),
]