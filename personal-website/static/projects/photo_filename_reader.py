import os
import json

current_dir_path = os.path.dirname(os.path.realpath(__file__))

all_projects = [name for name in os.listdir(
    current_dir_path) if os.path.isdir(os.path.join(current_dir_path, name))]

folder_dict = dict()
for project_dir in all_projects:
    filelist = [
        "../../../static/projects/" + project_dir + "/" + file for file in os.listdir(os.path.join(current_dir_path, project_dir))]
    folder_dict[project_dir] = filelist

print(json.dumps(folder_dict, indent=1))
