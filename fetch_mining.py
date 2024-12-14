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

def fetch_mining(profile_data: dict) -> str:
    mining_data = profile_data.get("data", {}).get("mining", {}).get("core", {})
    if not mining_data:
        return "Mining data not available."

    # Get and format the mining level
    level_data = mining_data.get("level", {})
    mining_level = level_data.get("level", 0)
    mining_level_formatted = format_number(mining_level)

    # Get and format powder values
    powder_data = mining_data.get("powder", {})
    mithril_available = powder_data.get("mithril", {}).get("available", 0)
    gemstone_available = powder_data.get("gemstone", {}).get("available", 0)
    glacite_available = powder_data.get("glacite", {}).get("available", 0)

    mithril_formatted = format_number(mithril_available)
    gemstone_formatted = format_number(gemstone_available)
    glacite_formatted = format_number(glacite_available)

    return (
        f"Heart Of The Mountain Level: {mining_level_formatted}\n"
        f"Mithril Powder: {mithril_formatted}\n"
        f"Gemstone Powder: {gemstone_formatted}\n"
        f"Glacite Powder: {glacite_formatted}"
    )
