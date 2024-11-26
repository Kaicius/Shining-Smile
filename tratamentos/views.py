from django.shortcuts import render

def tratamentos_view(request):
    return render(request, 'tratamentos.html')

def ortondontia_view(request):
    return render(request, 'Ortodontia.html')

def clareamento_view(request):
    return render(request, 'clareamento.html')

def proteses_view(request):
    return render(request, 'proteses.html')

def implantes_view(request):
    return render(request, 'Implantes.html')

#Parte logada

def tratamentoslogado_view(request):
    return render(request, 'tratamentos_logado.html')

def ortondontialogado_view(request):
    return render(request, 'Ortodontia_logado.html')

def clareamentologado_view(request):
    return render(request, 'clareamento_logado.html')

def proteseslogado_view(request):
    return render(request, 'proteses_logado.html')

def implanteslogado_view(request):
    return render(request, 'Implantes_logado.html')