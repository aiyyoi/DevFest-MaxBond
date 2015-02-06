GRAPH_DATA
-------------
### GET http://localhost:8000/graph_data
Display all the data for graph

**Success Response**
```json
{
  "nodes":[
    {"uid":0,"name":"Amy","photo":"/resources/photo0.png",""tags":[1,3],"link":"http://localhost:8000/users/0"},
    {"uid":1,"name":"Myriel","photo":"/resources/photo1.png","tags":[2,3],"link":"http://localhost:8000/users/1"},
    {"uid":2,"name":"Napoleon","photo":"/resources/photo2.png","tags":[4],"link":"http://localhost:8000/users/2"},
    {"uid":3,"name":"Mme.Hucheloup","photo":"/resources/photo3.png","tags":[0,4],"link":"http://localhost:8000/users/3"}
  ],
  "pplinks":[
    {"source":0,"target":1},
    {"source":0,"target":2},
    {"source":0,"target":3}
  ],
  "ptlinks":[
    {"source":0,"target":1},
    {"source":0,"target":3},
    {"source":1,"target":2}
    ...
  ]
  ,
  "tags":[
    {"tid":0,"name":"columbia","category":1,"nodes":[3],"link":"http://localhost:8000/tags/0"},
    {"tid":1,"name":"startup","category":2,"nodes":[0],"link":"http://localhost:8000/tags/1"},
    {"tid":2,"name":"beijing","category":3,"nodes":[1],"link":"http://localhost:8000/tags/2"},
    {"tid":3,"name":"google","category":4,"nodes":[0,1],"link":"http://localhost:8000/tags/3"},
    {"tid":4,"name":"python","category":5,"nodes":[3],"link":"http://localhost:8000/tags/4"}
  ]
}

```
### GET http://localhost:8000/graph_data?q="tag=columbia&tag=doubi&tag=startup"
Search for users with specific tags. Same format with above.

### POST http://localhost:8000/users/333/tags/1
### POST http://localhost:8000/tags/1/users/333
both requests can be used to add relation between tags and users


PEOPLE
-------------
### GET http://localhost:8000/users/333
Display the info of user 333

**Success Response**

```json
{
   "uid":333,
   "name":"Xiaoqian",
   "gender":"Male",
   "photo":"/resources/photo6.png"
   "tags":[
        {"tid":0,"name":"columbia","category":1,"nodes":[3],"link":"http://localhost:8000/tags/0"},
        {"tid":1,"name":"startup","category":2,"nodes":[0],"link":"http://localhost:8000/tags/1"}
   ]
}

```

### PUT http://localhost:8000/users/333

Update info of a user.

**Success Response**

No response



### POST http://localhost:8000/users

add a new user.

**Success Response**

```json
{
    "status":200,
    "Location":"http://localhost:8000/users/333"
}
```



### DELETE http://localhost:8000/users/333

Delete a user.

**Success Response**

```json
{
    "status": 204,
    "data":"delete success"
}
```

TAG
-------------
### GET http://localhost:8000/tags/333
Display the info of tag 333

**Success Response**

```json
{
   "tid":0,
   "name":"columbia",
   "category":1,
   "nodes":[
    {"uid":3,"name":"Mme.Hucheloup","photo":"/resources/photo3.png","tags":[0,4],"link":"http://localhost:8000/users/3"},
    {"uid":3,"name":"Mme.Hucheloup","photo":"/resources/photo3.png","tags":[0,4],"link":"http://localhost:8000/users/3"}
   ]
}

```

### PUT http://localhost:8000/tags/333

Update info of a tag.

**Success Response**

No response



### POST http://localhost:8000/tags

add a new tag.

**Success Response**

```json
{
    "status":200,
    "Location":"http://localhost:8000/tags/333"
}
```



### DELETE http://localhost:8000/tags/333

Delete a tag.

**Success Response**

```json
{
    "status": 204,
    "data":"delete success"
}
```