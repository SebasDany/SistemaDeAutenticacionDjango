from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from django.views import generic
import os
import random
from .models import Imagen 
from django.contrib.auth.models import User

from django.contrib import messages

import numpy as np
import matplotlib.pyplot as plt
import numpy as np


import random
import cv2;

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


import smtplib
 

class Home(LoginRequiredMixin,generic.TemplateView):
    template_name='base/index.html'
    login_url='bases:rP'

    



def validar(request):
    

    if request.method=='GET':
        
        ejemplo_dir = './media/claves/'
        
        # ran2=random.randint(1, 255)
        # ran3=random.randint(1, 255)
        # ran4=random.randint(1, 255)
        # ran1=random.randint(1, 255)
    
        
        contenido = os.listdir(ejemplo_dir)

        print(contenido)
        imagenes = []
        imsend=[]
        for fichero in contenido:
            if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith(('.jpg', '.jpeg', '.gif', '.png')):
                #i=fichero.split("'")[0]
                #
                imagenes.append(fichero)
    
        ran2=random.sample(range(0, len(imagenes)),12)
        print(ran2)

        print(len(imagenes))
        print(imagenes)

        for i in range(len(ran2)):
            print(ran2[i])
            val=ran2[i]
            imsend.append(imagenes[val])
            print('valor randomico',imagenes[val])
    
    
        #imsend.append(imagenes[ran1])
        print(imsend)
        ms="Seleccione una imagen para generar clave"
        estado='disabled '

        progress="https://www.gifde.com/gif/otros/decoracion/cargando-loading/cargando-loading-039.gif"
        return render(request, 'base/autenticar.html',{'im':imsend,'ms':ms,'estado':estado})

       

    return 0

def valid(request,name,email):
    if request.method=='GET':
        foto1 =cv2.imread('./media/claves/'+name)
        print(foto1)
            
        print(name)
        
        procesarImagen(foto1)
        messages.success(request, 'Su clave se ha generado correctamente!')
        sendImage('clave.png',email)
        


    if request.method=='POST':
        password=cv2.imread('clave.png')
        im=Imagen()
        print(im)
        im.imagen=request.FILES.get('myfile')
        if(im.imagen==None):
             messages.success(request, 'Por favor suba una imagen!')
             return render(request, 'base/autenticar.html')

        else:
                
            print("ggggggggggggggggg",im.imagen)
            im.save()
            print('Imagen Guardad..................',im.imagen.name)
            
            
            

            foto =cv2.imread('./media/'+im.imagen.name)
            upl = cv2.resize(foto, (255,255))
            #print(len(upl))
            print("===============",im.imagen.name)

            diferencia=cv2.subtract(upl,password)
            if not np.any(diferencia):
                print('estoy dentro')            
                messages.success(request, 'Autenticacion correcta!')
                print('Listo para eliminar imagen ',im.imagen.name)
                os.remove('./media/'+im.imagen.name)
                print('Eliminado')
                return render(request, 'base/base.html')
            else:
                print('estoy fuera')
                messages.success(request, 'Autenticacion  incorrecta!')

                return render(request, 'base/autenticar.html')
        
                       
    return render(request, 'base/autenticar.html',{'ms':'Suba una imagen'})

def procesarImagen(foto1):
    
    imagenrgb1=cv2.cvtColor(foto1,cv2.COLOR_BGR2RGB)
    newImg = cv2.resize(imagenrgb1, (255,255))
    imagenNegativo=newImg
    ran1=random.randint(1, 255)
    ran2=random.randint(1, 255)
    ran3=random.randint(1, 255)
    imagenNegativo[ran1,ran2,0]=1
    imagenNegativo[ran3, ran1,1]=255
    imagenNegativo[ran2,ran3,2]=0
    cv2.imwrite('clave.png',imagenNegativo)
    
   
    
    return imagenNegativo
    
    
def compararImage(im1,im2):
    
    diferencia=cv2.subtract(im1,im2)
    if not np.any(diferencia):
         print('estoy dentro')
         
    else:
        print('estoy fuera')

def sendImage(path,email):
    print("*******",User.objects.all())
    msg = MIMEMultipart()
    msg['From']="parajuegos6446@gmail.com"
    msg['To']=email
    msg['Subject']="Correo con imagen Adjunta"

    # Adjuntamos Imagen
    message = "Bienvenido al nuevo sistema de autenticacion  por favor descargue la imagen y  subalo en la en la pagina de autenticacion"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    file = open(path, "rb")
    attach_image = MIMEImage(file.read())
    attach_image.add_header('Content-Disposition', 'attachment; filename = "avatar.png"')
    msg.attach(attach_image)

    # Autenticamos
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login("parajuegos6446@gmail.com","hola1234s")

    # Enviamos
    mailServer.sendmail("parajuegos6446@gmail.com", email, msg.as_string())
    

    # Cerramos conexión
    mailServer.close()
            
def registrarPersona(request):
    # if request.method=='GET':
    #     print('esta del del get..................')
    #     form=RegstroForm()
    #     contexto={
    #         'form':form
    #         }
        
    # else:
    #     form=RegstroForm(request.POST)
    #     print(form)
    #     contexto={
    #         'form':form
    #         }
    #     if form.is_valid():
    #         form.save()
    #         return redirect('log')
    

    if request.method=='POST':
        print('segundo formulaei')
        form1=UserRegisterForm(request.POST)
        print(form1)
        pas=form1['password1'].value()

        username=form1['password1'].help_text
        
        print('$$$$$$$$$$$$',pas)
        if form1.is_valid():
            # username=form1.cleaned_data['username']
            
            form1.save()
            messages.success(request, 'Se ha registrado correctamente!')
            print()
            print('segundo formulaei')
            form1=UserRegisterForm()
            print(form1)
            form1.fields['password1'].help_text = None
            form1.fields['password2'].help_text = None
            contexto1={
                'form1':form1
                }

            return render(request,'base/index.html',contexto1)

        else:
            print('segundo formulaei')
            form1=UserRegisterForm()
            messages.success(request, 'No se ha podido registrar! La clave de contener numeros, letras mayusculas y minusculas, y debe contener mas de 8 carateres ')
            print(form1)
            contexto1={
                'form1':form1
            }

        return render(request,'base/index.html',contexto1)

           
    else:
        print('segundo formulaei')
        form1=UserRegisterForm()
        form1.fields['password1'].help_text = None
        form1.fields['password2'].help_text = None
        
        print(form1)
        contexto1={
            'form1':form1
        }
         

        print(contexto1)  
       
            



    # if request.method=='POST':
    #     print('esta del del post..................')
    #     contexto={
    #         'form':form
    #         }
       
    return render(request,'base/index.html',contexto1)
    

def hola(request):
     return render(request,'base/footer-header.html' )

