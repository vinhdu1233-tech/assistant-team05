from assistant.rules import reply

def test_help_message():
    result = reply("help")

    assert "campus offices" in result.lower()
    assert "Where is the Training Office?" in result
    assert "When does the IT Helpdesk open?" in result

def test_help_case_insensitive():
    result = reply("HELP")
    assert result == reply("help")
    assert "campus offices" in result.lower()

def test_help_with_punctuation():
    result = reply(" Help! ")
    assert result == reply("help")
    assert "campus offices" in result.lower()