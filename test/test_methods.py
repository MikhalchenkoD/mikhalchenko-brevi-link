from src.methods import check_valid_url


def test_valid_url():
    isvalid = check_valid_url('https://www.google.kz/')
    assert isvalid


def test_invalid_url():
    isvalid = check_valid_url('https://www.goooogle.ez/')
    assert not isvalid
