from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'



@user_passes_test(is_admin)
def admin_view(request):
    return render(request, template_name='relationship_app/admin_view.html')
