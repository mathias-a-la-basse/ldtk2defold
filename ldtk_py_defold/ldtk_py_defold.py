import logging
from math import floor
from typing import List
import LdtkJson153 as LdtkJson153

from LdtkJson153 import LdtkJSON, World, Level, LayerInstance, LayerDefinition, TileInstance
import json
import deftree
import sys
from pathlib import Path

logger = logging.getLogger('ldtk_py_defold')


def get_defold_rel_path(ldtk_root: Path,  defold_root: Path, ldtk_rel_path: Path):
  """
  Given the root ldtk path, the defold target project and a relative ldtk path
  return the relative path to use in defold
  """
  thepath = (ldtk_root / ldtk_rel_path).resolve().absolute().relative_to(defold_root)
  return '/' / thepath

def str_path(path: Path):
  return str(path).replace('\\','/')

DEFOLD_TILESOURCE_TEMPLATE = """image: ""
tile_width: 32
tile_height: 32
collision: ""
convex_hulls {
  index: 0
  count: 4
  collision_group: ""
}
collision_groups: "default"
"""

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def defold_element(el_name, *args):
  el = deftree.Element(el_name)
  for a_name, a_value in pairwise(args):
    if deftree.is_element(a_value) or deftree.is_attribute(a_value):
      el.append(a_value)
    else:
      el.add_attribute(a_name,a_value)
  return el

def defold_remove_element(doc: deftree.Element,el_name):
  e = doc.get_element(el_name)
  e_idx = doc.index(e)
  doc.remove(e)
  return e_idx

def defold_remove_attribute(doc: deftree.Element,a_name):
  e = doc.get_attribute(a_name)
  e_idx = doc.index(e)
  doc.remove(e)
  return e_idx

def defold_write_tree(tree: deftree.DefTree, filepath: Path):
  filepath.parent.mkdir(exist_ok=True, parents=True)
  tree.write(filepath)

def process_tilesets(ldtk_root: Path, model: LdtkJSON, defold_root: Path):
  tilesources_dir = defold_root/ ldtk_root.relative_to(defold_root)  / 'tilesources' 
  tilesources = {}
  for tileset_idx, tileset in enumerate(model.defs.tilesets):
    tilesource_file = tilesources_dir /  (tileset.identifier +'.tilesource')
    logger.info('create tilesource :' + str(tilesource_file))
    tree = deftree.from_string(DEFOLD_TILESOURCE_TEMPLATE)
    tilesource = tree.get_root()
    if tileset.rel_path is None:
      # TODO: HANDLE EMBEDED TILESET --> NO IMAGE!
      continue
    defold_image = str_path(get_defold_rel_path(ldtk_root, defold_root, Path(tileset.rel_path) ))
    tilesource.set_attribute("image", defold_image)
    tilesource.set_attribute("tile_width", tileset.tile_grid_size)
    tilesource.set_attribute("tile_height", tileset.tile_grid_size)
    tilesource.set_attribute("collision",defold_image)
    ## first create convex hulls - add collision groups if it is utilized:
    collision_groups_list = []
    total_tiles = tileset.c_hei * tileset.c_wid
    convex_hulls = [ {"index": i*4, "count":4,  "collision_group":""} for i in range(total_tiles)]
    if len(tileset.enum_tags)>0:
      for enum_tag in tileset.enum_tags:
        collision_groups_list.append(enum_tag.enum_value_id)
        for tile_id in  enum_tag.tile_ids:
          convex_hulls[tile_id]["collision_group"] = enum_tag.enum_value_id      
    ## output convex_hulls
    e_idx = defold_remove_element(tilesource, "convex_hulls")
    for hull_idx, hull in enumerate(convex_hulls):
      e_hull = ( defold_element("convex_hulls",
        "index",hull["index"],
        "count",hull["count"],
        "collision_group",hull["collision_group"]
          )
      )
      tilesource.insert(e_idx + hull_idx, e_hull)
    # handle collision_groups list
    if len(collision_groups_list)>0:
      #remove default:
      a_idx = defold_remove_attribute(tilesource, "collision_groups")
      for group_idx, group in enumerate(collision_groups_list):
        tilesource.add_attribute("collision_groups",str(group))
    # TODO: HANDLE animations from config or custom data?
    # TODO: HANDLE inner padding from config
    # TODO: HANDLE Sprite trim mode from config    
    # TODO: HANDLE extrude_borders from config
    tilesource.add_attribute("extrude_borders",2)
    
    # write to disk
    defold_write_tree(tree, tilesource_file)
    defold_tilesource = '/' + str_path(tilesource_file.relative_to(defold_root))
    tilesources[tileset.uid]={ "uid": tileset.uid, "identifier": tileset.identifier, "defold_image": defold_image, "tilesource_file": tilesource_file, "defold_tilesource": defold_tilesource}
    logger.info('tilesource created')
  return tilesources  

