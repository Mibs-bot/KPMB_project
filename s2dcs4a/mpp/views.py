from django.shortcuts import render
from mpp.models import Programme
from mpp.models import mentor
from mpp.models import Student

# Create your views here.
#function def kat sini kena ada dulu baru boleh letak dkt urls.py
def index(request): 
    myProgramme = Programme.objects.all().values()
    mymentor = mentor.objects.all().values()
    context={
        'studentname':' fitry',
        'myProgramme': myProgramme,
        'myMentor':mymentor, 
    }
    return render(request, 'index.html',context)

def mymentor(request):
    displaydata = mentor.objects.all().values()
    if request.method == 'POST':
        mentorcode1 = request.POST['mentorcode']
        mentorname1 = request.POST['mentorname']
        mentoraccdate1 = request.POST['mentoraccdate']
        data = mentor(mentorcode=mentorcode1, mentorname=mentorname1, mentoraccdate=mentoraccdate1)
        data.save()

        context = {
            'displaydata' : displaydata,
            'message' : 'NEW MENTOR HAS BEEN SAVE'
        }

        return render(request, 'mymentor.html',context)
    else:
        dict = {
            'message':'',
            'displaydata':displaydata,

        }
    return render(request, 'mymentor.html',dict)


def mystudent(request):

    stumentor1 = Student.objects.all().values()
    mymentor = mentor.objects.all().values()

    if request.method == 'POST':
        studentid1 = request.POST['studentid']
        studentname1 = request.POST['studentname']
        studentemail1 = request.POST['studentemail']
        studentage1 = request.POST['studentage']
        mentorcode1 = request.POST['mentorcode']
        mentornew = mentor.objects.get(mentorcode = mentorcode1)
        data = Student(studentid = studentid1, studentname = studentname1, studentemail = studentemail1, studentage = studentage1, mentorcode1 = mentornew)
        data.save()

        context = {
            'stumentor1' : stumentor1,
            'mymentor' : mymentor,
            'message' : 'NEW MENTOR HAS BEEN SAVE'
        }

        return render(request, 'mystudent.html',context)
    else:
        dict = {
            'stumentor1' : stumentor1,
            'mymentor' : mymentor,
            'message' : 'page is refreshed'

        }
    return render(request, 'mystudent.html',dict)

def viewdelete(request,menid):
    datanakdelete=mentor.objects.get(menid=menid)
    dict={
        'datatobedeleted':datanakdelete
    }
    return render(request,"delete.html",dict)

            
         




