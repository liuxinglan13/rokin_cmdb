from django.urls import path
from . import views



urlpatterns = [
    path('doc_list.html', views.DocListView.as_view(), name='doc_list'),
    path('doc-detail.html-<int:pk>', views.DocDetailView.as_view(), name='doc_detail'),
    path('doc-update.html-<int:pk>', views.DocUpdateView.as_view(), name='doc_update'),

]

app_name = 'doc'