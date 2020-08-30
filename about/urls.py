from django.urls import path # noqa
# from . import views
from .views import AboutView, PitchesView, AddInfo, EditAboutView, DeleteAboutView # noqa


urlpatterns = [
    # path('', views.news, name='news'),
    path('about/', AboutView.as_view(), name='about'),
    path('pitches', PitchesView.as_view(), name='pitches'),
    path('addinfo/', AddInfo.as_view(), name='addnews'),
    path('about/edit/', EditAboutView.as_view(), name='editinfo'),
    path('about/delete/', DeleteAboutView.as_view(), name='deleteinfo'),
]
