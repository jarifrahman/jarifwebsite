from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('searchhome', HomePageView.as_view(), name='searchhome'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('',views.allblogs, name='allblogs'),
    path('<int:blog_id>/',views.detail,name='detail')
    ]