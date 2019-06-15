import sqlite3

with sqlite3.connect('blog.db') as conn:
    c = conn.cursor()

    c.execute("CREATE TABLE blog(title TEXT, post TEXT)")

    titles = [
        "First Blog Post",
        "Second Blog Post",
        "Third Blog Post",
        "Fourth Blog Post",
        "Fifth Blog Post",
        "Sixth Blog Post",
        "Seventh Blog Post",
        "Eighth Blog Post",
        "Nineth Blog Post",
        "Tenth Blog Post"
        ]
    post = """

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in arcu elit. Vivamus nunc dolor, porttitor sed ultricies quis, pulvinar eget quam. Aenean tristique felis ac odio tincidunt faucibus. Nullam erat nulla, tincidunt a nibh ac, suscipit sagittis felis. Sed tempus erat non nulla elementum, ac volutpat lorem congue. In iaculis pellentesque nulla, et porttitor ligula pellentesque efficitur. In euismod lectus vitae magna porttitor, congue efficitur nisl mollis. Etiam diam libero, ultricies id feugiat sed, ullamcorper in est. Praesent vestibulum, turpis a fermentum ornare, tellus nunc rutrum diam, eget auctor dui eros at ante.

        Cras dignissim felis at risus elementum pulvinar. Nulla facilisi. Etiam nec rutrum tellus. Mauris vitae accumsan ex. Praesent fermentum purus sed diam porta sollicitudin. Donec non lorem eget orci condimentum cursus ut a mi. Aenean eget felis magna. Vestibulum ut est vehicula, tempor mauris a, auctor diam. Phasellus porttitor orci id est hendrerit, eget sagittis ipsum eleifend. Phasellus tincidunt imperdiet quam, vel malesuada lorem lacinia quis. Nam sed elit cursus, consectetur lacus id, ornare nulla. Nullam vel neque quis est gravida vestibulum in a lacus. Mauris dignissim ac metus quis sagittis. Aliquam pulvinar metus ac justo varius cursus. In interdum sit amet diam id lobortis. Aenean massa ex, tristique non rhoncus eget, feugiat vitae ex.

        Proin vel molestie justo. Aliquam ac dui eget lorem consequat pulvinar sit amet ac risus. Mauris eget odio eget sapien imperdiet pretium. Praesent placerat nisl vitae mi porttitor, sed tincidunt enim condimentum. Suspendisse non scelerisque nunc. Maecenas at metus eros. Donec at nunc non odio dictum volutpat consectetur efficitur odio. Sed sed augue sodales, vulputate sem sit amet, vehicula nisi. Integer sagittis blandit ante id viverra. Cras varius dui sapien, at efficitur nisl maximus a. Integer sollicitudin viverra vulputate. Praesent nec massa ultrices, mattis nisi vitae, vestibulum purus. Nunc quis neque lacus. Vivamus consectetur, ante nec volutpat facilisis, arcu nunc mollis magna, at faucibus libero elit in risus.

        Fusce malesuada ullamcorper malesuada. Maecenas sodales enim lacus, fermentum suscipit leo posuere sed. Aliquam vestibulum ultrices est, lacinia placerat enim commodo eget. Curabitur sagittis nisi felis, et dictum quam dapibus tristique. Maecenas vel pretium est, at suscipit lectus. Suspendisse mattis tellus nec justo faucibus tincidunt sed non est. In laoreet ante vel tellus venenatis interdum.

        Duis interdum diam sed magna tristique rhoncus. Nullam eu porttitor elit, sed scelerisque enim. Suspendisse sed finibus mauris, ac finibus sapien. Pellentesque posuere, metus pretium pulvinar convallis, tortor felis lacinia ligula, nec blandit risus sapien sit amet mi. Maecenas tortor metus, cursus et facilisis ac, pellentesque et libero. Aliquam auctor eros nec dolor convallis, at suscipit libero ullamcorper. Ut iaculis ex sed convallis finibus. Proin id dignissim nisl. Fusce id ligula non odio imperdiet bibendum et a quam. Aliquam a pulvinar nibh. Nullam erat massa, tempor sit amet purus sit amet, aliquam consequat purus. Integer enim velit, auctor eu tortor quis, scelerisque auctor dui. Curabitur ut ornare augue, eget pellentesque mauris. """


    for title in titles:
        c.execute("INSERT INTO blog VALUES(?, ?)", (title, post))
