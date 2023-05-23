def timeline(events, width=40):
    start_year = min([event['year'] for event in events])
    end_year = max([event['year'] for event in events])
    num_years = end_year - start_year + 1
    scale = width / num_years
    for i in range(len(events)):
        event = events[i]
        year = event['year'] - start_year
        label = event['label']
        line = '|' + ' ' * year + '•' + '-' * (int(scale) - 1) + label
        print(line)
events = [
    {'year': 1820, 'label': '2021: Paramount+, Discovery+'},
    {'year': 1810, 'label': '2020: NBCUniversal'},
    {'year': 1800, 'label': '2019: Disney+, Apple TV+'},
    {'year': 1790, 'label': '2018: ESPN+'},
    {'year': 1780, 'label': '2017: Youtube TV'},
    {'year': 1770, 'label': '2015: Sling TV, FuboTV'},
    {'year': 1760, 'label': '2014: Tubi'},
    {'year': 1750, 'label': '2011: Amazon Prime'},
    {'year': 1740, 'label': '2010: HBO'},
    {'year': 1730, 'label': '2008: Hulu, Kanopy'},
    {'year': 1720, 'label': '2007: Netflix, Mubi'},
    {'year': 1710, 'label': '2006: CrunchyRolls'},
    {'year': 1700, 'label': '2004: Vudu'},     
]