from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('titles',views.titles,name="titles"),
    path('choose',views.choose,name='choose'),
    path('discget',views.discget,name="discget"),
    path('luvget',views.luvget,name="luvget"),
    path('fitget',views.fitget,name="fitget"),
    path('finget',views.finget,name="finget"),
    path('forcget',views.forcget,name="forcget"),
    path('gtch',views.gtch,name="gtch"),
    path('per',views.per,name="per")
]
