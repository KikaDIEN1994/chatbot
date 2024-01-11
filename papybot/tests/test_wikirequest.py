from papybot.wikirequest import WikiRequest


class MockResponse1:
    @staticmethod
    def json():
        return {
            "batchcomplete": "",
            "query": {
                "geosearch": [
                    {
                        "pageid": 14307238,
                        "ns": 0,
                        "title": "Esplanade des Ouvriers-de-la-Tour-Eiffel",
                        "lat": 48.85834,
                        "lon": 2.29445,
                        "dist": 4.1,
                        "primary": "",
                    },
                    {
                        "pageid": 1359783,
                        "ns": 0,
                        "title": "Tour Eiffel",
                        "lat": 48.858296,
                        "lon": 2.294479,
                        "dist": 8.2,
                        "primary": "",
                    },
                    {
                        "pageid": 4641538,
                        "ns": 0,
                        "title": "Le Jules Verne",
                        "lat": 48.85825,
                        "lon": 2.2945,
                        "dist": 13.4,
                        "primary": "",
                    },
                    {
                        "pageid": 1869201,
                        "ns": 0,
                        "title": "Exposition universelle de 1889",
                        "lat": 48.8583,
                        "lon": 2.29417,
                        "dist": 24.1,
                        "primary": "",
                    },
                    {
                        "pageid": 14958049,
                        "ns": 0,
                        "title": "Sur la route des chefferies du Cameroun",
                        "lat": 48.8583,
                        "lon": 2.29417,
                        "dist": 24.1,
                        "primary": "",
                    },
                    {
                        "pageid": 5828872,
                        "ns": 0,
                        "title": "Buste de Gustave Eiffel par Antoine Bourdelle",
                        "lat": 48.85869444,
                        "lon": 2.29444444,
                        "dist": 36.2,
                        "primary": "",
                    },
                    {
                        "pageid": 2689115,
                        "ns": 0,
                        "title": "Rives de la Seine à Paris",
                        "lat": 48.85889,
                        "lon": 2.29333,
                        "dist": 102.2,
                        "primary": "",
                    },
                    {
                        "pageid": 5422123,
                        "ns": 0,
                        "title": "Avenue Gustave-Eiffel",
                        "lat": 48.857388,
                        "lon": 2.29463,
                        "dist": 109.7,
                        "primary": "",
                    },
                    {
                        "pageid": 5422017,
                        "ns": 0,
                        "title": "Allée Jean-Paulhan",
                        "lat": 48.859347,
                        "lon": 2.295585,
                        "dist": 135.3,
                        "primary": "",
                    },
                    {
                        "pageid": 14307333,
                        "ns": 0,
                        "title": "Quai Jacques-Chirac",
                        "lat": 48.8597,
                        "lon": 2.2943,
                        "dist": 148.5,
                        "primary": "",
                    },
                ]
            },
        }


class MockResponse2:
    @staticmethod
    def json():
        return {
            "batchcomplete": "",
            "query": {
                "pageids": ["14307238"],
                "pages": {
                    "14307238": {
                        "pageid": 14307238,
                        "ns": 0,
                        "title": "Esplanade des Ouvriers-de-la-Tour-Eiffel",
                        "extract": "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France.",
                    }
                },
            },
        }


def test_page_id_OK(mocker):
    lat = 123
    lng = 456
    mocker.patch("requests.get", return_value=MockResponse1())
    wikirequest = WikiRequest(lat, lng)
    result = wikirequest.get_pageid()
    expected_value = 14307238
    assert result == expected_value

def test_get_summary_OK(mocker):
    lat = 123
    lng = 456
    pageid = 14307238
    mocker.patch('requests.get', return_value=MockResponse2())
    wikiRequest = WikiRequest(lat, lng)
    result = wikiRequest.get_summary(pageid)
    expected_value = "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France."
    assert result == expected_value