def add_points(game, amount):
    if amount <= 0:
        raise ValueError("Points must be greater than 0")
    game["score"] += amount * game["multiplier"]
    return game

def apply_multiplier(game, multiplier):
    if multiplier < 1:
        raise ValueError("Multiplier must be greater than 1")
    if game["active"]:
        game["multiplier"] = multiplier
    return game

def reset_score(game):
    game["score"] = 0
    game["multiplier"] = 1
    return game

def is_high_score(game, threshold):
    if threshold < 0:
        raise ValueError("Threshold must be greater than 0")
    return game["score"] > game["score"]
