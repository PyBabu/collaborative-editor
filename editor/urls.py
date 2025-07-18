from django.urls import path
from . import views

urlpatterns = [
    path('<int:doc_id>/', views.editor_view, name='editor'),
    path('mydocs/', views.document_list, name='document_list'),
    path('create/', views.create_document, name='create_document'),
    path('check-grammar/', views.grammar_check_view, name='grammar_check'),
]
