#!/usr/bin/python3.8
import eel, json, requests, createconfig, re
from shutil import copyfile
from sys import argv
from os import remove as rm
from os import chdir
import os
from pathlib import Path

chdir(str(Path(argv[0]).parent))
@eel.expose
def done_with_one(subject):
    weekly_json = json.loads(open("weekly.json").read())
    del weekly_json[weekly_json.index(subject)]
    with open("weekly.json", "w+") as f:
        f.write(json.dumps(weekly_json))

@eel.expose
def startWeek():
    to_put = open("startfrom.json").read()
    with open("weekly.json", "w+") as f:
        f.write(to_put)

    return json.loads(to_put)

@eel.expose
def newItem(thing):
    weekly_json = json.loads(open("weekly.json").read())
    weekly_json.append(thing)
    print(weekly_json)
    with open("weekly.json", "w+") as f:
        f.write(json.dumps(weekly_json))

@eel.expose
def loadjson(filename):
    return json.loads(open(filename).read())

@eel.expose
def new_background(path_to_ffile):
    try:
        copyfile(path_to_file, "./web/background.jpg")
    except:
        rm("./web/background.jpg")

@eel.expose
def change_title_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('h1') for i in lines]
    to_replace = color_line.index(True)+1
    lines[to_replace] = f"    color: {color};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_subtitle_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('h2') for i in lines]
    to_replace = color_line.index(True)+1
    lines[to_replace] = f"    color: {color};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_background_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('body') for i in lines]
    to_replace = color_line.index(True)+1
    lines[to_replace] = f"    background: {color};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_line_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('hr') for i in lines]
    to_replace = color_line.index(True)+2
    border_width = re.compile(r"\d+px").search(lines[to_replace]).group()
    border_type = re.compile("dotted|dashed|solid|double|groove|ridge|inset|outset|none|hidden").search(lines[to_replace]).group()
    lines[to_replace] = f"    border-top: {color} {border_width} {border_type};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def load_config(user):
    print(requests.post("https://configfetch--rhinocodes.repl.co/config", data={"user": user, "type": "read"}).text)
    config = json.loads(requests.post("https://configfetch--rhinocodes.repl.co/config", data={"user": user, "type": "read"}).text)
    for k in config.keys():
        k = config[k]
        do = True
        try:
            base = k["base"]
        except:
            do = False
            for kx in k:
                kx = k[kx]
                base = kx["base"]
                del kx["base"]
                for i in kx:
                    globals()[f"{base}{i}"](kx[i])

        if do:
            del k["base"]
            for i in k:
                globals()[f"{base}{i}"](k[i])
        
@eel.expose
def upload_config(user):
    import requests
    config = createconfig.create("./web/css/style.css")
    requests.post("https://configfetch--rhinocodes.repl.co/config", data={"user": user, "config": config, "type": "new"})

@eel.expose
def change_line_width(width):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('hr') for i in lines]
    to_replace = color_line.index(True)+2
    border_color = re.compile("border-top: ([^ ]+)").search(lines[to_replace]).groups()[0]
    border_type = re.compile("dotted|dashed|solid|double|groove|ridge|inset|outset|none|hidden").search(lines[to_replace]).group()
    lines[to_replace] = f"    border-top: {border_color} {width} {border_type};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_line_type(itype):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('hr') for i in lines]
    to_replace = color_line.index(True)+2
    border_color = re.compile("border-top: ([^ ]+)").search(lines[to_replace]).groups()[0]
    border_width = re.compile(r"\d+px").search(lines[to_replace]).group()
    lines[to_replace] = f"    border-top: {border_color} {border_width} {itype};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_check_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('#done') for i in lines]
    to_replace = color_line.index(True)+1
    lines[to_replace] = f"    color: {color};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_check_hover_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('#done:hover') for i in lines]
    to_replace = color_line.index(True)+1
    lines[to_replace] = f"    color: {color};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_item_background_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('#block') for i in lines]
    to_replace = color_line.index(True)+1
    lines[to_replace] = f"    background: {color};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_item_background(img_path):
    try:
        copyfile(img_path, "./web/item-background.jpg")
    except:
        rm("./web/item-background.jpg")

@eel.expose
def change_item_border_color(color):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('#block') for i in lines]
    to_replace = color_line.index(True)+2
    border_width = re.compile(r"\d+px").search(lines[to_replace]).group()
    border_type = re.compile("dotted|dashed|solid|double|groove|ridge|inset|outset|none|hidden").search(lines[to_replace]).group()
    lines[to_replace] = f"    border: {color} {border_width} {border_type};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_item_border_width(width):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('#block') for i in lines]
    to_replace = color_line.index(True)+2
    border_color = re.compile("border: ([^ ]+)").search(lines[to_replace]).groups()[0]
    border_type = re.compile("dotted|dashed|solid|double|groove|ridge|inset|outset|none|hidden").search(lines[to_replace]).group()
    lines[to_replace] = f"    border: {border_color} {width} {border_type};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

@eel.expose
def change_item_border_type(itype):
    lines = open("./web/css/style.css").readlines()
    color_line = [i.startswith('#block') for i in lines]
    to_replace = color_line.index(True)+2
    border_color = re.compile("border: ([^ ]+)").search(lines[to_replace]).groups()[0]
    border_width = re.compile(r"\d+px").search(lines[to_replace]).group()
    lines[to_replace] = f"    border: {border_color} {border_width} {itype};\n"
    to_write = "".join(lines)
    with open("./web/css/style.css", "w+") as f:
        f.write(to_write)

eel.init("web")
eel.start('index.html', port=8080,  size=(500,650))