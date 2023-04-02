
## The Small Dog Directory by Maia Botek

This webpage was built to show off just how different each small dog is from other breeds. People tend to stereotype small dogs as annoying or unintelligent when that couldn't be farther from the truth! I gathered information from the

### About Each File

+ **Dog.html** is the templated detail page for each breed that is filled with information from the dictionary, using Jinja templates and allows the user to navigate back to the directory page.

+ **dogbreeds.csv** is a file with information from the American Kennel Club about 20 small dog breeds and their respective personality, average weight, life expectancy, and coat length. There is also information from Wikimedia Commons with an image of each dog breed and necessary information to attribute the content.

+ **Dogs.Py** is modified from code that was written for an example Presidents Flask app in a file called modules.py. It starts by importing Flask, render_template and the CSV module. In the function convert_to_dict, it reads the dogbreeds.csv file and converts it to a dictionary assigned to a variable named doglist.

    The file also runs a for loop to append the unique index keys and respective dog breeds (as a tuple) to an empty list, pairs_list. In the first route       and function (index) this list is assigned a variable, pairs, and passed to the index.html template.

    Finally, the second route with the function, detail, accounts for the fact that list indexes start at zero, and returns an error if the user adds an       invalid index into the url. Finally, the function renders the individualized breed pages, dog.html, with information from the dictionary that is           assigned to the variable name, dogs.

+ **Freeze.Py** is modified from code from the Flask Introduction page of our advanced web applications course website and imports the Flask App, dogs.py, to be baked out and uploaded on the server.

+ **Index.html** is the templated index page to display all 20 breeds that users start on and can use to navigate to other breeds.

+ **smalldogdirectory** is a renamed version of the build file that was created from Freeze.py and what is uploaded to FileZilla in order to support the hosted website.


### Challenges and What I Learned

1. One of the challenges I had was writing the for loop to allow the index page to display the links dynamically. After following the Flask Tutorial video, I made sure to be extra attentive to the variables I was passing through and how I defined them in the Flask App code and the subsequent template pages.

2. Another challenge I had was with Jinja formatting, so I looked closely at patterns. Making note of features like the double brackets and relationship to the dictionary allowed me to see which code in the template I needed to modify from the presidents example app to my own.

3. Finally, I was a bit confused on how I would be able to include the new files into my FileZilla and to my hosted site without interfering with a previous project I had uploaded. Given that there was another index.html, I was concerned that something would be overwritten incorrectly. I followed the instructions [in this video](https://www.youtube.com/watch?v=Ejo_2zRbQJk) and after freezing my Flask, I was careful to move it as a completely separate directory from other projects I had worked on, and the page was uploaded successfully to my [reclaim hosting site.](https://maiabotek.reclaim.hosting/smalldogdirectory/)


[^note]:
    Some of the code was modified and adapted from the presidents Flask app, which is found in [this repository](https://github.com/macloo/python-adv-web-apps/tree/master/python_code_examples/flask/presidents).
