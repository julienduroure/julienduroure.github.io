WWW_root = "/media/julien/Ju3D/3D/Projects/01 - In Progress/Rigs/script/julienduroure.github.io/"
WWW_dir  = "_blerifa/"
WWW_img  = "assets/post/"

BLERIFA_root = "/media/julien/Ju3D/3D/Projects/01 - In Progress/Rigs/script/BleRiFa/"
BLERIFA_dir  = "_posts/"
BLERIFA_img  = "assets/post/"
BLERIFA_URL  = "http://BleRiFa.com"

import os
from shutil import copyfile

def copy_img(yaml):
    if "img" in yaml.keys():
        if not os.path.isfile(WWW_root + WWW_dir + yaml["img"]):
            copyfile(BLERIFA_root + BLERIFA_img + yaml["img"], WWW_root + WWW_img + yaml["img"])

def create_new_file(filename, yaml):
    fil_ = open(WWW_root + WWW_dir + filename, "w")
    fil_.write("---\n")
    fil_.write("title: " + yaml["title"] + "\n")
    fil_.write("lang: " + yaml["lang"] + "\n")
    fil_.write("ref: " + yaml["ref"] + "\n")
    fil_.write("tags: " + "[BleRiFa]" + "\n")
    fil_.write("img: " + yaml["img"] + "\n")
    fil_.write("external: " + BLERIFA_URL + yaml["permalink"] + "\n")
    fil_.write("type: blerifa\n")
    fil_.write("version: " + yaml["version"] + "\n")
    fil_.write("---\n")

def get_yaml(dir_, filename):
    # open file and read YAML
    fil_ = open(dir_ + filename, "r")
    file_data = fil_.read()
    fil_.close()
    file_tab = file_data.split("\n")
    started = False
    yaml = {}
    for line in file_tab:
        if started == False and line == "---":
            started = True
        elif started == True and line == "---":
            break
        elif started == True:
            line_tab = line.split(":", 1)
            try:
            	yaml[line_tab[0]] = line_tab[1].lstrip()
            except: pass #TODO : currently, tabs are not taken into account
        else:
            break

    if "permalink" in yaml.keys():
        yaml["permalink"] = yaml["permalink"].replace(":year", filename[:4])
        yaml["permalink"] = yaml["permalink"].replace(":month", filename[5:7])
        yaml["permalink"] = yaml["permalink"].replace(":day", filename[8:10])

    return yaml

blerifa_list = os.listdir(BLERIFA_root + BLERIFA_dir)

for filename in blerifa_list:
    #check if corresponding file exists in WWW
    if not os.path.isfile(WWW_root + WWW_dir + filename):
        print("New file : " + filename)
        yaml = get_yaml(BLERIFA_root + BLERIFA_dir, filename)
        create_new_file(filename, yaml)
        copy_img(yaml)
    else:
        # already exists, but check if version changed
        yaml_target = get_yaml(WWW_root + WWW_dir, filename)
        yaml = get_yaml(BLERIFA_root + BLERIFA_dir, filename)
        if "version" in yaml_target.keys() and "version" in yaml.keys() and yaml_target["version"] != yaml["version"]:
            # update
            print("Update file : " + filename)
            create_new_file(filename, yaml)
            copy_img(yaml)
