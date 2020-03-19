from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
import os
import subprocess


# Create your views here.

def home(request):
    curr_url = "home"
    return render(request,'index.html',{"url":curr_url})

def detect(request):
    curr_url="detect"
    return render(request,'detect.html')

def camera(request):
    a=os.chdir("../../../")
    curr = os.getcwd()
    new_path = curr + "/pro/facedetection"
    os.chdir(new_path)
    print(os.getcwd())
    os.system("python detect_face_video.py")
    return render(request,'detect.html')

