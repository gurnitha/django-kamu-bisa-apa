# apps/profiles/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.profiles.models import Profile

# profile_list view
def profile_list(request):
	profiles = Profile.objects.all()
	context = {
		'profiles':profiles
	}
	return render(request, 'profiles/profile_list.html', context)


# profile_detail view
def profile_detail(request):
	return render(request, 'profiles/profile_detail.html')