from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Course, ArmyShop
from django.core.paginator import Paginator

def army_shop2(request, year, month):
  army_shop = ArmyShop.objects.filter(year=year, month=month)
  return render(
    request, 'secondapp/army_shop.html', 
    {'data': army_shop})

def army_shop(request):
  page = request.GET.get('page')
  if not page: page = '1'

  prd = request.GET.get('prd')
  if not prd: prd = ''
   # army_shop = ArmyShop.objects.all()
  army_shop = ArmyShop.objects.filter(name__contains = prd).order_by('-id')

  p = Paginator(army_shop,10)
  total_page = p.num_pages
  army_shop = p.page(page)
  start = (int(page)-1) // 10 * 10 + 1
  end = start + 9
  
  # 10페이지 나타내기
  # if int(page) % 10 == 0:
  #   start -=10
  # result += 145 - %s<hr>' % p.num_pages
  #              148 150
  end2 = min(total_page,end)

  return render (request, 'secondapp/army_shop.html',{'data': army_shop,'start': start,'end':end,'nums':range(start,end2 + 1),'total_page':total_page}
 )

def show(request):
  course = Course.objects.all()
  return render(
    request, 'secondapp/show.html', 
    {'data': course})

def insert(request):
  Course.objects.create(name='데이터 분석', cnt=30)
  c = Course()
  c.name = '데이터 수집'
  c.cnt = 20
  c.save()
  Course(name='웹개발', cnt=25).save()
  Course(name='인공지능', cnt=20).save()
  return HttpResponse('입력 완료')

def main(request):
  return HttpResponse('<u>Main</u>')

def json(request):
  d = {
    'name': 'AA',
    'age': 30,
    'address' : 'sejong'
  }
  return JsonResponse(d)
