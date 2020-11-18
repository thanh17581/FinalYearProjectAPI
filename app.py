from flask import Flask, jsonify, render_template, redirect, url_for, request

app = Flask(__name__)

true = True
false = False

arr = [1, 2, 3, 4]

dataRestaurant = [
    dict(id=1, title="The Jungle Beehive", image="http:\/\/i0sa.com\/food\/images\/rests\/1.jpg",
         delivery_time="30-40 min", rating=2.2, rating_count=116, genres=[
            "Koshari",
            "Koshari",
            "Sea Food"
        ], liked=false, is_exculsive=true),
    dict(id=2, title="The Cocoa Bites", image="http:\/\/i0sa.com\/food\/images\/rests\/2.jpg",
         delivery_time="30-40 min", rating=4.1, rating_count=68, genres=[
            "Koshari",
            "Koshari"
        ], liked=false, is_exculsive=false),
    dict(id=3, title="The Waterway Devil", image="http:\/\/i0sa.com\/food\/images\/rests\/3.jpg",
         delivery_time="30-40 min", rating=4.5, rating_count=63, genres=[
            "Kebda",
            "Sea Food",
            "Pizza"
        ], liked=false, is_exculsive=true),
    dict(id=4, title="The Jungle Beehive", image="http:\/\/i0sa.com\/food\/images\/rests\/4.jpg",
         delivery_time="30-40 min", rating=4.5, rating_count=107, genres=[
            "Sea Food",
            "Pizza",
            "Burgers"
        ], liked=true, is_exculsive=false),
    dict(id=5, title="The Waterway Devil", image="http:\/\/i0sa.com\/food\/images\/rests\/5.jpg",
         delivery_time="30-40 min", rating=3.4, rating_count=78, genres=[
            "Sea Food",
            "Kebda",
            "Burgers",
            "Sea Food"
        ], liked=true, is_exculsive=false),
    dict(id=6, title="The Light Paradise", image="http:\/\/i0sa.com\/food\/images\/rests\/6.jpg",
         delivery_time="30-40 min", rating=3.1, rating_count=124, genres=[
            "Pizza"
        ], liked=true, is_exculsive=false),
    dict(id=7, title="The Silk Exhibit", image="http:\/\/i0sa.com\/food\/images\/rests\/7.jpg",
         delivery_time="30-40 min", rating=3.1, rating_count=112, genres=[
            "Kebda",
            "Sea Food",
            "Pizza",
            "Burgers"
        ], liked=false, is_exculsive=false),
    dict(id=8, title="The Light Paradise", image="http:\/\/i0sa.com\/food\/images\/rests\/8.jpg",
         delivery_time="30-40 min", rating=5.3, rating_count=24, genres=[
            "Pizza",
            "Kebda",
            "Kebda",
            "Koshari"
        ], liked=false, is_exculsive=false),
    dict(id=9, title="The Waterway Devil", image="http:\/\/i0sa.com\/food\/images\/rests\/9.jpg",
         delivery_time="30-40 min", rating=2.5, rating_count=49, genres=[
            "Koshari"
        ], liked=false, is_exculsive=false),
    dict(id=10, title="The Abacus Hook", image="http:\/\/i0sa.com\/food\/images\/rests\/10.jpg",
         delivery_time="30-40 min", rating=5.3, rating_count=150, genres=[
            "Pizza",
            "Koshari",
            "Kebda"
        ], liked=false, is_exculsive=false),
    dict(id=11, title="The Silk Exhibit", image="http:\/\/i0sa.com\/food\/images\/rests\/11.jpg",
         delivery_time="30-40 min", rating=4.4, rating_count=100, genres=[
            "Sea Food",
            "Koshari",
            "Pizza"
        ], liked=false, is_exculsive=false),
    dict(id=12, title="Gentle", image="http:\/\/i0sa.com\/food\/images\/rests\/12.jpg", delivery_time="30-40 min",
         rating=4.1, rating_count=164, genres=[
            "Pizza",
            "Burgers",
            "Sea Food"
        ], liked=true, is_exculsive=false),
    dict(id=13, title="The Crystal Cow", image="http:\/\/i0sa.com\/food\/images\/rests\/13.jpg",
         delivery_time="30-40 min", rating=4.5, rating_count=154, genres=[
            "Kebda",
            "Kebda",
            "Koshari",
            "Burgers"
        ], liked=false, is_exculsive=false),
    dict(id=14, title="The Cocoa Bites", image="http:\/\/i0sa.com\/food\/images\/rests\/14.jpg",
         delivery_time="30-40 min", rating=4.4, rating_count=152, genres=[
            "Sea Food",
            "Pizza",
            "Kebda",
            "Koshari"
        ], liked=false, is_exculsive=false),
    dict(id=15, title="The Momument", image="http:\/\/i0sa.com\/food\/images\/rests\/15.jpg", delivery_time="30-40 min",
         rating=3.2, rating_count=165, genres=[
            "Kebda"
        ], liked=false, is_exculsive=false),
    dict(id=16, title="The Eastern Fish", image="http:\/\/i0sa.com\/food\/images\/rests\/16.jpg",
         delivery_time="30-40 min", rating=3.2, rating_count=192, genres=[
            "Burgers"
        ], liked=false, is_exculsive=false),
    dict(id=17, title="The Court Bites", image="http:\/\/i0sa.com\/food\/images\/rests\/17.jpg",
         delivery_time="30-40 min", rating=1.2, rating_count=146, genres=[
            "Koshari",
            "Burgers"
        ], liked=true, is_exculsive=false),
    dict(id=18, title="The Paradise Hook", image="http:\/\/i0sa.com\/food\/images\/rests\/18.jpg",
         delivery_time="30-40 min", rating=3.4, rating_count=131, genres=[
            "Pizza"
        ], liked=true, is_exculsive=false),
    dict(id=19, title="The Crystal Cow", image="http:\/\/i0sa.com\/food\/images\/rests\/19.jpg",
         delivery_time="30-40 min", rating=4.2, rating_count=138, genres=[
            "Koshari"
        ], liked=false, is_exculsive=false),
    dict(id=20, title="The Momument", image="http:\/\/i0sa.com\/food\/images\/rests\/20.jpg", delivery_time="30-40 min",
         rating=1.3, rating_count=110, genres=[
            "Sea Food",
            "Kebda"
        ], liked=false, is_exculsive=false)
]

