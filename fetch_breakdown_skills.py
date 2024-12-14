def format_number(number: float) -> str:
    """
    Formats a number to a human-readable format with suffixes (K, M, B, T).
    Handles invalid or None values gracefully.
    """
    if not isinstance(number, (int, float)) or number is None:
        return "N/A"
    
    suffixes = ['', 'K', 'M', 'B', 'T']
    index = 0
    while abs(number) >= 1000 and index < len(suffixes) - 1:
        number /= 1000.0
        index += 1
    return f"{number:.1f}{suffixes[index]}"


def fetch_skills(profile_data: dict) -> dict:
    """
    Fetches skills data and organizes it into a dictionary for use in embed creation.

    Parameters:
    - profile_data (dict): Profile data containing skills details.

    Returns:
    - dict: A dictionary containing skills details or an error message.
    """
    skills_data = profile_data.get("data", {}).get("skills", {}).get("skills", {})
    if not skills_data:
        return {"error": "Skills data not available."}

    skills_emojis = {
        "farming": "<:ezgif3253b436f08:1314522063545045012>",
        "mining": "<:1236755172139728997:1289571625666347110>",
        "combat": "<:1236756046098202625:1315250204793897021>",
        "foraging": "<:1236755374254850099:1289571627410915349>",
        "fishing": "<:Fishing:1315601878100217866>",
        "enchanting": "<:enchanting:1315601968894316577>",
        "alchemy": "<:alchemy:1315602049865351198>",
        "carpentry": "<:carpentry:1315602114545844244>",
        "runecrafting": "<:runecrafting:1315602207550345277>",
        "social": "<:social:1315602262231617616>",
        "taming": "<:taming:1315602317709410344>",
        "catacombs": "<:1236755555775807609:1289571632960245862>"
    }

    # Define the desired order of skills
    skills_order = [
        "combat", "mining", "farming", "foraging", "fishing", 
        "enchanting", "alchemy", "carpentry", "runecrafting", 
        "social", "taming", "catacombs"
    ]

    skills = {}
    for skill_name in skills_order:
        skills_info = skills_data.get(skill_name, {})
        level = skills_info.get("level", 0)
        xp = skills_info.get("xp", 0)
        xp_next = skills_info.get("xpForNext")

        # Handle xpForNext "null" and set a MAX LEVEL marker if applicable
        if xp_next in [None, "null"]:
            xp_next_display = "MAX LEVEL" if xp > 0 else "NONE"
        else:
            xp_next_display = format_number(xp_next)

        skills[skill_name.capitalize()] = {
            "emoji": skills_emojis.get(skill_name, ""),
            "level": level,
            "xp": format_number(xp),
            "xpnext": xp_next_display
        }

    return skills
