# fetch_breakdown_kuudra.py

def fetch_factions(kuudra_data_factions: dict) -> str:
    # Get the selected faction from the data
    faction = kuudra_data_factions.get("selected_faction", "")
    
    if not faction:
        return "No selected faction found."
   
    
    # Get the reputation value for the faction (default to 0 if not found)
    faction_rep = kuudra_data_factions.get("mages_reputation", 0)

    # Check if barbarians reputation exists and retrieve it
    barbarians_rep = kuudra_data_factions.get("barbarians_reputation", 0)
    
    # Return the formatted string with the faction and its reputation
    return f"Faction: {faction.capitalize()}\nReputation: {faction_rep}\nBarbarians Reputation: {barbarians_rep}"

def fetch_none(kuudra_data: dict) -> str:
    kuudra_emojis = {
        "None": ""
    }
    completions = kuudra_data.get("none", {}).get("completions", 0)
    return f"{kuudra_emojis['None']} Basic: {completions}"

def fetch_hot(kuudra_data: dict) -> str:
    kuudra_emojis = {
        "Hot": ""
    }
    completions = kuudra_data.get("hot", {}).get("completions", 0)
    return f"{kuudra_emojis['Hot']} Hot: {completions}"

def fetch_burning(kuudra_data: dict) -> str:
    kuudra_emojis = {
        "Burning": ""
    }
    completions = kuudra_data.get("burning", {}).get("completions", 0)
    return f"{kuudra_emojis['Burning']} Burning: {completions}"

def fetch_fiery(kuudra_data: dict) -> str:
    kuudra_emojis = {
        "Fiery": ""
    }
    completions = kuudra_data.get("fiery", {}).get("completions", 0)
    return f"{kuudra_emojis['Fiery']} Fiery: {completions}"

def fetch_infernal(kuudra_data: dict) -> str:
    kuudra_emojis = {
        "Infernal": ""
    }
    completions = kuudra_data.get("infernal", {}).get("completions", 0)
    return f"{kuudra_emojis['Infernal']} Infernal: {completions}"
