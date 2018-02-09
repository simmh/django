from django.shortcuts import render

# Create your views here.


def serve_html(request, path):
    return render(request, path)


def index(request, message=None):
    return render(request, 'index.html')


def post_detail_view(request, pk):
  return render(request, 'v1/app/board_create.html')

