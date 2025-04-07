from django.shortcuts import render #type:ignore
from django.http import JsonResponse #type:ignore
from django.views import View #type:ignore
from rest_framework.views import APIView #type: ignore
from rest_framework import status #type:ignore
from rest_framework.response import Response #type:ignore

from items.models import Item
from ...serializers import ItemSerializer
# from items.models import Item #type:ignore

import json

class Item(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        # return JsonResponse(data, safe=False)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)