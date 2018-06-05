from django.conf import settings
from django.forms import ModelForm, HiddenInput
from django.forms.models import ModelFormMetaclass
from django.forms.fields import CharField
from .models import GenericModel
from .validators import clean_and_validate


class DynamicModelFormMetaclass(ModelFormMetaclass):
    def __new__(cls, name, bases, attrs):
        for name in sorted(settings.SCHEME):
            attrs[name] = CharField(required=False)

        return super(DynamicModelFormMetaclass, cls).__new__(cls, name, bases, attrs)


class GenericModelForm(ModelForm, metaclass=DynamicModelFormMetaclass):
    def __init__(self, *args, **kwargs):
        super(GenericModelForm, self).__init__(*args, **kwargs)
        self.fields['_data'].widget = HiddenInput()
        self.fields['_data'].initial = None

        if self.instance.data:
            for name in settings.SCHEME:
                self.fields[name].initial = self.instance.data.get(name, '')

    def clean(self):
        data = {}

        for name in settings.SCHEME:
            if not self.data.get(name, None):
                continue
            data[name] = self.data[name]

        self.cleaned_data['_data'] = clean_and_validate(data, settings.SCHEME)

    class Meta:
        model = GenericModel
        fields = '__all__'
