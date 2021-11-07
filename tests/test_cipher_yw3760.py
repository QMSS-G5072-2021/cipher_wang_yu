from cipher_yw3760 import cipher_yw3760

import pytest

def test_cipher_singleword():
    example = 'Ceasar'
    expected = 'Dfbtbs'
    result = cipher(example, 1, True)
    assert result == expected