from django.http import request
from django.shortcuts import render, redirect
from .models import Landmark, Comment

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


