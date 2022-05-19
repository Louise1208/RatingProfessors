from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .form import *
from django.db.models.aggregates import Sum
# views.
def home(request):
    '''
    home page render
    :param request:
    :return:
    '''
    return render(request, 'MainPages/home.html',
                  {'MainPages': home})
def home(request):
    '''
    home page render
    :param request:
    :return:
    '''
    return render(request, 'MainPages/home.html',
                  {'MainPages': home})
def register(request):
    if request.method == "POST":
        user = request.POST['user']
        pwd = request.POST['pwd']
        re_pwd = request.POST['re_pwd']
        email = request.POST['email']
        if pwd != re_pwd:
            return HttpResponse("repeat password don't match!")
        person = User.objects.filter(username=user)
        if any(person):
            return HttpResponse("user exists！")
        user = User.objects.create_user(username=user, email=email, password=pwd)
        user.save()
        return render(request, 'MainPages/home.html')
    else:
        form = UserForm()
        return render(request, 'registration/register.html', {'form': form})

@login_required
def modules(request):
    """
    modules page render
    :param request:
    :return:
    """
    courses = Courses.objects.filter()
    return render(request, 'MainPages/modules.html',
                  {'modules': courses})
@login_required
def professors(request):
    """
    professor page render
    :param request:
    :return:
    """
    professors = Teacher.objects.filter()
    result = []
    for professor in professors:
        courses = Courses.objects.filter(taught_by=professor)
        rate = Rate.objects.filter(course__in=courses).aggregate(Sum('rate'))['rate__sum']
        if rate is None:
            result.append({"professor": professor, "rate": 0})
        else:
            result.append({"professor": professor, "rate": rate / len(courses)})
    return render(request, 'MainPages/professors.html',
                  {'professors': result})

@login_required
def rate(request):
    '''
    a page with a list of modules need to rate
    :param request:
    :return:
    '''
    if request.method == "POST":
        """store"""
        rateform = RateForm(request.POST)
        if rateform.is_valid():
            rate = rateform.save(commit=False)
            rate.save()
            return render(request, 'MainPages/home.html')
    else:
        rateform = RateForm()
    return render(request, 'MainPages/module_edit.html', {'form': rateform})

