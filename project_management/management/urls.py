from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectCreateView, ProjectListView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('projects/', ProjectCreateView.as_view(), name='project-list-create'),
    path('projects/user/', ProjectListView.as_view(), name='user-projects'),
]
