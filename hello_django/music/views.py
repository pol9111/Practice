from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def music2(request):
    str1 = 'THIS IS MY UMBRELLA'
    int1 = 12
    format_string = '%Y-%m-%d %H:%M:%P'
    lst = [1, 2, 3]
    return render(request, 'music2.html',
                  context={
                      'str1': str1,
                      'int1': int1,
                      'format_string': format_string,
                      'lst': lst,
                  })

