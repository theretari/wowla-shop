from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'owala',
        'price': '800000',
        'description': 'FreeSip water bottle'
    }

    return render(request, "main.html", context)