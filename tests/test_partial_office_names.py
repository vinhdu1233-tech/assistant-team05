from assistant.rules import reply

def test_partial_office_name():
    result = reply("where is training")
    assert "Training Office" in result
    assert "I.101" in result

def test_full_office_name():
    result = reply("where is the IT Helpdesk?")
    assert "IT Helpdesk" in result

def test_unknown_office():
    result = reply("where is the astronomy department")
    assert "don't know" in result

def test_ambiguous_office():
    result = reply("where is IT")
    assert "more specific" in result.lower()