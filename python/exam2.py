import json

team = {
    "team" : {
        "name" : "Super Heros",
        "location" : "Canton",
        "roster" : [
            {
                "name" : "Nanue",
                "powers" : ["strength", "bulletproof skin"]
            },
            {
                "name" : "Deadshot",
                "powers" : ["weapons"]
            },
            {
                "name" : "TDK",
                "powers" : ["detachable arms", "strength"]
            }
        ]
    }
}

print(json.dumps(team, indent=4))