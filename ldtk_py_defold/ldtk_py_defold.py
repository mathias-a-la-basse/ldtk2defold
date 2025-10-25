import LdtkJson153 as LdtkJson153

from LdtkJson153 import LdtkJSON, World, Level, LayerInstance, LayerDefinition
import json
import deftree 
import sys
from pathlib import Path

def convert_to_multiworlds(model: LdtkJSON):
  """ convert one world model to multi-world model
     create 1 World with levels array into it

  Args:
      model (LdtkJSON): The ldtk source model

  Returns:
      LdtkJSON: the modified model in multiworld
  """
  
  world = World( model.default_level_height  , model.default_level_width ,'World',model.iid,model.levels,model.world_grid_height,model.world_grid_width,model.world_layout)
  model.worlds.append(world)
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
  with open(level_file) as f:
    level_external = Level.from_dict(json.load(f))
  return level_external

def process_worlds(ldtk_root: Path, model: LdtkJSON,  defold_root: Path, tilesources, enums, entities_def):
  # first convert one-world project to multi-world project
  if model.levels and len(model.levels)>0:
    model = convert_to_multiworlds(model)
  
  for world_idx, world in enumerate(model.worlds):
    for level_idx, level in enumerate(world.levels):
      if model.external_levels:
        level = load_external_level(ldtk_root, level)
        model.worlds[world_idx].levels[level_idx] = level
      process_level(world, level)
  return model

def process_level(ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  return

def process_layer_intGrid(layer: LayerInstance, ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  return

def process_layer_autoLayer(layer: LayerInstance, ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  return

def process_layer_tileLayer(layer: LayerInstance, ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  return

def process_layer_entitiesLayer(layer: LayerInstance, ldtk_root: Path, world: World,level: Level, defold_root: Path, tilesources, enums, entities_def):
  return

def get_defold_rel_path(ldtk_root: Path,  defold_root: Path, ldtk_rel_path: Path):
  """
  Given the root ldtk path, the defold target project and a relative ldtk path
  return the relative path to use in defold
  """
  thepath = ldtk_root / ldtk_rel_path
  return '/' / thepath.relative_to(defold_root)

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
  tilesources_dir = defold_root/ ldtk_root.relative_to(defold_root)
  tilesources = []
  for tileset_idx, tileset in enumerate(model.defs.tilesets):
    tilesource_file = tilesources_dir / 'tilesources' / (tileset.identifier +'.tilesource')
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
    tilesources.append({"identifier": tileset.identifier, "defold_image": defold_image, "tilesource_file": tilesource_file})
    
  return tilesources  

def process_enums(ldtk_root, model, defold_root, tilesources):
  return []

def process_entities_def(ldtk_root, model, defold_root, tilesources):
  return []



def ldtk_to_defold(source_file,defold_root,config_file=None):
  model: LdtkJSON | None = None
  ldtk_path = Path(source_file).resolve().absolute()
  ldtk_root = ldtk_path.parent
  ldtk_stem = ldtk_path.stem
  
  with open(ldtk_path) as f:
    model = LdtkJson153.ldtk_json_from_dict(json.load(f))  
  
  defold_root = Path(defold_root).resolve().absolute()
  tilesources = process_tilesets(ldtk_root, model, defold_root)
  enums = process_enums(ldtk_root, model, defold_root, tilesources)
  entities_def = process_entities_def(ldtk_root, model, defold_root, tilesources)
  process_worlds(ldtk_root, model, defold_root, tilesources, enums, entities_def)
      
  

def main():
    args = sys.argv[1:]
    print(args[0])
    print(args[1])
    ldtk_to_defold(args[0], args[1])
    

if __name__ == "__main__":
    main()

    
    
  