from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# 

# Create your views here.




def registro(request):
    context ={}
    if request.method == 'POST':
        
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        nombres = request.POST['Nombres']
        email = request.POST['email']
        username= email.split()[0]
    
        #Validacion campos
        ok = True
        if not email:
         context['alarma'] = 'Ingrese el correo electronico'
         ok = False
        if not password or len(password) < 5:
         context['alarma'] = 'Ingrese un password de cinco (5) o mas caracteres'
         ok = False  
        if password != confirmPassword:
         context['alarma'] = '¡El password no coincide!'
         ok = False
         
        #Todo ok
        if ok:
            existe = Account.objects.filter(email=email).exists()
            if not existe:
                user = Account.objects.create_user(first_name=username, last_name=username, username=username, email=email, password=password)
                user.save()
                context['alarma'] = 'Usuario guardado con exito!'
            else:
                context['alarma'] = '¡El correo ya existe!'
                
    return render(request, 'registro.html', context);

def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(email=email, password=password)

		if user is not None:
			auth.login(request, user)
			return render(request, 'home.html')
		else:
			return render (request, 'login.html', {'alarma': 'Correo o constraseña inválida'})

	else:
		return render(request, 'login.html')

@login_required(login_url='login')
def logout(requerest):
    auth.logout(requerest)
    return redirect('login') 