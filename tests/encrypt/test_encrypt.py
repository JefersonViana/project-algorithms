import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "abcdef"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(10, 2)

    assert encrypt_message(message, 2) == "fedc_ba"
    assert encrypt_message(message, 3) == "cba_fed"
    assert encrypt_message("batatinha", 10) == "ahnitatab"
