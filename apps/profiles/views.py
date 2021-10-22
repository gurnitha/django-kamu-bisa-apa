# apps/profiles/views.py

# Django modules
from django.shortcuts import render


# profile_list view
def profile_list(request):
	return render(request, 'profiles/profile_list.html')


# profile_detail view
def profile_detail(request, pk):
	return render(request, 'profiles/profile_detail.html')