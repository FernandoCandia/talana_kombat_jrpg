import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kombat import services as kombat_services


def simulate_kombat(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and "json_file" in request.FILES:
        json_file = request.FILES["json_file"]
        try:
            decoded_json = json.loads(json_file.read())
            kombat_result = kombat_services.get_kombat_result(kombat_data=decoded_json)
            print(kombat_result)
            return render(
                request,
                template_name="kombat/simulate_kombat.html",
                context={"kombat_result": kombat_result}
            )
        except json.JSONDecodeError:
            return render(
                request,
                template_name="kombat/invalid_json_error.html",
                context={"message": "El archivo no es un JSON válido."}
            )
    elif request.method == "POST":
        return render(
            request,
            template_name="kombat/invalid_json_error.html",
            context={"message": "Debe seleccionar un archivo JSON."}
        )

    return render(request, template_name="kombat/load_json_file.html")
