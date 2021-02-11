# Create your views here.
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from .serializer import TokensSerializer
from .models import Tokens
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

import secrets
 
@api_view(['POST'])
def generate_token(request):
    if request.method =='POST':
        token  = secrets.token_hex(32) 
        token_serializer = TokensSerializer(data = {'token':token } )
        if token_serializer.is_valid():
            token_serializer.save()
            return JsonResponse({ 'status' : 0 , 'token':token }, status=status.HTTP_201_CREATED)
        return JsonResponse(token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    



@api_view(['DELETE'])
def delete_token(request, token=None):
        try:
            if request.method == 'DELETE':
                token = get_object_or_404(Tokens.objects.all() ,token=token)
                token.delete()   
                return JsonResponse({ 'status' : 0,'message' : 'Deleted!!' }, status=200)
        except Exception as e:
            return JsonResponse( { 'status' : 0,'message' : 'Not Found!!' }, status=status.HTTP_404_NOT_FOUND) 


@api_view(['POST'])
def assign_token(request):
    token = None
    try:
    	if request.method == 'POST': 
            token = Tokens.objects.filter(is_block=False).order_by("?").first()
            data = {} 
            if token:       
                data['is_block'] = True
                data['token'] = token.token
                import time
                curr_time  = int(time.time()) + 20 
                data['live_till'] = curr_time
                token_serializer = TokensSerializer(instance =token , data=data)
                if token_serializer.is_valid(raise_exception=True):
                    savetoken = token_serializer.save()
                    return JsonResponse({ 'status' : 0,'token' : savetoken.token }, status=200)
            else:
                return JsonResponse(token_serializer.errors, status=status.HTTP_404_NOT_FOUND) 
    except Exception as e:
        return JsonResponse( { 'status' : 1,'message' : e }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def unblock_token(request,token=None):
    try:
        if request.method == 'POST': 
            token = Tokens.objects.filter(is_block=True,token=token).first()
            if token:
                data = {}
                data['is_block'] = False
                data['token'] = token.token       
                token_serializer = TokensSerializer(instance =token , data=data)
                if token_serializer.is_valid(raise_exception=True):
                    token_obj = token_serializer.save()
                    return JsonResponse({ 'status' : 0,'token' : token.token,'Message':'Token has been released.' }, status=200)
    except Exception as e:
        return JsonResponse( { 'status' : 0,'message' : 'Not Found!!' }, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def keep_alive_token(request,token=None):
    try:
        if request.method == 'POST':
            token_obj = Tokens.objects.get(token=token , is_block = True)
            data = {'token':token}
            if token_obj:       
                generated_time  = token_obj.generated
                live_till       = token_obj.live_till 
                import time
                curr_time  = int(time.time())
                message = ''
                if not token_obj.is_block and (curr_time - generated_time) > 300  : 
                    token_obj.delete()
                    return JsonResponse({ 'status' : 0,'token' : token,'Message':'Token has already been expired!!.' }, status=200)
                elif(live_till - curr_time) > 0 : 
                    data['live_till'] =  curr_time + 60 ;
                    message = 'Token is alive!!.'
                elif ( live_till - curr_time) <= 0:
                    data['is_block'] = False
                    data['live_till'] = None 
                    message = 'Token is freed/released!!.'
                token_serializer =  TokensSerializer(instance=token_obj , data=data)
                if token_serializer.is_valid(raise_exception=True):
                    savetoken = token_serializer.save()
                    return JsonResponse({ 'status' : 0,'token' : savetoken.token,'Message':message }, status=200)
    except Exception as e:
        return JsonResponse( { 'status' : 0,'message' : e }, status=status.HTTP_404_NOT_FOUND)



