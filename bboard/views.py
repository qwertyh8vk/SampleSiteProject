from django.shortcuts import render, HttpResponse
from . models import Bb


def index(request):
    s =  'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type = 'text/plain; charset=utf-8')

def main_page(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'bboard/templates/index.html', {'bbs': bbs})

def home_page(request):
    return HttpResponse("Hello World!")

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/templates/by_rubric.html', context)