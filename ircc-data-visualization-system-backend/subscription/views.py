from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from django.http import JsonResponse
from rest_framework import status
from .serializer import SubscriptionSerializer

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def subscription_detail(request, user_id):
    try: 
        subscription = Subscription.objects.get(user_id=user_id) 
    except Subscription.DoesNotExist: 
        return JsonResponse({'message': "The user's subscription does not exist"}, status=status.HTTP_404_NOT_FOUND)
    subscription_serializer = SubscriptionSerializer(subscription)
    return JsonResponse(subscription_serializer.data, safe=False)

@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def subscription_update(request, sub_id):
    try: 
        subscription = Subscription.objects.get(id=sub_id) 
    except Subscription.DoesNotExist: 
        return JsonResponse({'message': "The user's subscription does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    plan_id = request.data['plan_id'] or None
    expire_date = request.data['expire_date'] or None

    try:
        subscription.plan_id = plan_id
        subscription.expire_date = expire_date
        subscription.save()
        return JsonResponse({'message': 'Subscription were updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
