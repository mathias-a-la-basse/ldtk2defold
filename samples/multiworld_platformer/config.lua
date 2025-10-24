local config = {}

-- assign collision map for images or not
-- if this option is enabled, the generator first searches for an upvalue in collsions table,
-- otherwise, the same image is assigned as the collision source
config.assign_collision = true
config.map_type = enums.map_type.MAIN_COLLECTION

-- config.data_file = '/example/scripts/data.lua'
config.main_collection_name = 'main'

config.tilesets = {
    ['SunnyLand_by_Ansimuz'] = '/samples/typical_platformer/SunnyLand_by_Ansimuz-extended.png'
}

config.entities = {}

config.save = true

return config
