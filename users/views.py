from .helpers import send_otp_to_phone
from .models import Profiles
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# @api_view(["GET"])
# def logout_user(request):
#     request.user.auth_token.delete()
#     logout(request)
#     return Response('User Logged out successfully')
#
#
# @api_view(['POST'])
# def login_user(request):
#     data = request.data
#     print(data)
#     login = data['username']
#     password = data['password']
#
#     if not login:
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Login requested'
#         })
#     if not password:
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Password requested'
#         })
#
#     user = authenticate(username=login, password=password)
#     print(user)
#     if not user:
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Wrong user'
#         })
#
#     token = Token.objects.get_or_create(user=user)[0].key
#     return Response(
#         {
#             "token": token
#         }
#     )
#
#
# @api_view(['POST'])
# def register_user(request):
#     data = request.data
#
#     login = data['username']
#     password = data['password']
#
#     if not login:
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Login talab etiladi'
#         })
#     if not password:
#         return Response({
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Parol talab etiladi'
#         })
#
#     user = authenticate(username=login, password=password)
#
#     if user:
#         return Response({
#             'status': 400,
#             'message': 'There is such a user.'
#         })
#
#     try:
#         user = User.objects.create(
#             username=login,
#             password=password
#         )
#     except Exception as e:
#         return Response({
#             'status': 400,
#             'message': 'Error found while creating an user'
#         })
#     token = Token.objects.get_or_create(user=user)[0].key
#     return Response({
#         'message': 'User added',
#         "token": token,
#         "is_admin": user.is_staff
#     }, status=status.HTTP_201_CREATED)
#

class ProfilesView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ProfilesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    filterset_fields = ['full_name', 'user']
    search_fields = ['-full_name']
    ordering_fields = '__all__'
    pagination_class = None


class TeachersView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = TeacherSerializer

    pagination_class = None
class TeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = TeacherSerializer
    filterset_fields = 'full_name', 'user'
    search_fields = ['-full_name']
    ordering_fields = '__all__'



class validateOTP(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone_number', False)
        otp_sent = request.data.get('otp', False)


@api_view(['GET'])
def logout_user(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User logged out successfully')

@api_view(['POST'])
def login_user(request):
    data = request.data
    phone = request.data.get('phone_number')
    sms = data.get('sms')
    if phone is None:
        return Response({
            'status': 400,
            'message': 'Phone number required'
        })

    if not phone.isdigit() or len(phone) != 12:
        return Response({
            'status': 400,
            'message': 'Phone has to be in +9981234567 format'
        })
    try:
        user = Profiles.objects.get(phone_number=phone)
    except Exception as e:
        return Response({
            'status': 400,
            'message': 'Wrong number'
        })
    try:
        token = Token.objects.get_or_create(user=user)[0].key

    except Exception as e:
        print(e)

    if sms is None:
        return Response({
            'status': 400,
            'message': 'Sms is required'
        })
    if len(sms) != 6:
        return Response({
            'status': 400,
            'message': 'Sms consists of 6 number digits'
        })

    try:
        user = Profiles.objects.get(phone_number=phone, otp=sms)
        user.is_phone_verified = True
        user.save()
    except Exception as e:
        return Response({
            'status': 400,
            'message': 'SMS pr phone number is wrong'
        })

    # token = Profiles.objects.create(user=user)
    if user.is_active:
        login(request, user)
        return Response({
            'status': 200,
            'user_id': user.id,
            'token': token,
            'is_admin': user.is_staff,
            'phone': phone,
            'user_name': user.full_name,
        })
    else:
        return Response({
            'status':400,
            'message': 'User is not active'
        })

@api_view(['POST'])
def register_user(request):
    data = request.data
    full_name = data.get('full_name')
    phone = data.get('phone_number')
    tmp_password = data.get('phone_number', None)
    if tmp_password:
        password = tmp_password
    else:
        password = phone
    if full_name is None:
        return Response({
            'status': 400,
            'message': 'Name required'
        })
    if phone is None:
        return Response({
            'status': 400,
            'message': 'Phone number required'
        })
    if not phone.is_digit() or len(phone) != 12:
        return Response({
            'status': 400,
            'message': "Phone must be in +998981234567 format"
        })
    try:
        user = Profiles.objects.get(phone_number=phone)
    except Exception as e:
        pass

    if user:
        return Response({
            'status': 400,
            'message': 'User found'
        })
    if password is None:
        return Response({
            'status': 400,
            'message': "Password required"
        })
    try:
        sms = send_otp_to_phone(phone)
        if not sms:
            return Response({
                'status': 400,
                'message': "Error while sending the sms, try again please"
            })
        user = Profiles.objects.create(
            phone_number=phone,
            password =password,
            firs_name=full_name,
            otp=sms
        )
    except Exception as e:
        return Response({
            'status': 400,
            'message': 'Found and error while creating the user, try again please'
        })
    return Response({
        'status': 200,
        'message': 'Sms sent',
        'user': user.id,
        'sms': sms,
        'is_admin': user.is_staff,
        'phone': phone,
        'user_name': full_name
    })

@api_view(['POST'])
def send_sms(request):
    data = request.data
    phone = request.data.get('phone_number')

    if phone is None:
        return Response({
            'status': 400,
            'message': 'Telefon raqam talab etiladi'
        })

    if not phone.isdigit() or len(phone) != 12:
        return Response({
            'status': 400,
            'message': "Telefon raqam 998971234567 formatida bo'lishi kerak"
        })
    user = None
    try:
        user = Profiles.objects.get(phone_number=phone)
    except Exception as e:
        return Response({
            'status': 400,
            'message': "Bunday foydalanuvchi mavjud emas. Ro'yxatdan o'ting"
        })

    sms = send_otp_to_phone(phone)
    if not sms:
        return Response({
            'status': 400,
            'message': 'SMS yuborishda xatolik. Qayta yuboring'
        })
    user.otp = sms
    user.save()
    return Response({
        'status': 200,
        'message': 'SMS yuborildi',
        'user_id': user.id,
        'sms': sms
    })
