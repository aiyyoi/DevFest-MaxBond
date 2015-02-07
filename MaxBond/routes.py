from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/maxbond'
root_path = 'localhost:5000'

class User(db.Model):
  __tablename__ = 'User'
  uid = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  gender = db.Column(db.Integer)
  image = db.Column(db.String(255))

class Tag(db.Model):
  __tablename__ = 'Tag'
  tid = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  category = db.Column(db.Integer)

class has_tag(db.Model):
  __tablename__ = 'has_tag'
  id = db.Column(db.Integer, primary_key = True)
  User_uid = db.Column(db.Integer)
  Tag_tid = db.Column(db.Integer)


@app.route('/graph_data/', methods=['GET'])
def graph_data():
  if request.method == 'GET':
    nodes = []
    nodes_results = User.query.all()
    user_ids = [result.uid for result in nodes_results]
    for result in nodes_results:
      tags = [tag.Tag_tid for tag in has_tag.query.filter_by(User_uid=result.uid).all()]
      d = {
        'id':result.uid,
        'name':result.name,
        'photo':result.image,
        'tags':tags,
        'link':root_path+"/users/"+str(result.uid),
        'isUser':True 
      }
      nodes.append(d)

    tags_results = Tag.query.all()
    for result in tags_results:
      users = [user.User_uid for user in has_tag.query.filter_by(Tag_tid=result.tid).all()]
      d = {
        'id':result.tid,
        'name':result.name,
        'category':result.category,
        'users':users,
        'link':root_path+'/tags/'+str(result.tid),
        'isUser':False 
      }
      nodes.append(d)

    links = []
    origin_user = user_ids[0]
    for uid in user_ids:
      d = {
        'source':origin_user,
        'target':uid
      }
    links.append(d)
    pt_results = has_tag.query.all()
    for result in pt_results:
      d = {
        'source':result.User_uid,
        'target':result.Tag_tid
      }
      links.append(d)


    return jsonify(nodes=nodes, links=links)

# @app.route('/sightings/<int:sighting_id>', methods=['GET'])
# def sighting(sighting_id):
#   if request.method == 'GET':
#     result = Sighting.query.filter_by(id=sighting_id).first()

#     json_results = {'sighted_at': result.sighted_at,
#                    'reported_at': result.reported_at,
#                    'location': result.location,
#                    'shape': result.shape,
#                    'duration': result.duration,
#                    'description': result.description,
#                    'lat': result.lat,
#                    'lng': result.lng}

#     res = jsonify(items=json_results)
#     res.headers['Access-Control-Allow-Origin'] = '*'
#     return res

if __name__ == '__main__':
  app.run(debug=True)
