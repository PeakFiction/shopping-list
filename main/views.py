from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Muhammad Sakhran',
        'class': 'PBP KI'
    }

    return render(request, 'main.html', context)