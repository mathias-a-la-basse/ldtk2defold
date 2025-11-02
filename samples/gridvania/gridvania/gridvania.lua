local enums = {
    ["ItemType"] = {
        ["Spell"] = 7,
        ["Green_gem"] = 5,
        ["Ammo"] = 10,
        ["GoldNuggets"] = 3,
        ["Healing_potion"] = 6,
        ["Gem"] = 4,
        ["Gold"] = 2,
        ["Armor"] = 8,
        ["Fire_blade"] = 11,
        ["Meat"] = 1,
        ["Bow"] = 9,
        ["Vorpal_blade"] = 12,
    },
    ["RoomType"] = {
        ["Exit"] = 2,
        ["Boss"] = 4,
        ["Shop"] = 3,
        ["Save"] = 5,
        ["Entrance"] = 1,
    },
}

local entity_fields = {
    [hash("a36811d0-66b0-11ec-9cd7-4367627fb745")] = {
        [hash("60d34a20-66b0-11ec-9ccd-d9d0dea2f003")] = {
        },
    },
    [hash("a367c3b0-66b0-11ec-9cd7-91690c910c97")] = {
        [hash("a367c3b7-66b0-11ec-9cd7-65b15caa5ba5")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Healing_potion"],
            ["count"] = 1,
        },
        [hash("aa59c4d0-66b0-11ec-9ccd-fdfb8075370d")] = {
        },
        [hash("bbe3dcc0-8dc0-11ec-92c1-954a1fe43153")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Ammo"],
            ["count"] = 5,
        },
        [hash("a367c3b6-66b0-11ec-9cd7-61bd30243515")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 100,
        },
        [hash("a367c3b8-66b0-11ec-9cd7-313e15c65fee")] = {
            ["inventory"] = {
                [1] = enums["ItemType"]["Ammo"],
                [2] = enums["ItemType"]["Bow"],
            },
            ["HP"] = 10,
        },
    },
    [hash("a373aa90-66b0-11ec-9cd7-a9310f178834")] = {
        [hash("1b892130-7820-11ed-b4b8-155ce4ee3573")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 50,
        },
        [hash("a373aa99-66b0-11ec-9cd7-d18008148c79")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gem"],
            ["count"] = 1,
        },
        [hash("1c19c870-7820-11ed-b4b8-9dba990f1c87")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 50,
        },
        [hash("a373aa96-66b0-11ec-9cd7-7903b95e3e7d")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 200,
        },
        [hash("a373aa97-66b0-11ec-9cd7-d715c6c71930")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 50,
        },
        [hash("a373aa98-66b0-11ec-9cd7-d5022af1eb97")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Green_gem"],
            ["count"] = 1,
        },
        [hash("a373aa9b-66b0-11ec-9cd7-bd56f31f6283")] = {
            ["playSecretJingle"] = false,
        },
    },
    [hash("a368fc30-66b0-11ec-9cd7-d141af83d44b")] = {
        [hash("b58d0c40-66b0-11ec-9ccd-71b951d72c41")] = {
        },
        [hash("a368fc37-66b0-11ec-9cd7-6da7cb2a925d")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Fire_blade"],
            ["count"] = 1,
        },
        [hash("a368fc36-66b0-11ec-9cd7-d54493e15d01")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Armor"],
            ["count"] = 1,
        },
    },
    [hash("a36c5790-66b0-11ec-9cd7-0d08d7991930")] = {
        [hash("e7eab980-66b0-11ec-9ccd-492e6ed5ee3f")] = {
        },
        [hash("c238e9f0-66b0-11ec-9ccd-019be134d42b")] = {
        },
        [hash("e945dcb0-66b0-11ec-9ccd-0f70f0549c1f")] = {
        },
        [hash("a36c5796-66b0-11ec-9cd7-abe4f8e55b6a")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Fire_blade"],
            ["count"] = 1,
        },
        [hash("c08daaf0-66b0-11ec-9ccd-e19e0bbbe943")] = {
        },
    },
    [hash("a37690c0-66b0-11ec-9cd7-5f87e3c093eb")] = {
        [hash("a37690c6-66b0-11ec-9cd7-91a751d327cb")] = {
            ["playSecretJingle"] = false,
        },
        [hash("a37690c7-66b0-11ec-9cd7-833be48de81f")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Vorpal_blade"],
            ["count"] = 1,
        },
    },
    [hash("a3707640-66b0-11ec-9cd7-59efc6b24075")] = {
        [hash("b9c16e00-66b0-11ec-a595-f73311b85ab0")] = {
            ["destination"] = {
                ["levelIid"] = "9312a0d0-66b0-11ec-a595-a934707bd447",
                ["entityIid"] = "b70d98a0-66b0-11ec-a595-b125edb525fa",
            },
        },
        [hash("efa1c030-66b0-11ec-8923-1f96484ed71d")] = {
            ["destination"] = {
                ["levelIid"] = "a36fda00-66b0-11ec-9cd7-ffa8f8d0b484",
                ["entityIid"] = "eec0d610-66b0-11ec-8923-93cc88ee368d",
            },
        },
    },
    [hash("a36f8be0-66b0-11ec-9cd7-a9c628ac47cf")] = {
        [hash("a36f8be7-66b0-11ec-9cd7-316971e16d32")] = {
            ["price"] = 100,
            ["type"] = enums["ItemType"]["Armor"],
            ["count"] = 1,
        },
        [hash("a36f8be8-66b0-11ec-9cd7-fd36870bdef5")] = {
            ["price"] = 500,
            ["type"] = enums["ItemType"]["Vorpal_blade"],
            ["count"] = 1,
        },
        [hash("9c20a1d0-66b0-11ec-b893-7dd8e9dfe663")] = {
            ["destination"] = {
                ["levelIid"] = "07caf540-66b0-11ec-a595-a55a7e13679d",
                ["entityIid"] = "3bde8fe0-66b0-11ec-a595-515a2ae1dbef",
            },
        },
        [hash("a36f8be6-66b0-11ec-9cd7-b5a8d5ccc437")] = {
            ["price"] = 5,
            ["type"] = enums["ItemType"]["Meat"],
            ["count"] = 1,
        },
        [hash("a36f8be9-66b0-11ec-9cd7-89a0e2fc55f0")] = {
            ["price"] = 250,
            ["type"] = enums["ItemType"]["Spell"],
            ["count"] = 1,
        },
    },
    [hash("a370eb70-66b0-11ec-9cd7-ef1d13410308")] = {
        [hash("9a28b800-66b0-11ec-9ccd-1bf7e7ba09a4")] = {
        },
    },
    [hash("a374bc00-66b0-11ec-9cd7-65fcab2d5d53")] = {
        [hash("d0d166d0-66b0-11ec-b893-fbba01a4c0d1")] = {
            ["destination"] = {
                ["levelIid"] = "a371aec0-66b0-11ec-9cd7-6f9e87cc2465",
                ["entityIid"] = "d4c0c970-66b0-11ec-b893-e744143e4b85",
            },
        },
        [hash("3baf9450-66b0-11ec-9ccd-095fcfe224e9")] = {
        },
    },
    [hash("a3727210-66b0-11ec-9cd7-aba0184f5034")] = {
        [hash("a5883f90-66b0-11ec-9ccd-15e7115af90e")] = {
        },
        [hash("a6d1af80-66b0-11ec-9ccd-e12feaf4f282")] = {
        },
        [hash("a3727216-66b0-11ec-9cd7-f345e02ef7d2")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 50,
        },
        [hash("a3727218-66b0-11ec-9cd7-1ddad18de70d")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Healing_potion"],
            ["count"] = 1,
        },
        [hash("a3727217-66b0-11ec-9cd7-8ff79d11908d")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gem"],
            ["count"] = 1,
        },
    },
    [hash("a3730e50-66b0-11ec-9cd7-65c84b0f9baa")] = {
        [hash("762fb910-7820-11ed-a6f2-95baf210def0")] = {
        },
    },
    [hash("a36e7a70-66b0-11ec-9cd7-67ffb406aba0")] = {
        [hash("a36e7a76-66b0-11ec-9cd7-9d8532e17d71")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Healing_potion"],
            ["count"] = 1,
        },
    },
    [hash("a36fda00-66b0-11ec-9cd7-ffa8f8d0b484")] = {
        [hash("0ab4ab60-66b0-11ec-9ccd-fdb315945fc4")] = {
        },
        [hash("ad891b20-66b0-11ec-8b7b-6bd6c116571f")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["GoldNuggets"],
            ["count"] = 1,
        },
        [hash("a67a5010-66b0-11ec-8b7b-d35918af82d9")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gem"],
            ["count"] = 1,
        },
        [hash("61c77d80-66b0-11ec-8b7b-9f180732e1db")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 1,
        },
        [hash("eec0d610-66b0-11ec-8923-93cc88ee368d")] = {
            ["destination"] = {
                ["levelIid"] = "a3707640-66b0-11ec-9cd7-59efc6b24075",
                ["entityIid"] = "efa1c030-66b0-11ec-8923-1f96484ed71d",
            },
        },
        [hash("a705a020-66b0-11ec-8b7b-394d1429f33c")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gem"],
            ["count"] = 1,
        },
        [hash("73315870-66b0-11ec-8b7b-79c435d3e320")] = {
        },
        [hash("e08334d0-66b0-11ec-8923-49bb818dd44a")] = {
        },
        [hash("647addb0-66b0-11ec-8b7b-bbc0182dd04a")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Armor"],
            ["count"] = 1,
        },
        [hash("a8208600-66b0-11ec-8b7b-f3f1f99dc9c5")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gem"],
            ["count"] = 1,
        },
    },
    [hash("a36a34b0-66b0-11ec-9cd7-09ebc042e238")] = {
        [hash("ad4d1430-66b0-11ec-9ccd-9d4683fc5a08")] = {
        },
        [hash("260c2b70-7820-11ed-b4b8-e7d3d85992e6")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 20,
        },
        [hash("1bebdd90-66b0-11ec-9ccd-bb4ef2660ecd")] = {
        },
        [hash("a36a34b7-66b0-11ec-9cd7-49f57098a445")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Gold"],
            ["count"] = 50,
        },
        [hash("a36a34bb-66b0-11ec-9cd7-5b38c50aa489")] = {
            ["playSecretJingle"] = false,
        },
        [hash("a36a34ba-66b0-11ec-9cd7-3d92ac9679f8")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Armor"],
            ["count"] = 1,
        },
        [hash("a36a34b6-66b0-11ec-9cd7-6192e3dc5680")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Green_gem"],
            ["count"] = 1,
        },
        [hash("b2ce1350-66b0-11ec-9ccd-313511d6a7cc")] = {
        },
        [hash("a36a34b9-66b0-11ec-9cd7-c1de732b0896")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Meat"],
            ["count"] = 1,
        },
    },
    [hash("a36d41f0-66b0-11ec-9cd7-e962574817d4")] = {
        [hash("f6a0ef30-66b0-11ec-9368-f1f32eefb458")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Fire_blade"],
            ["count"] = 1,
        },
        [hash("fd5d2d70-66b0-11ec-9368-d360386152ce")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Healing_potion"],
            ["count"] = 1,
        },
    },
    [hash("07caf540-66b0-11ec-a595-a55a7e13679d")] = {
        [hash("3bde8fe0-66b0-11ec-a595-515a2ae1dbef")] = {
            ["destination"] = {
                ["levelIid"] = "a36f8be0-66b0-11ec-9cd7-a9c628ac47cf",
                ["entityIid"] = "9c20a1d0-66b0-11ec-b893-7dd8e9dfe663",
            },
        },
        [hash("96ac8800-3b70-11ee-a30c-6baaf557e906")] = {
        },
    },
    [hash("9312a0d0-66b0-11ec-a595-a934707bd447")] = {
        [hash("abd6a7b0-66b0-11ec-a595-ffcc1299ef8f")] = {
            ["destination"] = {
                ["levelIid"] = "a36b6d30-66b0-11ec-9cd7-8145d2a69a56",
                ["entityIid"] = "1a247570-66b0-11ec-b893-3368fa8363b5",
            },
        },
        [hash("b70d98a0-66b0-11ec-a595-b125edb525fa")] = {
            ["destination"] = {
                ["levelIid"] = "a3707640-66b0-11ec-9cd7-59efc6b24075",
                ["entityIid"] = "b9c16e00-66b0-11ec-a595-f73311b85ab0",
            },
        },
    },
    [hash("a371aec0-66b0-11ec-9cd7-6f9e87cc2465")] = {
        [hash("d4c0c970-66b0-11ec-b893-e744143e4b85")] = {
            ["destination"] = {
                ["levelIid"] = "a374bc00-66b0-11ec-9cd7-65fcab2d5d53",
                ["entityIid"] = "d0d166d0-66b0-11ec-b893-fbba01a4c0d1",
            },
        },
        [hash("33248980-66b0-11ec-9ccd-7da3583966c5")] = {
        },
    },
    [hash("a375f480-66b0-11ec-9cd7-05be0d3437be")] = {
        [hash("a375f486-66b0-11ec-9cd7-fd86a8f321b7")] = {
        },
        [hash("473827b0-66b0-11ec-9ccd-136878feffb5")] = {
        },
    },
    [hash("a36b6d30-66b0-11ec-9cd7-8145d2a69a56")] = {
        [hash("0838d5f0-66b0-11ec-9ccd-e5960751723f")] = {
        },
        [hash("aa555670-3b70-11ee-a30c-f9307023a8f9")] = {
        },
        [hash("dda183f0-66b0-11ec-9ccd-6dd03959680e")] = {
        },
        [hash("8cee7d00-66b0-11ec-9ccd-e9d0ce504542")] = {
        },
        [hash("a36b6d36-66b0-11ec-9cd7-69fba161c5fc")] = {
            ["price"] = 0,
            ["type"] = enums["ItemType"]["Ammo"],
            ["count"] = 10,
        },
        [hash("deec0550-66b0-11ec-9ccd-b937773f1451")] = {
        },
        [hash("130bade0-66b0-11ec-9ccd-43c233a37d30")] = {
        },
        [hash("1a247570-66b0-11ec-b893-3368fa8363b5")] = {
            ["destination"] = {
                ["levelIid"] = "9312a0d0-66b0-11ec-a595-a934707bd447",
                ["entityIid"] = "abd6a7b0-66b0-11ec-a595-ffcc1299ef8f",
            },
        },
    },
}

