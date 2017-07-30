from flask import Flask, Response
from flask_restful import Resource, Api
import dataframe_lookup as dl
import json

app = Flask(__name__)
api = Api(app)

class GetRGBList(Resource):
  def get(self):
    result = dl.getRGBList()
    return Response(json.JSONEncoder().encode(result), mimetype='text/json')

class GetRGB(Resource):
    def get(self, color_name):
        result = json.dumps(dl.findRGBValues(color_name.lower()))
        return Response(result, mimetype='text/json')

class Default(Resource):
    def get(self):
        return Response(json.dumps({}), mimetype='text/json')

api.add_resource(GetRGBList, '/all')
api.add_resource(GetRGB, '/<color_name>')
api.add_resource(Default, '/')

if __name__ == '__main__':
    app.run(debug=True)
