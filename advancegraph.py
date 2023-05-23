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
    {'year': 1850, 'label': 'Virtual Assistants'},
    {'year': 1840, 'label': 'Wearable Technology'},
    {'year': 1830, 'label': 'Smartphone'},
    {'year': 1820, 'label': 'Cloud Storage'},
    {'year': 1810, 'label': 'Text Message'},
    {'year': 1800, 'label': 'World Wide Web'},
    {'year': 1790, 'label': 'Cellular Phone'},
    {'year': 1780, 'label': 'Email'},
    {'year': 1770, 'label': 'Communication Satellite'},
    {'year': 1760, 'label': 'Television'},
    {'year': 1750, 'label': 'Radio'},
    {'year': 1740, 'label': 'Telephone'},
    {'year': 1730, 'label': 'Telegraph'},
    {'year': 1720, 'label': 'Printing Press'},
    {'year': 1710, 'label': 'Homing Pigeons'},
    {'year': 1700, 'label': 'Cave Paintings'},     
]