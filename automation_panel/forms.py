from .models import Host
from django.forms import ModelForm

requiredError = "Заполните данное поле"

class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = "__all__"
        labels = {
            'name': "Имя",
            'network_name' : "Сетевое имя",
            'ip' : 'IP-адрес',
            'hardware' : 'Железо',
            'group' : 'Группа'
        }
