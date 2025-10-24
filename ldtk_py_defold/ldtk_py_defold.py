import ldtk_py_defold.LdtkJson153 as LdtkJson153

from ldtk_py_defold.LdtkJson153 import LdtkJSON, World, Level
import json
import deftree 
import sys
from pathlib import Path

def convert_to_multiworlds(model: LdtkJSON):
  """ convert one world model to multi-world model
     create 1 World with levels array into it

  Args:
      source (LdtkJSON): The ldtk source model

  Returns:
      LdtkJSON: the modified model in multiworld
  """
  
  world = World( model.default_level_height  , model.default_level_width ,'World',model.iid,model.levels,model.world_grid_height,model.world_grid_width,model.world_layout)
  model.worlds.append(world)
  return model

def load_external_level(project_root: Path, level: Level):
  """ load external .ldtkl file if level is stored in another file
  Args:
      level (_type_): _description_

  Returns:
      _type_: _description_
  """
  level_file = project_root / level.external_rel_path
  level_external = None
  with open(level_file) as f:
    level_external = Level.from_dict(json.load(f))
  return level_external

def process_worlds(project_root: Path, model: LdtkJSON):
  for world_idx, world in enumerate(model.worlds):
    for level_idx, level in enumerate(world.levels):
      if model.external_levels:
        level = load_external_level(project_root, level)
        model.worlds[world_idx].levels[level_idx] = level
      process_level(world, level)
  return model

def process_level(world: World,level: Level):
  return

def ldtk_to_defold(source_file,output_root):
  model = None
  source_path = Path(source_file)
  project_root = source_path.parent
  source_stem = source_path.stem
  
  with open(source_file) as f:
    model = LdtkJson153.ldtk_json_from_dict(json.load(f))
  # convert one-world project to multi-world project
  if model.levels:
    model = convert_to_multiworlds(model)
  
  process_worlds(project_root, model)
  
  

  return model
    
  

def main():
    args = sys.argv[1:]
    print(args[0])
    print(args[1])
    model = ldtk_to_defold(args[0], args[1])
    

if __name__ == "__main__":
    main()

    
    
  