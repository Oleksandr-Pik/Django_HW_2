from django.http import HttpRequest, HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render

def hello_by_name(request: HttpRequest, name: str | None = None):
    if name is not None:
        return HttpResponse(f"<h1>Hello, {name}</h1>")
    else:
        return HttpResponse(f"<h1>Hello</h1>")

def json(request: HttpRequest):
    return JsonResponse({"Nmae": "Test"})

def file(request: FileResponse):
    return FileResponse(
        open(r"D:\Python\Django_Projects\HW_2\project\test.txt", "rb"), 
        as_attachment=True
    )

def math(request: HttpRequest, num1: int, num2: int):
    result = num1 + num2

    context = {
        "num1": num1,
        "num2": num2,
        "result": result
    }
    return render(request, "main/index.html", context)
