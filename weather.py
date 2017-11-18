import urllib2
import json
key = "16db7e12721dfa85"
while 1:
    zip = raw_input('For which city would you like to see the weather? ')
    url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zip + '.json'
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    weather = parsed_json['current_observation']['weather']
    temperature_string = parsed_json['current_observation']['temperature_string']
    feelslike_string = parsed_json['current_observation']['feelslike_string']
    print 'Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.'
    f.close()
