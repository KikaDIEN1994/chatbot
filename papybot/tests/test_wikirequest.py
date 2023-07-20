from papybot.wikirequest import WikiRequest

def test_page_id_OK(mocker):
    lat = 48.85837009999999
    lng = 2.2944813
    mock_value = 14307238
    mocker.patch("requests.get", return_value=create_mock_response(mock_value))
    wikirequest = WikiRequest(lat,lng)
    result = wikirequest._get_pageid()
    expected_value = 14307238
    assert result == expected_value
"""
def test_page_id_NOK(mocker):
    lat = 48.85837009999999
    lng = 2.2944813
    mocker.patch =("requests.get", side_effet=Exception("An exception occured))
    wikirequest = WikiRequest(lat,lng)   
    result = wikirequest._get_pageid()
    expected_value = {'An exeption occured'}
    assert result == expected_value
"""
def test_get_summary_OK(mocker):
    mock_value = 14364038
    mocker.patch("requests.get", return_value=create_mock_response(mock_value))
    wikiRequest = WikiRequest(None,None)
    result = wikiRequest.get_summary()
    expected_value = "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France."
    assert result == expected_value
"""
def test_get_summary_NOK(mocker):
    keywords = {'status': 'NOK'}
    mock_value =
    result =
    expected_value = {'status': 'NOK'}
    assert result == expected_value
"""
"""
def test_get_summary_NOK(mocker):
    keywords = {'status': 'NOK'}
    mocker.patch("requests.get", side_effect=Exception("An exception occurred"))
    wikiRequest = WikiRequest(None, None)
    result = wikiRequest.get_summary()
    expected_value = {'status': 'NOK'}
    assert result == expected_value
"""
def create_mock_response(pageid):
    mock_response = {
        "query": {
            "pages": {
                str(pageid): {
                    "extract": "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France."
                }
            }
        }
    }
    return mock_response