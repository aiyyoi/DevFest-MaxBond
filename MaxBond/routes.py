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
    for result in nodes_results:
      d = {
        'uid':result.uid,
        'name':result.name,
        'photo':result.image,
        'tags':[1,2,3],  # chage here!
        'link':root_path+"/users/"+str(result.uid)
      }
      nodes.append(d)

    pplinks = []
    for i in xrange(1, len(nodes_results)):
      d = {"source":0, "target": nodes_results[i].uid}
      pplinks.append(d)


    return jsonify(nodes=nodes, pplinks=pplinks)

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
