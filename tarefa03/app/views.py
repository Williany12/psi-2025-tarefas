from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
        {"nome": "Williany" , "matricula" : "1234" ,"idade": 17, "cidade" : "Santa Maria"},
        {"nome": "Luna" , "matricula" : "4321" ,"idade": 18, "cidade" : "São Tomé"},
        {"nome": "Maria" , "matricula" : "567" ,"idade": 19, "cidade" : "Los Angeles"},
        {"nome": "João" , "matricula" : "765" ,"idade": 14, "cidade" : "Natal"},
        {"nome": "Paulo" , "matricula" : "890" ,"idade": 12, "cidade" : "São Paulo"},
    ]

    context = {
        "usuarios" : lista_usuarios
    }

    return render(request, "usuarios.html", context)
