from cipher_yw3760 import cipher_yw3760

def test_cipher_singleword():
    example = 'Ceasar'
    expected = 'Dfbtbs'
    result = cipher_yw3760.cipher(example, 1, True)
    assert result == expected