
from flask import Flask, render_template
app = Flask(__name__)
import csv

# code copied and modified from modules.py

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

doglist = convert_to_dict('dogbreeds.csv')

pairs_list= []
for d in doglist:
    pairs_list.append( (d['Dog-number'], d['Breed']) )

# code copied and modified from hello3.py and Flask Tutorials 1-4

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list)

@app.route('/dog/<num>')
def detail(num):
    try:
        dogs_dict = doglist[int(num) - 1 ]
    except:
        return f"<h1>Invalid value for dog number: {num}</h1>"
    return render_template('dog.html', dogs=dogs_dict)

if __name__ == '__main__':
    app.run(port=4999, debug=True)
