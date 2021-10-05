from django.shortcuts import redirect, render
from customusers.models import user_type

# Create your views here.
def thome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return render(request, 'teacher_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return redirect('shome')
    else: 
        return redirect('home')