def process_enums(ldtk_root, model, defold_root, tilesources):
  return []

def process_entities_def(ldtk_root, model, defold_root, tilesources):
  return []

def convert_to_multiworlds(model: LdtkJSON):
  """ convert one world model to multi-world model
     create 1 World with levels array into it

  Args:
      model (LdtkJSON): The ldtk source model

  Returns:
      LdtkJSON: the modified model in multiworld
  """
  logger.info('Convert one-world model to multi-world model')
  world = World( model.default_level_height  , model.default_level_width ,'World',model.iid,model.levels,model.world_grid_height,model.world_grid_width,model.world_layout)
  model.worlds.append(world)
  logger.info('multi-world model ok')
  return model

def load_external_level(ldtk_root: Path, level: Level):
  """ load external .ldtkl file if level is stored in another file
  Args:
      level (_type_): _description_

  Returns:
      _type_: _description_
  """
  level_file = ldtk_root / level.external_rel_path
  level_external = None
  logger.info('load external level file: '+ str(level_file))
  with open(level_file) as f:
    level_external = Level.from_dict(json.load(f))
  logger.info('external level file loaded')
  return level_external

def process_worlds(ldtk_root: Path, model: LdtkJSON,  defold_root: Path, tilesources, enums, entities_def):
  # first convert one-world project to multi-world project
  if model.levels and len(model.levels)>0:
    model = convert_to_multiworlds(model)
  
  for world_idx, world in enumerate(model.worlds):
    logger.info('Start of world processing for world '+ world.identifier)
    for level_idx, level in enumerate(world.levels):
      logger.info('Start of level  processing for level '+ level.identifier)
      if model.external_levels:
        level = load_external_level(ldtk_root, level)
        model.worlds[world_idx].levels[level_idx] = level
      # process level data to create tilemaps, collections and data files
      process_level(ldtk_root, world, level, defold_root, tilesources, enums, entities_def)
      logger.info('Level processing ok for level '+ level.identifier)
    logger.info('world processing ok for world '+ world.identifier)
  return model

