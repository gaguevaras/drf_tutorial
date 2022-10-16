from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('wrapped_snippets/', views.wrapped_snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('wrapped_snippets/<int:pk>/', views.wrapped_snippet_detail),
]