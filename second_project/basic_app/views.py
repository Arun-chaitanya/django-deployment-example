from django.shortcuts import render
from basic_app.forms import NewUserForm
# from django.http import HttpResponse
# from basic_app.models import User


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def users(request):

    form = NewUserForm()

    if request.method == "post":
        form = NewUserForm(request.post)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('ERROR in filling FORM')
    return render(request,'basic_app/users.html',{'form':form})

    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users' : user_list}
    # return render(request,'basic_app/users.html',context = user_dict)
