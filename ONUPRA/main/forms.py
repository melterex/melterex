from .models import CustomUser, Competition, Task, Article, File
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput, CharField, EmailField, ImageField, ClearableFileInput, IntegerField, NumberInput, ModelMultipleChoiceField, SelectMultiple, SplitDateTimeField, BooleanField, CheckboxInput, FileInput, FileField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationFrom(UserCreationForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    email = EmailField(label = 'Почта', widget = EmailInput())
    password1 = CharField(label = 'Пароль', widget = PasswordInput())
    password2 = CharField(label = 'Повторите пароль', widget = PasswordInput())
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserImageChangeFrom(UserChangeForm):
    image = ImageField(label = 'Изображение', widget = ClearableFileInput())
    class Meta:
        model = CustomUser
        fields = ['image']

class CustomUserUsernameChangeFrom(UserChangeForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    class Meta:
        model = CustomUser
        fields = ['username']

class CustomUserChangeFrom(UserChangeForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    email = EmailField(label = 'Почта', widget = EmailInput())
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class PasswordChangeForm(ModelForm):
    old_password = CharField(label = 'Старый пароль', widget = PasswordInput())
    new_password = CharField(label = 'Новый пароль', widget = PasswordInput())
    new_password_repeat = CharField(label = 'Повторите новый пароль', widget = PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password', 'new_password_repeat']

class CreateCompetitionForm(ModelForm):
    title = CharField(label = 'Название', widget = TextInput())
    start_time = SplitDateTimeField(label = 'Время старта', input_time_formats=['%H:%M:%S'])
    duration = IntegerField(label = 'Длительность', widget = NumberInput())
    tasks = ModelMultipleChoiceField(label = 'Выберете задания', queryset=Task.objects.all(), widget = SelectMultiple)
    class Meta:
        model = Competition
        fields = ['title','start_time','duration','tasks',]

class CreateTaskForm(ModelForm):
    title = CharField(label = 'Название задания', widget = TextInput())
    description = CharField(label = 'Описание задачи', widget = Textarea())
    input_exmaple = CharField(label = 'Пример ввода', widget = Textarea())
    output_exmaple = CharField(label = 'Пример вывода', widget = Textarea())
    extra_text = CharField(label = 'Дополнительный текст', widget = Textarea(), required=False)
    input_values = CharField(label = 'Вводимые значения', widget = Textarea())
    output_values = CharField(label = 'Получаемые значения', widget = Textarea())
    soft = BooleanField(label = 'Чувствительность', widget = CheckboxInput(), required=False)
    score = IntegerField(label = 'Счет', widget = NumberInput())
    class Meta:
        model = Task
        fields = ['title','description','input_exmaple','output_exmaple', 'extra_text','input_values','soft','score',]

class ArticleForm(ModelForm):
    text = CharField(label = 'Текст статьи', widget = Textarea())
    class Meta:
        model = Article
        fields = ['text']

class FileForm(ModelForm):
    files = FileField(label = 'Изображение', widget = FileInput(attrs = {'multiple': 'multiple'}))
    class Meta:
        model = File
        fields = ['files']
