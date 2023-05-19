from google_api.geocoding import Geocoding
import pytest

def test_geocode_OK(mocker):
    keywords = "Tour eiffel"
    mock_value = [{'address_components': [{'long_name': '5', 'short_name': '5', 'types': ['street_number']}, {'long_name': 'Avenue Anatole France', 'short_name': 'Av. Anatole France', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Département de Paris', 'short_name': 'Département de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75007', 'short_name': '75007', 'types': ['postal_code']}], 'formatted_address': 'Champ de Mars, 5 Av. Anatole France, 75007 Paris, France', 'geometry': {'location': {'lat': 48.85837009999999, 'lng': 2.2944813}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.85974613029151, 'lng': 2.295661530291502}, 'southwest': {'lat': 48.85704816970851, 'lng': 2.292963569708498}}}, 'partial_match': True, 'place_id': 'ChIJLU7jZClu5kcR4PcOOO6p3I0', 'plus_code': {'compound_code': 'V75V+8Q Paris, France', 'global_code': '8FW4V75V+8Q'}, 'types': ['establishment', 'point_of_interest', 'tourist_attraction']}]
    mocker.patch("googlemaps.client.Client.geocode", return_value = mock_value)
    geocoding = Geocoding(keywords)
    result = geocoding.geocode()
    expected_value = {"address": "Champ de Mars, 5 Av. Anatole France, 75007 Paris, France", "location": { "lat": 48.85837009999999, 'lng': 2.2944813 }, "status": "OK" }
    assert result == expected_value

def test_geocode_NOK(mocker):
    keywords = "hikhsdquih" 
    mock_value = []
    mocker.patch("googlemaps.client.Client.geocode", return_value = mock_value)
    geocoding = Geocoding(keywords)
    result = geocoding.geocode()
    expected_value = {'status': 'NOK'}
    assert result == expected_value