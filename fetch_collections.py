def fetch_collections(profile_data: dict) -> str:
    """
    Fetches collection data, showing the number of maxed and unlocked collections.

    Parameters:
    - profile_data (dict): The profile data dictionary.

    Returns:
    - str: A formatted string showing maxed and unlocked collections.
    """
    # Default total collections count
    total_possible_collections = 76

    # Retrieve collection data
    collections_data = profile_data.get("data", {}).get("collections", {})
    maxed_collections = collections_data.get("maxedCollections", 0)
    total_collections = collections_data.get("totalCollections", 0)

    # Calculate unlocked collections (total - maxed)
    unlocked_collections = total_collections - maxed_collections

    # Format output
    return (
        f"Maxed: {maxed_collections}/{total_possible_collections}\n"
        f"Unlocked: {unlocked_collections}/{total_possible_collections}"
    )
