import re
import sys
import os
from datetime import date
# import locale
# import pytils
from django.http import JsonResponse
from django.utils.timezone import localtime, now, timedelta, localdate,  get_default_timezone_name, datetime
from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import CustomUser, Competition, Task, Attempt, File, Article, ScorePoint
from django.contrib.auth.hashers import check_password
from .forms import CustomUserCreationFrom, CustomUserChangeFrom, PasswordChangeForm, CreateCompetitionForm, CustomUserImageChangeFrom, CustomUserUsernameChangeFrom, CreateTaskForm, ArticleForm, FileForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView, UpdateView
from django.db.models import Max

import subprocess

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def create_output_file(command):
    global compile_error, delete_files
    try:
        subprocess.run(command, shell=True, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        compile_error = 0
    except subprocess.CalledProcessError as e:
        compile_error = 1


def run_command(file_name, tests_input, tests_output):
    global compile_error, delete_files
    path = 'main\\media\\comp_files\\'
    command = ""
    if file_name.endswith(".py"):
        command = "python " + path + file_name
    elif file_name.endswith(".cpp"):
        command = "g++ " + path + file_name + \
            " -o " + f"{path + file_name[:-4]}.out"
        create_output_file(command)
        command = f"{path + file_name[:-4]}.out"
        delete_files.append(f"{path + file_name[:-4]}.out")
    elif file_name.endswith(".pas"):
        command = "fpc " + path + file_name
        create_output_file(command)
        command = path + file_name[:-4] + ".exe"
        delete_files.append(path + file_name[:-4] + ".exe")
    elif file_name.endswith(".c"):
        command = "gcc " + path + file_name + \
            " -o " + f"{path + file_name[:-2]}.out"
        create_output_file(command)
        command = f"{path + file_name[:-2]}.out"
        delete_files.append(f"{path + file_name[:-4]}.out")
    elif file_name.endswith(".cs"):
        command = "csc " + path + file_name
        create_output_file(command)
        command = "mono " + path + file_name[:-3] + ".exe"
        delete_files.append(path + file_name[:-3] + ".exe")
    elif file_name.endswith(".go"):
        command = "go run " + path + file_name
    elif file_name.endswith(".kt"):
        command = "kotlinc " + path + file_name + \
            f" -include-runtime -d {path + file_name[:-3]}.jar"
        create_output_file(command)
        command = f"java -jar {path + file_name[:-3]}.jar"
        delete_files.append(f"{path + file_name[:-3]}.jar")
    elif file_name.endswith(".php"):
        command = "php " + path + file_name
    elif file_name.endswith(".rb"):
        command = "ruby " + path + file_name
    elif file_name.endswith(".rs"):
        command = "rustc " + path + file_name + \
            f" -o {path + file_name[:-3]}.out"
        create_output_file(command)
        command = f"{path + file_name[:-3]}.out"
        delete_files.append(f"{path + file_name[:-4]}.out")
    elif file_name.endswith(".js"):
        command = "d8 " + path + file_name
    else:
        compile_error = 1
        return "Нет такого языка програмирования"
    # delete_files.append(path + file_name)
    if compile_error == 0:
        for i in range(len(tests_input)):
            try:
                result = subprocess.run(command, input=(tests_input[i] + "\n"), text=True, shell=True,
                                        timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                if result.stdout.strip() != tests_output[i].strip():
                    # for j in delete_files:
                        # os.remove(j)
                    return [(i / len(tests_input)), f"Неправильный ответ на тесте {i}"]
            except subprocess.TimeoutExpired:
                compile_error = 1
                # for j in delete_files:
                    # os.remove(j)
                return [(i / len(tests_input)), f"Превышено ограничение времени на тесте {i}"]
            except subprocess.CalledProcessError as e:
                compile_error = 1
                # for j in delete_files:
                    # os.remove(j)
                return [(i / len(tests_input)), f"Проблема с принятием входных данных на тесте {i}"]
        else:
            return [1, "Все тесты прошли успешно"]
    else:
        # for i in delete_files:
            # os.remove(i)
        return [0, "Не удалось скомпилировать файл"]


def Index(request):
    # locale.setlocale(locale.LC_TIME, 'ru_RU')
    comp = Competition.objects.filter(actual=True).order_by('start_time')
    if comp:
        comp = comp[0]
        # user_tz = request.COOKIES.get('timezone')
        # if user_tz:
        #     user_tz = pytz.timezone(user_tz)
        #     server_time = comp.start_time
        #     user_time = server_time.astimezone(user_tz)
        #     date = user_time.strftime(u'%d.%m')
        #     time = user_time.strftime(u'%H:%M')
        # else:
        #     date = comp.start_time.strftime(u'%d.%m')
        #     time = comp.start_time.strftime(u'%H:%M')
        date = comp.start_time.strftime(u'%d.%m')
        time = comp.start_time.strftime(u'%H:%M')
        # return render(request, 'main/home.html', {'comp': comp, 'date': pytils.dt.ru_strftime(u'%d %B', inflected=True, date=comp.start_time)})
        return render(request, 'main/home.html', {'comp': comp, 'date': date, 'time': time})
    return render(request, 'main/home.html', {'comp': comp})

def my_ajax_view(request):
    if request.method == 'POST':
        # handle the form submission here
        a = request.POST.get("name")
        # do something with the content
        data = {
        'message': f'{a}1111',
        }
        return JsonResponse(data)
    data = {
        'message': f'22',
        }
    return JsonResponse(data)

def Test(request):
    return render(request, 'main/test.html')

def Account_REDIR(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('account', request.user.username)

def Top(request):
    user = CustomUser.objects.filter(is_staff=False).filter(
        is_superuser=False).order_by('-rating')
    return render(request, 'main/top.html', {'users': user})

def Profile(request, username):
    user = CustomUser.objects.get(username=username)
    # если решили обновить аватарку
    if request.method == 'POST' and request.user.is_authenticated:
        if 'reset image' in request.POST:
            request.user.image = 'default.png'
            request.user.save()
            # Редиректим
            return redirect('account', request.user.username)
        elif 'update image' in request.POST and request.FILES:
            # В форму добавляем инфу которую пользователь добавил
            form = CustomUserImageChangeFrom(
                request.POST, request.FILES, instance=request.user)
            print(form.errors)
            if form.is_valid():
                form.save()
                return redirect('account', request.user.username)
        elif 'new post' in request.POST:
            form = ArticleForm(request.POST)
            form2 = FileForm(request.POST, request.FILES)
            if form.is_valid():
                if form2.is_valid():
                    article = form.save(commit=False)
                    article.user = request.user
                    article.save()
                    form2.save(commit=False)
                    for i in request.FILES.getlist('files'):
                        File.objects.create(files=i, article=article)
                else:
                    article = form.save(commit=False)
                    article.user = request.user
                    article.save()
                return redirect('account', request.user.username)
    content = {
        'user': user,
        'form': ArticleForm(),
        'form2': FileForm(),
        'articles': Article.objects.filter(user=user),
        'point': ScorePoint.objects.filter(link_user=user).order_by("date")
    }
    return render(request, 'main/profile.html', content)

def Settings(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Если метод пост
    if request.method == 'POST':
        # Если отправлена форма проверки никнейма
        if "check_username" in request.POST:
            successfully = False
            nickname = request.POST.get('username')
            form = CustomUserUsernameChangeFrom(request.POST, instance=request.user)
            if (form.is_valid) and (not CustomUser.objects.filter(username=nickname).exists()):
                successfully = True
            data = {
                'username': request.POST.get('username').strip(),
                'successfully': successfully,
                }
            return JsonResponse(data)
        # Если отправлена форма редактирования пользователя
        if "username_edit" in request.POST:
            successfully = False
            nickname = request.POST.get('username')
            form = CustomUserUsernameChangeFrom(request.POST, instance=request.user)
            if form.is_valid and (not CustomUser.objects.filter(username=nickname).exists()):
                successfully = True
            if successfully:
                request.user.username = request.POST.get('username')
                request.user.save()
            data = {
                'username': request.user.username,
                'successfully': successfully,
                }
            return JsonResponse(data)
        # Если отправлена форма редактирования почты
        if "email_edit" in request.POST:
            print(request)
            email_successfully = False
            password_successfully = False
            email = request.POST.get('email').strip()
            password = request.POST.get('password').strip()
            print(email, ((not CustomUser.objects.filter(email=email).exists()) and (not email.strip() == "") and ('@' in email) and ('.' in email)))
            print(password, (check_password(password, request.user.password) and (not password.strip() == "")))
            if ((not CustomUser.objects.filter(email=email).exists()) and (not email.strip() == "") and ('@' in email) and ('.' in email)):
                email_successfully = True
            if (check_password(password, request.user.password) and (not password.strip() == "")):
                password_successfully = True
            if email_successfully and password_successfully:
                request.user.email = email
                request.user.save()
            data = {
                'email': request.user.email,
                'email_successfully': email_successfully,
                'password_successfully': password_successfully,
                }
            return JsonResponse(data)
        # Если нажали кнопку редактирования пароля
        elif "password_edit" in request.POST:
            successfully = False
            old_password = request.POST.get("old_password")
            new_password = request.POST.get("new_password")
            new_password2 = request.POST.get("new_password2")
            # Если все совпадает устанвливаем новый пароль и редиректим
            if check_password(old_password, request.user.password) and new_password == new_password2:
                successfully = True
                request.user.set_password(new_password)
                request.user.save()
            print(old_password, new_password, new_password2, check_password(old_password, request.user.password), successfully)
            data = {
                'successfully': successfully,
                }
            return JsonResponse(data)
        elif "delete" in request.POST:
            successfully = False
            delete_password = request.POST.get("delete_password")
            print(delete_password, successfully, check_password(delete_password, request.user.password))
            if check_password(delete_password, request.user.password):
                request.user.delete()
                successfully = True
            data = {
                'successfully': successfully,
                }
            return JsonResponse(data)
    return render(request, 'main/settings.html')

def CreateCompetition(request):
    if request.method == 'POST':
        if 'task' in request.POST:
            task_form = CreateTaskForm(request.POST)
            print(request.POST)
            if task_form.is_valid():
                print("eeeee")
                task_form.save()
            else:
                print(task_form.errors)
                print("Nooooo")
        if 'competition' in request.POST:
            comp_form = CreateCompetitionForm(request.POST)
            print(request.POST)
            if comp_form.is_valid():
                print("eeeee")
                comp_form.save()
            else:
                print(comp_form.errors)
                print("Nooooo")
    comp_form = CreateCompetitionForm()
    task_form = CreateTaskForm()
    content = {
        'comp_form': comp_form,
        'task_form': task_form
    }
    return render(request, 'main/create_competition.html', content)


def Competitions(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    comp = Competition.objects.filter(actual=True).order_by('-start_time')
    past_comp = Competition.objects.filter(actual=False).order_by('-start_time')
    content = {
        'comp': comp,
        'past_comp': past_comp,
    }
    return render(request, 'main/competition.html', content)


def Сurrent_competition(request, id):
    return redirect('competition_task', id, 0)


def Competition_now(request, id, taskid):
    comp = Competition.objects.get(id=id)
    task = Task.objects.filter(compet=comp).order_by('title')[taskid]
    print(request.FILES)
    if not request.user.is_authenticated:
        return redirect('login')
    elif comp.start_time > localtime():
        return redirect('home')
    elif request.method == 'POST' and comp.actual and request.FILES:
        # if not Attempt.objects.filter(link_competition = comp).filter(link_user = request.user):
        #     comp.amount_of_users += 1
        #     comp.save()
        file = request.FILES['file']
        atmpt = Attempt(link_competition=comp, link_task=task,
                        link_user=request.user, document=file)
        atmpt.save()
        global compile_error, delete_files
        delete_files = []
        compile_error = 0
        file_name_num = atmpt.document.path.rfind("\\")
        if file_name_num == -1:
            file_name_num = atmpt.document.path.rfind("/")
            file_name = atmpt.document.path[file_name_num + 1:]
            # path = atmpt.document.path[0 : file_name_num]
        else:
            file_name = atmpt.document.path[file_name_num + 1:]
            # path = atmpt.document.path[0 : file_name_num]
        del file_name_num
        answer = run_command(file_name, [task.input_values_1.replace('\r\n', '\n'), task.input_values_2.replace('\r\n', '\n'), task.input_values_3.replace('\r\n', '\n'), task.input_values_4.replace('\r\n', '\n'), task.input_values_5.replace(
            '\r\n', '\n')], [task.output_values_1.replace('\r\n', '\n'), task.output_values_2.replace('\r\n', '\n'), task.output_values_3.replace('\r\n', '\n'), task.output_values_4.replace('\r\n', '\n'), task.output_values_5.replace('\r\n', '\n')])
        if compile_error == 0:
            atmpt.successfully = True
            timeleft = comp.duration - \
                int((localtime() - comp.start_time).total_seconds() // 60)
            x = timeleft / comp.duration
            h = 1
            k = 0.4
            y = h * x
            if y > 1:
                y = 1
            elif y < k:
                y = k
            atmpt.points = round(task.score * y * answer[0])
            atmpt.error = answer[1]
        else:
            atmpt.error = answer[1]
        atmpt.save()
        data = {
        'id': atmpt.id,
        'link_competition': atmpt.link_competition,
        'link_task': atmpt.link_task,
        'link_user': atmpt.link_user,
        'document': atmpt.document.url,
        'successfully': atmpt.successfully,
        'points': atmpt.points,
        'error': atmpt.error,
        'time': atmpt.time,
        }
        return JsonResponse(data)
    timeleft = comp.duration - \
        int((localtime() - comp.start_time).total_seconds() // 60)
    x = timeleft / comp.duration
    h = 1
    k = 0.4
    y = h * x
    if y > 1:
        y = 1
    elif y < k:
        y = k
    if comp.start_time + timedelta(minutes=comp.duration) < localtime():
        time_shower = False
    else:
        time_shower = True
    content = {
        'comp': comp,
        'actual_task': task,
        'task': Task.objects.filter(compet=comp).order_by('title'),
        'time': localtime().strftime("%H:%M:%S"),
        'timeleftH': (datetime.combine(date.today(), datetime.min.time()) + timedelta(minutes=comp.duration) - (localtime() - comp.start_time)).strftime("%H"),
        'timeleftM': (datetime.combine(date.today(), datetime.min.time()) + timedelta(minutes=comp.duration) - (localtime() - comp.start_time)).strftime("%M"),
        'timeleftS': (datetime.combine(date.today(), datetime.min.time()) + timedelta(minutes=comp.duration) - (localtime() - comp.start_time)).strftime("%S"),
        'actual_score': round(task.score * y),
        'time_shower': time_shower,
        'actual': comp.actual,
        'attempt': Attempt.objects.filter(link_user=request.user).order_by('-time')[0:15],
        'time': comp.start_time + timedelta(minutes=comp.duration)
    }
    return render(request, 'main/competition_now.html', content)

# def Competition_task(request, id, taskid):
#     error = ''
#     comp = Competition.objects.get(id = id)
#     if comp.start_time > now():
#         return redirect('home')
#     task = comp.tasks.get(id = taskid)
#     if not request.user.is_authenticated:
#         return redirect('login')
#     if request.method == 'POST':
#         if comp.actual:
#             # Если отправлена задание
#             if "test" in request.POST:
#                 # Если отправили файл
#                 if request.FILES:
#                     print(11)
#                     # Получаем загруженный файл
#                     file = request.FILES['file']
#                     fs = FileSystemStorage()
#                     # Сохраняем на файловой системе, решаем и удаляем
#                     filename = fs.save(file.name, file)
#                     # Функция которая будет декодировать ответ файла в нормальный
#                     encoding = sys.getdefaultencoding()
#                     # Если прописано много запусков, то создаем списки с различными запусками
#                     if '/br' in task.input_values:
#                         inptvals = task.input_values.strip().split("/br")
#                         ouptvals = task.output_values.strip().split("/br")
#                         listoutput = []
#                         for i in range(len(ouptvals)):
#                             listoutput.append(list(map(str, ouptvals[i].strip().split())))
#                         more = True
#                         b = False
#                     # Создаем "текст" который будем подовать в полученую программу
#                     else:
#                         target = task.input_values.strip()
#                         answer = list(map(str, task.output_values.strip().split()))
#                         more = False
#                     # Запускаем циклом если несколько запусков
#                     if more:
#                         for i in range(len(listoutput)):
#                             try:
#                                 checkruncode = subprocess.run(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(inptvals[i].strip(), encoding='utf8'), timeout=1)
#                                 if checkruncode.returncode == 0:
#                                     runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(inptvals[i].strip(), encoding='utf8'), timeout=1)
#                                     if listoutput[i] == list(map(str, runcode.decode(encoding).strip().split())):
#                                         print('fff')
#                                     else:
#                                         atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = f'Не верный ответ, запуск {i+1}', hidden = False)
#                                         detuser = comp.determined_users.filter(user=request.user)
#                                         print(detuser.exists())
#                                         print(detuser)
#                                         if detuser.exists():
#                                             detuserx = detuser[0].task.filter(task=task)
#                                             print(detuserx.exists())
#                                             print(detuserx)
#                                             if detuserx.exists():
#                                                 print('dobavil')
#                                                 detuserx[0].attempts.add(atmpt)
#                                             else:
#                                                 print('sozdal i dobavil')
#                                                 atmpttsk = AttemptTask.objects.create()
#                                                 atmpttsk.task.add(task)
#                                                 atmpttsk.attempts.add(atmpt)
#                                                 detuser[0].task.add(atmpttsk)
#                                         else:
#                                             print('nebilo')
#                                             atmpttsk = AttemptTask.objects.create()
#                                             atmpttsk.task.add(task)
#                                             atmpttsk.attempts.add(atmpt)
#                                             dtmd = Determined.objects.create()
#                                             dtmd.user.add(request.user)
#                                             dtmd.task.add(atmpttsk)
#                                             comp.determined_users.add(dtmd)
#                                         break
#                                 else:
#                                     atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы', hidden = False)
#                                     detuser = comp.determined_users.filter(user=request.user)
#                                     print(detuser.exists())
#                                     print(detuser)
#                                     if detuser.exists():
#                                         detuserx = detuser[0].task.filter(task=task)
#                                         print(detuserx.exists())
#                                         print(detuserx)
#                                         if detuserx.exists():
#                                             print('dobavil')
#                                             detuserx[0].attempts.add(atmpt)
#                                         else:
#                                             print('sozdal i dobavil')
#                                             atmpttsk = AttemptTask.objects.create()
#                                             atmpttsk.task.add(task)
#                                             atmpttsk.attempts.add(atmpt)
#                                             detuser[0].task.add(atmpttsk)
#                                     else:
#                                         print('nebilo')
#                                         atmpttsk = AttemptTask.objects.create()
#                                         atmpttsk.task.add(task)
#                                         atmpttsk.attempts.add(atmpt)
#                                         dtmd = Determined.objects.create()
#                                         dtmd.user.add(request.user)
#                                         dtmd.task.add(atmpttsk)
#                                         comp.determined_users.add(dtmd)
#                             except subprocess.TimeoutExpired as e:
#                                 atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение', hidden = False)
#                                 detuser = comp.determined_users.filter(user=request.user)
#                                 print(detuser.exists())
#                                 print(detuser)
#                                 if detuser.exists():
#                                     detuserx = detuser[0].task.filter(task=task)
#                                     print(detuserx.exists())
#                                     print(detuserx)
#                                     if detuserx.exists():
#                                         print('dobavil')
#                                         detuserx[0].attempts.add(atmpt)
#                                     else:
#                                         print('sozdal i dobavil')
#                                         atmpttsk = AttemptTask.objects.create()
#                                         atmpttsk.task.add(task)
#                                         atmpttsk.attempts.add(atmpt)
#                                         detuser[0].task.add(atmpttsk)
#                                 else:
#                                     print('nebilo')
#                                     atmpttsk = AttemptTask.objects.create()
#                                     atmpttsk.task.add(task)
#                                     atmpttsk.attempts.add(atmpt)
#                                     dtmd = Determined.objects.create()
#                                     dtmd.user.add(request.user)
#                                     dtmd.task.add(atmpttsk)
#                                     comp.determined_users.add(dtmd)
#                                 break
#                         else:
#                             if not b:
#                                 # Считаем сколько получилось поинтов за задание
#                                 timeleft = comp.duration - int((now() - comp.start_time).total_seconds() // 60)
#                                 x = timeleft / comp.duration
#                                 h = 1
#                                 k = 0.4
#                                 y = h * x
#                                 if y > 1:
#                                     y = 1
#                                 elif y < k:
#                                     y = k
#                                 # Добавляем попытку в бд
#                                 atmpt = Attempt.objects.create(time = now(), points = round(task.score*y), successfully = True, error = '-', hidden = False)
#                                 detuser = comp.determined_users.filter(user=request.user)
#                                 print(detuser.exists())
#                                 print(detuser)
#                                 if detuser.exists():
#                                     detuserx = detuser[0].task.filter(task=task)
#                                     print(detuserx.exists())
#                                     print(detuserx)
#                                     if detuserx.exists():
#                                         print('dobavil')
#                                         detuserx[0].attempts.add(atmpt)
#                                     else:
#                                         print('sozdal i dobavil')
#                                         atmpttsk = AttemptTask.objects.create()
#                                         atmpttsk.task.add(task)
#                                         atmpttsk.attempts.add(atmpt)
#                                         detuser[0].task.add(atmpttsk)
#                                 else:
#                                     print('nebilo')
#                                     atmpttsk = AttemptTask.objects.create()
#                                     atmpttsk.task.add(task)
#                                     atmpttsk.attempts.add(atmpt)
#                                     dtmd = Determined.objects.create()
#                                     dtmd.user.add(request.user)
#                                     dtmd.task.add(atmpttsk)
#                                     comp.determined_users.add(dtmd)
#                                 print(True)
#                     # Иначе запускаем одним разом
#                     elif not more:
#                         try:
#                             checkruncode = subprocess.run(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'), timeout=1)
#                             if checkruncode.returncode == 0:
#                                 runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'), timeout=1)
#                                 if answer == list(map(str, runcode.decode(encoding).strip().split())):
#                                     # Считаем сколько получилось поинтов за задание
#                                     timeleft = comp.duration - int((now() - comp.start_time).total_seconds() // 60)
#                                     x = timeleft / comp.duration
#                                     h = 1
#                                     k = 0.4
#                                     y = h * x
#                                     if y > 1:
#                                         y = 1
#                                     elif y < k:
#                                         y = k
#                                     # Добавляем попытку в бд
#                                     atmpt = Attempt.objects.create(time = now(), points = round(task.score*y), successfully = True, error = '-', hidden = False)
#                                     detuser = comp.determined_users.filter(user=request.user)
#                                     print(detuser.exists())
#                                     print(detuser)
#                                     if detuser.exists():
#                                         detuserx = detuser[0].task.filter(task=task)
#                                         print(detuserx.exists())
#                                         print(detuserx)
#                                         if detuserx.exists():
#                                             print('dobavil')
#                                             detuserx[0].attempts.add(atmpt)
#                                         else:
#                                             print('sozdal i dobavil')
#                                             atmpttsk = AttemptTask.objects.create()
#                                             atmpttsk.task.add(task)
#                                             atmpttsk.attempts.add(atmpt)
#                                             detuser[0].task.add(atmpttsk)
#                                     else:
#                                         print('nebilo')
#                                         atmpttsk = AttemptTask.objects.create()
#                                         atmpttsk.task.add(task)
#                                         atmpttsk.attempts.add(atmpt)
#                                         dtmd = Determined.objects.create()
#                                         dtmd.user.add(request.user)
#                                         dtmd.task.add(atmpttsk)
#                                         comp.determined_users.add(dtmd)
#                                     print(True)
#                                 else:
#                                     atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Не верный ответ, запуск 1', hidden = False)
#                                     detuser = comp.determined_users.filter(user=request.user)
#                                     print(detuser.exists())
#                                     print(detuser)
#                                     if detuser.exists():
#                                         detuserx = detuser[0].task.filter(task=task)
#                                         print(detuserx.exists())
#                                         print(detuserx)
#                                         if detuserx.exists():
#                                             print('dobavil')
#                                             detuserx[0].attempts.add(atmpt)
#                                         else:
#                                             print('sozdal i dobavil')
#                                             atmpttsk = AttemptTask.objects.create()
#                                             atmpttsk.task.add(task)
#                                             atmpttsk.attempts.add(atmpt)
#                                             detuser[0].task.add(atmpttsk)
#                                     else:
#                                         print('nebilo')
#                                         atmpttsk = AttemptTask.objects.create()
#                                         atmpttsk.task.add(task)
#                                         atmpttsk.attempts.add(atmpt)
#                                         dtmd = Determined.objects.create()
#                                         dtmd.user.add(request.user)
#                                         dtmd.task.add(atmpttsk)
#                                         comp.determined_users.add(dtmd)
#                                         for l in comp.objects.all():
#                                             if l == task:
#                                                 continue
#                                             else:
#                                                 atmpt1 = Attempt.objects.create(time = now(), points = 0, successfully = False, error = '-', hidden = True)
#                                                 user = comp.determined_users.get(user = request.user)
#                                                 atmpttsk1 = AttemptTask.objects.create()
#                                                 atmpttsk1.task.add(l)
#                                                 atmpttsk1.attempts.add(atmpt1)
#                                                 user.task.add(atmpttsk)
#                             else:
#                                 atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы', hidden = False)
#                                 detuser = comp.determined_users.filter(user=request.user)
#                                 print(detuser.exists())
#                                 print(detuser)
#                                 if detuser.exists():
#                                     detuserx = detuser[0].task.filter(task=task)
#                                     print(detuserx.exists())
#                                     print(detuserx)
#                                     if detuserx.exists():
#                                         print('dobavil')
#                                         detuserx[0].attempts.add(atmpt)
#                                     else:
#                                         print('sozdal i dobavil')
#                                         atmpttsk = AttemptTask.objects.create()
#                                         atmpttsk.task.add(task)
#                                         atmpttsk.attempts.add(atmpt)
#                                         detuser[0].task.add(atmpttsk)
#                                 else:
#                                     print('nebilo')
#                                     atmpttsk = AttemptTask.objects.create()
#                                     atmpttsk.task.add(task)
#                                     atmpttsk.attempts.add(atmpt)
#                                     dtmd = Determined.objects.create()
#                                     dtmd.user.add(request.user)
#                                     dtmd.task.add(atmpttsk)
#                                     comp.determined_users.add(dtmd)
#                         except subprocess.TimeoutExpired as e:
#                             atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение', hidden = False)
#                             detuser = comp.determined_users.filter(user=request.user)
#                             print(detuser.exists())
#                             print(detuser)
#                             if detuser.exists():
#                                 detuserx = detuser[0].task.filter(task=task)
#                                 print(detuserx.exists())
#                                 print(detuserx)
#                                 if detuserx.exists():
#                                     print('dobavil')
#                                     detuserx[0].attempts.add(atmpt)
#                                 else:
#                                     print('sozdal i dobavil')
#                                     atmpttsk = AttemptTask.objects.create()
#                                     atmpttsk.task.add(task)
#                                     atmpttsk.attempts.add(atmpt)
#                                     detuser[0].task.add(atmpttsk)
#                             else:
#                                 print('nebilo')
#                                 atmpttsk = AttemptTask.objects.create()
#                                 atmpttsk.task.add(task)
#                                 atmpttsk.attempts.add(atmpt)
#                                 dtmd = Determined.objects.create()
#                                 dtmd.user.add(request.user)
#                                 dtmd.task.add(atmpttsk)
#                                 comp.determined_users.add(dtmd)
#                     # Если не верно
#                     else:
#                         print("neverno")
#                     # Удаляем файл
#                     fs.delete(file.name)
#                 # УДАЛИТЬ
#                 else:
#                     pass
#         else:
#             pass
#     if len(task.extra_text) > 0:
#         extra = True
#     else:
#         extra = False
#     timeleft = comp.duration - int((now() - comp.start_time).total_seconds() // 60)
#     x = timeleft / comp.duration
#     h = 1
#     k = 0.4
#     y = h * x
#     if y > 1:
#         y = 1
#     elif y < k:
#         y = k
#     content = {
#         'comp': comp,
#         'task': task,
#         'extra': extra,
#         'score': round(task.score*y)
#     }
#     return render(request, 'main/competition_task.html', content)

# Переписать


def Reg_page(request):
    if request.user.is_authenticated:
        return redirect('account', request.user.username)
    error_username = False
    error_email = False
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        email = request.POST.get('email')
        nickname = request.POST.get('username')
        if CustomUser.objects.filter(username=nickname).exists():
            if CustomUser.objects.filter(email=email).exists():
                error_email = True
            error_username = True
        elif CustomUser.objects.filter(email=email).exists():
            error_email = True
        elif re.search('[а-яА-Я]', nickname):
            pass
        # Если форма коректна, то она сохраняется
        elif form.is_valid():
            formsv = form.save()
            login(request, formsv)
            return redirect('you')

    form = CustomUserCreationFrom()
    content = {
        'error_username': error_username,
        'error_email': error_email
    }
    return render(request, 'main/registration.html', content)