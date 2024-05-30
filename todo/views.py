from django.shortcuts import render,redirect
from django.contrib import messages
from todo.models import todo_list
# Create your views here.


def tasks(request):
    records=todo_list.objects.all().order_by("-target_date")[::-1]
    context={'data':records}
    if request.method=="POST":
        task_name = request.POST.get("task_name")
        end_date=request.POST.get("end_date")
        
        task_obj=todo_list(task=task_name,target_date=end_date)
        task_obj.save()
        messages.info(request,"Your task added successfully")
        return redirect("tasks")
    return render(request,'tasks.html',context)
    

def deleteView(request,pk):
    if todo_list.objects.filter(id=pk).exists():
        obj=todo_list.objects.get(id=pk)
        obj.delete()
        #obj.save()
        messages.success(request,"You deleted task")
        return redirect("tasks")
    else:
        messages.warning(request,"No Task Found to Delete")
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
            messages.warning(request,"You enter wrong id ..!!")
            return redirect("update")
        
    return render(request,"update.html")