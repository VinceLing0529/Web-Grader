from django.shortcuts import render
from .forms import NewStudentForm
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def studentlogin(request):
    return render(request,'main/studentlogin.html')

def teacherlogin(request):
    return render(request,'main/teacherlogin.html')


def signup(request):
    form = NewStudentForm()

    if request.method == "POST":
        form = NewStudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'main/signup.html',{'form':form})
