from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from django.views import generic
import os
import random
from .models import Imagen 

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
    
        ran2=random.sample(range(0, len(imagenes)),4)
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
        ms="Seleccionar imagen para generar clave"
        estado='disabled '
        return render(request, 'base/autenticar.html',{'im':imsend,'ms':ms,'estado':estado})

       

    return 0

def valid(request,name):
    if request.method=='GET':
        foto1 =cv2.imread('./media/claves/'+name)
        print(foto1)
            
        print(name)
        
        procesarImagen(foto1)
        messages.success(request, 'Su clave se ha creado correctamente!')
        


    if request.method=='POST':
        password=cv2.imread('clave.png')
        im=Imagen()
        print(im)
        im.imagen=request.FILES.get('myfile')
        im.save()
        print('Imagen Guardad..................',im.imagen.name)
        for i in range(10000):
            print(i)
        
        

        foto =cv2.imread('./media/'+im.imagen.name)
        upl = cv2.resize(foto, (255,255))
        #print(len(upl))
        print("===============",im.imagen.name)

        diferencia=cv2.subtract(upl,password)
        if not np.any(diferencia):
            print('estoy dentro')            
            messages.success(request, 'Autenticacion correcta!')
            return render(request, 'base/base.html')
        else:
            print('estoy fuera')
            messages.success(request, 'Autenticacion  incorrecta!')

            return render(request, 'base/autenticar.html')
                    
    return render(request, 'base/autenticar.html')

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
    sendImage('clave.png')
   
    
    return imagenNegativo
    
    
def compararImage(im1,im2):
    
    diferencia=cv2.subtract(im1,im2)
    if not np.any(diferencia):
         print('estoy dentro')
         
    else:
        print('estoy fuera')

def sendImage(ms):
    import smtplib
    import email.message
    server = smtplib.SMTP('smtp.gmail.com:587')
    
    email_content = """
    <html>
    
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        
    <title>Calidad de Software</title>
    <style type="text/css">
        a {color: #d80a3e;}
    body, #header h1, #header h2, p {margin: 0; padding: 0;}
    #main {border: 1px solid #cfcece;}
    img {display: block;}
    #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
    #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
    #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
    h5 {margin: 0 0 0.8em 0;}
        h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
    p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
    </style>
    </head>
    
    <body>
    
    
    <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
    <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
        <td align="center">
            <p><a href="#">View in Browser</a></p>
        </td>
        </tr>
    </table>
    
    <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
        <tr>
        <td>
            <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
            <tr>
                <td width="570" align="center"  bgcolor="#d80a3e"><h1>Evanto Limited</h1></td>
            </tr>
            <tr>
                <td width="570" align="right" bgcolor="#d80a3e"><p>November 2020</p></td>
            </tr>
            </table>
        </td>
        </tr>
    
        <tr>
        <td>
            <table id="content-3" cellpadding="0" cellspacing="0" align="center">
            <tr>
                <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                <img src="clave.png" width="250" height="150"  />
                </td>
                <td width="15"></td>
                <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                    <img src="clave.png" width ="250" height="150" />
                </td>
            </tr>
            </table>
        </td>
        </tr>
        <tr>
        <td>
            <table id="content-4" cellpadding="0" cellspacing="0" align="center">
            <tr>
                <td width="200" valign="top">
                <h5>How to Get Up and Running With Vue</h5>
                <p>In the introductory post for this series we spoke a little about how web designers can benefit by using Vue. In this tutorial we will learn how to get Vue up..</p>
                </td>
                <td width="15"></td>
                <td width="200" valign="top">
                <h5>Introducing Haiku: Design and Create Motion</h5>
                <p>With motion on the rise amongst web developers so too are the tools that help to streamline its creation. Haiku is a stand-alone..</p>
                </td>
            </tr>
            </table>
        </td>
        </tr>
        
    
    </table>
    <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
        <td align="center">
            <p>Design better experiences for web & mobile</p>
            <p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
        </td>
        </tr>
    </table><!-- top message -->
    </td></tr></table><!-- wrapper -->
    
    </body>
    </html>
    
    
    """
    
    msg = email.message.Message()
    msg['Subject'] = 'Calidad de Software'
    
    
    password = "hola1234s"
    msg['From'] = "parajuegos6446@gmail.com"
    msg['To'] = "parajuegos6446@gmail.com"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
            
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
        if form1.is_valid():
            username=form1.cleaned_data['username']
            form1.save()
            messages.success(request, 'Se ha registrado correctamente!')
            print()
            print('segundo formulaei')
            form1=UserRegisterForm()
            print(form1)
            contexto1={
                'form1':form1
                }

            return render(request,'base/index.html',contexto1)

        else:
            print('segundo formulaei')
            form1=UserRegisterForm()
            messages.success(request, 'No se ha registrado!')
            print(form1)
            contexto1={
                'form1':form1
            }

        return render(request,'base/index.html',contexto1)

           
    else:
        print('segundo formulaei')
        form1=UserRegisterForm()
        
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
    

