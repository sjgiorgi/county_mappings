# Regions
regions = {
	'Northeast' : ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania'],
	'Midwest' : ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin', 'Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota'],
	'South' : ['Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'West Virginia', 'Alabama', 'Kentucky', 'Mississippi', 'Tennessee', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas'],
	'West' : ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming', 'Alaska', 'California', 'Hawaii', 'Oregon', 'Washington'],
}

regions_abbrv = {
  'Northeast': ['CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ', 'NY', 'PA'],
  'Midwest': ['IL', 'IN', 'MI', 'OH', 'WI', 'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD'],
  'South': ['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX'],
  'West': ['AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT', 'WY', 'AK', 'CA', 'HI', 'OR', 'WA']}

# Divisions
divisions = {
	'New England' : ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont'], 
	'Middle Atlantic' : ['New Jersey', 'New York', 'Pennsylvania'], 
	'East North Central' : ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin'], 
	'West North Central' : ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota'], 
	'South Atlantic' : ['Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'West Virginia'], 
	'East South Central' : ['Alabama', 'Kentucky', 'Mississippi', 'Tennessee'], 
	'West South Central' : ['Arkansas', 'Louisiana', 'Oklahoma', 'Texas'], 
	'Mountain' : ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming'], 
	'Pacific' : ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington'], 
}

divisions_abbrv = {
	'New England' : ['CT', 'ME', 'MA', 'NH', 'RI', 'VT'], 
	'Middle Atlantic' : ['NJ', 'NY', 'PA'], 
	'East North Central' : ['IL', 'IN', 'MI', 'OH', 'WI'], 
	'West North Central' : ['IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD'], 
	'South Atlantic' : ['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'WV'], 
	'East South Central' : ['AL', 'KY', 'MS', 'TN'], 
	'West South Central' : ['AR', 'LA', 'OK', 'TX'], 
	'Mountain' : ['AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT', 'WY'], 
	'Pacific' : ['AK', 'CA', 'HI', 'OR', 'WA'], 
}

# States
abbrv_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
states_abbrv = dict((v,k) for k,v in abbrv_states.items())

# Counties
