from datetime import datetime

def fetch_mineinfo(profile_data: dict) -> str:
    core_data = profile_data.get("data", {}).get("mining", {}).get("core", {})
    
    # Level
    level = core_data.get("level", {}).get("level", 0)
    
    # Tokens
    tokens_data = core_data.get("tokens", {})
    total_tokens = tokens_data.get("total", 0)
    spent_tokens = tokens_data.get("spent", 0)
    
    # Powder
    powder_data = core_data.get("powder", {})
    mithril_total = powder_data.get("mithril", {}).get("total", 0)
    gemstone_total = powder_data.get("gemstone", {}).get("total", 0)
    glacite_total = powder_data.get("glacite", {}).get("total", 0)
    
    # HOTM last reset
    hotm_last_reset = core_data.get("hotm_last_reset", None)
    if hotm_last_reset:
        try:
            hotm_last_reset_seconds = int(hotm_last_reset) // 1000
            hotm_last_reset_formatted = f"<t:{hotm_last_reset_seconds}:F>"
        except ValueError:
            hotm_last_reset_formatted = "Invalid timestamp"
    else:
        hotm_last_reset_formatted = "Unknown"
    
    return (
        f"<:hotm:1314594410633232436> Mining Level: {level}\n"
        f"<:ezgif59a9fe94ecc:1314595180057460766> Tokens: {spent_tokens}/{total_tokens} spent.\n"
        f"<:1236753058835206314:1289571624026378342> Mithril: {mithril_total}\n"
        f"<:1236755501631668304:1289571630950907977> Gemstone: {gemstone_total}\n"
        f"<:1252915492293705759:1289571642732843162> Glacite: {glacite_total}\n"
        f"<:ezgif50d66e3edd9:1314595177695940620> HOTM Last Reset: {hotm_last_reset_formatted}"
    )

def fetch_crystaltime(profile_data: dict) -> str:
    # Fetch the timestamp from the profile data
    crystal_hollows_last_access = profile_data.get("data", {}).get("mining", {}).get("core", {}).get("crystal_hollows_last_access", None)
    
    # Check if the timestamp is available and valid
    if crystal_hollows_last_access:
        try:
            # Convert the Unix timestamp from milliseconds to seconds
            timestamp_seconds = int(crystal_hollows_last_access) // 1000
            # Format it for Discord
            discord_timestamp = f"<t:{timestamp_seconds}:F>"
            return f"Crystal Hollows Last Access: {discord_timestamp}"
        except ValueError:
            return "Crystal Hollows Last Access: Invalid timestamp"
    else:
        return "Crystal Hollows Last Access: Unknown"

def fetch_crystals(profile_data: dict) -> str:
    crystals_data = profile_data.get("data", {}).get("mining", {}).get("core", {}).get("crystal_nucleus", {}).get("crystals", {})
    
    formatted_crystals = []
    for crystal, details in crystals_data.items():
        state = details.get("state", "NOT_FOUND")
        # Proper formatting for crystal name and bold state
        crystal_name = crystal.replace("_", " ").title()
        state_formatted = f"**{state.replace('_', ' ').title()}**"
        formatted_crystals.append(f"{crystal_name}: {state_formatted}")
    
    return "\n".join(formatted_crystals)

