import pytest

@pytest.fixture
def player():
    return {"health": 100, "max_health": 100, "alive": True}

@pytest.fixture
def dead_player():
    return {"health": 0, "max_health": 100, "alive": False}

@pytest.fixture
def game():
    return {"score": 0, "multiplier": 1, "active": True}

@pytest.fixture
def inventory():
    return {"items": [], "capacity": 10, "locked": False}

@pytest.fixture
def inventory_full():
    return {"items": ["Duplicator","Jesus","Manifesto","Holy Grail","Jesus","Python Vile", "Chicken Soup", "Mr.McCuen", "Ms.Keller", "Mr.Gardner"], "capacity": 10, "locked": False}