from django.shortcuts import render
# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306240143',
        'name': 'Muhammad Rizky Ramadhani',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
