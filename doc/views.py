from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Doc
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import DocForm

# 文档列表
class DocListView(LoginRequiredMixin, ListView):
    model = Doc
    context_object_name = 'doc_list'
    template_name = 'doc/doc_list.html'

    def get_context_data(self, **kwargs):
        context = {
            "doc_active": "active",
            "doc_zhishiku_active": "active",
        }
        kwargs.update(context)
        return super(DocListView, self).get_context_data(**kwargs)


# 文档详情页
class DocDetailView(DetailView):
    model = Doc
    template_name = 'doc/doc-detail.html'
    context_object_name = 'doc_detail'

    def get_context_data(self, **kwargs):
        context = {
            "doc_active": "active",
            "doc_zhishiku_active": "active",
        }
        kwargs.update(context)
        return super(DocDetailView, self).get_context_data(**kwargs)


# 编辑文档
class DocUpdateView(UpdateView):
    model = Doc
    form_class = DocForm
    template_name = 'doc/doc-update.html'


    def get_context_data(self, **kwargs):
        context = {
            "doc_active": "active",
            "doc_zhishiku_active": "active",
        }
        kwargs.update(context)
        return super(DocUpdateView, self).get_context_data(**kwargs)