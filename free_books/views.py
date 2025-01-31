
from rest_framework import generics
from .models import FreeBook
from .serializers import FreeBookSerializer
from .permissions import IsAdminUser  

class FreeBookListCreateView(generics.ListCreateAPIView):
    queryset = FreeBook.objects.all()
    serializer_class = FreeBookSerializer
    permission_classes = [IsAdminUser]  

class FreeBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FreeBook.objects.all()
    serializer_class = FreeBookSerializer
    permission_classes = [IsAdminUser]  
