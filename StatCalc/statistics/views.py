# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import stat_func

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def calculate(request):
    query = request.GET.get('q')
    output=[0]*10

    if query is None or len(query) == 0: 
        output[9] = 1                                    #No input case
        return render_to_response("stat_html.html", {
             "results": output,
             "query": query
              })

    string = []
    if(query is not None):
        string = query.split(",")


    string = query.split(',')
    error=0
    try:
        string = [float(x) for x in string]
    except Exception as e:
        error = error+1

    if error == 1:
        output[9]=1
        return render_to_response("stat_html.html", {
             "results": output,
             "query": query
              })

    output = stat_func.calc(string)
    output.append(2)


    return render_to_response("stat_html.html", {
             "results": output,
             "query": query
              })