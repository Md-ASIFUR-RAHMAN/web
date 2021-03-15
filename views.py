from django.shortcuts import redirect, render
from details.models import Student
from details.models import Teacher
from details.models import Course
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'details/home.html')

def student(request):
    global details_student

    if request.method == "GET":
        details_student = Student.objects.all()
        context = {
            'student_key': details_student
        }
        return render(request,'details/student.html',context)

    elif request.method == 'POST':
        v_id = request.POST["v_id"]
        name = request.POST["name"]
        email = request.POST["email"]
        cgpa = request.POST["cgpa"]

        Student.objects.create(versity_id=v_id,name=name,email=email,cgpa=cgpa)
        details_student = Student.objects.all()
        context = {
            'student_key': details_student
        }
        return render(request, 'details/student_show.html', context)
        #return redirect('/')


def teacher(request):
    global details_teacher

    if request.method == "GET":
        details_teacher = Teacher.objects.all()
        context = {
            'teacher_key': details_teacher
        }
        return render(request, 'details/teacher.html', context)

    elif request.method == 'POST':
        t_id = request.POST["t_id"]
        name = request.POST["name"]


        Teacher.objects.create(teacher_id=t_id,teacher_name=name)
        details_teacher = Teacher.objects.all()
        context = {
            'teacher_key': details_teacher
        }
        return render(request, 'details/teacher_show.html', context)

def course(request):
    global details_course

    if request.method == "GET":
        details_course = Course.objects.all()
        context = {
            'teacher_key': details_course
        }
        return render(request, 'details/course.html', context)

    elif request.method == 'POST':
        title = request.POST["title"]
        code = request.POST["code"]
        credit = request.POST["credit"]

        Course.objects.create( Title=title,Code=code,Credit=credit)
        details_course = Course.objects.all()
        context = {
            'course_key': details_course
        }
        return render(request, 'details/course_show.html', context)




def action_hander(request,action,id):
    #Delete
    if action == 'delete':
        student = Student.objects.get(id=id)
        student.delete()


        details_student = Student.objects.all()
        context = {
            'student_key': details_student
        }
        return render(request, 'details/student_show.html', context)
    #Update
    if action == 'update':
        if request.method == 'GET':
            update_student = Student.objects.get(id=id)
            context = {
                'student_key': update_student
            }
            return render(request, 'details/stu_edit.html', context)

        if request.method =='POST':
            # Get from the data
            name = request.POST['name']
            email = request.POST['email']
            cgpa = request.POST['cgpa']

            # which student edited
            update_student = Student.objects.get(id=id)

            #Update the values

            update_student.name = name
            update_student.email = email
            update_student.cgpa = cgpa

            update_student.save()

            details_student = Student.objects.all()
            context = {
                'student_key': details_student
            }
            return render(request, 'details/student_show.html', context)




