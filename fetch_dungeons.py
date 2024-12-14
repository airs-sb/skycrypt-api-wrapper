def format_number(number: float) -> str:
    """
    Formats a number to a human-readable format with suffixes (K, M, B, T).
    """
    suffixes = ['', 'K', 'M', 'B', 'T']
    index = 0
    while number >= 1000 and index < len(suffixes) - 1:
        number /= 1000.0
        index += 1
    return f"{number:.1f}{suffixes[index]}"


def fetch_dungeons(profile_data: dict, breakdown: bool = False) -> str:
    """
    Fetches dungeon-related data from the profile, returning a structured dictionary or formatted string for detailed embed formatting.

    Parameters:
    - profile_data (dict): The profile data dictionary.
    - breakdown (bool): Whether to include a detailed breakdown of dungeon data.

    Returns:
    - str or dict: A formatted string for non-breakdown mode or a structured dictionary for detailed breakdown mode.
    """
    dungeons_data = profile_data.get("data", {}).get("dungeons", {})
    
    if not dungeons_data:
        return "Error: Dungeons data not available."

    # Basic catacombs data
    catacombs_data = dungeons_data.get("catacombs", {}).get("level", {})
    catacombs_level = catacombs_data.get("level", 0)
    catacombs_xp = catacombs_data.get("xp", 0)

    if not breakdown:
        # Format response for non-breakdown mode
        return f"Level: {catacombs_level}\nXP: {format_number(catacombs_xp)}"

    # Detailed response for breakdown mode
    response = {
        "catacombs": {
            "level": catacombs_level,
            "xp": format_number(catacombs_xp)
        },
        "floor_completions": dungeons_data.get("floor_completions", 0),
        "secrets_found": dungeons_data.get("secrets_found", 0),
        "average_class_level": dungeons_data.get("classes", {}).get("average_level", 0),
        "total_class_experience": format_number(
            dungeons_data.get("classes", {}).get("experience", 0)
        ),
        "classes": {}
    }

    # Class-specific data with emojis
    class_emojis = {
        "healer": "<:1236755679860232243:1315250202965311509>",
        "mage": "<:1236755549102669894:1315250201098981430>",
        "berserk": "<:1236756046098202625:1315250204793897021>",
        "archer": "<:1236756108794794110:1315232779809853521>",
        "tank": "<:1236755129785389067:1315250199224127558>"
    }

    classes = ["healer", "mage", "berserk", "archer", "tank"]
    for class_name in classes:
        class_data = dungeons_data.get("classes", {}).get("classes", {}).get(class_name, {})
        class_level = class_data.get("level", {}).get("level", 0)
        class_xp = class_data.get("level", {}).get("xp", 0)
        response["classes"][class_name] = {
            "emoji": class_emojis.get(class_name, ""),  # Add class-specific emoji
            "level": class_level,
            "xp": format_number(class_xp)
        }

    return response
