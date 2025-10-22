import ldtk_py_defold.LdtkJson153 as LdtkJson153

from ldtk_py_defold.LdtkJson153 import LdtkJSON, World, Level
import json
import deftree 
import sys

def convert_to_multiworlds(model: LdtkJSON):
  """ convert one world model to multi-world model
     create 1 World with levels array into it

  Args:
      source (LdtkJSON): The ldtk source model

  Returns:
      LdtkJSON: the modified model in multiworld
  """
  
  world = World( model.default_level_height  , model.default_level_width ,'world1',model.iid,model.levels,model.world_grid_height,model.world_grid_width,model.world_layout)
  model.worlds.append(world)
  return model

def load_external_level(project_path, level: Level):
  """ load external .ldtkl file if level is stored in another file

  Args:
      level (_type_): _description_

  Returns:
      _type_: _description_
  """
  return level

def process_worlds(model: LdtkJSON,external_levels: bool):
  for world in model.worlds:
    for level in world.levels:
      process_level(world, level)
  return model

def process_level(world: World,level: Level):
  return

def ldtk_to_defold(source_file,output_root):
  model = None
  with open(source_file) as f:
    model = LdtkJson153.ldtk_json_from_dict(json.load(f))
  # convert one-world project to multi-world project
  if model.levels:
    model = convert_to_multiworlds(model)

  return model
    
  

def main():
    args = sys.argv[1:]
    print(args[0])
    print(args[1])
    model = ldtk_to_defold(args[0], args[1])
    

if __name__ == "__main__":
    main()

    
    
  