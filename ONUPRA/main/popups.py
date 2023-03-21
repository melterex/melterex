from popup_field.views import PopupCRUDViewSet
from .models import Task
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','input_exmaple','output_exmaple','extra_text','input_values','output_values','soft','score']


class TaskPopupCRUDViewSet(PopupCRUDViewSet):
    model = Task
    form_class = TaskForm
    template_name_create = 'main/popup_create_task.html'
    template_name_update = 'main/popup_update_task.html'