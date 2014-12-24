from django.shortcuts import render_to_response
from .models import Entry
from random import shuffle
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from forms import searchForm

def home(request):
    ## Three random articles
    entry = Entry.objects.all()
    entr = []
    if entry.exists():
        t = range(len(entry))
        shuffle(t)
        entr.append(entry[t[0]])
        if len(t) > 1:
            entr.append(entry[t[1]])
        if len(t) > 2:
            entr.append(entry[t[2]])
    
    form = searchForm()
    context = {'entry':entr,'form':form}
    return render_to_response('home.html',context)



def homeredirect(request):
    return redirect('/home/')



def blog(request,entrynumber):
    
    #if len(entrynumber) != 8:
    #    return render_to_response('404.html')
    #
    #param_1 = int(str(entrynumber)[0:2])
    #param_2 = int(str(entrynumber)[2:4])
    #param_3 = int(str(entrynumber)[4:8])
    #
    #try:
    #    param = date(param_3,param_2,param_1)
    #except:
    #    return render_to_response('404.html')
    
    entry = Entry.objects.filter(hashval=entrynumber)
    form = searchForm()
    help_text = "Looks like you have come to the wrong place."
    context = {'entry':entry,'form':form,'help_text':help_text}
    
    if entry.exists():
        return render_to_response('blog.html',context)
    else:
        return render_to_response('404.html',context)



@csrf_exempt
def search(request,search_term):
    form =searchForm()
    if request.method == 'GET':
        form = searchForm(request.GET)
        
        if form.is_valid():
            search_result = Entry.objects.filter(content__icontains=form.cleaned_data['search_term'])
            help_text = "No entries found for the search term: " + str(form.cleaned_data['search_term'])
            form = searchForm()
            context = {'entry':search_result,'form':form,'help_text':help_text}
            
            if search_result.exists():
                return render_to_response('search_results.html',context)
            else:
                return render_to_response('404.html',context)
    
    return redirect('/home/') # Empty Search
        
    
def about(request):
    form = searchForm()
    context = {'form':form}
    return  render_to_response('about.html',context)




def archive(request):
    entry = Entry.objects.all()
    form = searchForm()
    context = {'entry':entry,'form':form}
    return render_to_response("archive.html",context)



def _404_(request):
    form = searchForm()
    context = {'form':form}
    return render_to_response('404.html',context)
