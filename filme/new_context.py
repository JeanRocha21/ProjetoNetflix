from .models import Filme

def listas_filmes_recentes(request):
    listas_filmes = Filme.objects.all().order_by('-data_criacao')
    if listas_filmes:
        filme_destaque = listas_filmes[0]
    else:
        filme_destaque = None
    return {"listas_filmes_recentes": listas_filmes, "filme_destaque": filme_destaque}

def listas_filmes_emalta(request):
    listas_filmes = Filme.objects.all().order_by('-visualizacoes')
    return {"listas_filmes_emalta": listas_filmes}