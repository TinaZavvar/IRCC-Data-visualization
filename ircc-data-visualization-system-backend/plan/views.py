from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Plan
from django.http import JsonResponse
from rest_framework import status
from .serializer import PlanSerializer
from rest_framework.parsers import JSONParser 

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def plan_create(request):
    plan_data = JSONParser().parse(request)
    plan_serializer = PlanSerializer(data=plan_data)
    if plan_serializer.is_valid():
        plan_serializer.save()
        return JsonResponse(plan_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(plan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def plan_detail(request, plan_id):
    if plan_id == '*':
        plans = Plan.objects.all()

        plan_serializer = PlanSerializer(plans, many=True)
        return JsonResponse(plan_serializer.data, safe=False)
    else:
        try: 
            plan = Plan.objects.get(plan_id=plan_id) 
        except Plan.DoesNotExist: 
            return JsonResponse({'message': 'The plan does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # GET, Update, Delete plan by id
    if request.method == 'GET':
        plan_serializer = PlanSerializer(plan)
        return JsonResponse(plan_serializer.data)
    elif request.method == 'PUT':
        plan = Plan.objects.get(plan_id=plan_id)
        plan_serializer = PlanSerializer(instance=plan, data=request.data)
        if plan_serializer.is_valid():
            plan_serializer.save()
            return JsonResponse({'message': 'Plan were updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': plan_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            Plan.objects.get(plan_id=plan_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'Plan were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)