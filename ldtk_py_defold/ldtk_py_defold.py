from LdtkJson import ldtk_json_from_dict, World, LdtkJSON
import json

# converte one world model to multiworld model
# create 1 World with levels array into it
def convert_to_multiworlds(source: LdtkJSON):
  source.worlds.append(World(0,0,'world','1',source.levels,source.world_grid_height,source.world_grid_width,source.world_layout))
  return source

def process_worlds(source,external_levels):
  return source

def process_levels(world,levels,external_levels):
  return

def process_level(world,level):
  

def ldtk_to_defold(source_file,output_root):
  source = None 
  with open(source_file) as f:
    source = ldtk_json_from_dict(json.load(f))
  
  if source.levels:
    source = convert_to_multiworlds(source)
  
  
    
    
  