from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_phones = request.GET.get('sort', 'name')
    phones = {
        'name':Phone.objects.all().order_by('name'),
        'min_price':Phone.objects.all().order_by('price'),
        'max_price':Phone.objects.all().order_by('price').reverse()
    }
    template = 'catalog.html'

    print(phones)
    context = {
        'phones': phones[sort_phones]
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone':phone
    }
    return render(request, template, context)
