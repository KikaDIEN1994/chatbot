from papybot.wikirequest import WikiRequest

def test_page_id_OK(mocker):
    keywords = "lat = 48.85837009999999","lng = 2.2944813"
    expected_value = "14307238"

def test_page_id_NOK(mocker):
    keywords = {0,2.2950275}
    expected_value = {'An exeption occured'}

def test_get_summary_OK(mocker):
    keywords = 14364038
    expected_value = "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France."

def test_get_summary_NOK(mocker):
    keywords = {'status': 'NOK'}
    expected_value = {'status': 'NOK'}