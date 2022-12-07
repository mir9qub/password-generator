from django.shortcuts import render
from random import choice
# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'title':'Password Generator'})


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 8))
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialchars'):
        chars.extend(list('`~!@#$%^&*()'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    password = ''

    while length:
        password += choice(chars)

        length -= 1

    return render(request, 'generator/password.html', {'title': 'Your password', 'password': password})
