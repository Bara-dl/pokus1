from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from .views import ContactCreateView, ContactUpdateView, ContactDeleteView, ContactListView, Contact
from .views import my_image_view, my_file_view, my_json_view, search_contact

urlpatterns = [
    path("",
         ContactListView.as_view(),
         name="contacts_list"),
    path("con/<int:pk>/",
         DetailView.as_view(template_name="contact_detail.html",
                                         model=Contact),
         name="contact_detail"),
    path("create/", ContactCreateView.as_view(), name="contact_create"),
    path("update/<int:pk>/", ContactUpdateView.as_view(), name="contact_update"),
    path("delete/<int:pk>/", ContactDeleteView.as_view(), name="contact_delete"),
    path('download/', my_file_view, name='file_view'),
    path('download_img/', my_image_view, name='img_view'),
    path('json/', my_json_view, name='json_view'),
    path('search/', search_contact, name='search'),

    re_path(r'^con/.*$', ContactListView.as_view(), name='catch_all_news'),
]
