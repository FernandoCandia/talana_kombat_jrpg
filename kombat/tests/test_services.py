from kombat.services import get_kombat_result


def test_get_kombat_result():
    kombat_data = {
       "player1":{
          "movimientos": [
             "D",
             "DSD",
             "S",
             "DSD",
             "SD"
          ],
          "golpes": [
             "K",
             "P",
             "",
             "K",
             "P"
          ]
       },
       "player2":{
          "movimientos": [
             "SA",
             "SA",
             "SA",
             "ASA",
             "SA"
          ],
          "golpes": [
             "K",
             "",
             "K",
             "P",
             "P"
          ]
       }
    }
    expected_result = [
        "Tonyn Stallone se mueve y da una patada.",
        "Arnaldor Shuatseneguer conecta un Remuyuken.",
        "Tonyn Stallone conecta un Taladoken.",
        "Arnaldor Shuatseneguer se mueve.",
        "Tonyn Stallone se mueve.",
        "Arnaldor Shuatseneguer conecta un Remuyuken.",
        "Arnaldor Shuatseneguer gana la pelea y aún le queda 2 de energía!",
    ]

    result = get_kombat_result(kombat_data)

    assert result == expected_result