types = [
    dict(id=0, image="http://i0sa.com/food/images/types/all.jpeg", title="All"),
    dict(id=1, image="http://i0sa.com/food/images/types/chinese.jpg", title="Chinese"),
    dict(id=2, image="http://i0sa.com/food/images/types/egyptian.jpg", title="Egyptian"),
    dict(id=3, image="http://i0sa.com/food/images/types/french.jpg", title="French"),
    dict(id=4, image="http://i0sa.com/food/images/types/indian.jpg", title="Indian")
]

data = {
    "status": "success",
    "message": "No data",
    "data": {
        "title": "Naser City, Cairo",
        "types": [
            {
                "id": 0,
                "image": "http://i0sa.com/food/images/types/all.jpeg",
                "title": "All"
            },
            {
                "id": 1,
                "image": "http://i0sa.com/food/images/types/chinese.jpg",
                "title": "Chinese"
            },
            {
                "id": 2,
                "image": "http://i0sa.com/food/images/types/egyptian.jpg",
                "title": "Egyptian"
            },
            {
                "id": 3,
                "image": "http://i0sa.com/food/images/types/french.jpg",
                "title": "French"
            },
            {
                "id": 4,
                "image": "http://i0sa.com/food/images/types/indian.jpg",
                "title": "Indian"
            }
        ]
    }
}

