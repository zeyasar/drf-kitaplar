from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework.generics import GenericAPIView, get_object_or_404
from kitaplar.models import Kitap, Yorum
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics, permissions
from kitaplar.api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.exceptions import ValidationError
from kitaplar.api.pagination import SmallPagination, LargePagination

class KitapListCreateView(generics.ListCreateAPIView):
    queryset=Kitap.objects.all()
    serializer_class=KitapSerializer
    permission_classes=[IsAdminOrReadOnly]
    pagination_class= LargePagination

class KitaplarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Kitap.objects.all()
    serializer_class=KitapSerializer
    permission_classes=[IsAdminOrReadOnly]


class YorumCreateAPIView(generics.CreateAPIView):
    queryset=Yorum.objects.all()
    serializer_class= YorumSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        kitap_pk=self.kwargs.get('kitap_pk')
        kitap=get_object_or_404(Kitap, pk=kitap_pk)
        kullanici = self.request.user
        yorumlar= Yorum.objects.filter(kitap=kitap, yorum_sahibi=kullanici)
        if yorumlar.exists():
            raise ValidationError('Bu kitaba sadece bir sefer yorum yapabilirsiniz!')
        serializer.save(kitap=kitap, yorum_sahibi=kullanici)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Yorum.objects.all()
    serializer_class= YorumSerializer
    permission_classes=[IsOwnerOrReadOnly]



# class KitapListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset=Kitap.objects.all()
#     serializer_class=KitapSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


