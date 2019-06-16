"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Наши контакты',
            'year':datetime.now().year,
        })

def product(request, index):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    if (index == 1):
        title = "Регулируемые источники питания";
        message = title;
        content = "app/products/rip.html";
        image1 = "RegIstPit.jpg";
        image2 = "";
    if (index == 2):
        title = "СКЗ Протрон";
        message = title;
        content = "app/products/skz.html";
        image1 = "skz.png";
        image2 = "skz2.png";
    if (index == 3):
        title = "Для монтажа в 19\" стойку";
        message = title;
        content = "app/products/19.html";
        image1 = "19.png";
        image2 = "";
    return render(request,
        'app/product.html',
        {
            'title': title,
            'message': message,
            'content': content,
            'image1': image1,
            'image2': image2,
            'year':datetime.now().year,
        })

def complicted(request):
    """Renders the complicted page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/complicted.html',
        {
            'title':'Реализованные проекты',
            'message':'Реализованные проекты',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Информация о компании',
            'year':datetime.now().year,
        })
