from django.db import models
from django.contrib.auth.models import AbstractUser
import django
from django.utils.timezone import timedelta
from autoslug import AutoSlugField
from PIL import Image

class CustomUser(AbstractUser):
    image = models.ImageField('Изображение', blank=True, null=True, default='default.png', upload_to='img/')
    rating = models.IntegerField('Рейтинг', blank=True, default=0)
    email = models.EmailField('Адрес электронной почты', max_length=254, unique=True, blank=False)
    username = models.CharField(help_text = '', max_length=32, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    slug = AutoSlugField(populate_from='username')
    
    def get_absolute_url(self):
        return redirect('accountRED')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)

class ScorePoint(models.Model):
    link_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField('Рейтинг', default=0)
    date = models.DateTimeField('Дата изменения', auto_now_add=True)

    def __str__(self):
        return str(self.score)

class Competition(models.Model):
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    start_time = models.DateTimeField('Дата старта')
    duration = models.PositiveIntegerField('Длительность соревнования') # минимум 30
    title = models.CharField('Название', unique=True, max_length=30)
    actual = models.BooleanField('Не закончен', default=True)
    verified = models.BooleanField('Проверено администратором', default=False)
    rating = models.BooleanField('Рейтинговое ли соревнование', default=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    compet = models.ForeignKey(Competition, on_delete=models.CASCADE)
    title = models.CharField('Название задания', max_length=30)
    condition = models.TextField('Описание задания')
    required_input = models.TextField('Входные данные')
    required_output = models.TextField('Выходные данные')
    input_exmaple = models.TextField('Пример ввода кода')
    output_exmaple = models.TextField('Пример ввода кода')
    extra_text = models.TextField('Дополнительные пояснение, недочеты', blank=True)
    input_values_1 = models.TextField('Вводимые значения 1')
    output_values_1 = models.TextField('Получаемые значения 1')
    input_values_2 = models.TextField('Вводимые значения 2')
    output_values_2 = models.TextField('Получаемые значения 2')
    input_values_3 = models.TextField('Вводимые значения 3')
    output_values_3 = models.TextField('Получаемые значения 3')
    input_values_4 = models.TextField('Вводимые значения 4')
    output_values_4 = models.TextField('Получаемые значения 4')
    input_values_5 = models.TextField('Вводимые значения 5')
    output_values_5 = models.TextField('Получаемые значения 5')
    score = models.PositiveIntegerField('Количество очков за задание', help_text = 'Указывать половину от максимального числа')

    def __str__(self):
        return self.title

class Attempt(models.Model):
    link_competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    link_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    link_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    points = models.PositiveIntegerField('Количество полученых очков', default=0)
    successfully = models.BooleanField('Успешное решение', default=False)
    error = models.CharField('Ошибка', max_length=30, default='-')
    document = models.FileField(upload_to='comp_files/')
    hidden = models.BooleanField('Скрытая попытка', default=False)

    def __str__(self):
        return str(self.points)

class Article(models.Model):
    text = models.CharField('О чем вы хотите рассказать?', max_length=500, blank=True, null=True)
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) + ' at ' + str(self.creation_date) + ' ' + str(self.text)[0:9]

class File(models.Model):
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    article = models.ForeignKey(Article, related_name='files', on_delete=models.CASCADE)
    files = models.FileField(upload_to='article_files/', null=True)
    
    def __str__(self):
        return str(self.creation_date) + ' and ' + str(self.article)

