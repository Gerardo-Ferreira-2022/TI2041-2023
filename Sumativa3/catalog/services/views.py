from django.shortcuts import render, redirect


# Redirecting to django administrator
def index(request):
    return redirect('admin/')