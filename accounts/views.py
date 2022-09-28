from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
# 

# Create your views here.




def registro(request):
    context ={}

    if request.method == 'POST':
        print('------ 1')
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
            print('------ 2')
            existe = Account.objects.filter(email=email).exists()
            if not existe:
                user = Account.objects.create_user(first_name=nombres, last_name=nombres, username=username, email=email, password=password)
                user.save()
                context['alarma'] = 'Usuario guardado con exito!'

                # correo --------------------
                print('------ 3')
                current_site= get_current_site(request)
                mail_subject = 'Verificación del Correo'

                body = render_to_string('email.html',{
                'nombre': user,
                'domain': current_site,
                'uid': str(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': default_token_generator.make_token(user)
                 
                })
                 #Lista con el o los correos de destino
                to_email = email  
                send_email = EmailMessage(mail_subject, body, to=[to_email])
                send_email.send()
                print('------ 4')
                # fin correo ----------------



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

def activate(request, uidb64, token):
    try:
        uid= urlsafe_base64_decode(uidb64).decode()
        user= Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user= None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active= True
        user.save()
        return redirect('login')
    else:
        return redirect('registro')

def logout(requerest):
    auth.logout(requerest)
    return redirect('login')



    