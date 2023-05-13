from django.shortcuts import render
from django.views.generic import View
from calculation.forms import OperationForm

# Create your views here.

class Indexview(View):
    def get(self,request):
        return render(request,"home.html")


class Addview(View):
    def get(self,request,):
        form=OperationForm()
        return render(request,"add.html",{"form":form})

    def post(self,request):
        if request.method=="POST":
            # n1=int(request.POST.get("num1"))
            # n2=int(request.POST.get("num2"))
            form=OperationForm(request.POST)
            if form.is_valid():
                n1=(form.cleaned_data.get("num1"))
                n2=(form.cleaned_data.get("num2"))
                result=int(n1)+int(n2)
                return render(request,"add.html",{"result":result})
            else:
                return render(request,"add.html",{"form":form})

class Subview(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"sub.html",{"form":form})

    def post(self,request):
        if request.method=="POST":
            # n1=int(request.POST.get("num1"))
            # n2=int(request.POST.get("num2"))
            form=OperationForm(request.POST)
            if form.is_valid():
                n1=int(form.cleaned_data.get("num1"))
                n2=int(form.cleaned_data.get("num2"))
                result=n1-n2
                return render(request,"sub.html",{"result":result})

class Mulview(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"mul.html",{"form":form})

    def post(self,request):
        if request.method=="POST":
            # n1=int(request.POST.get("num1"))
            # n2=int(request.POST.get("num2"))
            form=OperationForm(request.POST)
            if form.is_valid():
                n1=int(form.cleaned_data.get("num1"))
                n2=int(form.cleaned_data.get("num2"))
                result=n1*n2
                return render(request,"mul.html",{"result":result})

class Divview(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"div.html",{"form":form})

    def post(self,request):
        if request.method=="POSt":
            # n1=int(request.POST.get("num1"))
            # n2=int(request.POST.get("num2"))
            form=OperationForm(request.POST)
            if form.is_valid():
                n1=int(form.cleaned_data.get("num1"))
                n2=int(form.cleaned_data.get("num2"))
                result=n1/n2
                return render(request,"div.html",{"result":result})


def add(request):
    print(request.method)
    if request.method=="POST":
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=n1+n2
        return render(request,"add.html",{"result":result})
    return render(request,"add.html")

def sub(request):
    if request.method=="POST":
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=(n1-n2)
        return render(request,"sub.html",{"result":result})
    return render(request,"sub.html")

def mul(request):
    if request.method=="POST":
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=(n1*n2)
        return render(request,"mul.html",{"result":result})
    return render(request,"mul.html")

def div(request):
    if request.method=="POST":
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=(n1/n2)
        return render(request,"div.html",{"result":result})
    return render(request,"div.html")

def vowels(request):
    if request.method=="POST":
        word=request.POST.get("word")
        vowels=[char for char in word if char in["a","e","i","o","u"]]
        return render(request,"vowels.html",{"result":vowels})
    return render(request,"vowels.html")

