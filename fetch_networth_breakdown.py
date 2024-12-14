# parser/fetch_networth.py

def format_number(value: int) -> str:
    """
    Formats a number into K/M/B/T notation.

    Parameters:
    - value (int): The number to format.

    Returns:
    - str: The formatted number.
    """
    if value >= 1_000_000_000_000:
        return f"{value / 1_000_000_000_000:.2f}T"
    elif value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    elif value >= 1_000:
        return f"{value / 1_000:.2f}K"
    else:
        return str(value)


def fetch_networth_basic(profile_data: dict) -> str:
    """
    Fetches basic networth-related data from the profile.

    Parameters:
    - profile_data (dict): The profile data dictionary.

    Returns:
    - str: A formatted string containing the basic networth information.
    """
    networth_data = profile_data.get("data", {}).get("networth", {})
    networth = format_number(networth_data.get("networth", 0))
    unsoulbound_networth = format_number(networth_data.get("unsoulboundNetworth", 0))
    purse = format_number(networth_data.get("purse", 0))
    bank = format_number(networth_data.get("bank", 0))

    return (
        f"<:12367560445882531841:1289571638832136192> Networth: {networth}\n"
        f"<:12367560445882531841:1289571638832136192> Unsoulbound Networth: {unsoulbound_networth}\n"
        f"<:coin:1291711299511910450> Purse: {purse}\n"
        f"🏦 Bank: {bank}"
    )


def fetch_networth_types(profile_data: dict) -> dict:
    """
    Fetches detailed networth-related data for different types.

    Parameters:
    - profile_data (dict): The profile data dictionary.

    Returns:
    - dict: A dictionary where keys are types and values are formatted strings.
    """
    types_data = profile_data.get("data", {}).get("networth", {}).get("types", {})
    result = {}

    for type_name, type_values in types_data.items():
        # Format the type name: capitalize and replace underscores with spaces
        display_name = type_name.replace("_", " ").capitalize()

        # Format the values
        total = format_number(type_values.get("total", 0))
        unsoulbound_total = format_number(type_values.get("unsoulboundTotal", 0))

        result[display_name] = (
            f"Total: {total}\n"
            f"Unsoulbound Total: {unsoulbound_total}"
        )

    return result
