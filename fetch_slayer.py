# fetch_slayer.py

def fetch_slayer(profile_data: dict) -> str:
    slayer_data = profile_data.get("data", {}).get("slayer", {}).get("slayers", {})
    if not slayer_data:
        return "Slayer data not available."

    slayers = ["zombie", "spider", "wolf", "enderman", "blaze", "vampire"]
    slayer_levels = []

    for slayer in slayers:
        level_data = slayer_data.get(slayer, {}).get("level", {})
        current_level = level_data.get("currentLevel", 0)
        slayer_levels.append(str(current_level))

    return "/".join(slayer_levels)
