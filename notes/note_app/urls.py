from django.urls import path
from . import views


app_name = 'note'
urlpatterns = [
    path('',views.editor,name='editor'),
    path('delete_note/<int:docid>/',views.delete, name='delete')
]
