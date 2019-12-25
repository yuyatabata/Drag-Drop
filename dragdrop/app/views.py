from django.shortcuts import get_object_or_404,redirect,render
from .models import Image
from django.contrib import messages
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    # fname = '../dragdrop/images/testfiles.jpg'
    if request.method == "POST":
        updata = request.FILES['image']
        print("updata:",updata)
        print("FILES:",request.FILES)
        print("POST:",request.POST)
        print("path:",request.path)
        # f = open(fname,'wb+')
        # print("f:",f)
        if updata != None:
            fs = FileSystemStorage()
            filename = fs.save(updata.name, updata)
            uploaded_file_url = fs.url(filename)
            # for chunk in updata.chunks():
            #     f.write(chunk)
            #     print("f",f)
            # f.close()
            img = Image()
            img.image_f = uploaded_file_url
            print(img.image_f)
            images = Image.objects.all().order_by("-created_at")
        return render(request, 'index.html', {'images':images})
    else:
        # form = ImageForm()
        # images = Image.objects.all()
        # return render(request, 'index.html', {'form':form ,'images':images})
        return render(request, 'index.html')
