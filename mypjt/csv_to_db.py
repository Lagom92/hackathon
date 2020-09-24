# csv 파일을 db에 저장하기
import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypjt.settings")
django.setup()

from boards.models import Landmark
from boards.models import Comment

def getLandmark(landmark_path):
    hand = open(landmark_path, encoding='UTF8')
    reader = csv.reader(hand)

    bulk_list = []
    next(reader)
    for row in reader:
        bulk_list.append(Landmark(
            country = row[0],
            name = row[1],
            photo = row[2],
        ))

    Landmark.objects.bulk_create(bulk_list)

    return True


def getcomment(comment_path):
    hand = open(comment_path, encoding='UTF8')
    reader = csv.reader(hand)

    bulk_list = []
    next(reader)
    for row in reader:
        try:
            bulk_list.append(Comment(
                landmark = Landmark.objects.get(name=row[1]),
                title = row[2],
                contents = row[3],
            ))

        except:
            pass

    Comment.objects.bulk_create(bulk_list)

    return True


comment_file_lst = os.listdir('./data/comment')
country_file_lst = os.listdir('./data/country')
print(comment_file_lst)
print(country_file_lst)

for file in country_file_lst:
    path = './data/country/' + file
    getLandmark(path)

for file in comment_file_lst:
    path = './data/comment/' + file
    getcomment(path)