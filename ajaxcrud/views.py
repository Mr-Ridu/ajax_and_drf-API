from django.shortcuts import render
from .models import employee_information
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.db.models import Q
# 
def lajax(request):
    employees = employee_information.objects.all().order_by('-id')
    return render (request, 'ajax/Lajax.html',{'employees':employees})

def save_data(request):
    if request.method == "POST":
        nameid = request.POST['nameid']
        emailid = request.POST['emailid']
        phnid = request.POST['phnid']
        editid = request.POST['editid']
        if editid:
            x= employee_information.objects.get(id=editid)
            x.em_name=nameid
            x.em_email=emailid
            x.em_phn=phnid
            x.save()
            all_em= employee_information.objects.values()
            all_em_list = list(all_em)
            return JsonResponse({'status':'save','all_val':all_em_list})
        else:               
            emp = employee_information(em_name= nameid,em_email = emailid,em_phn=phnid)
            emp.save()
            all_em= employee_information.objects.values()
            all_em_list = list(all_em)
            return JsonResponse({'status':'save','all_val':all_em_list})
    else:
        return JsonResponse({'status': 0})


def dlt_data(request,id):
    employee_information.objects.get(id=id).delete()
    return JsonResponse({'status':'done'})


def edt_data(request,id):
    data = employee_information.objects.get(id=id)
    results = [{ 'id':data.id , 'name':data.em_name,'email':data.em_email,'phone':data.em_phn}]
    return JsonResponse({'result':results})

def search_data(request):
    if request.method=='POST':
        search = request.POST['search']
        datas = employee_information.objects.filter(Q(em_name__icontains=search)|Q(em_email__icontains=search)|Q(em_phn__icontains=search))
        results = [{ 'id':data.id , 'name':data.em_name,'email':data.em_email,'phone':data.em_phn} for data in datas]
        return JsonResponse({'result':results})
    return JsonResponse({'result':0})




#Django Rest Framework bellow
#serializar
from .seriailizer import EmployeeSeriailizer
from rest_framework.renderers import JSONRenderer 

def emp_info(request,id):
    em = employee_information.objects.get(id=id)
    seriailizer = EmployeeSeriailizer(em)
    json_data =  JSONRenderer().render(seriailizer.data)
    # return render(request, "DRF/drf.html",{'json_data':json_data})
    return HttpResponse(json_data, content_type= 'application/json')

def all_emp_info(request):
    em = employee_information.objects.all()
    seriailizer = EmployeeSeriailizer(em,many=True)
    json_data =  JSONRenderer().render(seriailizer.data)
    # return render(request, "DRF/drf.html",{'json_data':json_data})
    return HttpResponse(json_data, content_type= 'application/json')





#de-serializer/create data
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def em_create(request):
    if request.method== 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seri = EmployeeSeriailizer(data =pythondata)
        if seri.is_valid():
            seri.save()
            res = {'msg':'Data Saved'}
            return JsonResponse({'msg':res})
        res = {'msg':'Data not Saved'}
        return JsonResponse({'msg':res})




#update data using put method
@csrf_exempt
def put_em(request):
    if request.method== 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        em = employee_information.objects.get(id=id)
        seri = EmployeeSeriailizer(em,data =pythondata, partial=True)
        if seri.is_valid():
            seri.save()
            res = {'msg':'Data updated'}
            return JsonResponse({'msg':res})
        res = {'msg':'Data not updated'}
        return JsonResponse({'msg':res})


#delete using delete method
@csrf_exempt
def dlt_em(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id = python_data.get('id')
        em = employee_information.objects.get(id=id)
        em.delete()
        res = {'msg':'Data deleted'}
        return JsonResponse({'msg':res})
    res = {'msg':'Data not deleted'}
    return JsonResponse({'msg':res})
