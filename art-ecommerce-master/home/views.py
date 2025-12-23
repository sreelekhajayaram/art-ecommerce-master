from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from newsposts.models import NewsPost
from products.models import Product


def index(request):
    """
    get the most recents articles (posts) and the most recent products,
    sorted by date and return them to the index.html file
    """
    posts = NewsPost.objects.filter(published_date__lte=timezone.now
        ()).order_by('-published_date')

    products = Product.objects.filter(upload_date__lte=timezone.now
                ()).order_by('-upload_date')
    context = {'posts': posts, 'products': products}
    return render(request, 'index.html', context)


def contact_view(request):
    """Return the contact.html file on request"""
    return render(request, 'contact.html')


def contact_form(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        if name and email and subject and message:
            # Here you would typically send an email or save to database
            # For now, we'll just show a success message
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return render(request, 'contact.html')
        else:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'contact.html')
    
    return render(request, 'contact.html')


def faq(request):
    """Return the faq.html file on request"""
    return render(request, 'faq.html')


def about(request):
    """Return the about.html file with artist information"""
    return render(request, 'about.html')
