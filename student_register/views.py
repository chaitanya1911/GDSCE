from django.http import response
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
import datetime,jwt
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class logoutView(APIView):
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'messsage':'success'
        }
        return response

class createToken(APIView):
    def post(self,request):
        payload={
       'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=1440),
       'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        response= Response()
        response.set_cookie(key='jwt',value=token,httponly=True)

        response.data={
            'jwt':token
        }
        return response
class getRoute(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')

        if not token:
            return Response("Unauthenticated!")
        try:
            print(token)
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
            return Response(token)
        except jwt.ExpiredSignatureError:
            raise Response('Unauthenticated!')

def student_list(request):
   
   
       token=request.COOKIES.get('jwt')
       if not token:
            return response.HttpResponse("Unauthenticated!")
       try:
            division=set()
            data=Student.objects.all()
            for x in data:
                division.add(x.division)
            print(division)
            return render(request, "student_register/student_list.html", {'student_list': data,'divisions':division})
       except jwt.ExpiredSignatureError:
            raise response.HttpResponse('Unauthenticated!')
       
       
   
   


def student_form(request, id=0):
    token=request.COOKIES.get('jwt')

    if not token:
        return Response("Unauthenticated!")
    try:
        if request.method == "GET":
            if id == 0:
                form = StudentForm()
            else:
                student = Student.objects.get(pk=id)
                form = StudentForm(instance=student)
            return render(request, "student_register/student_form.html", {'form': form})
        else:
            if id == 0:
                form = StudentForm(request.POST)
            else:
                student = Student.objects.get(pk=id)
                form = StudentForm(request.POST,instance= student)
            if form.is_valid():
                form.save()
            return redirect('/student/list')
    except jwt.ExpiredSignatureError:
        raise response.HttpResponse('Unauthenticated!')
    


def student_delete(request,id):
    token=request.COOKIES.get('jwt')

    if not token:
        return response.HttpResponse("Unauthenticated!")
    try:
        student = Student.objects.get(pk=id)
        student.delete()
        return redirect('/student/list')
    except jwt.ExpiredSignatureError:
        raise response.HttpResponse('Unauthenticated!')
    

