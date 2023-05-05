from django.views import generic
from . import models
from django.shortcuts import render
from .forms import ClientsForm


class Client(generic.CreateView):
    template_name = "spasibo.html"
    form_class = ClientsForm
    success_url = "/"

    def form_valid(self, form):
        return super(Client, self).form_valid(form=form)


def home(request):
    img = models.Slaider.objects.all()
    new = models.News.objects.all()
    inai = models.Inai.objects.all()
    foot = models.Foot.objects.all()
    context = {
        "img": img,
        "new": new,
        "inai": inai,
        "foot": foot,
    }
    return render(request, "post_list.html", context)


def service(request):
    children = models.Forchildren.objects.all()
    man = models.Forman.objects.all()
    foot = models.Foot.objects.all()
    context = {"children": children, "man": man, "foot": foot}
    return render(request, "usluga.html", context)
