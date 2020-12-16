from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import winequaityserializer
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import pickle
@csrf_exempt
# Create your views here.
def wineview(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer=winequaityserializer(data=data)


        if serializer.is_valid():
            fixedacidity=serializer.data['fixedacidity']
            volatileacidity= serializer.data['volatileacidity']
            citricacid= serializer.data['citricacid']
            residualsugar=serializer.data['residualsugar']
            chlorides=serializer.data['chlorides']
            freesulfurdioxide=serializer.data['freesulfurdioxide']
            totalsulfurdioxide=serializer.data['totalsulfurdioxide']
            density=serializer.data['density']
            pH=serializer.data['pH']
            sulphates=serializer.data['sulphates']
            alcohol=serializer.data['alcohol']
            s=np.array([fixedacidity, volatileacidity, citricacid, residualsugar, chlorides, freesulfurdioxide, totalsulfurdioxide, density, pH, sulphates,alcohol])
            file=open('modeel.pkl','rb')
            pickled_svm=pickle.load(file)
            file.close()
            s=s.reshape(1,-1)
            respoce=pickled_svm.predict(s)
            print(int(respoce))
            return JsonResponse('The Rtating for wine with the given details is :'+str(int(respoce)),safe=False)
        return JsonResponse(serializer.errors,status=400)
    return HttpResponse('hello')
