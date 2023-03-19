from django.shortcuts import render, HttpResponse
from . models import Bb
from . models import Rubric

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/templates/index.html', context)

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