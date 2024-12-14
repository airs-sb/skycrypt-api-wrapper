def fetch_minions(profile_data: dict) -> str:
    """
    Fetches minion-related data from the profile, including slots and a calculated total.

    Parameters:
    - profile_data (dict): The profile data dictionary.

    Returns:
    - str: A formatted string containing the minion slots and the combined total.
    """
    # Fetch data from misc -> profile_upgrades -> minion_slots
    misc_data = profile_data.get("data", {}).get("misc", {}).get("profile_upgrades", {})
    minion_slots_upgrade = misc_data.get("minion_slots", 0)

    # Fetch data from minions -> minion_slots -> current
    minions_data = profile_data.get("data", {}).get("minions", {}).get("minion_slots", {})
    current_minion_slots = minions_data.get("current", 0)

    return (
        f"Minion Slots from Upgrades: {minion_slots_upgrade}\n"
    )
