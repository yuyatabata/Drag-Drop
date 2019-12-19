from django.shortcuts import get_object_or_404,redirect,render
from django.contrib.auth.models import User
from .models import Image
from .forms import ImageForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            messages.success(request, "投稿が完了しました！")
        return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form':form})
