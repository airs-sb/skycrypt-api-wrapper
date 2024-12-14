def get_level(profile_data: dict) -> str:
    skills_data = profile_data.get("data", {}).get("skills", {}).get("skills", {}).get("farming", {})
    farming_level = skills_data.get("level", 0)
    
    contests_data = profile_data.get("data", {}).get("farming", {}).get("contests", {})
    attended_contests = contests_data.get("attended_contests", 0)
    
    return (
        f"<:ezgif3253b436f08:1314522063545045012> Farming Level: {farming_level}\n"
        f"<:ezgif35358eaecbf:1314522065356984372> Contests Attended: {attended_contests}"
    )

def get_badges(profile_data: dict) -> str:
    badges_data = profile_data.get("data", {}).get("farming", {}).get("total_badges", {})
    bronze = badges_data.get("bronze", 0)
    silver = badges_data.get("silver", 0)
    gold = badges_data.get("gold", 0)
    
    return (
        f"<:ezgif3b921dc7d59:1314521311166337064> Bronze: {bronze}\n"
        f"<:ezgif35182a48ac2:1314521309182562335> Silver: {silver}\n" 
        f"<:ezgif33f5734286e:1314521307517554759> Gold: {gold}"
    )

def get_golds(profile_data: dict) -> str:
    golds_data = profile_data.get("data", {}).get("farming", {})
    unique_golds = golds_data.get("unique_golds", 0)
    
    return f"Unique Golds: {unique_golds}"

def get_perks(profile_data: dict) -> str:
    perks_data = profile_data.get("data", {}).get("farming", {}).get("perks", {})
    double_drops = perks_data.get("double_drops", 0)
    farming_level_cap = perks_data.get("farming_level_cap", 0)
    
    return (
        f"<:ezgif36c9c07c6cd:1314519974601031681> Extra Farming Drops: {double_drops}/60\n" 
        f"<:ezgif327ce231da7:1314519631725199400> Farming Level Cap: {farming_level_cap}/10"
    )