from django.shortcuts import render, redirect

from .models import DareExchange

from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, "home/home.html")

# =================================== DARES =============================

def dares(request):

    dares = DareExchange.objects.all()

    parameters = {
        "dares": dares
    }

    return render(request, "home/dares.html", parameters)


# =================================== CREATING DARE =============================

def create_dare(request):

    if request.method == "POST":
        
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_phone_number = request.POST.get("phone_number")
        user_deadline = request.POST.get("deadline")
        user_dare = request.POST.get("dare")

        # Creating an object

        new_dare = DareExchange(
            name = user_name,
            email = user_email,
            phone_number = user_phone_number,
            deadline = user_deadline,
            dare = user_dare
        )

        new_dare.save()

        print("new dare added successfully!")

        return redirect("dares")
    
    
    return render(request, "home/create_dare.html")

# =================================== DELETE A DARE =============================


def delete_dare(request, id):

    dare = DareExchange.objects.get(id = id)

    dare.delete()

    return redirect("dares")

# ==================================== EDIT DARE ==================

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

        return redirect("dares")


    parameters = {
        "dare": dare
    }
    
    return render(request, "home/edit_dare.html", parameters)


