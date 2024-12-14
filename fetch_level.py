# fetch_level.py

def fetch_level(profile_data: dict) -> str:
    level_data = profile_data.get("data", {}).get("skyblock_level", {})
    if not level_data:
        return "Skyblock level data not available."

    level = level_data.get("level", 0)
    return f"Skyblock Level: {level}"
