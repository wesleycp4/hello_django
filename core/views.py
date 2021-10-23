from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'.format(nome, idade))

def soma(request, num_1, num_2):
    resultado = num_1+num_2
    return HttpResponse('O Resultado de {} + {} é {}'.format(num_1,num_2,resultado))

def subtracao(request, num_1, num_2):
    resultado = num_1-num_2
    return HttpResponse('O Resultado de {} - {} é {}'.format(num_1,num_2,resultado))

def multiplicacao(request, num_1, num_2):
    resultado = num_1*num_2
    return HttpResponse('O Resultado de {} * {} é {}'.format(num_1,num_2,resultado))

def divisao(request, num_1, num_2):
    #Trata divisão por zero
    if num_2 == 0:
        return HttpResponse('Informe um numero diferente de 0!')
    else:
        resultado = num_1/num_2
        return HttpResponse('O Resultado de {} / {} é {}'.format(num_1,num_2,resultado))
