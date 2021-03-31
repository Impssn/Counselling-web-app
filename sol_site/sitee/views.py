from django.shortcuts import render
from . models import comments

# Create your views here.

def home(request):
    return render(request,"home.html")

def titles(request):
    return render(request,"titl.html")

def choose(request):
    ch=request.POST.get("choosetitl")
    if(ch=="forced"):
       return render(request,"forc.html")
    elif(ch=="finance"): 
       return render(request,"fin.html")
    elif(ch=="fitness"):
       return render(request,"fit.html")
    elif(ch=="love"):
       return render(request,"luv.html")
    elif(ch=="discrimination"):
       return render(request,"disc.html")
    elif(ch==None):
       return render(request,"titl.html")
   
def discget(request):
   dch=request.POST.get("dget")
   if(dch=="edu"):
      return render(request,"edu.html")
   elif(dch=="office"):
      return render(request,"offi.html")
   elif(dch==None):
      return render(request,"disc.html")

def luvget(request):
   lch=request.POST.get("lget")
   if(lch=="l20"):
      return render(request,"lt.html")
   elif(lch==None):
       return render(request,"luv.html")
   else:
      return render(request,"gt.html")

def fitget(request):
   fch=request.POST.get("fget")
   if(fch=="deadly"):
      return render(request,"dead.html")
   elif(fch==None):
       return render(request,"fit.html")
   else:
      return render(request,"long.html")

def finget(request):
   fich=request.POST.get("figet")
   if(fich=="debt"):
      return render(request,"debt.html")
   elif(fich==None):
       return render(request,"fin.html")
   else:
      return render(request,"lmy.html")

def forcget(request):
   frget=request.POST.get("fcget")
   if(frget=="kid"):
      return render(request,"kid.html")
   elif(frget== None):
       return render(request,"forc.html")
   elif(frget=="marry"):
      return render(request,"marry.html")
   else:
      return render(request,"carr.html")

def gtch(request):
   gtchh=request.POST.get("hty")
   if(gtchh=="bkup"):
      return render(request,"brkup.html")
   elif(gtchh==None):
       return render(request,"gt.html")
   else:
      return render(request,"misud.html")

def per(request):
   perr1=request.POST["cmt1"]
   perr2=request.POST["cmt2"]
   obj=comments()
   obj.email=perr1
   obj.comment=perr2
   obj.save()
   return render(request,"home.html")
