from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('docontact/', docontact, name='docontact'),
    path('signin/', signin, name='signin'),
    path('signincheck/', signincheck, name='signincheck'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('dosignup/', dosignup, name='dosignup'),
    path('gallery/', gallery, name='gallery'),
    path('single/<int:pid>/', single, name='single'),
    path('addcart/<int:gid>/', addcart, name='addcart'),
    path('cartdetail/', cartdetail, name='cartdetail'),
    path('checkout/', checkout, name='checkout'),
    path('removecart/<int:rid>/', removecart, name='removecart'),
    path('myorder/', myorder, name='myorder'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
