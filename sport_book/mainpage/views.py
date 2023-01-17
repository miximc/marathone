from django.shortcuts import render
import random
def index(request):
    context = {
        'nomer_okowko': 25,
        'phone': 2,
        'slovar': [1,2,3,4,5,6]}

    return render(
        request,                # Запрос
        'mainpage/index.html',
        context,                 # подстановки


    )


