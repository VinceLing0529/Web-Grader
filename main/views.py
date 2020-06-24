from django.shortcuts import render
from .forms import NewStudentForm,UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def studentlogin(request):
    return render(request,'main/studentlogin.html')

def teacherlogin(request):
    return render(request,'main/teacherlogin.html')


def signup(request):


    if request.method == "POST":
        user_form = NewStudentForm(data = request.POST)
        profile_form = UserProfileInfoForm(data= request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'main/signup.html',{'form':form})
