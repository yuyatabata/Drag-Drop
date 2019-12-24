from django.shortcuts import get_object_or_404,redirect,render
from .models import Image
from .forms import ImageForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        f = request.FILES.get('file_upload')
        print("f:",f)
        print("FILES:",request.FILES)
        print("POST:",request.POST)
        print("path:",request.path)
        # form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        if f != None:
            image = f.save(commit=False)
            image.save()
            messages.success("投稿が完了しました！")
            images = Image.objects.all()
        return redirect(request, '/', {'images':images})
    else:
        form = ImageForm()
    images = Image.objects.all()
    return render(request, 'index.html', {'form':form ,'images':images})
