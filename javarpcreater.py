import json
import os


def is_empty(file_path):
    if not os.path.exists(file_path):
        return True


def pack(pack_name, custom_item_name):
    file_dir = 'java/assets/' + pack_name + '/models/item/'
    file_name = custom_item_name + '.json'
    file_path = file_dir + file_name
    if is_empty(file_dir):
        os.makedirs(file_dir)
    with open(file_path, 'w') as f:
        textures = {"layer0": pack_name + ":item/" + custom_item_name}
        json_j = {"parent": "minecraft:item/handheld", "textures": textures}
        f.write(json.dumps(json_j, indent=4))


def mcmeta(description):
    file_dir = 'java/'
    file_name = 'pack.mcmeta'
    file_path = file_dir + file_name
    if is_empty(file_dir):
        os.makedirs(file_dir)
    with open(file_path, 'w') as f:
        pack_var = {"description": description, "pack_format": 18}
        json_w = {"pack": pack_var}
        f.write(json.dumps(json_w, indent=4))


def java_rp(pack_name, minecraft_item, custom_item_name, custom_model_data):
    file_dir = 'java/assets/minecraft/models/item/'
    file_name = minecraft_item + '.json'
    file_path = file_dir + file_name
    if is_empty(file_dir):
        os.makedirs(file_dir)
    if is_empty(file_path):
        with open(file_path, 'w') as f:
            layer0 = {"layer0": "minecraft:item/" + minecraft_item}
            json_j = {"overrides": [], "parent": "minecraft:item/handheld", "textures": layer0}
            f.write(json.dumps(json_j, indent=4))
    with open(file_path, 'r') as f:
        json_load = json.load(f)
        predicate = {"custom_model_data": custom_model_data}
        overrides = {"model": pack_name + ":item/" + custom_item_name, "predicate": predicate}
        if overrides not in json_load["overrides"]:
            json_load["overrides"].append(overrides)
    with open(file_path, 'w') as f:
        f.write(json.dumps(json_load, indent=4))
    pack(pack_name, custom_item_name)


if __name__ == '__main__':
    mcmeta('description')
    java_rp('test', 'cookie', 'ginger_bread_man', 111002)
