from .models import Filme, usuarios
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse, render
from .forms import CriarContaForm, FormHome

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:Homefilmes')

        return super().get(self, request, *args, **kwargs) #redireciona para homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuario = usuarios.objects.filter(email=email)
        if usuario:
            return reverse("filme:login")
        else:
            return reverse("filme:criarconta")

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme

class Detalhesfilmes(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes +=1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)

        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context["filmes_relacionados"] = filmes_relacionados

        return context
class pesquisafilmes(LoginRequiredMixin, ListView):
    template_name = "pesquisafilmes.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')

        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class editarperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = usuarios
    fields = ["first_name", "last_name", "email"]

    def get_success_url(self):
        return reverse('filme:homefilmes')


class criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('filme:login')
