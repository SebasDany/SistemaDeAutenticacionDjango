from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
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


class Home(LoginRequiredMixin,generic.TemplateView):
    template_name='base/base.html'
    login_url='bases:login'



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
    
    return imagenNegativo
    
    
def compararImage(im1,im2):
    
    diferencia=cv2.subtract(im1,im2)
    if not np.any(diferencia):
         print('estoy dentro')
         
    else:
        print('estoy fuera')
        
   
    

