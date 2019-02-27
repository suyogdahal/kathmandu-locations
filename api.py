from flask import Flask
from flask_restful import Api,Resource
import json

app = Flask(__name__)
api = Api(app)

data = dict(
	
	locations=json.loads(open('locations.json').read())
	
	)

class API(Resource):	
	def get(self):
		return data

api.add_resource(API,"/")

if __name__=="__main__":
	app.run(debug=False)