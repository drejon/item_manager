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

class ItemDetail(APIView):
    def get(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def delete(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        item.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)