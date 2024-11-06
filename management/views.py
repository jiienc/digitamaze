from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Student, Teacher, Class
from .forms import StudentForm, TeacherForm, ClassForm

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'management/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Home view
def home(request):
    return render(request, 'management/home.html')

# List students
def list_students(request):
    students = Student.objects.all()
    return render(request, 'management/list_students.html', {'students': students})

# Create student (with AJAX support)
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return JsonResponse({'message': 'Student created successfully'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = StudentForm()
        html = render_to_string('management/partials/student_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

# Edit student (with AJAX support)
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Student updated successfully'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = StudentForm(instance=student)
        html = render_to_string('management/partials/student_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

# Delete student (with AJAX support)
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully'}, status=200)
    else:
        html = render_to_string('management/partials/student_confirm_delete.html', {'student': student}, request=request)
        return JsonResponse({'html': html})

# List teachers
def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'management/list_teachers.html', {'teachers': teachers})

# Create teacher (with AJAX support)
def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            return JsonResponse({'message': 'Teacher created successfully'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = TeacherForm()
        html = render_to_string('management/partials/teacher_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

# Edit teacher (with AJAX support)
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Teacher updated successfully'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = TeacherForm(instance=teacher)
        html = render_to_string('management/partials/teacher_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

# Delete teacher (with AJAX support)
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == "POST":
        teacher.delete()
        return JsonResponse({'message': 'Teacher deleted successfully'}, status=200)
    else:
        html = render_to_string('management/partials/teacher_confirm_delete.html', {'teacher': teacher}, request=request)
        return JsonResponse({'html': html})

# List classes
def list_classes(request):
    classes = Class.objects.all()
    return render(request, 'management/list_classes.html', {'classes': classes})

# Create class (with AJAX support)
def create_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            class_instance = form.save()
            return JsonResponse({'message': 'Class created successfully'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ClassForm()
        html = render_to_string('management/partials/class_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

# Edit class (with AJAX support)
def edit_class(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form = ClassForm(request.POST, instance=class_instance)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Class updated successfully'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ClassForm(instance=class_instance)
        html = render_to_string('management/partials/class_form.html', {'form': form}, request=request)
        return JsonResponse({'html': html})

# Delete class (with AJAX support)
def delete_class(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        class_instance.delete()
        return JsonResponse({'message': 'Class deleted successfully'}, status=200)
    else:
        html = render_to_string('management/partials/class_confirm_delete.html', {'class': class_instance}, request=request)
        return JsonResponse({'html': html})
