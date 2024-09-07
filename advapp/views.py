from django.shortcuts import render, redirect
from django.http import request

# Create your views here.

def main(request):
    return render(request,'index.html')