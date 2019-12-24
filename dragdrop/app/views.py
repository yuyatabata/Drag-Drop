from django.shortcuts import get_object_or_404,redirect,render
# from .models import Image
# from .forms import ImageForm
from django.contrib import messages
from PIL import Image
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
        # form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        if updata != None:
            for chunk in updata.chunks():
                f.write(chunk)
                print("f",f)
            f.close()
            # image = Image.open(f)
            # temp_image = open(os.path.join('/tmp',filename), 'w')
            # image.save(temp_image, 'JPEG')
            # print("image:",image)

            # messages.success("投稿が完了しました！")
            # images = Image.objects.all()
        return render(request, 'index.html', {'f':f})
    else:
        # form = ImageForm()
        # images = Image.objects.all()
        # return render(request, 'index.html', {'form':form ,'images':images})
        return render(request, 'index.html')