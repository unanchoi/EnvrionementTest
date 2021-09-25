from django.shortcuts import render
from django.http import HttpResponse, HttpResponse
from django.urls import reverse
from .models import Question, Embti, Choice, Result

# Create your views here.

count = 0
result5 = 1
result4 = 1
result3 = 1
result2 = 1
result1 = 1

def index(request):
    global count # 바깥영역의 변수를 사용할 때 global
    count = count + 1 # 접속할 때마다 방문자 1 증가
    
    return render(request, 'index.html', {'cnt': count})

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'form.html', context=context)


def result(request):
    print(f'POST : {request.POST}')
    global result5
    global result4
    global result3
    global result2
    global result1

    per = 0
    sum = 0

    for i in range(10):
        j = str(i+1)
        sum += int(request.POST['question-'+j])
        
        
    if sum == 10:
        result5 = result5 +1
        per = round((count / result5) * 100, 2)
        return render(request, 'result5.html', {'per' : per})
    elif 8 <= sum and sum <= 9:
        result4 = result4 +1
        per = round((count / result4) * 100, 2)
        return render(request, 'result4.html', {'per' : per})
    elif 6 <= sum and sum <= 7:
        result3 = result3 +1
        per = round((count / result3) * 100, 2)
        return render(request, 'result3.html', {'per' : per})
    elif 3 <= sum and sum <= 5:
        result2 = result2 +1
        per = round((count / result2) * 100, 2)
        return render(request, 'result2.html', {'per' : per})
    else:
        result1 = result1 +1
        per = round((count / result1) * 100, 2)
        return render(request, 'result1.html', {'per' : per})
    
    # if request.method == 'POST':
    #     post = Result()


def loading(request):
    return render(request, 'loading_page.html')