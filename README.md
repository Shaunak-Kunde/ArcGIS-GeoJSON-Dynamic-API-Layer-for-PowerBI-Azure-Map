# ArcGIS-GeoJSON-Dynamic-API-Layer-for-PowerBI-Azure-Map
This is a repo created to store a combined.geojson file. First, in ArcGIS Online, I created a web map with multiple layers. Then in metadata, I got the resource URL. Then I used REST Query for Each URL to load and save a Json file for each map layer. Then I used a Python Script to merge all the json files into a single GeoJSON file, saved here. 


# Step-by-Step Implementation of ArcGIS Layers into PowerBI Azure Map
I implemented an automated pipeline that merges ArcGIS layers externally and provides a single GeoJSON URL for Az-ure Maps.
1.	Opened ArcGIS Online and explored public Web Maps containing geographic layers.
2.	Identified useful layers such as Palestine border and Agricultural parcels. 
3.	Opened the Layer Metadata page in ArcGIS Online. 
4.	Located the ArcGIS REST FeatureServer endpoint for each layer. 
5.	Used the REST query parameter ?where=1=1&outFields=*&f=geojson to export the layer as GeoJSON. 
________________________________________
# 🟢 Milestone 1 — Extract ArcGIS GeoJSON Layers
6.	Verified the GeoJSON response in the browser. 
7.	Saved each ArcGIS layer locally as .json GeoJSON files. 
________________________________________
8.	Used Python to write a script that reads multiple GeoJSON files. 
9.	Extracted the features from each file. 
10.	Combined them into a single GeoJSON FeatureCollection. 
________________________________________
# 🟢 Milestone 2 — Merge Multiple ArcGIS Layers
11.	Generated a merged file called combined_layers_3.geojson. 
________________________________________
12.	Tested the merged GeoJSON inside Microsoft Power BI. 
13.	Loaded it in the Azure Maps Power BI visual using a Reference Layer. 
14.	Successfully visualized multiple ArcGIS layers in one map. 
________________________________________
# 🟢 Milestone 3 — ArcGIS → Azure Maps Integration Verified
________________________________________
15.	Created a repository on GitHub. 
16.	Uploaded combined_layers_3.geojson to the repository. 
17.	Used the GitHub raw file URL as the data source for Azure Maps. 
________________________________________
# 🟢 Milestone 4 — Public GeoJSON Endpoint Created
________________________________________
18.	Implemented automation using GitHub Actions. 
19.	Created a workflow (update_geojson.yml) that fetches ArcGIS layers, merges them using Python, and updates the GeoJSON file. 
20.	Scheduled the workflow to run automatically every hour. 
________________________________________
# 🟢 Milestone 5 — Automated Dynamic GeoJSON Pipeline
ArcGIS FeatureServer
        ↓
GitHub Actions (fetch + merge)
        ↓
combined_layers_3.geojson (auto-updated)
        ↓
Azure Maps Reference Layer in Power BI
Result: Azure Maps always loads the latest merged ArcGIS layer data from a single GeoJSON URL.
