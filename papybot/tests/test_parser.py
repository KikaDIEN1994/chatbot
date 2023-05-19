from papybot.parser import Parser


def test_remove_upper_letter():
    question = "Tour Eiffel"
    expected_value = "tour eiffel"
    parser = Parser(question)
    result = parser.parse()
    assert result == expected_value


def test_remove_ponctuation():
    question = "tour-eiffel."
    expected_value = "tour eiffel"
    parser = Parser(question)
    result = parser.parse()
    assert result == expected_value

def test_remove_stop_words():
    question = "bonjour ou se trouve la tour eiffel"
    expected_value = "tour eiffel"
    parser = Parser(question)
    result = parser.parse()
    assert result == expected_value


