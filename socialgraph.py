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
    {'year': 1795, 'label': '2020: ClubHouse'},
    {'year': 1790, 'label': '2019: Rizzle'},
    {'year': 1785, 'label': '2018: Lasso'},
    {'year': 1780, 'label': '2017: Sarahah'},
    {'year': 1775, 'label': '2016: Tiktok'},  
    {'year': 1770, 'label': '2015: Periscope, Discord'},
    {'year': 1765, 'label': '2014: Ello'},  
    {'year': 1760, 'label': '2013: Vine'},  
    {'year': 1755, 'label': '2012: Pinterest'},
    {'year': 1750, 'label': '2011: Snapchat, WeChat, NextDoor'},
    {'year': 1745, 'label': '2010: Instagram'},
    {'year': 1740, 'label': '2009: Quora'},  
    {'year': 1735, 'label': '2008: Spotify'},
    {'year': 1730, 'label': '2007: Tumblr'},
    {'year': 1725, 'label': '2006: Twitter'},
    {'year': 1720, 'label': '2005: Youtube, Bebo'},  
    {'year': 1715, 'label': '2004: Facebook'},  
    {'year': 1710, 'label': '2003: MySpace'},  
    {'year': 1705, 'label': '2002: Friendster, LinkedIn'},  
    {'year': 1700, 'label': '2001: Ryze'},     
]