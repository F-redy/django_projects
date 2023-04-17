from django.shortcuts import render
from random import randint, shuffle
from string import ascii_lowercase, ascii_uppercase

chars = {
    'lowercase': ascii_lowercase,
    'uppercase': ascii_uppercase,
    'numbers': '0123456789',
    'special': '!#$%&*+-:;?@',
}


def index(request):
    context = {
        'title': 'Password Generator',
    }
    return render(request, 'generator/index.html', context=context)


def password(request):
    length = int(request.GET.get('length'), 12)
    count = int(request.GET.get('count'))
    character_set = list()

    for name_char, char in chars.items():
        if request.GET.get(name_char) == 'on':
            character_set.extend(char)
    shuffle(character_set)

    context = {
        'title': 'Your Password',
        'passwords': [generator(length, character_set) for _ in range(count)],
    }

    return render(request, 'generator/passwords.html', context=context)


def generator(length: int, symbols: list[str]) -> str:
    if not symbols:
        symbols = list(ascii_lowercase)
    return ''.join(symbols[randint(0, len(symbols) - 1)] for _ in range(length))
