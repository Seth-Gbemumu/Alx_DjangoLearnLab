from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'



@user_passes_test(is_member)
def member_view(request):
    return render(request, template_name='relationship_app/member_view.html')
