from  django.urls import path
from . import  views



urlpatterns = [

   path('',views.firstpage),
   path('login',views.login_request,name="login"),
  path("register", views.register_request, name="register"),
  path("saveinfo", views.saveinfo),
    path("whyblood", views.whyblood),
    path("eligibility", views.eligibility),
    path("tips", views.tips),
    path("happen", views.happen),
    path("donarlist", views.donarlist),
    path("search", views.search),
    path("O+", views.o_positive),
    path("O-", views.o_negative),
    path("A+", views.a_positive),

    path("A-", views.a_negative),
    path("B+", views.b_positive),

    path("B-", views.b_negative),
    path("AB+", views.ab_positive),

    path("AB-", views.ab_negative),

]