# parser/fetch_minions.py

def fetch_minion_basic(profile_data: dict) -> str:
    """
    Fetches basic minion-related data from the profile.

    Parameters:
    - profile_data (dict): The profile data dictionary.

    Returns:
    - str: A formatted string containing the basic minion information.
    """
    # Extracting data from the JSON
    minions_data = profile_data.get("data", {}).get("minions", {})
    total_minions = minions_data.get("totalMinions", 0)
    maxed_minions = minions_data.get("maxedMinions", 0)
    unlocked_tiers = minions_data.get("unlockedTiers", 0)
    unlockable_tiers = minions_data.get("unlockableTiers", 0)

    return (
        f"Total Minions: {total_minions}\n"
        f"Maxed Minions: {maxed_minions}\n"
        f"Unlocked Tiers: {unlocked_tiers}\n"
        f"Unlockable Tiers: {unlockable_tiers}"
    )


def fetch_minion_two(profile_data: dict) -> dict:
    """
    Fetches detailed minion-related data for different categories.

    Parameters:
    - profile_data (dict): The profile data dictionary.

    Returns:
    - dict: A dictionary where keys are categories and values are formatted strings of total and maxed minions.
    """
    # Extracting data from the JSON
    minions_group = profile_data.get("data", {}).get("minions", {}).get("minions", {})
    categories = ["farming", "mining", "combat", "foraging", "fishing"]

    result = {}
    for category in categories:
        category_data = minions_group.get(category, {})
        total_minions = category_data.get("totalMinions", 0)
        maxed_minions = category_data.get("maxedMinions", 0)

        result[category.capitalize()] = (
            f"Total Minions: {total_minions}\n"
            f"Maxed Minions: {maxed_minions}"
        )

    return result