def process_level(ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  for layer_idx, layer in enumerate(level.layer_instances):
    tiles = []
    if len(layer.auto_layer_tiles)>0:
      tiles = layer.auto_layer_tiles # Pure AutoLayer or IntGrid with AutoLayer
    elif len(layer.grid_tiles)>0:
      tiles = layer.grid_tiles # TilesLayer
    if len(tiles)>0:
      process_layer_tiles(tiles, layer, ldtk_root, world,level, defold_root, tilesources, enums, entities_def)


def process_layer_intGrid(layer: LayerInstance, ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
   return 
   
def process_layer_tiles(tiles: List[TileInstance], layer: LayerInstance, ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  tilemaps_dir = defold_root/ ldtk_root.relative_to(defold_root) / 'tilemaps'
  tilesource = tilesources[layer.tileset_def_uid]
  tilemap_file = tilemaps_dir / world.identifier / level.identifier / (level.identifier+'_'+layer.identifier +'.tilemap')
  # create Defold tilemap
  logger.info('Start of tilemap creation in: '+str(tilemap_file))
  tree = deftree.DefTree()
  tilemap = tree.get_root()
  tilemap.add_attribute("tile_set", tilesource['defold_tilesource'] )
  
  def _build_layers(tilemap: deftree.Element, layer_name: str,tiles: List[TileInstance], layer: LayerInstance,z_initial=0, z_delta_tilestack=0.001,iteration=1):
    # build layers, recursivly
    # we add a tilemap layer if there is tile stacking in the LDTK Layer instance.
    # the z property used to handle stacking with a small z_delta_tilestack. z_initial
    deflayer = tilemap.add_element("layers")
    deflayer.add_attribute("id", layer_name)
    deflayer.add_attribute("z", z_initial+(iteration-1)*z_delta_tilestack)
    # build cells:
    total_height = layer.c_hei * layer.grid_size
    # we use a set to check if the tile px has already been used in the current layer, if so, the tile
    # will go to the next_tiles and added to the next layer.
    tiles_set = set()
     # will store the tiles for next iteration
    next_tiles = []
    for tile in tiles:
      # first check if celle is already added -> if so continue and keep tile for next layer
      tile_px = tuple(tile.px)
      if tile_px in tiles_set:
        next_tiles.append(tile)
        continue
      else:
        tiles_set.add(tile_px)
      cell = deflayer.add_element('cell')
      cell.add_attribute('x', floor(tile.px[0] / layer.grid_size))
      cell.add_attribute('y', floor( (total_height - tile.px[1]) / layer.grid_size ) )
      cell.add_attribute('tile', tile.t)
      if tile.f == 1 or tile.f == 3:
        cell.add_attribute('h_flip', 1)
      if tile.f == 2 or tile.f == 3:
        cell.add_attribute('v_flip', 1)
    # now handle next layer if stacked tiles
    if len(next_tiles)>0:
      iteration += 1
      _build_layers(tilemap, layer.identifier + str(iteration),next_tiles,layer,z_initial, z_delta_tilestack,iteration)
        
  ## build all layers, handling stacked tiles
  _build_layers(tilemap, layer.identifier + "1", tiles, layer)
  # add material.
  # TODO: HANDLE material from configuration
  tilemap.add_attribute('material','/builtins/materials/tile_map.material')
    # Write tilemap file
  defold_write_tree(tree, tilemap_file)
  logger.info('tilemap written in '+str(tilemap_file))
  return

def process_layer_entitiesLayer(layer: LayerInstance, ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  return

def ldtk_to_defold(source_file,defold_root,config_file=None):
  model: LdtkJSON | None = None
  ldtk_path = Path(source_file).resolve().absolute()
  ldtk_root = ldtk_path.parent
  ldtk_stem = ldtk_path.stem
  
  logging.basicConfig(filename= str(ldtk_root / 'ldtk_py_defold.log'), level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                      filemode='w')
  logger.info('** START LDTK 2 DEFOLD CONVERTER')
  logger.info('ldtk file is: ' + str(source_file))
  logger.info('defold root is: ' + str(defold_root))
  
  logger.info('load ldtk file:' + str(ldtk_path))
  try:
    with open(ldtk_path) as f:
      model = LdtkJson153.ldtk_json_from_dict(json.load(f)) 
  except Exception as e:
    logger.error("I/O error: {0}".format(e))
    sys.exit(1)
  logger.info('ldtk file loaded')
  defold_root = Path(defold_root).resolve().absolute()
  tilesources = process_tilesets(ldtk_root, model, defold_root)
  enums = process_enums(ldtk_root, model, defold_root, tilesources)
  entities_def = process_entities_def(ldtk_root, model, defold_root, tilesources)
  process_worlds(ldtk_root, model, defold_root, tilesources, enums, entities_def)
      
  logger.info('** FINISHED LDTK 2 DEFOLD CONVERTER')

def main():
    args = sys.argv[1:]
    ldtk_to_defold(args[0], args[1])
    

if __name__ == "__main__":
    main()

    
    
  