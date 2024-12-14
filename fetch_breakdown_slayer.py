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


def fetch_slayers(profile_data: dict) -> dict:
    """
    Fetches slayer data and organizes it into a dictionary for use in embed creation.

    Parameters:
    - profile_data (dict): Profile data containing slayer details.

    Returns:
    - dict: A dictionary containing slayer details or an error message.
    """
    slayer_data = profile_data.get("data", {}).get("slayer", {}).get("slayers", {})
    if not slayer_data:
        return {"error": "Slayer data not available."}

    # Slayer emojis
    slayer_emojis = {
        "zombie": "<:1236748511127670946:1315254902833938462>",
        "spider": "<:1236748512830689300:1315254904557670451>",
        "wolf": "<:1236748516701769799:1315254908420882453>",
        "enderman": "<:1236748518513705013:1315254910455119882>",
        "blaze": "<:1236747415667609711:1315254901152153650>",
        "vampire": "<:1236748514910797895:1315254906419937320>"
    }

    slayers = {}
    for slayer_name, slayer_info in slayer_data.items():
        # Extract slayer details
        level = slayer_info.get("level", {}).get("currentLevel", 0)
        xp = slayer_info.get("level", {}).get("xp", 0)
        
        # Format the values
        slayers[slayer_name.capitalize()] = {  # Capitalize the slayer name
            "emoji": slayer_emojis.get(slayer_name, ""),  # Add slayer-specific emoji
            "level": level,
            "xp": format_number(xp)
        }

    return slayers
