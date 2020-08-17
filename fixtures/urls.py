from django.urls import path
# from . import views
from .views import FixturesView, FixturesDetailView, AddFixturesView, UpdateFixturesView, DeleteFixturesView # noqa


urlpatterns = [
    # path('', views.news, name='news'),
    path('fixtures/', FixturesView.as_view(), name='fixtures'),
    path('fixtures/<int:pk>', FixturesDetailView.as_view(), name='fixturesdetail'), # noqa
    path('addfixture/', AddFixturesView.as_view(), name='addfixtures'),
    path('fixtures/edit/<int:pk>', UpdateFixturesView.as_view(), name='editfixtures'), # noqa
    path('fixtures/delete/<int:pk>', DeleteFixturesView.as_view(), name='deletefixtures'), # noqa
]
