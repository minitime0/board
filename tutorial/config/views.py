from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from secondapp.models import ArmyShop
from django.forms.models import model_to_dict

def home(request):
  return render(request,'home.html')




  
def text(request, ccc):
  adata = ArmyShop.objects.filter(name__contains=ccc)
  data = []
  for c in adata:
    c = model_to_dict(c)
    data.append(c)
  return JsonResponse(data, safe=False)