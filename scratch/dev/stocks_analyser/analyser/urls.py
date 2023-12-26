from django.urls import path
from . import views,customer_views

urlpatterns=[
    path('',views.analyser, name='analyser'),
    path('upload/',views.upload, name='upload'),

    path('equity/',views.equity, name='equity'),
    path('equity_upload/',views.equity_file_upload_v2,name='equity_upload'),
    path('delete_equity_file/',views.delete_equity_file,name='delete_equity_file'),
    path('equity_files/',views.equity_files,name='equity_files'),
    path('equity_filter/',views.equity_filter,name='equity_filter'),
    path('equity_view_file/<str:equity_file_name>/',views.equity_view_file,name='equity_view_file'),
    path('equity_file_select/',views.equity_file_select,name='equity_file_select'),
    path('equity_create_filer/',views.equity_create_filer,name='equity_create_filer'),
    path('equity_create_filer_temp_store/',views.equity_create_filer_temp_store,name='equity_create_filer_temp_store'),

    path('equity_analyser/',views.equity_analyser,name='equity_analyser'),

    path('customer/',customer_views.customer,name='customer'),
    path('add_customer/',customer_views.add_customer,name='add_customer'),
    
]