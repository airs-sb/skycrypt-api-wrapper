def fetch_skills(profile_data: dict) -> str:
    skills_data = profile_data.get("data", {}).get("skills", {})
    if not skills_data:
        return "Skills data not available."

    average_skill_level = skills_data.get("averageSkillLevel", 0)
    formatted_skill_level = f"{average_skill_level:.1f}"

    return f"{formatted_skill_level} Skill Average"
