from django.shortcuts import render, redirect
import smtplib
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Category, Product


# Create your views here.
# Home
def home(request):
    category = Category.objects.filter(status=0)
    products = Product.objects.filter(status=0)
    context = {'category': category, 'products': products}
    return render(request, "store/index.html", context)


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "store/collections.html", context)


def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, 'no such category found')
    return redirect('collections')


def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
        else:
            messages.error(request, "No such Product Found")
            return redirect('collections')
    else:
        messages.error(request, "No such Category Found")
        return redirect('collections')
    return render(request, 'store/products/view.html', context)


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'contact form',
            message,
            'settings.EMAIL_HOST_USER',
            ['iamquofii@gmail.com'],
            fail_silently=False)
    return render(request, "store/contact.html")


def gallery(request):
    return render(request, "store/collections.html")


def about(request):
    return render(request, "store/about_us.html")


def services(request):
    return render(request, "store/serv.html")


def test(request):
    return render(request, "store/test.html")
