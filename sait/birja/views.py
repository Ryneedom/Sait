from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from .models import Applicant, Company, Post, ListPost, Vacancy


# Авторизация

# Авторизованный пользователь
authorizated_applicant = Applicant()
# Авторизованная компания
authorizated_company = Company()


# Логин пользователей и компаний
def authenticate(request):
    if request.method == "POST":
        if request.POST.get('login') == 'user':
            try:
                global authorizated_applicant
                applicant = Applicant.objects.get(name=request.POST.get('name'))
                authorizated_applicant = applicant
                return HttpResponseRedirect('applicants/mainpage')
            except ObjectDoesNotExist:
                return render(request, 'auth/login.html', {'message': 'Такого пользователя не существует'})
        else:
            try:
                global authorizated_company
                print(request.POST.get('name'))
                company = Company.objects.get(company_name=request.POST.get('name'))
                authorizated_company = company
                return HttpResponseRedirect('companies/mainpage')
            except ObjectDoesNotExist:
                return render(request, 'auth/login.html', {'message': 'Такой компании не существует'})

    else:
        return render(request, 'auth/login.html', {'message': ''})


# Регистрация пользователей
def register(request):
    if request.method == "POST":
        global authorizated_applicant
        new_applicant = Applicant.objects.create(name=request.POST.get('name'), condition=request.POST.get('condition'))
        authorizated_applicant = Applicant.objects.get(id=new_applicant.id)
        return HttpResponseRedirect('applicants/mainpage')
    else:
        return render(request, 'auth/register.html')


# Выход пользователя из системы
def logout(request):
    global authorizated_applicant
    authorizated_applicant = Applicant()
    return HttpResponseRedirect('/login')


# Страничка пользователя
def applicant_show(request):
    global authorizated_applicant
    if authorizated_applicant.name == '':
        return HttpResponseRedirect('login')

    try:
        applicant_listposts = ListPost.objects.filter(post_id=authorizated_applicant.id)
        posts = []
        for listpost in applicant_listposts:
            posts.append(Post.objects.get(id=listpost.post_id))
        return render(request, 'applicant/mainpage.html', {'authorizated': authorizated_applicant, 'posts': posts})
    except ObjectDoesNotExist:
        return render(request, 'applicant/mainpage.html', {'authorizated': authorizated_applicant, 'posts': 0})


def applicant_index(request):
    applicants = Applicant.objects.order_by('id')
    data = {'applicants': applicants}
    return render(request, 'applicant/index.html', context=data)


# Отдел REST API для company
def company_index(request):
    companies = Company.objects.order_by('id')
    p = Paginator(companies, 100)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'company/index.html', context)


def company_show(request):
    global authorizated_company
    if authorizated_company.company_name == '':
        return HttpResponseRedirect('login')
    return render(request, 'company/show.html', {'company': authorizated_company})


# сохранение данных в бд
def company_create(request):
    if request.method == "POST":
        company = Company.objects.create(company_name=request.POST.get("company_name"))
        return render(request, "company/show.html", {"company": company})
    else:
        return render(request, "company/create.html", {"company": Company()})


# изменение данных в бд
def company_edit(request, id):
    try:
        company = Company.objects.get(id=id)

        if request.method == "POST":
            company.company_name = request.POST.get("company_name")
            company.save()
            return render(request, "company/show.html", {"company": company})
        else:
            return render(request, "company/edit.html", {"company": company})
    except Company.DoesNotExist:
        return HttpResponseNotFound("<h2>Company not found</h2>")


# удаление данных из бд
def company_delete(request, id):
    try:
        company = Company.objects.get(id=id)
        company.delete()
        return HttpResponseRedirect("/companies")
    except Company.DoesNotExist:
        return HttpResponseNotFound("<h2>Company not found</h2>")


# Отдел REST API для post
def post_index(request):
    posts = Post.objects.order_by('id')
    return render(request, 'post/index.html', context={'posts': posts})


# сохранение данных в бд
def post_create(request):
    if request.method == "POST":
        post = Post.objects.create(post=request.POST.get("post"))
        return render(request, "post/show.html", {"post": post})
    else:
        return render(request, "post/create.html", {"post": Post()})


# изменение данных в бд
def post_edit(request, id):
    try:
        post = Post.objects.get(id=id)

        if request.method == "POST":
            post.post = request.POST.get("post")
            post.save()
            return render(request, "post/show.html", {"post": post})
        else:
            return render(request, "post/edit.html", {"post": post})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")


# удаление данных из бд
def post_delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/posts")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")


# Отдел REST API для Vacancy
def vacancy_index(request):
    vacancies = Vacancy.objects.order_by('id')
    return render(request, 'vacancy/index.html', context={'vacancies': vacancies})


def start(request):
    return render(request, 'start.html')
