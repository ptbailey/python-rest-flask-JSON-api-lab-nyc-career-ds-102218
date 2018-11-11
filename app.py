from flask import Flask, render_template, jsonify
from pictures_data import Pictures

# create Flask app
app = Flask(__name__)

# --- API Routes ---
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
#by putting int before our variable id, tell route to expect integer
def picture_id(id):
    picture = next(picture for picture in Pictures if picture['id'] == id)
    return jsonify(picture)

@app.route('/api/pictures/<country>')
def picture_country(country):
    picture = next(picture for picture in Pictures if picture['country'].lower()\
     == country.lower())
    return jsonify(picture)

# --- HTML Routes ---
@app.route('/pictures')
def pictures_general():
    return render_template('pictures_index.html', pictures = Pictures)

@app.route('/pictures/<int:id>')
def pictures_show(id):
    for pic in Pictures:
        if pic['id'] == id:
            return render_template('picture_show.html', picture=pic)
    return "<h1>Sorry, no there is no picture with that id!</h1>"

@app.route('/pictures/<country>')
def pictures_list_by_country(country):
    pictures = [picture for picture in Pictures if \
    picture['country'].lower() == country.lower()]
    return render_template('pictures_index.html', pictures=pictures)

# run our Flask app
if __name__ == '__main__':
    app.run(debug = True)
