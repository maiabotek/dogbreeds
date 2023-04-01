
# Copied from Python Beginners Deploy an App Page

"""standard freeze script"""

from flask_frozen import Freezer

from dogs import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
