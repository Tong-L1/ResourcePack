import json
import os


def isEmpty(file_path):
    if not os.path.exists(file_path):
        return True


def minecraft(pack_name, minecraft_item, custom_item_name, custom_model_data):
    file_dir = 'minecraft/models/item/'
    file_name = minecraft_item + '.json'
    file_path = file_dir + file_name
    if isEmpty(file_dir):
        os.makedirs(file_dir)
    if isEmpty(file_path):
        with open(file_path, 'w') as f:
            layer0 = {"layer0": "minecraft:item/" + minecraft_item}
            json_j = {"overrides": [], "parent": "minecraft:item/handheld", "textures": layer0}
            f.write(json.dumps(json_j, indent=4))
    with open(file_path, 'r+') as f:
        json_load = json.load(f)
        predicate = {"custom_model_data": custom_model_data}
        overrides = {"model": pack_name + ":item/" + custom_item_name, "predicate": predicate}
        if overrides not in json_load["overrides"]:
            json_load["overrides"].append(overrides)
        with open(file_path, 'r+') as fw:
            fw.write(json.dumps(json_load, indent=4))
    pack(pack_name, custom_item_name)


def pack(pack_name, custom_item_name):
    file_dir = pack_name + '/models/item/'
    file_name = custom_item_name + '.json'
    file_path = file_dir + file_name
    if isEmpty(file_dir):
        os.makedirs(file_dir)
    with open(file_path, 'w') as f:
        textures = {"layer0": pack_name + ":item/" + custom_item_name}
        json_j = {"parent": "minecraft:item/handheld", "textures": textures}
        f.write(json.dumps(json_j, indent=4))


if __name__ == '__main__':
    minecraft('examplename', 'paper', 'flag0', 122001)
