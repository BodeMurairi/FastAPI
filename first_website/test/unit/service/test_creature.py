from model.creature import Creature
from service import creature as code

sample = Creature(
    name="Dragon",
    country="FantasyLand",
    area = "Mountains",
    description="A large, fire-breathing reptile",
    aka = "Fire Drake"
)

def test_create():
    resp = code.create_creature(sample)
    assert resp == sample

def test_get_exist():
    resp = code.get_creature_by_name("Yetti")
    assert resp is not None
    assert resp.name == "Yetti"
    assert resp.country == "CN"
    assert resp.area == "Himalayas"
    assert resp.description == "Hirsute Himalayan"
    assert resp.aka == "Abominable Snowman"

def test_get_missing():
    resp = code.get_creature_by_name("boxturtle")
    assert resp is None
