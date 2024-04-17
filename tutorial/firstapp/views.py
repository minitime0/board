from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curriculum,Member

def id_check(request):
  email = request.GET.get('email')
  try:
    Member.objects.get(email=email)
  except: #가입가능
    return HttpResponse("Y")
  return HttpResponse("N")

def change(request):
  email = request.session.get('user_email')
 
  if not email:
    return redirect('/')

  method = request.method
  if method == 'GET':
    m = Member.objects.get(email=email)
    return render(request,'firstapp/change.html',{'data': m})

  email = request.POST.get('email')
  pwd = request.POST.get('pwd')
  name = request.POST.get('name')
  m = Member.objects.get(email=email)
  m.email = email
  m.pwd = pwd
  m.name =name
  m.save()
  request.session ['user_name'] = name

  return HttpResponse('''수정 완료
                      <script>
                       setTimeout(() => {
                        location = '/'
                        },5100)
                      </script>
  
  ''')


def signout(request):
  del request.session['user_email']
  del request.session['user_name']  
  request.session.flush()
  return redirect('/') 

def signin(request):
  method = request.method
  if method == 'GET':
    return render(request, 'firstapp/signin.html')
  else:
    import hashlib  
    m = hashlib.sha256()

    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    m.update(pwd.encode('utf-8'))
    pwd = m.hexdigest()
    try:
      member = Member.objects.get(email=email, pwd=pwd)
      print('정상')
      request.session['user_email'] = email 
      request.session['user_name'] = member.name 

    except:
      print('오류')
      return HttpResponse('아이디와 비밀번호를 다시 확인해주세요.') 
    return redirect('/')
    # return HttpResponse('로그인 완료')



def signup(request):
  method = request.method
  if method == 'GET':
    return render(request, 'firstapp/signup.html')
  else:
    import hashlib
    s = hashlib.sha256()

    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    name = request.POST.get('name')

    s.update(pwd.encode('utf-8'))
    pwd= s.hexdigest()

    m= Member(email=email, pwd=pwd, name=name)
    m.save()
    return redirect('/')
    # return HttpResponse('가입 완료')


def show(request):
  data = Curriculum.objects.all()
  return render(request, 'firstapp/show.html', {'name': data})


  # curriculum = Curriculum123.objects.all()
  # result = ''
  # for c in curriculum:
  #   result += c.name123 + c.age + '<br>'
  # return HttpResponse(result)

def insert(request):
  Curriculum.objects.create(name='kim')

  c = Curriculum(name='lee')
  c.save()

def index1(request):
  return HttpResponse('<u>Hello</u>')

def index2(request):
  return HttpResponse('<u>Hi</u>')

def main(request):
  return HttpResponse('<u>Main</u>')