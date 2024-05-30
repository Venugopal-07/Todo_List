from django.shortcuts import render,redirect
from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, logout, login
from todo.models import todo_list
# Create your views here.

# def home(request):
#     if request.user.is_authenticated:
#         messages.warning(request,"You Fool you already Logged in")
#         return redirect("tasks")

#     if request.method=="POST":
#         user_name = request.POST.get("username")
#         pass_word=request.POST.get("password")
#         #print(user_name,pass_word)
#         user = authenticate(request, username=user_name, password=pass_word, is_active=True)
#         print(user.last_name)
#         if user is not None:
#             login(request,user)
#             messages.success(request,"Hey Hero {} U are successfuly logged in".format(user.username))
#             return redirect("tasks")
#         else:
#             messages.error(request,"Wrong Credentials or Not Active User")
#             return render(request,"login.html")
#         #return render(request,"login.html")
#     return render(request,'login.html')

#@login_required(login_url="login")
def tasks(request):
    records=todo_list.objects.all().order_by("-target_date")[::-1]
    context={'data':records}
    if request.method=="POST":
        task_name = request.POST.get("task_name")
        end_date=request.POST.get("end_date")
        print(task_name,end_date)
        task_obj=todo_list(task=task_name,target_date=end_date)
        task_obj.save()
        messages.info(request,"Your task added successfully")
        return redirect("tasks")
    return render(request,'tasks.html',context)


# def logoutView(request):
#     logout(request)
#     messages.warning(request,"You Left from Session")
#     return redirect("login")
    

def deleteView(request,pk):
    if todo_list.objects.filter(id=pk).exists():
        obj=todo_list.objects.get(id=pk)
        obj.delete()
        #obj.save()
        messages.success(request,"You deleted task")
        return redirect("tasks")
    else:
        messages.error(request,"No Task Found to Delete")
        return redirect("tasks")
    
def editView(request):
    if request.method=="POST":
        update_name=request.POST.get("task_name")
        pk=request.POST.get("task_id")
        if todo_list.objects.filter(id=pk).exists():
            obj=todo_list.objects.get(id=pk)
            obj.task=update_name
            obj.save()
            messages.success(request,"task with id {} is updated with given content".format(pk))
            return redirect("tasks")
        else:
            messages.error(request,"Niku Kavalsindhi Na dagara ledhu..!!")
            return redirect("update")
        
    return render(request,"update.html")