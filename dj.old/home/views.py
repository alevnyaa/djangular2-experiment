from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    h1 = 'Selam, Alev'
    paragraph = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum suscipit metus sit amet augue viverra condimentum ut at ipsum. '
    return render(request,'index.html', {'h1': h1, 'paragraph': paragraph})
