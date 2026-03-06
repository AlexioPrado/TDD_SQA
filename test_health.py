import pytest
from health import *

# ---- take_damage ----
def test_take_damage_reduces_health(player):
    result = take_damage(player, 30)
    assert result["health"] == 70


# ---- heal ----
def test_heal_increases_health(player):
    player["health"] = 60
    result = heal(player, 20)
    assert result["health"] == 80


def test_heal_dead_player(dead_player):
    result = heal(dead_player, 20)
    assert result["health"] == 0


# ---- is_alive ----
def test_is_alive_returns_true_when_healthy(player):
    take_damage(player, 30)
    assert is_alive(player) == True


def test_is_alive_returns_false_when_not_healthy(dead_player):
    assert is_alive(dead_player) == False
