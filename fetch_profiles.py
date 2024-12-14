# fetch_profiles.py

def fetch_profiles(data: dict) -> list:
    """
    Processes profile data and returns a list of profiles with required information.
    """
    if not data or 'profiles' not in data:
        print("No profiles found or error in response data.")
        return []

    profiles = data['profiles']  # Access the profiles dictionary
    profile_list = []

    # Extract only the required fields for each profile
    for profile_id, profile_data in profiles.items():
        profile_info = {
            "profile_id": profile_id,
            "cute_name": profile_data.get("cute_name", "Unnamed Profile"),
            "game_mode": profile_data.get("game_mode", "Unknown"),
            "current": profile_data.get("current", False),
            "is_ironman": profile_data.get("game_mode") == "ironman",
            "is_active": profile_data.get("current", False)
        }
        profile_list.append(profile_info)

    return profile_list
