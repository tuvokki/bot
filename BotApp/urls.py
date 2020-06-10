from django.urls import path

from BotApp.api import ApiAnswer
from BotApp.views import IntentListView, SearchView, NewAnswerView

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('list/', IntentListView.as_view(), name='intent-list'),
    path('add/', NewAnswerView.as_view(), name='intent-create'),
    path('api/search', ApiAnswer.as_view(), name='api-search'),
]
