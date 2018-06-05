from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import GenericModel
from .forms import GenericModelForm


class CreateGenericModelView(CreateView):
    model = GenericModel
    form_class = GenericModelForm
    template_name = 'generic_model/create.html'
    success_url = reverse_lazy('generic_model:create')
