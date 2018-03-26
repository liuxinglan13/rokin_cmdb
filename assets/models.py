from django.db import models
from django.urls import reverse

# 资产
class assets(models.Model):
    assets_type_choices = (
        ('server', u'服务器'),
        ('vmser', u'虚拟机'),
        ('switch', u'交换机'),
    )
    assets_status_choices = (
        ('runing', u'在用'),
        ('stop', u'停用'),
    )
    # 资产状态
    assets_status = models.CharField(choices=assets_status_choices, max_length=100, default='runing', verbose_name='资产状态')
    # 资产类型
    assets_type = models.CharField(choices=assets_type_choices, max_length=100, default='server', verbose_name='资产类型')
    # 资产用途/描述
    assets_description = models.CharField(max_length=100, verbose_name='主机的用途', null=True, blank=True)
    # 资产名称
    hostname = models.CharField(max_length=64, verbose_name='资产名称', null=True, blank=True)
    # IP地址
    network_ip = models.GenericIPAddressField(verbose_name='IP地址')
    # 管理IP
    manage_ip = models.GenericIPAddressField(verbose_name='管理IP', null=True,blank=True)
    # 资产型号 硬件型号
    model = models.CharField(max_length=128, verbose_name='型号', null=True,blank=True)
    # 资产 系统类型 版本
    system = models.CharField(max_length=128,verbose_name='系统版本',null=True,blank=True)
    # 产品线 名
    pro_name = models.CharField(default='', max_length=64, verbose_name='项目名', blank=True)
    # 数据中心
    data_center = models.ForeignKey(to="data_centers", to_field='id', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='数据中心')
    # 机柜
    cabinet = models.CharField(max_length=64, verbose_name='机柜', blank=True)
    # 位置
    position = models.CharField(max_length=64, verbose_name='位置', blank=True)
    # 登录用户名
    user_name = models.CharField(default='', max_length=32, verbose_name='登录用户名', blank=True)
    # 登录密码
    pass_word = models.CharField(default='', max_length=64, verbose_name='登录密码', blank=True)
    # SN
    sn = models.CharField(max_length=64,verbose_name='序列号', blank=True)
    # CPU
    cpu = models.CharField(max_length=64,verbose_name='CPU', blank=True)
    # 内存
    memory = models.CharField(default=8, max_length=64, verbose_name='内存', blank=True)
    # 硬盘
    disk = models.CharField(default=300, max_length=256,verbose_name="硬盘", blank=True)
    # 备注
    ps = models.TextField(max_length=1024,verbose_name="备注", blank=True)
    # 创建记录时间
    ctime= models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间',blank=True)
    # 最后更新记录时间
    utime = models.DateTimeField(auto_now=True, null=True,verbose_name='更新时间',blank=True)


    class  Meta:
        # 数据库中指定 表名
        db_table ="asset"
        # 后台中显示的名称
        verbose_name="资产管理"
        # 去掉s 没有的话 在后台中会显示  资产管理s
        verbose_name_plural = '资产管理'

    def __str__(self):
        return self.network_ip

    # 这个函数 用来生成 url
    def get_absolute_url(self):
        return reverse('assets:asset_detail', kwargs={'pk': self.pk})


# 数据中心
class data_centers(models.Model):
    data_center_list = models.CharField(max_length=128, verbose_name='数据中心', null=True)


    class Meta:
        db_table = "data_centers"
        verbose_name = "数据中心"
        verbose_name_plural = '数据中心'

    def __str__(self):
        return self.data_center_list