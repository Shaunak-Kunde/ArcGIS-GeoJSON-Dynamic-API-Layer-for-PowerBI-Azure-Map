const express = require("express");
const fetch = require("node-fetch");

const app = express();
const port = 3000;

const layers = [
 "https://services8.arcgis.com/x3OYmfTujNHGdoex/arcgis/rest/services/Palestine_border/FeatureServer/4/query?where=1%3D1&outFields=*&returnGeometry=true&outSR=4326&f=geojson",
 "https://services8.arcgis.com/x3OYmfTujNHGdoex/arcgis/rest/services/Palestine_border/FeatureServer/3/query?where=1%3D1&outFields=*&returnGeometry=true&outSR=4326&f=geojson"
];

app.get("/merged.geojson", async (req, res) => {

 let allFeatures = [];

 for (const url of layers) {
  const response = await fetch(url);
  const data = await response.json();

  allFeatures = allFeatures.concat(data.features);
 }

 res.json({
  type: "FeatureCollection",
  features: allFeatures
 });

});

app.listen(port, () => {
 console.log(`API running on port ${port}`);
});
