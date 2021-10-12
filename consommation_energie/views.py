from django.shortcuts import render
from django.http import JsonResponse
from .models import Consommation

def home(request):
    return render(request, 'consommation_energie/home.html')

def consommation_chart(request):
    labels = []
    dataPower = []
    data = []
    data2 =[]
    data3=[]
    data6=[]
    data7=[]
    data2Cumulee=[] 
    data3Cumulee=[] 
    data6Cumulee=[] 
    data7Cumulee=[] 
    #Récupération des champs de la base de données. 
    queryset = Consommation.objects.values('dt', 'power', 'json_data','installation_id').order_by('dt') 
     
    
    for entry in queryset:
        if entry['installation_id']==1: # installation 1 = Bureaux la Défense 
            labels.append(entry['dt'])
            dataPower.append((entry['power']))
            data.append(entry['json_data'])
               
                      
    # Récuperation des énergies (W) relatives à la catégorie 2 : Ventilation    
    for champ in data: 
        for key in champ:
            if key=="2":
                data2.append(champ[key])
    # Calcule de l'énergie cumulée (WH par jour) de la catégorie 2 : Ventilation       
    data2Cumulee.extend([sum(data2[0:11])/6,sum(data2[12:150])/6,sum(data2[151:289])/6,sum(data2[290:431])/6,sum(data2[432:569])/6,sum(data2[570:713])/6,sum(data2[714:854])/6,sum(data2[855:995])/6,sum(data2[996:1137])/6,sum(data2[1138:1281])/6,sum(data2[1282:1413])/6])

    # Récuperation des énergies (W) relatives à la catégorie 3 : Éclairage
    for champ in data: 
        for key in champ:
            if key=="3":
                data3.append(champ[key])
    # Calcule de l'énergie cumulée (en Wh par jour) de la catégorie catégorie 3 : Éclairage      
    data3Cumulee.extend([sum(data3[0:11])/6,sum(data3[12:150])/6,sum(data3[151:289])/6,sum(data3[290:431])/6,sum(data3[432:569])/6,sum(data3[570:713])/6,sum(data3[714:854])/6,sum(data3[855:995])/6,sum(data3[996:1137])/6,sum(data3[1138:1281])/6,sum(data3[1282:1413])/6])
    
    # Récuperation des énergies (W) relatives à la catégorie 6 : Ascenseurs
    for champ in data: 
        for key in champ:
            if key=="6":
                data6.append(champ[key])   
        # Calcule de l'énergie cumulée (en Wh par jour) de la catégorie catégorie 6 : Ascenseurs      
    data6Cumulee.extend([sum(data6[0:11])/6,sum(data6[12:150])/6,sum(data6[151:289])/6,sum(data6[290:431])/6,sum(data6[432:569])/6,sum(data6[570:713])/6,sum(data6[714:854])/6,sum(data6[855:995])/6,sum(data6[996:1137])/6,sum(data6[1138:1281])/6,sum(data6[1282:1413])/6])        

    # Récuperation des énergies (W) relatives à la catégorie 7 : Traitement de l'air
    for champ in data: 
        for key in champ:
            if key=="7":
                data7.append(champ[key])
        # Calcule de l'énergie cumulée (en Wh par jour) de la catégorie catégorie 7 : Traitement de l'air    
    data7Cumulee.extend([sum(data7[0:11])/6,sum(data7[12:150])/6,sum(data7[151:289])/6,sum(data7[290:431])/6,sum(data7[432:569])/6,sum(data7[570:713])/6,sum(data7[714:854])/6,sum(data7[855:995])/6,sum(data7[996:1137])/6,sum(data7[1138:1281])/6,sum(data7[1282:1413])/6])

    return JsonResponse(data={
        'labels': labels,
        'dataPower':dataPower,
        'data2': data2,
        'data3': data3,
        'data6': data6,
        'data7': data7,
        'data2C':data2Cumulee,
        'data3C':data3Cumulee,
        'data6C':data6Cumulee,
        'data7C':data7Cumulee
    })

 