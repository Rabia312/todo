from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Bookhouse

# Create your views here.

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def homework31(request):
    return render(request, "homework31.html")

def books(request):
    book_list = Bookhouse.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book = Bookhouse(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)