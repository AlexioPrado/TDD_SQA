import pytest
from inventory import *

# ---- add_item ----
def test_add_item(inventory):
    result = add_item(inventory, "Boobah Eradicator")
    assert result["items"] == ["Boobah Eradicator"]

def test_add_item_empty_string(inventory):
    with pytest.raises(ValueError):
        result = add_item(inventory,"")
        assert result["items"] == []

def test_add_item_nonString(inventory):
    with pytest.raises(ValueError):
        result = add_item(inventory,67)
        assert result["items"] == []

def test_add_item_max_capacity(inventory_full):
    with pytest.raises(ValueError):
        result = add_item(inventory_full,"Item 11")
        assert len(result["items"]) == 10

def test_add_item_inventory_locked(inventory):
    with pytest.raises(ValueError):
        inventory["locked"] = True
        result = add_item(inventory,"Boobah Duplicator")
        assert result["items"] == []

# ---- remove_item ----
def test_remove_item_in_inventory(inventory_full):
    result = remove_item(inventory_full,"Duplicator")
    inside = "Duplicator" in result["items"]
    assert inside == False

def test_remove_item_not_in_inventory(inventory_full):
    with pytest.raises(ValueError):
        result = remove_item(inventory_full,"Jingbah")
        assert inventory_full["items"] == result["items"]

def test_remove_item_locked_inventory(inventory_full):
    with pytest.raises(ValueError):
        inventory_full["locked"] = True
        result = remove_item(inventory_full,"Jesus")
        assert len(result["items"]) == 10

def test_remove_item_duplicate(inventory_full):
    before = inventory_full["items"].count("Jesus")
    result = remove_item(inventory_full,"Jesus")
    after = result["items"].count("Jesus")
    #This assert verifies that only one of a duplicate item was removed
    assert  after == before - 1

# ---- get_item_count ----
def test_item_count(inventory_full):
    result = get_item_count(inventory_full)
    assert result == 10

def test_item_count_locked_inventory(inventory_full):
    inventory_full["locked"] = True
    result = get_item_count(inventory_full)
    assert result == 10

def test_item_count_empty_inventory(inventory):
    result = get_item_count(inventory)
    assert result == 0

