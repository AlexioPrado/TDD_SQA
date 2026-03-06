import pytest
from score import *

# ---- add_points ----
def test_add_negative_points(game):
    with pytest.raises(ValueError):
        result = add_points(game, -5)
        assert result["score"] == 0

def test_add_positive_points(game):
    result = add_points(game, 67)
    assert result["score"] == 67

def test_add_zero_points(game):
    with pytest.raises(ValueError):
        result = add_points(game, 0)
        assert result["score"] == 0

def test_add_points_with_multiplier(game):
    game["multiplier"] = 3
    result = add_points(game, 23)
    assert result["score"] == 69

# ---- apply_multiplier ----
def test_apply_zero_multiplier(game):
    with pytest.raises(ValueError):
        result = apply_multiplier(game, 0)
        assert result["multiplier"] == 1

def test_apply_multiplier_while_inactive(game):
    game["active"] = False
    result = apply_multiplier(game, 3)
    assert result["multiplier"] == 1

def test_apply_multiplier_while_active(game):
    result = apply_multiplier(game, 4)
    assert result["multiplier"] == 4

# ---- reset_score ----
def test_reset_score_inactive(game):
    game["active"] = False
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"] == 1

# ---- is_high_score ----
def test_high_score_equal_to_threshold(game):
    game["score"] = 15
    result = is_high_score(game, 15)
    assert result == False

def test_high_score_threshold_less_than_0(game):
    with pytest.raises(ValueError):
        game["score"] = 12
        result = is_high_score(game, -4)
        assert result == False
