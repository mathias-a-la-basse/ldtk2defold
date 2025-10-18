local enums = {
    ["Items"] = {
        ["Items1"] = 2,
        ["Items2"] = 3,
        ["Items3"] = 4,
        ["Items0"] = 1,
    },
}

local entity_fields = {
    [hash("d6e7c9b0-c210-11ef-bc88-2393468a5fab")] = {
        [hash("a168e070-c210-11ef-bc88-bfb526423006")] = {
        },
        [hash("9fd7a730-c210-11ef-bc88-63ab02b0ff5e")] = {
            ["target"] = {
                ["levelIid"] = "d6e7c9b0-c210-11ef-bc88-2393468a5fab",
                ["entityIid"] = "79197c40-c210-11ef-bc88-4d3d1fbaa0ad",
            },
        },
        [hash("79197c40-c210-11ef-bc88-4d3d1fbaa0ad")] = {
        },
        [hash("1407ddb0-c210-11ef-b069-f56b07cb3c0d")] = {
            ["speed"] = 100,
            ["path"] = {
                [1] = vmath.vector3(14.0, 22.0, 0),
                [2] = vmath.vector3(14.0, 10.0, 0),
            },
            ["wait_time"] = 2,
        },
        [hash("c94cfd80-c210-11ef-bc88-5b457e99bdcc")] = {
        },
    },
}

local level_fields = {
    [hash("d6e7c9b0-c210-11ef-bc88-2393468a5fab")] = {
    },
}

return {
    enums = enums,
    entity_fields = entity_fields,
    level_fields = level_fields,
}
