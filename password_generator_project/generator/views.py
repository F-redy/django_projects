from django.shortcuts import render
from random import randint, shuffle
from string import ascii_lowercase, ascii_uppercase

chars = {
    'lowercase': ascii_lowercase,
    'uppercase': ascii_uppercase,
    'numbers': '0123456789',
    'special': '!#$%&*?@',
}


def index(request):
    if request.POST:
        context = password(request)
    else:
        simbols = list(chars['lowercase'] + chars['uppercase'])
        context = {
            'title': 'Password generator',
            'passwords': [generator(12, simbols)]

        }
    return render(request, 'generator/generator.html', context=context)


def password(request):
    length = int(request.POST.get('length'), 12)
    count = int(request.POST.get('count'))
    character_set = list()

    for name_char, char in chars.items():
        if request.POST.get(name_char) == 'on':
            character_set.extend(char)
    shuffle(character_set)

    context = {
        'title': 'Password generator',
        'passwords': [generator(length, character_set) for _ in range(count)],
    }

    return context


def about(request):
    return render(request, 'generator/about.html', {'title': 'about - site'})


def generator(length: int, symbols: list[str]) -> str:
    if not symbols:
        symbols = list(ascii_lowercase)
    return ''.join(symbols[randint(0, len(symbols) - 1)] for _ in range(length))
