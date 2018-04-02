from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('assets.html', views.AssetListView.as_view(), name='assets_list'),
    path('asset-add.html',views.AssetAdd.as_view(),name='asset_add'),
    path('asset-detail-<int:pk>.html',views.AssetDetail.as_view(),name='asset_detail'),
    path('asset-update-<int:pk>.html', views.AssetUpdate.as_view(), name='asset_update'),
    path('asset-all-del.html',views.AssetAllDel.as_view(),name='asset_all_del'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('portmap/list.html', views.PortMapListView.as_view(), name='portmap_list'),
    # 端口映射
    path('port/map/list/', views.PortMapListView.as_view(), name='port_map_list'),
    # 添加端口映射
    path('port/map/add/', views.AddPortMapView.as_view(), name='add_port_map'),

    # 删除映射记录
    path('port/delete/<int:p_id>/', views.DeletePortMapView.as_view(), name='delete_port'),

    # 修改映射记录
    path('port/map/change/<int:p_id>/', views.ChangePortMapView.as_view(), name='change_port'),
]

app_name = 'assets'