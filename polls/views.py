from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'context_text': "Hello World"
    }
    
    return render(request, 'polls/index.html', context)
