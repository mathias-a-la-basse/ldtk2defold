# LDTK-PY-DEFOLD

A python tool to convert LDTK files into Defold ressources.

### LDTK Tilesets

* each ldtk tileset {model.tilesets} become
  * 1 defold tilesources:
    * file:   `{config.fn_tileset_path(identifier, tags)}/{model.tilesets.identifier}.tilesource`
    * image={model.tilesets.relPath} -> relative to defold project
    * size W = {model.tilesets.pxWid}, H = {model.tilesets.pxHei}
    * tile width = {model.tilesets.tileGridSize}
    * tile height = {model.tilesets.tileGridSize}
    * tile margin = {model.tilesets.padding}
    * tile spacing = {model.tilesets.spacing}
    * !! extrude borders = {config.tilesets[identifier].extrude_borders} !!
    * !! inner padding = {config.tilesets[identifier].inner_padding} !!
    * Collision (image) =
      * {config.tilesets[identifier].collision}
      * or nil if {config.tilesets[identifier].no_collision}
      * default idem defold.image
    * !! Sprite trim mode {config.tilesets[identifier].inner_padding} !!
    * For each enumTags value (not custom) add a collision group and mark tiles
      * collision_group = {model.tilesets.enumTags.enumValueId}
      * create a convex hull data for each cell in {model.tilesets.enumTags.tileIds}
      * how to calculate "index" and "count"
    
  * 1 tileset lua table  with data:
    * identifier
    * uid
    * image = defold path
    * tags = {model.tilesets.tags}
    * grid_width = {model.tilesets.__cWid}
    * grid_height = {model.tilesets.__cHei}
    * custom_data = {model.tilesets.customData} -> convert to lua table 
      * [{model.tilesets.customData.tileId}] => {model.tilesets.customData}
    * enum_tags: convert to lua table
      * [{model.tilesets.enumTags.enumValueId}] => {model.tilesets.enumTags.tileIds}
      * OR  [{model.tilesets.enumTags.enumValueId}] => table [{model.tilesets.enumTags.tileIds}] => true/1 ?
    * enum_tags_tiles: revert tags on tile by tile
      * [{model.tilesets.enumTags.tileIds}] => table [{model.tilesets.enumTags.enumValueId}]=>true/1 ?
    * enum_tags_uid: {model.tilesets.enumTags.tagsSourceEnumUid}

Defold tilesource example:
```protobuf
image: "/example/assets/images/tileset/level_tileset.png"
tile_width: 32
tile_height: 32
collision: "/example/assets/images/tileset/level_tileset.png"
convex_hulls {
  index: 0
  count: 5
  collision_group: "walls"
}
convex_hulls {
  index: 5
  count: 4
  collision_group: "walls"
}
convex_hulls {
  index: 9
  count: 4
  collision_group: "walls"
}
convex_hulls {
  index: 24
  count: 6
  collision_group: ""
}
convex_hulls {
  index: 148
  count: 5
  collision_group: "slope"
}
convex_hulls {
  index: 153
  count: 4
  collision_group: "slope"
}
convex_hulls {
  index: 157
  count: 4
  collision_group: "slope"
}
convex_hulls {
  index: 318
  count: 0
  collision_group: ""
}
convex_hulls {
  index: 318
  count: 9
  collision_group: ""
}
convex_hulls {
  index: 327
  count: 4
  collision_group: ""
}
convex_hulls {
  index: 331
  count: 9
  collision_group: ""
}
convex_hulls {
  index: 340
  count: 6
  collision_group: ""
}
convex_hulls {
  index: 346
  count: 8
  collision_group: ""
}
convex_hulls {
  index: 354
  count: 4
  collision_group: ""
}
convex_hulls {
  index: 358
  count: 4
  collision_group: ""
}
collision_groups: "slope"
collision_groups: "walls"
extrude_borders: 2
```