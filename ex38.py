# create a mapping of state to abbreviation
states = {
    'Ofregon': 'OR',
    'Florida': 'FL',
    'Califonia': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 30
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 30
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 30
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 30
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 30
for abbrev, city  in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 30
for state, abbrev in states.items():
    print "%snstate is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."
    
# get a city eith a defaul value
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % city
