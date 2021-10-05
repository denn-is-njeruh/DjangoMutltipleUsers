from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import user_type, User

# Create your views here.
def signup(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        st = request.POST.get('student')
        te = request.POST.get('teacher')

        user = User.objects.create_user(email=email,)
        user.set_password(password)
        user.save()

        usert = None
        if st:
            usert = user_type(user=user, is_student=True,)
        elif te:
            usert = user_type(user=user, is_teach=True)
        
        usert.save()
        return redirect('home')
    return render(request, 'registration/register.html')


def login(request):
    if(request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_student:
                return redirect('shome') #Navigate to student homepage
            elif user.is_authenticated and type_obj.is_teach:
                return redirect('thome') #Navigate to teacher homepage
        else:
            return redirect('home')

    return render(request, 'index.html')