local level_fields = {
    [hash("a36811d0-66b0-11ec-9cd7-4367627fb745")] = {
    },
    [hash("a367c3b0-66b0-11ec-9cd7-91690c910c97")] = {
        ["roomType"] = enums["RoomType"]["Entrance"],
    },
    [hash("a373aa90-66b0-11ec-9cd7-a9310f178834")] = {
    },
    [hash("a368fc30-66b0-11ec-9cd7-d141af83d44b")] = {
    },
    [hash("a36c5790-66b0-11ec-9cd7-0d08d7991930")] = {
    },
    [hash("a37690c0-66b0-11ec-9cd7-5f87e3c093eb")] = {
    },
    [hash("a3707640-66b0-11ec-9cd7-59efc6b24075")] = {
    },
    [hash("a36f8be0-66b0-11ec-9cd7-a9c628ac47cf")] = {
        ["roomType"] = enums["RoomType"]["Shop"],
    },
    [hash("a370eb70-66b0-11ec-9cd7-ef1d13410308")] = {
    },
    [hash("a374bc00-66b0-11ec-9cd7-65fcab2d5d53")] = {
    },
    [hash("a3727210-66b0-11ec-9cd7-aba0184f5034")] = {
    },
    [hash("a3730e50-66b0-11ec-9cd7-65c84b0f9baa")] = {
        ["roomType"] = enums["RoomType"]["Save"],
    },
    [hash("a36e7a70-66b0-11ec-9cd7-67ffb406aba0")] = {
    },
    [hash("a36fda00-66b0-11ec-9cd7-ffa8f8d0b484")] = {
    },
    [hash("a36a34b0-66b0-11ec-9cd7-09ebc042e238")] = {
    },
    [hash("a36d41f0-66b0-11ec-9cd7-e962574817d4")] = {
        ["roomType"] = enums["RoomType"]["Boss"],
    },
    [hash("07caf540-66b0-11ec-a595-a55a7e13679d")] = {
    },
    [hash("9312a0d0-66b0-11ec-a595-a934707bd447")] = {
    },
    [hash("a371aec0-66b0-11ec-9cd7-6f9e87cc2465")] = {
    },
    [hash("a375f480-66b0-11ec-9cd7-05be0d3437be")] = {
        ["roomType"] = enums["RoomType"]["Exit"],
    },
    [hash("a36b6d30-66b0-11ec-9cd7-8145d2a69a56")] = {
    },
}

return {
    enums = enums,
    entity_fields = entity_fields,
    level_fields = level_fields,
}
