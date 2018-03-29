from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexView, name='index'),
    path('assets.html', views.AssetListView.as_view(), name='assets_list'),
    path('asset-add.html',views.AssetAdd.as_view(),name='asset_add'),
    path('asset-detail-<int:pk>.html',views.AssetDetail.as_view(),name='asset_detail'),
    path('asset-update-<int:pk>.html', views.AssetUpdate.as_view(), name='asset_update'),
    path('asset-all-del.html',views.AssetAllDel.as_view(),name='asset_all_del'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('portmap/list.html', views.PortMapListView.as_view(), name='portmap_list')
]

app_name = 'assets'