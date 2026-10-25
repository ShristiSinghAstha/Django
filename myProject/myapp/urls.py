from django.urls import path
from . import views
from django.urls import re_path,path

urlpatterns = [
    path('',views.home),
    # path('/about',views.about),
    path('greet_time/',views.greet_time),
    path('weather/',views.weather),
    path('menuitems/',views.menuitems),
    path('greet/<str:name>/',views.greet),
    path('menu/<str:item>/',views.menu),
    re_path(r'^user/(?P<username>[a-zA-Z0-9]+)/$', views.user_profile),
    re_path(r'^item/(?P<item_id>\d{4})/$', views.item_detail),
    re_path(r'^restaurant/(?P<category>[\w-]+)/(?P<subcategory>[\w-]*)/?$',
            views.restro_detail
            ),

    path('aboutus/', views.aboutus),
    path('marks/<str:subject>/<int:marks>/', views.marks), #ques3
    path('book/<str:book_name>/', views.book), #ques4
    re_path(r'^issue/(?P<issue_number>\d{4})/$', views.issue),
    path('studentform/', views.newform)
]
