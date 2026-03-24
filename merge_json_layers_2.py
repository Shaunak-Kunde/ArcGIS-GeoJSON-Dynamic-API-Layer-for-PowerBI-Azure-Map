import json
import os

folder_path = r"C://Users//shaunak.kunde//Downloads//Shaunak FLR Files//Internship Work//PowerBI ArcGIS//ArcGIS Geojson POC//arcgis geojson file//arcgis layers data json file//shaunak_israel_public_data online public json//multiple layers of israel"

all_features = []
unique_id = 1

for file in os.listdir(folder_path):

    if not file.endswith(".json"):
        continue

    if "combined" in file:
        continue

    file_path = os.path.join(folder_path, file)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    except Exception as e:
        print(f"❌ Skipping {file}: {e}")
        continue

    if data.get("type") != "FeatureCollection":
        continue

    layer_name = file.replace(".json", "")

    for feature in data.get("features", []):

        feature["id"] = unique_id
        unique_id += 1

        if "properties" not in feature:
            feature["properties"] = {}

        feature["properties"]["layer"] = layer_name

        all_features.append(feature)

# save output
output = {
    "type": "FeatureCollection",
    "features": all_features
}

with open(os.path.join(folder_path, "combined_layers_3.geojson"), "w", encoding="utf-8") as f:
    json.dump(output, f)

print("✅ Fixed combined file created")