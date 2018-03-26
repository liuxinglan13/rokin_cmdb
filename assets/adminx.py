import xadmin
from xadmin import views
from .models import *

class AssetsAdmin(object):
    list_display = ['hostname', 'network_ip', 'system', 'ctime']
    search_fields = ['hostname', 'network_ip', 'system', 'ctime']
    list_filter = ['hostname', 'network_ip', 'system', 'ctime']

class DataCentsAdmin(object):
    list_display = ['data_center_list']


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "后台管理系统"
    menu_style = "accordion"        # 设置收起菜单

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(assets, AssetsAdmin)
xadmin.site.register(data_centers, DataCentsAdmin)