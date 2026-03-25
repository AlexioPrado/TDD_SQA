def take_damage(player, amount):
    player["health"] = max(0, player["health"] - amount)
    if player["health"] == 0:
        player["alive"] = False
    return player


def heal(player, amount):
    if not player["alive"]:
        return player
    player["health"] = min(player["max_health"], player["health"] + amount)
    return player


def is_alive(player):
    return player["alive"] and player["health"] > 0
