from django.views.generic import TemplateView
from core.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView ):
    template_name = 'index/index.html'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)