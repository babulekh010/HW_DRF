from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Category
from .serializers import CategorySerializers
from .permissions import IsAdminOrAllowAny


class ListCreateCategoryView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = (IsAdminOrAllowAny, )