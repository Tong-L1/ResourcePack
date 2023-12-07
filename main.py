import json
import os


# minecraft/models/item/xxx.json
def isEmpty(file_path):
    if not os.path.exists(file_path):
        return True


def minecraft(pack_name, minecraft_item, custom_item_name, custom_model_data):
    file_path = 'minecraft/models/item/' + minecraft_item + '.json'
    if isEmpty(file_path):
        with open(file_path, 'w+') as f:
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
    # write model
    pack(pack_name, custom_item_name)


# xxx/models/item/xxx.json
def pack(pack_name, custom_item_name):
    file_path = pack_name + '/models/item/' + custom_item_name + '.json'
    with open(file_path, 'w') as f:
        textures = {"layer0": pack_name + ":item/" + custom_item_name}
        json_j = {"parent": "minecraft:item/handheld", "textures": textures}
        f.write(json.dumps(json_j, indent=4))


if __name__ == '__main__':
    minecraft('myserver', 'paper', 'flag', 122002)
