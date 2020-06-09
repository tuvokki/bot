from django.urls import path

from BotApp.views import IntentListView, SearchView, NewAnswerView

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('list/', IntentListView.as_view(), name='intent-list'),
    path('add/', NewAnswerView.as_view(), name='intent-create'),
]
