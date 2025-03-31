from django.shortcuts import render #type:ignore
from django.http import JsonResponse #type:ignore
from django.views import View #type:ignore
from rest_framework.views import APIView
from rest_framework import status #type:ignore
from rest_framework.response import Response #type:ignore

from items.models import Item
from .serializers import ItemSerializer
# from items.models import Item #type:ignore

import json

class ItemAPI(APIView):
    def get(self, request):
        items = Item.objects.all()
        data = json.dumps({'message': 'Hello'})
        serializer = ItemSerializer(items, many=True)
        # return JsonResponse(data, safe=False)
        return Response(serializer.data)

class ItemDetailAPI(APIView):
    def get(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
# Create your views here.
