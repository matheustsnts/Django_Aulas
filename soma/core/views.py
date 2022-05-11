from django.shortcuts import render, HttpResponse

# Create your views here.

def calculo(request, op, num1,num2):

    if (op == 'adição'):
        res = num1 + num2
        return HttpResponse(f'<h1>{res}</h1>')
    elif (op == 'subtração'):
        res = num1 - num2
        return HttpResponse(f'<h1>{res}</h1>')
    elif (op == 'multiplicação'):
        res = num1 * num2
        return HttpResponse(f'<h1>{res}</h1>')
    elif (op == 'divisão'):
        res = num1 / num2
        return HttpResponse(f'<h1>{res}</h1>')
    else:
        return HttpResponse('<h1>Você digitou a operação errada, cowboy.</h1>')