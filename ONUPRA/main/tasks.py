from celery import Celery
from .models import Competition, Task, Attempt, ScorePoint
from django.utils.timezone import now

app = Celery('ONUPRA')

@app.task(name='foo')
def foo():
    print('Hello world!')

@app.task(name='checker')
def cheker():
    comp = Competition.objects.filter(actual = True).order_by('start_time')
    if comp:
        for i in range(len(comp)):
            timeLeft = comp[i].duration - int((now() - comp[i].start_time).total_seconds() // 60)
            if timeLeft <= 0:
                comp[i].actual = False
                comp[i].save()
                if comp[i].rating:
                    users = []
                    d1 = {}
                    max_score = 0
                    tasks = Task.objects.filter(compet = comp[i])
                    for j in tasks:
                        d0 = {}
                        max_score += j.score
                        for k in Attempt.objects.filter(link_competition = comp[i]).filter(link_task = j).filter(hidden = False):
                            if not (k.link_user in users):
                                users.append(k.link_user)
                            if not (k.link_user in d0):
                                d0[k.link_user] = k.points
                            else:
                                if d0[k.link_user] < k.points:
                                    d0[k.link_user] = k.points
                        for k in d0:
                            if not (k in d1):
                                d1[k] = d0[k]
                            else:
                                d1[k] += d0[k]
                    average_score = max_score / len(users)
                    del d0, max_score
                    # print(users)
                    for j in users:
                        if j.rating == 0:
                            # print(j.username, j.rating, d1[j], average_score, 200 * ((d1[j] / average_score - 1) / 3 + 1))
                            j.rating = 200 * ((d1[j] / average_score - 1) / 3 + 1)
                        else:
                            # print(j.username, j.rating, d1[j], average_score, j.rating * ((d1[j] / average_score - 1) / 3 + 1))
                            j.rating = j.rating * ((d1[j] / average_score - 1) / 3 + 1)
                        j.save()
                        point = ScorePoint(score = j.rating, link_user = j)
                        point.save()
            else:
                break

# @app.task(name='checker')
# def cheker():
#     comp = Competition.objects.filter(actual = True).order_by('start_time')
#     if comp:
#         for i in range(len(comp)):
#             timeLeft = comp[i].duration - int((now() - comp[i].start_time).total_seconds() // 60)
#             if timeLeft <= 0:
#                 print(f"He is dead ({i})")
#                 comp[i].actual = False
#                 comp[i].save()
#                 if comp[i].rating:
#                     user_dict = {}
#                     max_score = 0
#                     for j in comp[i].tasks.all():
#                         max_score += j.score
#                     for j in comp[i].determined_users.all():
#                         user_score = 0
#                         print(j.user.all()[0].username)
#                         for k in j.task.all():
#                             q = k.attempts.order_by('-points')
#                             print(q[0].points)
#                             user_score += q[0].points
#                             print(user_score)
#                         user_count = len(comp[i].determined_users.all())
#                         average_score = max_score / user_count
#                         user_dict[j.user.all()[0].username] = user_score
#                     for j in comp[i].determined_users.all():
#                         user = j.user.all()[0]
#                         user_score = user_dict[user.username]
#                         # place = sorted_user_dict.index(index_u)
#                         # place_coeff = (len(comp[i].determined_users.all()) - place) / len(comp[i].determined_users.all())
#                         # rating_coeff = user.rating / 5000
#                         if user.rating == 0:
#                             user.rating = 200 * ((user_score / average_score - 1) / 3 + 1)
#                         else:
#                             user.rating = user.rating * ((user_score / average_score - 1) / 3 + 1)
#                         user.save()
#             else:
#                 print(f"All okay, nearest end of competetion in {timeLeft} (UTC)")
#                 break
#     else:
#         print('the list is empty')