from base64 import urlsafe_b64encode
import email
from email.message import EmailMessage
from multiprocessing import context
from urllib import request
from django.shortcuts import render



def home(request):
    return render(request, 'home.html');

def bienvenido(request):
    return render(request, 'bienvenido.html');

def contactenos(request):
    return render(request, 'contactenos.html');

def servicios(request):
    return render(request, 'servicios/servicios.html');

def registro(request):
    context={}
    if request.method=='POST':
        rol=request.POST['rol']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        username=request.POST['username']
        email=request.POST['correo']


    #Validación de Campos

    ok=True
    if not email:
        context['alarma']='Ingrese el correo electronico'
        ok=False

    if not password or len(password)<5:
        context['alarma']='Ingrese una contraseña de 5 o más caracteres.'
        ok=False

    if password!=confirmPassword:
        context['alarma']='Las contraseñas no coinciden'
#Ok

if ok:
    existe=Account.objects.filter(email=email).exists()
    print('---------')
    print(existe)

    if not existe:
        user=Account.objects.create_user(first_name=username,last_name=username,username=username,email=email,password=password)
        user.save()
        context['mensaje']='Usuario guardado con exito'

#Modulo para envío de correo

        current_site=get_current_site(request)
        mail_subject='Por favor activa tu cuenta'

        body=render_to_string(¿usuarios/account_verification_email.html',{
            'user':user,
            'domain':current_site,
            'uid':str(urlsafe_base64encode(force_bytes(user.pk)))
            'token':default_token_generator.make_token(user),
        })
        to_email=email
        send_email=EmailMessage(mail_subject,body, to=[to_email])
        send_email.send()
        context={'mensaje':'Bienvenido'+first_name+'.Favor activar su cuenta con el enlace que enviamos a su correo'}

        return redirect('accounts/login/')

    else:
        context['alarma']= '!El correo ya existe!'

return render(request, 'registro.html',context);#Y



        #--- return render(request, 'registro.html'); Us




