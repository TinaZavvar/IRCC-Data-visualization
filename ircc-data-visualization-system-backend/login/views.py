from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser 
from django.http import JsonResponse
from .serializer import UserProfileSerializer, UserProfileSerializerLogin, UserProfileSerializerInfo
from rest_framework import status
from .models import UserProfile
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from subscription.models import Subscription
from subscription.serializer import SubscriptionSerializer
from plan.models import Plan
from plan.serializer import PlanSerializer

# Create your views here.

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def check_login(request):
    username = request.data['username'] or None
    password = request.data['password'] or None
    # will create a free subscription when login if there's no previous data
    if username and password:
        username = username.strip()
        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if user.password == password:
            user_profile_serializer = UserProfileSerializer(user)
            token, _ = Token.objects.get_or_create(user=user)
            subscription_data = Subscription.objects.get_or_create(id=user.id)[0]
            subscription_serializer = SubscriptionSerializer(subscription_data)
            return JsonResponse({'user': user_profile_serializer.data, 'token': token.key, 'subscription': subscription_serializer.data})
        else:
            return JsonResponse({'message': 'Password Didnt Match!'}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Username or Password can not be empty!'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_register(request):
    # POST a new user
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_profile_serializer = UserProfileSerializerLogin(data=user_data)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()
            return JsonResponse(user_profile_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def user_detail(request, id):
    if id == '*':
        users = UserProfile.objects.all()

        user_profile_serializer = UserProfileSerializerInfo(users, many=True)
        return JsonResponse(user_profile_serializer.data, safe=False)
    else:
        try: 
            userProfile = UserProfile.objects.get(id=id) 
        except UserProfile.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # GET, Update, Delete user by id
    if request.method == 'GET':
        user_profile_serializer = UserProfileSerializer(userProfile)
        subscription_data = Subscription.objects.get_or_create(id=userProfile.id)[0]
        subscription_serializer = SubscriptionSerializer(subscription_data)
        return JsonResponse({'user': user_profile_serializer.data, 'subscription': subscription_serializer.data})
    elif request.method == 'PUT':
        userProfile = UserProfile.objects.get(id=id)
        user_profile_serializer = UserProfileSerializer(instance=userProfile, data=request.data)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()
            return JsonResponse({'message': 'User were updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': user_profile_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            UserProfile.objects.get(id=id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'User were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
