from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from django.views.generic import TemplateView, ListView, View, CreateView, UpdateView, DeleteView, DetailView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import AssetForm, AddPortMapForm
import json
from django.conf import settings
from django.db.models import Q


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')

# 资产列表类视图
class AssetListView(LoginRequiredMixin, ListView):
    model = assets
    context_object_name = 'asset_list'
    paginate_by = settings.DISPLAY_PER_PAGE
    template_name = 'assets/assets.html'
    queryset = assets.objects.all()
    ordering = ('id',)

    def get_context_data(self, **kwargs):
        context = {
            "asset_active": "active",
            "asset_list_active": "active",
        }
        kwargs.update(context)
        return super(AssetListView, self).get_context_data(**kwargs)

    ### 查询
    def get_queryset(self,*args,**kwargs):
        self.queryset = super().get_queryset()
        if  self.request.GET.get('name'):
            query = self.request.GET.get('name',None)
            # 主机名和IP地址的模糊查询
            queryset = self.queryset.filter(Q(network_ip__contains=query)| Q(hostname__contains=query)).order_by('id')
        else:
            queryset = super().get_queryset()
        return queryset

# 资产详情页
class AssetDetail(DetailView):
    model = assets
    template_name = 'assets/asset-detail.html'
    context_object_name = 'assets'

    def get_context_data(self, **kwargs):
        context = {
            "asset_active": "active",
            "asset_list_active": "active",
        }
        kwargs.update(context)
        return super(AssetDetail, self).get_context_data(**kwargs)


# 新增资产
class AssetAdd(CreateView):
    model = assets
    form_class = AssetForm
    template_name = 'assets/asset-add.html'

    def get_context_data(self, **kwargs):
        context = {
            "asset_active": "active",
            "asset_list_active": "active",
        }
        kwargs.update(context)
        return super(AssetAdd, self).get_context_data(**kwargs)


# # 更新资产信息
# class AssetUpdate(UpdateView):
#     model = assets
#     form_class = AssetForm
#     template_name = 'assets/asset-update.html'
#
#
#     def get_context_data(self, **kwargs):
#         asset_type = self.object.assets.assets_type
#         context = {
#             "asset_active": "active",
#             "asset_list_active": "active",
#             "asset_type": "asset_type",
#         }
#         kwargs.update(context)
#         return super(AssetUpdate, self).get_context_data(**kwargs)


# 更新资产信息
class AssetUpdate(LoginRequiredMixin, View):

    def get(self, request, pk):
        print(request.body)
        print(request.POST)
        asset = assets.objects.filter(id=pk)
        print(asset)
        context = {
            "asset": asset,
        }
        return render(request, 'assets/asset-update.html', context)

    def post(self, request, pk):
        change_host_form = AssetForm(request.POST)
        if change_host_form.is_valid():
            host = assets()
            host.id = int(pk)
            host.network_ip = request.POST.get('network_ip')
            host.hostname = request.POST.get('hostname')
            host.assets_description = request.POST.get('assets_description')
            host.assets_type = request.POST.get('assets_type')
            host.assets_status = request.POST.get('assets_status')
            host.system = request.POST.get('system')
            host.disk = int(request.POST.get('disk'))
            host.memory = int(request.POST.get('memory'))
            host.ps = request.POST.get('ps')
            host.save()
            assets_list = assets.objects.all()
            context = {
                "asset_list": assets_list
            }

            return render(request, 'assets/assets.html', context)

            #return HttpResponse('{"status":"success", "msg":"记录修改成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"记录修改失败！"}', content_type='application/json')




# 删除资产
class AssetAllDel(LoginRequiredMixin,View):

    model = assets

    def post(self, request):
        ret = {'status': True, 'error': None, }
        try:
            if  request.POST.get('nid') :
                id = request.POST.get('nid', None)
                assets.objects.get(id=id).delete()
            else:
                print(1)
        finally:
            return HttpResponse(json.dumps(ret))

# 二级联动 获取城市 测试
def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'assets/city_dropdown_list_options.html', {'cities': cities})



### 端口映射列表视图
class PortMapListView(ListView):
    model = PortMap
    context_object_name = 'portmap_list'
    template_name = 'assets/portmap-list.html'

    def get_context_data(self, **kwargs):
        assets_list = assets.objects.all()
        context = {
            "asset_active": "active",
            "port_map_list_active": "active",
            "assets": assets_list
        }
        kwargs.update(context)
        return super(PortMapListView, self).get_context_data(**kwargs)





########################################################################################################################
## 添加映射视图
########################################################################################################################
class AddPortMapView(LoginRequiredMixin, View):
    def post(self, request):
        add_portmap_form = AddPortMapForm(request.POST)
        if add_portmap_form.is_valid():
            # 判断记录是否存在
            if PortMap.objects.filter(in_ip=request.POST.get('in_ip')).filter(in_port=request.POST.get('in_port')):
                return HttpResponse('{"status":"fail", "msg":"映射已存在！"}', content_type='application/json')

            # 添加新记录
            portmap = PortMap()
            portmap.in_ip_id = request.POST.get('in_ip')
            portmap.in_port = request.POST.get('in_port')
            portmap.out_ip = request.POST.get('out_ip')
            portmap.out_port = request.POST.get('out_port')
            portmap.ask_user = request.POST.get('ask_user')
            portmap.use_for = request.POST.get('use_for')
            portmap.start_time = request.POST.get('start_time')
            portmap.stop_time = request.POST.get('stop_time')
            portmap.ps = request.POST.get('ps')
            portmap.save()

            return HttpResponse('{"status":"success", "msg":"映射记录添加成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"映射记录添加失败！"}', content_type='application/json')


########################################################################################################################
## 删除映射视图
########################################################################################################################
class DeletePortMapView(LoginRequiredMixin, View):
    def post(self, request, p_id):
        try:
            ports = PortMap.objects.get(id=int(p_id))
            ports.delete()
            return HttpResponse('{"status":"success", "msg":"映射记录删除成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"fail", "msg":"映射记录删除失败！"}', content_type='application/json')


########################################################################################################################
## 修改映射视图
########################################################################################################################
class ChangePortMapView(LoginRequiredMixin, View):
    def post(self, request, p_id):
        change_portmap_form = AddPortMapForm(request.POST)
        if change_portmap_form.is_valid():
            # 删除旧的记录
            old_ports = PortMap.objects.get(id=int(p_id))
            old_ports.delete()
            # 添加新的记录
            portmap = PortMap()
            portmap.in_ip_id = request.POST.get('in_ip')
            portmap.in_port = request.POST.get('in_port')
            portmap.out_ip = request.POST.get('out_ip')
            portmap.out_port = request.POST.get('out_port')
            portmap.ask_user = request.POST.get('ask_user')
            portmap.use_for = request.POST.get('use_for')
            portmap.start_time = request.POST.get('start_time')
            portmap.stop_time = request.POST.get('stop_time')
            portmap.ps = request.POST.get('ps')
            portmap.save()
            return HttpResponse('{"status":"success", "msg":"映射记录修改成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"映射记录修改失败！"}', content_type='application/json')