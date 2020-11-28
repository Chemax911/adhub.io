from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


# def home(request):
#     if request.method == 'POST':
#         return HttpResponse('Hi')
#     elif request.method == 'GET':
#         return HttpResponse('Good')


class HomeView(View):
    def get(self, request):
        return render(request, 'catalog/home.html')

