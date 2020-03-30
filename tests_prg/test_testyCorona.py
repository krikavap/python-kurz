"""
test_testyCorona.py

"""

from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from testyCorona import TestyCorona_json
import pytest

def test_prvniData():
    db = TestyCorona_json()
    db.connect("testy.json")
    prvniData = db.nacti_data("27.1.2020")
    assert prvniData["datum"] == "27.1.2020"
    assert prvniData["testy-den"] == 20
    assert prvniData["testy-celkem"] == 20


def test_druhyData():
    db = TestyCorona_json()
    db.connect("testy.json")
    prvniData = db.nacti_data("28.1.2020")
    assert prvniData["datum"] == "28.1.2020"
    assert prvniData["testy-den"] == 8
    assert prvniData["testy-celkem"] == 28