from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path,include
from . import views


urlpatterns = [
    path('' ,views.lajax, name="ajax"),

    # path('ajax',views.lajax,name="ajax"),
    path('save_data/',views.save_data,name="save_data"),
    path('dlt_data/<int:id>/',views.dlt_data,name="dlt_data"),
    path('edt_data/<int:id>/',views.edt_data,name="edt_data"),
    path('search_data/',views.search_data,name="search_data"),

    #for DRF
    path('em_info/<int:id>',views.emp_info,name="em_info"),
    path('em_info/',views.all_emp_info,name="em_info"),

    
    path('em_create/',views.em_create,name="em_create"),

    path('put_em/',views.put_em,name="put_em"),
    path('dlt_em/',views.dlt_em,name="dlt_em"),

]   
 