dataR = {
    "data": [
        {
            "id": 1,
            "title": "The Jungle Beehive",
            "image": "http://i0sa.com/food/images/rests/1.jpg",
            "delivery_time": "30-40 min",
            "rating": 2.2,
            "rating_count": 116,
            "genres": [
                "Koshari",
                "Koshari",
                "Sea Food"
            ],
            "liked": false,
            "is_exculsive": true
        },
        {
            "id": 2,
            "title": "The Cocoa Bites",
            "image": "http://i0sa.com/food/images/rests/2.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.1,
            "rating_count": 68,
            "genres": [
                "Koshari",
                "Koshari"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 3,
            "title": "The Waterway Devil",
            "image": "http://i0sa.com/food/images/rests/3.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.5,
            "rating_count": 63,
            "genres": [
                "Kebda",
                "Sea Food",
                "Pizza"
            ],
            "liked": false,
            "is_exculsive": true
        },
        {
            "id": 4,
            "title": "The Jungle Beehive",
            "image": "http://i0sa.com/food/images/rests/4.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.5,
            "rating_count": 107,
            "genres": [
                "Sea Food",
                "Pizza",
                "Burgers"
            ],
            "liked": true,
            "is_exculsive": false
        },
        {
            "id": 5,
            "title": "The Waterway Devil",
            "image": "http://i0sa.com/food/images/rests/5.jpg",
            "delivery_time": "30-40 min",
            "rating": 3.4,
            "rating_count": 78,
            "genres": [
                "Sea Food",
                "Kebda",
                "Burgers",
                "Sea Food"
            ],
            "liked": true,
            "is_exculsive": false
        },
        {
            "id": 6,
            "title": "The Light Paradise",
            "image": "http://i0sa.com/food/images/rests/6.jpg",
            "delivery_time": "30-40 min",
            "rating": 3.1,
            "rating_count": 124,
            "genres": [
                "Pizza"
            ],
            "liked": true,
            "is_exculsive": false
        },
        {
            "id": 7,
            "title": "The Silk Exhibit",
            "image": "http://i0sa.com/food/images/rests/7.jpg",
            "delivery_time": "30-40 min",
            "rating": 3.1,
            "rating_count": 112,
            "genres": [
                "Kebda",
                "Sea Food",
                "Pizza",
                "Burgers"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 8,
            "title": "The Light Paradise",
            "image": "http://i0sa.com/food/images/rests/8.jpg",
            "delivery_time": "30-40 min",
            "rating": 5.3,
            "rating_count": 24,
            "genres": [
                "Pizza",
                "Kebda",
                "Kebda",
                "Koshari"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 9,
            "title": "The Waterway Devil",
            "image": "http://i0sa.com/food/images/rests/9.jpg",
            "delivery_time": "30-40 min",
            "rating": 2.5,
            "rating_count": 49,
            "genres": [
                "Koshari"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 10,
            "title": "The Abacus Hook",
            "image": "http://i0sa.com/food/images/rests/10.jpg",
            "delivery_time": "30-40 min",
            "rating": 5.3,
            "rating_count": 150,
            "genres": [
                "Pizza",
                "Koshari",
                "Kebda"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 11,
            "title": "The Silk Exhibit",
            "image": "http://i0sa.com/food/images/rests/11.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.4,
            "rating_count": 100,
            "genres": [
                "Sea Food",
                "Koshari",
                "Pizza"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 12,
            "title": "Gentle",
            "image": "http://i0sa.com/food/images/rests/12.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.1,
            "rating_count": 164,
            "genres": [
                "Pizza",
                "Burgers",
                "Sea Food"
            ],
            "liked": true,
            "is_exculsive": false
        },
        {
            "id": 13,
            "title": "The Crystal Cow",
            "image": "http://i0sa.com/food/images/rests/13.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.5,
            "rating_count": 154,
            "genres": [
                "Kebda",
                "Kebda",
                "Koshari",
                "Burgers"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 14,
            "title": "The Cocoa Bites",
            "image": "http://i0sa.com/food/images/rests/14.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.4,
            "rating_count": 152,
            "genres": [
                "Sea Food",
                "Pizza",
                "Kebda",
                "Koshari"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 15,
            "title": "The Momument",
            "image": "http://i0sa.com/food/images/rests/15.jpg",
            "delivery_time": "30-40 min",
            "rating": 3.2,
            "rating_count": 165,
            "genres": [
                "Kebda"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 16,
            "title": "The Eastern Fish",
            "image": "http://i0sa.com/food/images/rests/16.jpg",
            "delivery_time": "30-40 min",
            "rating": 3.2,
            "rating_count": 192,
            "genres": [
                "Burgers"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 17,
            "title": "The Court Bites",
            "image": "http://i0sa.com/food/images/rests/17.jpg",
            "delivery_time": "30-40 min",
            "rating": 1.2,
            "rating_count": 146,
            "genres": [
                "Koshari",
                "Burgers"
            ],
            "liked": true,
            "is_exculsive": false
        },
        {
            "id": 18,
            "title": "The Paradise Hook",
            "image": "http://i0sa.com/food/images/rests/18.jpg",
            "delivery_time": "30-40 min",
            "rating": 3.4,
            "rating_count": 131,
            "genres": [
                "Pizza"
            ],
            "liked": true,
            "is_exculsive": false
        },
        {
            "id": 19,
            "title": "The Crystal Cow",
            "image": "http://i0sa.com/food/images/rests/19.jpg",
            "delivery_time": "30-40 min",
            "rating": 4.2,
            "rating_count": 138,
            "genres": [
                "Koshari"
            ],
            "liked": false,
            "is_exculsive": false
        },
        {
            "id": 20,
            "title": "The Momument",
            "image": "http://i0sa.com/food/images/rests/20.jpg",
            "delivery_time": "30-40 min",
            "rating": 1.3,
            "rating_count": 110,
            "genres": [
                "Sea Food",
                "Kebda"
            ],
            "liked": false,
            "is_exculsive": false
        }
    ],
    "status": "success",
    "message": "No data"
}

dataHome = dict(title="Naser City, Cairo", types=types)


@app.route("/Home")
def dummy_api():
    # return jsonify(data=data, status="200", message="success")
    return data


@app.route("/RestTypes")
def dummy_api1():
    # return jsonify(data=dataRestaurant, status="200", message="success")
    if request.args.get("id"):
        id = request.args.get("id")
        p = data["data"]["title"]
        return str(p)
    else:
        return dataR

@app.route("/Rest")
def dummy_api2():
    return jsonify(data=dataRestaurant, status="200", message="success")


@app.route("/PlaceOrder")
def dummy_api3():
    return jsonify(data=dataRestaurant, status="200", message="success")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return "success"
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run()
