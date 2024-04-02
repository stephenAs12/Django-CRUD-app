from django.shortcuts import render, redirect

# Create your views here.
from .models import Employee

# Create Employee

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail, EmpDesignation= EmpDesignation)
        data.save()
  
        return redirect('show/')
    else:
        return render(request, 'insert.html')
    
def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees} )
    
def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            employees.EmpName = request.POST['EmpName']
            employees.EmpGender = request.POST['EmpGender']
            employees.EmpEmail = request.POST['EmpEmail']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.save()   
            return redirect('/show')
    context = {
        'employees': employees,
    }

    return render(request,'edit.html',context)

def remove_emp(request, pk):
    employees = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employees.delete()
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request, 'delete.html', context)