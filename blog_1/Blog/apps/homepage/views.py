from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.homepage.forms import ContactForm
from apps.data.models import Entry
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required ## To ensure that the user is logged in


def index(request):
    entries = Entry.objects.published_entries()
    context = {'entries':entries}
    return render_to_response('homepage/index.html',context)


def about(request):
    return render_to_response('homepage/about.html')

## @csrf_exempt for having Cross Site Request Forgery protection disabled
def contact(request):
    success = False
    email = ""
    title = ""
    text = "" 
    contact_sent = request.session.get('contact_sent', False) ## This needs to be understood
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']
            request.session["contact_sent"] = True
    
    else:
        contact_form = ContactForm()
        
    ctx = {'contact_form':contact_form, 'email':email, 'title':title, 'text':text,'success':success,'contact_sent':contact_sent}
        
    return render_to_response('homepage/contact.html',ctx,context_instance=RequestContext(request))



def archive(request):
    return render_to_response('homepage/archive.html')



@login_required
def profile(request):
    ctx = {}
    return render_to_response('homepage/profile.html',ctx,context_instance=RequestContext(request))
