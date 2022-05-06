from django.shortcuts import render
from rest_framework import generics
from que import serializers
from .models import Quiz
from django.http import HttpResponse, JsonResponse
from .forms import NumsForm
import requests


class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = serializers.QuizSerializer


class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = serializers.QuizSerializer


def send_request(request, num):
    r = requests.get(f'https://jservice.io/api/random?count={num}', data=request.GET)
    data = r.json()
    return data


def save_data(request, data):
    num_list = Quiz.objects.values_list('question_id')
    for el in data:
        if el['id'] in num_list:
            new_data = send_request(request, 1)
            save_data(request, new_data)
        else:
            quiz = Quiz()
            quiz.question_id = el['id']
            quiz.question = el['question']
            quiz.answer = el['answer']
            quiz.created_at = el['created_at']
            quiz.save()
    return


def get_questions(request):
    if 'questions_num' in request.POST:
        num = request.POST['questions_num']
        data = send_request(request, num)
        save_data(request, data)
        return render(request, 'success.html')
    return HttpResponse('Something went wrong')


def get_num_of_questions(request):
    if request.method == 'POST':
        return get_questions(request)
    else:
        form = NumsForm()
    return render(request, 'form.html', {'form': form})


def last_object(request):
    context = {}
    last_obj = Quiz.objects.last()
    if last_obj:
        context['id'] = last_obj.question_id
        context['question'] = last_obj.question
        context['answer'] = last_obj.answer
        context['created_at'] = last_obj.created_at
        return context

    return None


def view_last_obj(request):
    context = last_object(request)
    if context:
        return render(request, 'last.html', context)

    return render(request, 'no_last.html')

def get_last_obj(request):
    if request.method == 'GET':
        context = last_object(request)
        if context:
            return JsonResponse(context)
        else:
            context = {}
            return JsonResponse(context)

    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def get_q(request):
    q = request.POST.get('questions_num', False)
    if q:
        data = send_request(request, q)
        save_data(request, data)
        return render(request, 'success.html')
    
    return render(request, 'index.html')
