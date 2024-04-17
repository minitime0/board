from django.shortcuts import render
from django.http import HttpResponse

def download(request):
    f = open('a.png','rb')
    res = HttpResponse(f, content_type='application/octet-stream')

    # res['content-dispoesition'] = 'attachment; filename=a.png'
    return res
    # return HttpResponse(f,content_type='application/octet-stream')

    # HttpResponse(f,content_type='image/png')

def upload1(request):
  method = request.method
  if method == 'GET':
    return render(request,'file/upload1.html')
  
  files = request.FILES.getlist('file2')
  for file in files:
    f_name = file.name
    f_size = file.size
    with open (f_name,'wb') as f:
        for chunk in file.chunks():
            f.write(chunk) 
  
   
  
  
  
  
  file = request.FILES.get('file')
  f_name = file.name
  f_size = file.size
  with open (f_name,'wb') as f:
    for chunk in file.chunks():
        f.write(chunk)

  return  HttpResponse(f'{f_name},{f_size}')