# fetch_networth.py

def format_number(number: float) -> str:
    suffixes = ['', 'K', 'M', 'B', 'T']
    index = 0
    while number >= 1000 and index < len(suffixes) - 1:
        number /= 1000.0
        index += 1
    return f"{number:.1f}{suffixes[index]}"

def fetch_networth(profile_data: dict) -> str:
    networth_data = profile_data.get("data", {}).get("networth", {})
    if not networth_data:
        return "Net worth data not available."

    total_networth = networth_data.get("networth", 0)
    unsoulbound_networth = networth_data.get("unsoulboundNetworth", 0)
    purse = networth_data.get("purse", 0)
    bank = networth_data.get("bank", 0)

    soulbound_networth = total_networth - unsoulbound_networth
    total_networth_formatted = format_number(total_networth)
    purse_formatted = format_number(purse)
    bank_formatted = format_number(bank)
    soulbound_networth_formatted = format_number(soulbound_networth)

    return f"{total_networth_formatted} ({purse_formatted} + {bank_formatted})\n{soulbound_networth_formatted} Soulbound"
