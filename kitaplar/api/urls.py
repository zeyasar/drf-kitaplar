from django.urls import path

from kitaplar.api.views import KitapListCreateView, KitaplarDetailAPIView, YorumCreateAPIView, YorumDetailAPIView


urlpatterns = [
    path('kitaplar/', KitapListCreateView.as_view(), name='kitap-listesi'),
    path('kitaplar/<int:pk>/', KitaplarDetailAPIView.as_view(), name='kitap-detay'),
    path('kitaplar/<int:kitap_pk>/yorum', YorumCreateAPIView.as_view()),
    path('yorumlar/<int:pk>/', YorumDetailAPIView.as_view(),name='yorumlar')
]