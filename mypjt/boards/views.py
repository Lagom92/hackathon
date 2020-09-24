from django.http import request
from django.shortcuts import render, redirect
from .models import Landmark, Comment
import json

def getKey():
    with open('./boards/secret.json') as file:
        key = json.load(file)
        google_key = key.get('google_key', '')
    return google_key


def main(request):
    
    return render(request, 'main.html')


def landmark(request):
    if request.method == "POST":
        country = request.POST['country']
        landmarks = Landmark.objects.filter(country__contains=country)
        if landmarks:
            context = {
                'landmarks': landmarks,
                'country': country,
            }

            return render(request, 'landmark.html', context)
        else:
            # 검색한 나라가 없으면 우선은 메인으로 이동
            return redirect('main')
        
    return redirect('main')


def detail(request, id):
    landmark = Landmark.objects.get(id=id)
    comments = landmark.comment.all()
    key = getKey()
    context = {
        'country': landmark.country,
        'photo': landmark.photo,
        'info': landmark.info,
        'landmark': landmark,
        'comments': comments,
        'key': key,
    }

    return render(request, 'detail.html', context)