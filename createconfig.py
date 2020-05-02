import re, json

def get_item_config(filename: str) -> dict:
    file_contents = open(filename).read()
    x = re.compile("#block{\n    background: ([^\n;]+);\n    border: ([^\n;]+)", re.MULTILINE)
    config = [i.split() for i in x.search(file_contents).groups()]
    for i in config:
        x = 0
        at = 0
        start = 0
        end = 0
        for y in i:
            if y.__contains__("rgb("):
                start = x
            elif y.__contains__(")"):
                end = x
                rgb = " ".join(config[at][start:end+1])
                del config[at][start:end+1]
                config[at].insert(start, rgb)
                break
            
            x += 1
        
        at +=1

    check = re.compile("#done {\n    color: ([^\n;]+);", re.MULTILINE)
    check_hover = re.compile("#done:hover{\n    color: ([^\n;]+);", re.MULTILINE)
    check_color = check.search(file_contents).groups()[0]
    check_hover_color = check_hover.search(file_contents).groups()[0]
    config = {"border": {"color": config[1][0], "width": config[1][1], "type": config[1][2], "base": "change_item_border_"}, "background": {"color": config[0][0], "base": "change_item_background_"}, "check": {"color": check_color, "hover_color": check_hover_color, "base": "change_check_"}}
    return config

def get_line_config(filename: str) -> dict:
    x = re.compile("hr{\n    border: 0;\n    border-top: ([^\n;]+)", re.MULTILINE)
    config = x.search(open(filename).read()).groups()[0].split()
    config = {"color": config[0], "width": config[1], "type": config[2], "base": "change_line_"}
    return config

def get_title_config(filename: str) -> dict:
    x = re.compile("h1{\n    color: ([^\n;]+);", re.MULTILINE)
    config = x.search(open(filename).read()).groups()[0].split()
    config = {"color": config[0], "base": "change_title_"}
    return config

def get_subtitle_config(filename: str) -> dict:
    x = re.compile("h2{\n    color: ([^\n;]+);", re.MULTILINE)
    config = x.search(open(filename).read()).groups()[0].split()
    config = {"color": config[0], "base": "change_subtitle_"}
    return config

def get_background_config(filename: str) -> dict:
    x = re.compile("body{\n    background: ([^\n;]+);", re.MULTILINE)
    config = x.search(open(filename).read()).groups()[0].split()
    config = {"color": config[0], "base": "change_background_"}
    return config

def create(filename: str) -> str:
    config = {"item": get_item_config(filename), "hr": get_line_config(filename), "heading": {"h1": get_title_config(filename), "h2": get_subtitle_config(filename)}, "background": get_background_config(filename)}
    return json.dumps(config, indent=4)

