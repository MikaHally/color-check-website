from matplotlib.colors import is_color_like

color = input("What is you favorite color? ")
header = f"<h1 style=\"color:{color};text-align:center;font-size:70px\">{color} is a beautiful color.</h1>"
error = "<h1 style=\"text-align:center;font-size:70px\">I am sorry but this is not a color.</h1>"

if is_color_like(color):
    print("I really like the color " + color.lower() + ".")
    html = open("index.html", "w")
    html.write(header)
    html.close()
else:
    print("I am sorry but this is not a color.")
    html = open("index.html", "w")
    html.write(error)
    html.close()
