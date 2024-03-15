import pytest

from django.urls import reverse
from io import BytesIO


@pytest.mark.parametrize(
    "file_content, expected_template, expected_context",
    [
        (b'{"player1": {"movimientos": [], "golpes": []}, "player2": {"movimientos": [], "golpes": []}}',
         "kombat/simulate_kombat.html",
         {"kombat_result": ["Resultado de la simulación"]}),
        (b'',
         "kombat/invalid_json_error.html",
         {"message": "El archivo no es un JSON válido."}),
        (b'',
         "kombat/invalid_json_error.html",
         {"message": "Debe seleccionar un archivo JSON."}),
    ],
)
def test_simulate_kombat(client, file_content, expected_template, expected_context, mocker):
    mocker.patch(
        "kombat.views.kombat_services.get_kombat_result",
        return_value=["Resultado de la simulación"]
    )

    response = client.post(
        reverse("simulate_kombat"),
        {"json_file": BytesIO(file_content)},
        format="multipart"
    )

    assert response.status_code == 200
    assert response.templates[0].name == expected_template
