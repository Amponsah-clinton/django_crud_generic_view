from django.urls import path
from geeks.views import TemplateViews, form_view, ListView, Updateview, Deleteview

urlpatterns = [
    path('', TemplateViews.as_view()),
    path('form_view', form_view.as_view(), name ='form_view'),
    path('list_view', ListView.as_view(), name ='list_view'),
    path('update_view<pk>', Updateview.as_view(), name ='update'),
    path('delete/<pk>', Deleteview.as_view(), name ='delete'),
]
