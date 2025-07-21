from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import DareExchange
from accounts.models import Student

@login_required
def dashboard(request):

    student = Student.objects.get(id = request.user.id)

    dares = DareExchange.objects.filter(student = request.user)

    parameters = {
        "student": student,
        "dares": dares
    }

    return render(request, "dashboard/index.html", parameters)

# =================================== CREATING DARE =============================

@login_required
def create_dare(request):

    if request.method == "POST":
        
        student = Student.objects.get(id = request.user.id)
        title = request.POST.get("title")
        user_deadline = request.POST.get("deadline")
        user_dare = request.POST.get("dare")

        # Creating an object

        new_dare = DareExchange(
            student = student,
            title = title,
            deadline = user_deadline,
            dare = user_dare
        )

        new_dare.save()

        print("new dare added successfully!")

        return redirect("dashboard")
    
    
    return render(request, "dashboard/create_dare.html")

# =================================== DELETE A DARE =============================

@login_required
def delete_dare(request, id):

    dare = DareExchange.objects.get(id = id)

    dare.delete()

    return redirect("dashboard")

# ==================================== EDIT DARE ==================

@login_required
def edit_dare(request, id):
    dare = DareExchange.objects.get(id = id)

    if request.method == "POST":

        dare.name = request.POST.get("name")
        dare.email = request.POST.get("email")
        dare.phone_number = request.POST.get("phone_number")
        dare.deadline = request.POST.get("deadline")
        dare.dare = request.POST.get("dare")


        dare.is_edited = True
        dare.save()

        return redirect("dashboard")


    parameters = {
        "dare": dare
    }
    
    return render(request, "dashboard/edit_dare.html", parameters)


