from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup_view, name = "signup"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('my-page/', mypage, name = "my-page"),
    path('my-post', mypost, name = "my-post"),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)