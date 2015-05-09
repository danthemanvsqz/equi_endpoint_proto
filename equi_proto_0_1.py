from flask import Flask, request, make_response 
from yelpclient import YelpClient

import json

app = Flask(__name__)

keys = dict(
	consumer_key = 'L72j0smNCe7V_LsO5TOR6Q',
	consumer_secret = 'fuKJGiwM02CiT9_OKVf4que2-o0',
	token = 'zUF4IS8oRqVXvbMdqPN1xTXIDBrLobcl',
	token_secret = 'ly7PS3Rm9Fr4TSjtOHCNVQg2UvI')


@app.route('/')
def home():
    try:
	    term = request.args.get('term')
	    latlong = request.args['latlong']
	    radius = request.args['radius']
    except KeyError as unused_e:
	return make_response('404', 404)
    points_l = latlong.strip('()').split(',')
    latlong = float(points_l[0]), float(points_l[1])
    
    client = YelpClient(keys)
    api_resp = client.search_by_geo_coord(latlong=latlong, term=term, radius=float(radius))
    return json.dumps(api_resp)

if __name__ == '__main__':
    app.run(debug=True)
