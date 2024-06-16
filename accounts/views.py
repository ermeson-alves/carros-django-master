from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    
    else:
        user_form = UserCreationForm()
    
    return render(
        request,
        'authentication.html',
        {'user_form': user_form}  
    )


# VER COMO FAZER O REDIRECT PARA A TELA QUE CHAMOU A AUTENTICAÇÃO
def login_view(request):
    if request.method == 'POST':
        # request.POST serve para capturar os dados dessa request
        username = request.POST['username']
        password = request.POST['password']
        # validação:
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()

    else:
        login_form = AuthenticationForm()

    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )


def logout_view(request):
    logout(request)
    return redirect('cars_list')