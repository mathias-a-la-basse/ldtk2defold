import sys
import os 
from pathlib import Path

if __name__ == "__main__":

  dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
  project_file='multiworld_platformer.ldtk'
  
  project_path=dir_path / project_file
  
  
  defold_root = (dir_path / '../..').resolve().absolute()
  program_path = defold_root / 'ldtk_py_defold/ldtk_py_defold.py'
  
  sys.exit(os.system('python '+str(program_path) +' '+ str(project_path) +' '+ str(defold_root)))
  