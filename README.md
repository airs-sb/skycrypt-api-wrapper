# Skycrypt API Wrapper 
This is API wrapper for the skycrypt API in **python**.
Extremely WIP and hard to customise, should be easy to use for your bots in estimatedly 2-3 days.
- Requires NOTHING to fetch stats, decently fast and formats the stats recieved.
- Easy to use, extremely beginnner friendly.
- Lightweight, and can grab all stats without any extra requests.

## Installation
- Install the parser and place it in your bot folder, save it is "parser" preferably.
- Use the `fetch_stats` function to get the original API response.
- Then, fetch the profile you want to use:
```py
data = fetch_data(username)
profiles = fetch_profiles(data)
# Fetch Active Profile
selected_profile_name = profile or next((p["cute_name"] for p in profiles if p["is_active"]), None)
# Use Custom Profile
selected_profile_name = Mango
selected_profile_data = next(
  (profile_data for _, profile_data in data["profiles"].items() if profile_data["cute_name"] == selected_profile_name),
  None
)
```
- Then use the data to format/parse the stats:
```py
# Import the function from /parser folder.
from parser.fetch_networth import fetch_networth


networth = fetch_networth(selected_profile_data)
print(networth)
```
# Contribution
- Fix the unclean code that uses multiple files if needed to get more stats.
- Add more fetching, e.g **Musuem, Fishing**
