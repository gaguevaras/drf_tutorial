from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>/", views.snippet_detail),
    path("wrapped_snippets/", views.wrapped_snippet_list),
    path("wrapped_snippets/<int:pk>/", views.wrapped_snippet_detail),
    path('class_based_snippets/', views.SnippetList.as_view()),
    path('class_based_snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
