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
def get_graph_data():
  if request.method == 'GET':
    # search_tags = request.values.getlist('tag')
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


@app.route('/users/<int:uid>', methods=['GET'])
def get_one_user(uid):
  if request.method == 'GET':
    result = User.query.filter_by(uid=uid).first()
    tag_info = []
    for tag in has_tag.query.filter_by(User_uid=result.uid).all():
      tmp = Tag.query.filter_by(tid=tag.Tag_tid).first()
      tag_info.append({'tid':tmp.tid,'name': tmp.name,'category': tmp.category,'link':root_path+"/tags/"+str(tmp.tid)})
    json_results = {
      'uid': result.uid,
      'name': result.name,
      'gender': result.gender,
      'photo': result.image,
      'tags':tag_info
    }
    return jsonify(json_results)


@app.route('/tags/<int:tid>', methods=['GET'])
def get_one_tag(tid):
  if request.method == 'GET':
    result = Tag.query.filter_by(tid=tid).first()
    users = [user.User_uid for user in has_tag.query.filter_by(Tag_tid=result.tid).all()]
    user_info = []
    for user in has_tag.query.filter_by(Tag_tid=result.tid).all():
      tmp = User.query.filter_by(uid=user.User_uid).first()
      user_info.append({'uid':tmp.uid,'name': tmp.name,'gender': tmp.gender,'photo':tmp.image,'link':root_path+"/users/"+str(tmp.uid)})
    json_results = {
      'tid': result.tid,
      'name': result.name,
      'category': result.category,
      'users': user_info
    }
    return jsonify(json_results)


# @app.route('/graph_data?tag=', methods=['GET'])
# def get_one_tag(tid):
#   if request.method == 'GET':
#     result = Tag.query.filter_by(tid=tid).first()
#     users = [user.User_uid for user in has_tag.query.filter_by(Tag_tid=result.tid).all()]
#     json_results = {
#       'tid': result.tid,
#       'name': result.name,
#       'category': result.category,
#       'users': users
#     }
#     return jsonify(json_results)

if __name__ == '__main__':
  app.run(debug=True)
