from django.shortcuts import render


def bomb_timer(request):
    return render(request, 'bomb_view.html')
