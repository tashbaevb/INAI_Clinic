from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import CommentForm
from .models import Comment


def contact(request):
    kontakt = models.Contacts.objects.all()
    return render(request, "contact.html", {"kontakt": kontakt})


def about(request):
    abouts = models.About.objects.all()
    return render(request, "about_us.html", {"abouts": abouts})


def doctors_all(request):
    doctor = models.Doctors.objects.all()
    return render(request, "doctors.html", {"doctor": doctor})


def doctors_more(request, id):
    more1 = get_object_or_404(models.Doctors, id=id)
    error = ""
    comment = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctors")
        else:
            error = "incorrect form"
    form = CommentForm
    context = {"form": form, "error": error, "comment": comment, "more1": more1}
    return render(request, "vrach.html", context)
