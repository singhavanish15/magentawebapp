from urllib import response
from django.shortcuts import render, HttpResponse
from home.models import person, gallery1, gallery_subitem
import requests
# Create your views here.
def home (request):
   #return HttpResponse('this is home')
   resp1 = requests.get("http://125.63.74.18:67/api/values")
   resp = resp1.json()
   return render(request, 'home.html', {'resp':resp})

#def api (request):
   resp1 = requests.get("http://125.63.74.18:67/api/values")
   resp = resp1.json()
   print(resp)
   return render(request, 'api.html', {'resp':resp})

def about (request):
   #return HttpResponse('this is about')
    return render(request, 'about.html')


def team (request):
   #return HttpResponse('this is about')
    return render(request, 'team.html')

def gallery (request):
  
   gall_subitem = gallery_subitem.objects.filter(gallery_ty= ga)


   gallery_con = gallery1.objects.all()
   data={
      'gallery_con':gallery_con,
      'gall_subitem':gall_subitem
   }
   print(gall_subitem)
   print(gallery_con)
   print(data)
   return render(request, 'gallery.html',data)
    
def services (request):
  # return HttpResponse('this is services')
    return render(request, 'services.html')

def contact(request):
   if request.method=="POST":
      name1=request.POST['name']
      email1=request.POST['email']
      messagge1=request.POST['messagge']
      ins = person(name=name1, email=email1, messagge= messagge1)
      ins.save()
      

   return render(request, 'contact.html')