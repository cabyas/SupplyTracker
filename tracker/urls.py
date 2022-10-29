from django.urls import path

from tracker import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        'token/<str:contract_address>',
        views.TokenDetailView.as_view(),
        name='details')
    # path('language/<int:pk>/', views.LanguageDetailView.as_view(), name='language_detail'),
    # path('language/create/', views.LanguageCreateView.as_view(), name='language_create'),
    # path('language/update/<int:pk>/', views.LanguageUpdateView.as_view(), name='language_update'),
    # path('language/delete/<int:pk>/', views.LanguageDeleteView.as_view(), name='language_delete')
]
