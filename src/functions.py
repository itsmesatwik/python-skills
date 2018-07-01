def function():
    #do something
    return 0
# function end

def change_name(name):
    name = "lol"

name = "yolo"
change_name(name)
# has no effect on the global var name

name = change_name(name)
#changes name to yolo

