"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def 함수(request):
    return HttpResponse ("안녕")

def emp(request):
    html = ''
    import pymysql
    conn = pymysql.connect(
            host='127.0.0.1', user='root', password='1234', port=3306, db='human', charset='utf8'
    )
    cursor = conn.cursor()
    sql = '''SELECT * FROM emp'''
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        html += f'<u>{row[2]}</u><br>'
    cursor.close()
    conn.close()
    print(html)

    return HttpResponse (html)

def lotto(request):
    import requests
    address = 'https://dhlottery.co.kr/gameResult.do?method=byWin' 
    res = requests.get(address) 						
    from bs4 import BeautifulSoup as bs
    soup = bs(res.text)
    nums = soup.select('.ball_645')
    num2 = [n.next for n in nums]
    return HttpResponse (' ,'.join(num2))

urlpatterns = [
    path("admin/", admin.site.urls),
    path("a/",함수),
    path("emp/",emp),
    path("lotto/",lotto),

]
