from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


names = {"micalela": {"age": 27, "gender": "female", "occupation": "cutie"},
          }

""" class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    
    def post(self):
        return {"data": "Posted"}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>") """

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is missing", required=True)
video_put_args.add_argument("views", type=int, help="Views are missing", required=True)
video_put_args.add_argument("likes", type=int, help="Likes are missing", required=True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}
    
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)