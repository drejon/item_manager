from django.shortcuts import render #type:ignore
from django.http import JsonResponse #type:ignore
from django.views import View #type:ignore
from rest_framework import status #type:ignore
from rest_framework.response import Response
from items.models import Item #type:ignore

import json

class ItemAPI(view):
    def get(self, request):
        items = []
        return Response(items, status=status.HTTP_200_OK)

# Create your views here.
