from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306256280',
        'name': 'Damar Aryaputra Rahman',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)