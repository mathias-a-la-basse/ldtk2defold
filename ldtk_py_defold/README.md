# LDTK-PY-DEFOLD

A python tool to convert LDTK files into Defold ressources.

### LDTK Tilesets

* each ldtk tileset {model.tilesets} become
  * 1 defold tilesources:
    * file:   `{config.fn_tileset_path(identifier, tags)}/{model.tilesets.identifier}.tilesource`
    * image={model.tilesets.relPath} -> relative to defold project
    * size W = {model.tilesets.pxWid}, H = {model.tilesets.pxHei}
    * tile width = {model.tilesets.tile_grid_size}
    * tile height = {model.tilesets.tile_grid_size}
    * tile margin = {model.tilesets.padding}
    * tile spacing = {model.tilesets.spacing}
    * !! extrude borders = {config.tilesets[identifier].extrude_borders} !!
    * !! inner padding = {config.tilesets[identifier].inner_padding} !!
    * Collision (image) =
      * {config.tilesets[identifier].collision}
      * or nil if {config.tilesets[identifier].no_collision}
      * default idem defold.image
    * !! Sprite trim mode {config.tilesets[identifier].inner_padding} !!
    * For each enumTags value (not custom data) add a collision group and mark tiles
      * for each tile, create a convex hull data. If in {model.tilesets.enumTags.tileIds} -> set collision_group = {model.tilesets.enumTags.enumValueId}, else "" (no group)
      * how to calculate "index" and "count":
        * index start at 0, then it is index += count over each tile.
        * count is the number of edges of convex hull -> set 4 everywhere.
    
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

## Enums definitions

* For each enums
TODO

## Entities definitions

* 1 lua file with entities definitions

## World

* 1 collection per world containing
  * 1 collection proxy --> dynamic loading of levels
* Full World
  * 1 full world collection per world containing
    * 1 collection per level -> position??

## World - Level

* 1 collection per level containing
  * 1 eGO "world" with iid and world infos?
  * 1 eGO "level" with iid and level clear color
  * 1 eGO per layerInstance
    * Id = layer identifier
    * position = 0
    * 1 eGO per tilemap
      * id = layer identifier
      * use z position for layer ordering
      * component script with iid, opacity
      * component tilemap (position 0) -> to tilemap
      * component collisionobject 
        * -> Collision Shape -> tilemap
        * Type Static
        * !! Mask --> get from config , default "player"!!

### World - Level - Layer - IntGrid / Entities

* 1 lua file per level with intGrid and entities data + entities definitions if used + enums def if used
* generate intGrid tilesources with simple colored tiles -> png+tilesource + tilemap

### World - Level - Layer - TileLayer

* idem basic layer

### World - Level - Layer - AutoLayer

* idem basic layer

### World - Level - Layer - Entities

* idem basic layer

## Defold Tilemap mapping

For each LayerInstance if TileLayer or AutoLayer (pure or via IntGrid layer), create a tilemap:
  * tile_set = find tilesources[model.layer.__tilesetDefUid]
  * 1 defold layers with name "model.layer.__identifier"+ #1
    * id = model.layer.__identifier
    * z: 0.0
    * for each tile in gridTiles (TileLayer) or autoLayerTiles (AutoLayer or IntGrid)
      * 1 cell:
        * x= tile.px[0]
        * y= convertY(tile.px[1], totalHeight ) where totalHeight = __cHei * __gridSize
              * y = totalHeight - tile.px[1]
        * tile: tile.t
        * h_flip: 1 if tile.f=1 or 3
        * v_flip: 1 if tile.f=2 or 3
    * material: "/builtins/materials/tile_map.material"  
      * TODO: HANDLE material via configuration

```protobuf
tile_set: "/samples/typical_platformer/typical_platformer/tilesources/SunnyLand_by_Ansimuz.tilesource"
layers {
  id: "Collisions1"
  z: 0.0
  cell {
    x: 0
    y: -1
    tile: 48
  }
  cell {
    x: 1
    y: -1
    tile: 48
  }
  cell {
    x: 2
    y: -1
    tile: 48
  }
  cell {
    x: 3
    y: -1
    tile: 48
  }
  cell {
    x: 20
    y: -1
    tile: 152
    h_flip: 1
  }
  cell {
    x: 29
    y: 4
    tile: 152
    h_flip: 1
    v_flip: 1
  }
}
layers {
  id: "Collisions2"
  z: 1.0E-4
  cell {
    x: 17
    y: 0
    tile: 211
  }
  cell {
    x: 13
    y: 1
    tile: 211
    h_flip: 1
    v_flip: 1
  }
}
material: "/builtins/materials/tile_map.material"
```

## Configuration

* tilesources:
  * create collision groups?
* tilemaps / layers:
  * material
  * add collision objects? if yes, Mask list?
  * create file GO?
  