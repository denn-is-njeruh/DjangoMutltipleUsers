from django.shortcuts import redirect, render
from customusers.models import user_type

# Create your views here.
def shome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return render(request,'student_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return redirect('thome')
    else:
        return redirect('login')
