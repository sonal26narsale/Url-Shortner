from django.shortcuts import redirect, render
from django.http import HttpResponse
from root.models import Url
# Created my views here.

def createUrl(req):
    if req.method == "POST":
        full_url = req.POST.get('full_url') 
        obj = Url.create(full_url)
        return render(req, 'root/index.html', {
        'full_url': obj.full_url,
        'short_url': req.get_host() + '/'+obj.short_url
        })
    
    return render(req, 'root/index.html')
      
def routeToURL (req, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except :
        return redirect(createUrl)
    # return redirect()