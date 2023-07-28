from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
# Create your views here.
def retrieve_view(request):
    #emp_list = Employee.objects.all()
    #print(type(emp_list))
    #emp_list = Employee.objects.filter(esal__gt=15000)
    #emp_list = Employee.objects.filter(esal__gte=15000)
    #emp_list = Employee.objects.filter(ename__exact='Sairam')
    #emp_list = Employee.objects.filter(ename__iexact='sairam')
    #emp_list = Employee.objects.filter(ename__contains='john')
    #emp_list = Employee.objects.filter(id__in=[1,3,5,101])
    #emp_list = Employee.objects.filter(ename__startswith='A')
    #emp_list = Employee.objects.filter(ename__endswith='a')
    #emp_list = Employee.objects.filter(esal__range=[12000,15000])
    #emp_list = Employee.objects.filter(ename__startswith='D') | Employee.objects.filter(esal__lt=11000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='D') | Q(esal__lt=11000))
    #emp_list = Employee.objects.filter(ename__startswith='D') & Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='A') & Q(esal__lt=15000))
    #emp_list = Employee.objects.filter(ename__startswith='A',esal__lt=15000)
    #emp_list = Employee.objects.exclude(ename__startswith='A')
    #emp_list = Employee.objects.filter(~Q(ename__startswith='A'))
    #return render(request,'testapp/index.html',{'emp_list':emp_list})
    #emp_list = Employee.objects.all().values_list('ename','esal')
    #emp_list = Employee.objects.all().values('ename','esal')
    emp_list = Employee.objects.all().only('ename','esal')
    return render(request,'testapp/specificcolums.html',{'emp_list':emp_list})
