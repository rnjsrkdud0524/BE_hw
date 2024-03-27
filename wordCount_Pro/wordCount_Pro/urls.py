"""
URL configuration for wordCount_Pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from wordCountApp import views      #wordCountApp에 있는 views를 사용하겠다는 의미
#views.py에 있는 함수를 사용하기 위해 내가 사용하는 모듈에 대해 알려줘야 함
#하나의 .py 파일은 모듈이며, 모듈을 포함하는 디렉토리는 패키지라고 함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),     #urls.py의 urlpatterns 리스트에 추가
#도메인 뒤에 붙는 path부분에 아무것도 붙지 않은 url을 의미하며,
#wordCountApp의 views.py에서 정의한 index 함수를 실행하고 이 path의 이름은 "index"라고 할게(가급적 함수 이름과 name일치시키기)
    path('wordCount/', views.wordCount, name="wordCount"),
    path('result/', views.result, name="result"),
#urls.py에서 설정한 name이 template언어에서 사용된다
]