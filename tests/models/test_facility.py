import textwrap
import pytest
from pydantic import ValidationError
from ssr import load_yaml, Facility

def test_facility_1():
    text = textwrap.dedent('''
    ---
    !Facility
    name: Valid Facility 1
    type: Satellite Control Site
    lat: 12.345
    lon: 23.456
    ---
    !Facility
    name: Valid Facility 2
    type: Satellite Control Site
    lat: 23.456
    lon: 12.345
    ''')
    print(text)
    seq = load_yaml(text)
    print(seq)
    for f in seq:
        assert isinstance(f, Facility)

def test_invalid_type():
    text = textwrap.dedent('''
    !Facility
    name: Invalid Type
    type: Invalid Facility Type
    lat: 12.345
    lon: 23.456
    ''')
    with pytest.raises(ValidationError):
        print(list(load_yaml(text)))

def test_invalid_latitude():
    text = textwrap.dedent('''
    !Facility
    name: Invalid Latitude
    type: Satellite Control Site
    lat: 99.345
    lon: 23.456
    ''')
    with pytest.raises(ValidationError):
        print(list(load_yaml(text)))

def test_invalid_longitude():
    text = textwrap.dedent('''
    !Facility
    name: Invalid Longitude
    type: Satellite Control Site
    lat: 12.345
    lon: 320.456
    ''')
    with pytest.raises(ValidationError):
        print(list(load_yaml(text)))
