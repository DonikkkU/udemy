
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class SitePagination(PageNumberPagination):
    page_size = 3

class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LimitOffsetPagination
    filterset_fields = ['name']
    search_fields = ['^name']


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CategoryPagination(PageNumberPagination):
    page_size = 3

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = '__all__'
    search_fields = ['^title']
    ordering_fields = ['title']
    pagination_class = CategoryPagination


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderPagination(LimitOffsetPagination):
    page_size = 3

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    search_fields = "__all__"
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    pagination_class = OrderPagination

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class HomeworkPagination(LimitOffsetPagination):
    page_size = 1

class HomeworkView(generics.ListCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    pagination_class = HomeworkPagination
    filterset_fields = ["student"]
    search_fields = ["^student"]


class HomeworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSerializer

class ThemePagination(PageNumberPagination):
    page_size = 3

class ThemeView(generics.ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filterset_fields = ['name']
    search_fields = ["^name"]
    pagination_class = ThemePagination
    ordering_fields = ['name']

class ThemeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filterset_fields = ['name']
    search_fields = ["^name"]
    ordering_fields = ['name']

class ThemeUserView(generics.ListCreateAPIView):
    queryset = Theme_user.objects.all()
    serializer_class = ThemeUserSerializer
    filterset_fields = ['student', "theme"]
    search_fields = ["student"]

class ThemeUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theme_user.objects.all()
    serializer_class = ThemeUserSerializer














# from rest_framework import status
#
# from .models import Course, Category
# from .serializers import CourseSerializer, CategorySerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
#
# @api_view(['GET', 'POST', 'PUT'])
# def course(request):
#     if request.method == 'GET':
#         projects = Course.objects.all()
#         serializer = CourseSerializer(projects, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def course_detail(request, pk):
#     try:
#         course = Course.objects.get(pk=pk)
#     except Course.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST', 'PUT'])
# def category(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
