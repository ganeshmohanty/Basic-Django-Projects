from django.shortcuts import render
from .froms import StudentForm
from .models import Student
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    form = StudentForm()
    stu = Student.objects.all()
    return render(request,'home.html',{'form':form,'stu':stu})

#@csrf_exempt
def save(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('sid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (sid == ''):
                usr = Student(name=name,email=email,password=password)
            else:
                usr = Student(id=sid,name=name,email=email,password=password)
            usr.save()
            stud=Student.objects.values()
            #print(stud)
            student=list(stud)
            return JsonResponse({'status':'save','student':student})
        else:
            return JsonResponse({'status':'error'})


def delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        user = Student.objects.get(pk=id)
        user.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



def edit(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        stu = Student.objects.get(pk=id)
        sd = {"id":stu.id,"name":stu.name,"email":stu.email,"password":stu.password}
        return JsonResponse(sd)
    else:
        return JsonResponse({'status':0})