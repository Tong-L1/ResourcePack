import json
import os
import uuid


def is_empty(file_path):
    if not os.path.exists(file_path):
        return True


def get_rp_name():
    with open('java/pack.mcmeta', 'r') as f:
        description = json.load(f)["pack"]["description"]
    return description


def manifest():
    description = get_rp_name()
    with open('./manifest.json', 'r') as f:
        json_load = json.load(f)
    file_dir = 'bedrock/'
    file_name = 'manifest.json'
    file_path = file_dir + file_name
    if is_empty(file_dir):
        os.makedirs(file_dir)
    json_load["header"]["name"] = description
    json_load["header"]["description"] = description
    json_load["header"]["uuid"] = str(uuid.uuid4())
    json_load["modules"][0]["description"] = description
    json_load["modules"][0]["uuid"] = str(uuid.uuid4())
    with open(file_path, 'w') as f:
        f.write(json.dumps(json_load, indent=4))


def mapping():
    file_dir = 'bedrock/'
    if is_empty(file_dir):
        os.makedirs(file_dir)

    file_dir2 = 'java/assets/minecraft/models/item/'
    files = os.listdir(file_dir2)
    json_j = {"format_version": "1", "items": {}}
    for file in files:
        file_path2 = file_dir2 + file
        jsonl = json.load(open(file_path2, 'r'))
        minecraft_item = file.split('.')[0]
        arrays = []
        for item in jsonl["overrides"]:
            name = item["model"].split('item/')[1]
            custom_model_data = item["predicate"]["custom_model_data"]
            minecraft_json = {
                "name": name,
                "allow_offhand": True,
                "icon": name,
                "custom_model_data": custom_model_data
            }
            arrays.append(minecraft_json)
        json_j["items"]["minecraft:" + minecraft_item] = arrays

    file_name = 'mapping.json'
    file_path = file_dir + file_name
    with open(file_path, 'w') as f:
        f.write(json.dumps(json_j, indent=4))


def texture():
    file_dir = 'bedrock/textures/'
    file_name = 'item_texture.json'
    file_path = file_dir + file_name
    if is_empty(file_dir):
        os.makedirs(file_dir)
    if is_empty('bedrock/textures/items/'):
        os.makedirs('bedrock/textures/items/')
    json_item_texture = {
        "resource_pack_name": get_rp_name(),
        "texture_name": "atlas.items",
        "texture_data": {}
    }

    file_dir2 = 'java/assets/minecraft/models/item/'
    files = os.listdir(file_dir2)
    for file in files:
        file_path2 = file_dir2 + file
        jsonl = json.load(open(file_path2, 'r'))
        for item in jsonl["overrides"]:
            name = item["model"].split('item/')[1]
            json_item_texture["texture_data"][name] = {"textures": "textures/items/" + name}
    with open(file_path,'w') as f:
        f.write(json.dumps(json_item_texture, indent=4))


if __name__ == '__main__':
    manifest()
    mapping()
    texture()
