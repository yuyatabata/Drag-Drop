from django.shortcuts import get_object_or_404,redirect,render
from .models import Image
from django.contrib import messages
import os


# Create your views here.
def index(request):
    fname = '../dragdrop/images/testfiles.jpg'
    if request.method == "POST":
        updata = request.FILES.get('image')
        print("updata:",updata)
        print("FILES:",request.FILES)
        print("POST:",request.POST)
        print("path:",request.path)
        f = open(fname,'wb+')
        print("f:",f)
        # form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        if updata != None:
            for chunk in updata.chunks():
                f.write(chunk)
                print("f",f)
            f.close()
            img = Image()
            img.image_f = f
            print(img.image_f.url)
            images = img.objects.all().order_by("-created_at")
        return render(request, 'index.html', {'images':images})
    else:
        # form = ImageForm()
        # images = Image.objects.all()
        # return render(request, 'index.html', {'form':form ,'images':images})
        return render(request, 'index.html')
