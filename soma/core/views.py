from django.shortcuts import render, HttpResponse

# Create your views here.

def calculo(request, op, num1,num2):

    if (op == 'adição'):
        res = num1 + num2
        return HttpResponse(f'<h1>{res}</h1>')
    if (op == 'subtração'):
        res = num1 - num2
        return HttpResponse(f'<h1>{res}</h1>')
    if (op == 'multiplicação'):
        res = num1 * num2
        return HttpResponse(f'<h1>{res}</h1>')
    if (op == 'divisão'):
        res = num1 / num2
        return HttpResponse(f'<h1>{res}</h1>')