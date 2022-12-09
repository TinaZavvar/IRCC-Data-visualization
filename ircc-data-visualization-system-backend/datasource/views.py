from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import ImmigrationStatusData, CountryData, CategoryData, DestinationData
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializer import ImmigrationStatusDataSerializer, CategoryDataSerializer, CountryDataSerializer, DestinationDataSerializer
import base64
import csv
import io

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_immigration(request, data_id):
    if data_id == '*':
        datas = ImmigrationStatusData.objects.all()
        immigration_status_data_serializer = ImmigrationStatusDataSerializer(datas, many=True)
        return JsonResponse(immigration_status_data_serializer.data, safe=False)
    elif data_id == 'free':
        datas = ImmigrationStatusData.objects.all()[0:20]
        immigration_status_data_serializer = ImmigrationStatusDataSerializer(datas, many=True)
        return JsonResponse(immigration_status_data_serializer.data, safe=False)
    else:
        try: 
            data = ImmigrationStatusData.objects.get(id=data_id) 
        except ImmigrationStatusData.DoesNotExist: 
            return JsonResponse({'message': 'The immigration_status_data does not exist'}, status=status.HTTP_202_ACCEPTED)

    # GET, Create, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        immigration_status_data_serializer = ImmigrationStatusDataSerializer(data)
        return JsonResponse(immigration_status_data_serializer.data)
    elif request.method == 'POST':
        immigration_status_data = JSONParser().parse(request)
        immigration_status_data_serializer = ImmigrationStatusDataSerializer(data=immigration_status_data)
        if immigration_status_data_serializer.is_valid():
            immigration_status_data_serializer.save()
            return JsonResponse(immigration_status_data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(immigration_status_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        immigration_status_data = ImmigrationStatusData.objects.get(id=data_id)
        immigration_status_data_serializer = ImmigrationStatusDataSerializer(instance=immigration_status_data, data=request.data)
        if immigration_status_data_serializer.is_valid():
            immigration_status_data_serializer.save()
            return JsonResponse({'message': 'The immigration_status_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': immigration_status_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            ImmigrationStatusData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The immigration_status_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def upload_immigration(request):
    upload_file = request.data['upload_file'] or None
    decrypted = base64.b64decode(upload_file).decode('utf-8')
    with io.StringIO(decrypted) as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        upload_file_list = []
        itercars = iter(reader)
        next(itercars)
        for row in reader:
            upload_file_list.append({
                'year': row[1],
                'gender': row[2],
                'age': row[3],
                'category': row[4],
                'source': row[5],
                'address': row[6],
                'status': row[7]
            })
    immigration_status_data_serializer = ImmigrationStatusDataSerializer(data=upload_file_list, many=True)
    if immigration_status_data_serializer.is_valid():
        immigration_status_data_serializer.save()
        return JsonResponse({'message': 'The immigration_status_data was uploaded successfully!'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': immigration_status_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_category(request, data_id):
    datas = CategoryData.objects.all()
    category_data_serializer = CategoryDataSerializer(datas, many=True)
    if data_id == '*':
        datas = CategoryData.objects.all()
        category_data_serializer = CategoryDataSerializer(datas, many=True)
        return JsonResponse(category_data_serializer.data, safe=False)
    else:
        try: 
            data = CategoryData.objects.get(id=data_id) 
        except CategoryData.DoesNotExist: 
            return JsonResponse({'message': 'The category_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET, Create, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        category_data_serializer = CategoryDataSerializer(data)
        return JsonResponse(category_data_serializer.data)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_data_serializer = ImmigrationStatusDataSerializer(data=category_data)
        if category_data_serializer.is_valid():
            category_data_serializer.save()
            return JsonResponse(category_data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(category_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        category_data = CategoryData.objects.get(id=data_id)
        category_data_serializer = CategoryDataSerializer(instance=category_data, data=request.data)
        if category_data_serializer.is_valid():
            category_data_serializer.save()
            return JsonResponse({'message': 'The category_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': category_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            CategoryData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The category_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_country(request, data_id):
    datas = CountryData.objects.all()
    country_data_serializer = CountryDataSerializer(datas, many=True)
    if data_id == '*':
        datas = CountryData.objects.all()
        country_data_serializer = CountryDataSerializer(datas, many=True)
        return JsonResponse(country_data_serializer.data, safe=False)
    else:
        try: 
            data = CountryData.objects.get(id=data_id) 
        except CountryData.DoesNotExist: 
            return JsonResponse({'message': 'The country_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET, Create, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        country_data_serializer = CountryDataSerializer(data)
        return JsonResponse(country_data_serializer.data)
    elif request.method == 'POST':
        country_data = JSONParser().parse(request)
        country_data_serializer = ImmigrationStatusDataSerializer(data=country_data)
        if country_data_serializer.is_valid():
            country_data_serializer.save()
            return JsonResponse(country_data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(country_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        country_data = CountryData.objects.get(id=data_id)
        country_data_serializer = CountryDataSerializer(instance=country_data, data=request.data)
        if country_data_serializer.is_valid():
            country_data_serializer.save()
            return JsonResponse({'message': 'The country_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': country_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            CountryData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The country_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_destination(request, data_id):
    datas = DestinationData.objects.all()
    destination_data_serializer = DestinationDataSerializer(datas, many=True)
    if data_id == '*':
        datas = DestinationData.objects.all()
        destination_data_serializer = DestinationDataSerializer(datas, many=True)
        return JsonResponse(destination_data_serializer.data, safe=False)
    else:
        try: 
            data = DestinationData.objects.get(id=data_id) 
        except DestinationData.DoesNotExist: 
            return JsonResponse({'message': 'The destination_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET, Create, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        destination_data_serializer = DestinationDataSerializer(data)
        return JsonResponse(destination_data_serializer.data)
    elif request.method == 'POST':
        destination_data = JSONParser().parse(request)
        destination_data_serializer = ImmigrationStatusDataSerializer(data=destination_data)
        if destination_data_serializer.is_valid():
            destination_data_serializer.save()
            return JsonResponse(destination_data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(destination_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        destination_data = DestinationData.objects.get(id=data_id)
        destination_data_serializer = DestinationDataSerializer(instance=destination_data, data=request.data)
        if destination_data_serializer.is_valid():
            destination_data_serializer.save()
            return JsonResponse({'message': 'The destination_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': destination_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            DestinationData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The destination_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)