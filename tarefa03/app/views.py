from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
        {"nome": "Williany" , "matrícula" : "2023118" , "cidade" : "Sm"},
        {"nome": "Luna" , "matrícula" : "202311820" , "cidade" : "Sm"},
        {"nome": "Maria" , "matrícula" : "2023118" , "cidade" : "Sm"},
        {"nome": "João" , "matrícula" : "1456" , "cidade" : "Sm"},
        {"nome": "Paulo" , "matrícula" : "12345" , "cidade" : "Sm"},
    ]

    context = {
        "usuarios" : lista_usuarios
    }

    return render(request, "usuarios.html", context)
