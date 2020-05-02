function uploadfile(){
    eel.new_background(document.getElementsByName('filepath')[0].value)
}

function change_title_color(){
    eel.change_title_color(document.getElementsByName('color')[1].value)
}

function change_subtitle_color(){
    eel.change_subtitle_color(document.getElementsByName('color')[2].value)
}

function change_background_color(){
    eel.change_background_color(document.getElementsByName('color')[0].value)
}

function change_line_color(){
    eel.change_line_color(document.getElementsByName('color')[3].value)
}

function change_line_width(){
    eel.change_line_width(document.getElementsByName('width')[0].value+"px")
}

function change_line_type(){
    eel.change_line_type(document.getElementsByName('type')[0].value)
}

function load_config_file(){
    eel.load_config(document.getElementsByName('user')[0].value)
}

function change_check_color(){
    eel.change_check_color(document.getElementsByName('check_color')[0].value)
}

function change_check_hover_color(){
    eel.change_check_hover_color(document.getElementsByName('check_hover_color')[0].value)
}

function change_item_background_color(){
    eel.change_item_background_color(document.getElementsByName('item_background_color')[0].value)
}

function change_item_background(){
    eel.change_item_background(document.getElementsByName('item_background_path')[0].value)
}

function change_item_border_color(){
    eel.change_item_border_color(document.getElementsByName('item_border_color')[0].value)
}

function change_item_border_width(){
    eel.change_item_border_width(document.getElementsByName('item_border_width')[0].value+"px")
}

function change_item_border_type(){
    eel.change_item_border_type(document.getElementsByName('item_border_type')[0].value)
}

function upload_config(){
    eel.upload_config(document.getElementsByName("your_username")[0].value)
}