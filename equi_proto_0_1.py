from flask import Flask, request, make_response 
from yelpclient import YelpClient

import json
import os

app = Flask(__name__)

KEYS = dict(
	consumer_key = 'L72j0smNCe7V_LsO5TOR6Q',
	consumer_secret = 'fuKJGiwM02CiT9_OKVf4que2-o0',
	token = 'zUF4IS8oRqVXvbMdqPN1xTXIDBrLobcl',
	token_secret = 'ly7PS3Rm9Fr4TSjtOHCNVQg2UvI')

RADIUS = 500.0

SFO_GEO = 37.618889, -122.375

@app.route('/')
def home():
    try:
	    term = request.args.get('term')
	    latlong_raw = request.args['latlong']
    except KeyError as unused_e:
	    return make_response('404', 404)
	    
    points = latlong_raw.strip('()').split(',')
    points = float(points[0]), float(points[1])
    
    latlong = (SFO_GEO[0] + points[0])/2.0, (SFO_GEO[1] + points[1])/2.0

    client = YelpClient(KEYS)
    api_resp = client.search_by_geo_coord(latlong=latlong, term=term)
    return json.dumps(api_resp)

if __name__ == '__main__':
    app.run(debug=True, host=str(os.environ['IP']), port=int(os.environ['PORT']))