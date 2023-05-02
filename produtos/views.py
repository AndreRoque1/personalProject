from django.shortcuts import render

def vender(request):
    return render(request, 'venderProdutos.html')
