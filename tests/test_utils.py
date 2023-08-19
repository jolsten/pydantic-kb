import pytest
from ssr.utils import catalog_number_to_alpha5, alpha5_to_catalog_number

ALPHA5_TEST_CASES = {
     12345: '12345',
    100000: 'A0000',
    148493: 'E8493',
    182931: 'J2931', 
    234018: 'P4018',
    301928: 'W1928',
    339999: 'Z9999',
}

@pytest.mark.parametrize('number, alpha5', ALPHA5_TEST_CASES.items())
def test_number_to_alpha5(number: int, alpha5: str):
    assert catalog_number_to_alpha5(number) == alpha5

@pytest.mark.parametrize('number, alpha5', ALPHA5_TEST_CASES.items())
def test_alpha5_to_number(number: int, alpha5: str):
    assert number == alpha5_to_catalog_number(alpha5)
