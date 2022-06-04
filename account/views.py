# from crypt import methods
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from account.models import patientdb
from .forms import LoginForm, RegistrationUser

# Create your views here.
from django.shortcuts import render

# Create your views here.

# def doc_reg(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         gender = request.POST['radiogroup1']

#         if password1 == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already registered')
#                 return redirect('doc_reg')
#             elif User.objects.filter(username = username).exists():
#                 messages.info(request, 'Username already taken')
#                 return redirect('doc_reg')
#             else:
#                 user = User.objects.create_user(username=username, password = password1, email=email, first_name = first_name, last_name = last_name)
#                 user.save()
#                 return redirect('doc_login')
#         else:
#             messages.info(request, "Password aren't same")
#             return redirect('doc_reg')
#     else:
#         return render(request, 'account/doc_reg.html')

# def doc_login(request):
#     if request.method == 'POST':
#         emailUsername = request.POST['emailUsername']
#         password = request.POST['password']

#         user1 = auth.authenticate(username = emailUsername , password = password)
#         user2 = auth.authenticate(email = emailUsername , password = password)
#         if user1 or user2 is not None:
#             auth.login(request, user1)
#             return redirect('/')
#         else:
#             messages.info(request, 'Invalid credentials')
#             return redirect('doc_login')
#     else:
#         return render(request, 'account/doc_login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def doc_rec(request):
#     return render(request, 'account/doc_reg.html')

# def doc_login(request):
#     return render(request, 'account/doc_login.html')

def patient_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        img = request.POST.get('img')
        medHistory = request.POST.get('medHistory')
        transectionDone = request.POST.get('transectionDone')
        transectionDue = request.POST.get('transectionDue')
        symptoms = request.POST.get('symptoms')
        billCopy = request.POST.get('billCopy')
        labReport = request.POST.get('labReport')

        patient  = patientdb(name=name, age = age, gender=gender, address = address, img = img, medHistory=medHistory, transectionDone=transectionDone, transectionDue=transectionDue,symptoms=symptoms, billCopy=billCopy, labReport=labReport )
        patient.save()
        messages.info(request, "Patient Details added successfully")
        return redirect('patientdetails.html')
    else:
        return render(request, 'account/patientdetails.html')

def register(request):
    title = 'Regestraion'
    if request.method == 'POST':
        form = RegistrationUser(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            form.save()
            password = form.cleaned_data.get('password1')

            # saving rest data
            gender = request.POST.get('gender')
            mobile = request.POST.get('mobile')
            account = request.POST.get('account')
            full_name = request.POST.get('name')
            userRestDetails  = userRestDetailsdb(full_name=full_name, gender=gender,  mobile = mobile, account=account)
            userRestDetails.save()
            # login user after siging up
            user = authenticate(username = user.username, password = password)
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, form.errors)
            return redirect('register')
    else:
        form = RegistrationUser()
        context = {'form': form, 'title': title}
        return render(request, 'account/register.html', context=context)
    

# def login(request):
#     if request.method == 'POST':
#         emailUsername = request.POST.get('emailUsername')
#         emailUsername = request.POST.get('emailUsername')
#         password = request.POST.get('password')
#         if Doctordb.objects.filter(email=emailUsername).exists():
#             user1 = auth.authenticate(username = emailUsername , password = password)
#             user2 = auth.authenticate(email = emailUsername , password = password)
#             if user1 or user2 is not None:
#                 auth.login(request, user1)
#                 return redirect('/')
#             else:
#                 messages.info(request, 'Invalid credentials')
#                 return redirect('/')
#         else:
#             messages.info(request, "User doesn't exixt")
#     else:
#         return render(request, 'account/login.html')

def loginUser(request):
    title = "Login"
    form = LoginForm(request.POST or None)
    context={
        'form':form,
        'title': title,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user1 = authenticate(request, username=username, password = password)
            user2 = authenticate(request, email=email, password = password)
            if(user1):
                login(request, user1)
            else:
                login(request, user2)
            return redirect('index')
        else:
            messages.warning(request,form.errors)
            print(form.errors)
            return redirect('login')
    else:
        return render(request, 'account/login.html', context=context)