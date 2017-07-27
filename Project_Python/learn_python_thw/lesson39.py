# Create a mapping of state to abbreviation
states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'Jharkhand' : 'JH',
	'Telangana' : 'TL',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'JH' : 'Dhanbad',
	'TL' : 'Hyderabad',
	'FL' : 'Jacksonville'
}


# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities

print '-' * 15
print 'NY state has: ', cities['NY']
print 'OR state has: ', cities['OR']

# Print some states
print '-' * 15
print 'Jharkhand\'s abbreviation is: ', states['Jharkhand']
print 'Florida\'s abbreviation is: ', states['Florida']

# Do it by using the states and cities dict

print '-' * 15
print 'Michigan has: ', cities[states['Michigan']]
print 'Jharkhand has:', cities[states['Jharkhand']]

# Print every state abbreviation
print '-' * 15
for state, abbrev in states.items():
	print '%s is abbreviated as %s' % (state, abbrev)

# Print every city in state
print '-' * 15
for abbrev, city in cities.items():
	print '%s has city: %s' % (abbrev, city)

# Now do both at the same time
print '-' * 15
for state, abbrev in states.items():
	print '%s(abbreviated as %r) has state: %s' % (state, abbrev, cities[abbrev])

print '-' * 15
# Safely get an abbreviation by state that might not be there
m_state = states.get('TX', None)
if not m_state:
	print 'Sorry no Texas'

# Get a city with a default value
m_city = cities.get('TX', 'Does\'nt exist.')
print 'The city for state \'TX\' is %r' % m_city


