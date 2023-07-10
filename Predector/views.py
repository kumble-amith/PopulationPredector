from django.shortcuts import render
from django.http import HttpResponse
from . import user
import numpy as np

# Create your views here.


def home(request):
    return render(request,'home.html',{'name': 'Amith K Kumble '})

def predectionResult(request):
    model = user.Predict()
    year = int(request.POST['year']) 
    if year <=1922:
        return HttpResponse('''<h1>Unable to Get the Result 
        The Population is having a decreased value than Expected 
        <h1>''')
    else:
        year_transformed = model.transform(np.array(year))
        predection = (model.reverse(model.predict(year_transformed)))
        
        return render(request,'predectionResult.html',{'year': year,'value':(predection)})
    
    