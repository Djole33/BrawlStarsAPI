# Import Flask library for creating web applications
from flask import Flask, jsonify
import os

# Initialize Flask application
app = Flask(__name__)
port = int(os.getenv('PORT', 4000))

# List of brawlers
brawlers = [
    {
        "id": 1,
        "name": "8-Bit",
        "1st gadget": "Cheat Cartridge",
        "2nd gadget": "Extra Credits",
        "1st star power": "Boosted Booster",
        "2nd star power": "Plugged In"
    },
    {
        "id": 2,
        "name": "Amber",
        "1st gadget": "Fire Starters",
        "2nd gadget": "Dancing Flames",
        "1st star power": "Wild Flames",
        "2nd star power": "Scorchin' Siphon"
    },
    {
        "id": 3,
        "name": "Angelo",
        "1st gadget": "Stinging Flight",
        "2nd gadget": "Master Fletcher",
        "1st star power": "Empower",
        "2nd star power": "Flow"
    },
    {
        "id": 4,
        "name": "Ash",
        "1st gadget": "Chill Pill",
        "2nd gadget": "Rotten Banana",
        "1st star power": "First Bash",
        "2nd star power": "Mad As Heck"
    },
    {
        "id": 5,
        "name": "Barley",
        "1st gadget": "Sticky Syrup Mixer",
        "2nd gadget": "Herbal Tonic",
        "1st star power": "Medical Use",
        "2nd star power": "Extra Noxious"
    },
    {
        "id": 6,
        "name": "Bea",
        "1st gadget": "Honey Molasses",
        "2nd gadget": "Rattled Hive",
        "1st star power": "Insta Beeload",
        "2nd star power": "Honey Coat"
    },
    {
        "id": 7,
        "name": "Belle",
        "1st gadget": "Nest Egg",
        "2nd gadget": "Reverse Polarity",
        "1st star power": "Positive Feedback",
        "2nd star power": "Grounded"
    },
    {
        "id": 8,
        "name": "Bibi",
        "1st gadget": "Vitamin Booster",
        "2nd gadget": "Extra Sticky",
        "1st star power": "Home Run",
        "2nd star power": "Batting Stance"
    },
    {
        "id": 9,
        "name": "Bo",
        "1st gadget": "Super Totem",
        "2nd gadget": "Tripwire",
        "1st star power": "Circling Eagle",
        "2nd star power": "Snare a Bear"
    },
    {
        "id": 10,
        "name": "Bonnie",
        "1st gadget": "Sugar Rush",
        "2nd gadget": "Crash Test",
        "1st star power": "Black Powder",
        "2nd star power": "Wisdom Tooth"
    },
    {
        "id": 11,
        "name": "Brock",
        "1st gadget": "Rocket Laces",
        "2nd gadget": "Rocket Fuel",
        "1st star power": "Incendiary",
        "2nd star power": "Rocket Number Four"
    },
    {
        "id": 12,
        "name": "Bull",
        "1st gadget": "T-Bone Injector",
        "2nd gadget": "Stomper",
        "1st star power": "Berserker",
        "2nd star power": "Tough Guy"
    },
    {
        "id": 13,
        "name": "Buster",
        "1st gadget": "Utility Belt",
        "2nd gadget": "Slo-Mo Replay",
        "1st star power": "Blockbuster",
        "2nd star power": "Kevlar Vest"
    },
    {
        "id": 14,
        "name": "Buzz",
        "1st gadget": "Reserve Buoy",
        "2nd gadget": "X-Ray-Shades",
        "1st star power": "Tougher Torpedo",
        "2nd star power": "Eyes Sharp"
    },
    {
        "id": 15,
        "name": "Byron",
        "1st gadget": "Shot In The Arm",
        "2nd gadget": "Booster Shots",
        "1st star power": "Malaise",
        "2nd star power": "Injection"
    },
    {
        "id": 16,
        "name": "Carl",
        "1st gadget": "Heat Ejector",
        "2nd gadget": "Flying Hook",
        "1st star power": "Power Throw",
        "2nd star power": "Protective Pirouette"
    },
    {
        "id": 17,
        "name": "Charlie",
        "1st gadget": "Spiders",
        "2nd gadget": "Personal Space",
        "1st star power": "Digestive",
        "2nd star power": "Slimy"
    },
    {
        "id": 18,
        "name": "Chester",
        "1st gadget": "Spicy Dice",
        "2nd gadget": "Candy Beans",
        "1st star power": "Bell'o'mania",
        "2nd star power": "Sneak Peek"
    },
    {
        "id": 19,
        "name": "Chuck",
        "1st gadget": "Rerouting",
        "2nd gadget": "Ghost Train",
        "1st star power": "Pit Stop",
        "2nd star power": "Tickets Please!"
    },
    {
        "id": 20,
        "name": "Colette",
        "1st gadget": "Na-Ah!",
        "2nd gadget": "Gotcha!",
        "1st star power": "Push It",
        "2nd star power": "Mass Tax"
    },
    {
        "id": 21,
        "name": "Colt",
        "1st gadget": "Speedloader",
        "2nd gadget": "Silver Bullet",
        "1st star power": "Slick Boots",
        "2nd star power": "Magnum Special"
    },
    {
        "id": 22,
        "name": "Cordelius",
        "1st gadget": "Replanting",
        "2nd gadget": "Poison Mushroom",
        "1st star power": "Comboshrooms",
        "2nd star power": "Mushroom Kingdom"
    },
    {
        "id": 23,
        "name": "Crow",
        "1st gadget": "Defense Booster",
        "2nd gadget": "Slowing Toxin",
        "1st star power": "Extra Toxic",
        "2nd star power": "Carrion Crow"
    },
    {
        "id": 24,
        "name": "Darryl",
        "1st gadget": "Recoiling Rotator",
        "2nd gadget": "Tar Barrel",
        "1st star power": "Steel Hoops",
        "2nd star power": "Rolling Reload"
    },
    {
        "id": 25,
        "name": "Doug",
        "1st gadget": "Double Sausage",
        "2nd gadget": "Extra Mustard",
        "1st star power": "Fast Food",
        "2nd star power": "Self Service"
    },
    {
        "id": 26,
        "name": "Draco",
        "1st gadget": "Upper Cut",
        "2nd gadget": "Last Stand",
        "1st star power": "Expose",
        "2nd star power": "Shredding"
    },
    {
        "id": 27,
        "name": "Dynamike",
        "1st gadget": "Fidget Spinner",
        "2nd gadget": "Satchel Charge",
        "1st star power": "Dyna-Jump",
        "2nd star power": "Demolition"
    },
    {
        "id": 28,
        "name": "Edgar",
        "1st gadget": "Let's Fly",
        "2nd gadget": "Hardcore",
        "1st star power": "Hard Landing",
        "2nd star power": "Fisticuffs"
    },
    {
        "id": 29,
        "name": "El Primo",
        "1st gadget": "Suplex Supplement",
        "2nd gadget": "Asteroid Belt",
        "1st star power": "El Fuego",
        "2nd star power": "Meteor Rush"
    },
    {
        "id": 30,
        "name": "Emz",
        "1st gadget": "Friendzoner",
        "2nd gadget": "Acid Spray",
        "1st star power": "Bad Karma",
        "2nd star power": "Hype"
    },
    {
        "id": 31,
        "name": "Eve",
        "1st gadget": "Gotta Go!",
        "2nd gadget": "Motherly Love",
        "1st star power": "Unnatural Order",
        "2nd star power": "Happy Surprise"
    },
    {
        "id": 32,
        "name": "Fang",
        "1st gadget": "Corn-Fu",
        "2nd gadget": "Roundhouse Kick",
        "1st star power": "Fresh Kicks",
        "2nd star power": "Divine Soles"
    },
    {
        "id": 33,
        "name": "Frank",
        "1st gadget": "Active Noise Canceling",
        "2nd gadget": "Irresistible Attraction",
        "1st star power": "Power Grab",
        "2nd star power": "Sponge"
    },
    {
        "id": 34,
        "name": "Gale",
        "1st gadget": "Spring Ejector",
        "2nd gadget": "Twister",
        "1st star power": "Blustery Blow",
        "2nd star power": "Freezing Snow"
    },
    {
        "id": 35,
        "name": "Gene",
        "1st gadget": "Lamp Blowout",
        "2nd gadget": "Vengeful Spirits",
        "1st star power": "Magic Puffs",
        "2nd star power": "Spirit Slap"
    },
    {
        "id": 36,
        "name": "Gray",
        "1st gadget": "Walking Cane",
        "2nd gadget": "Grand Piano",
        "1st star power": "Fake Injury",
        "2nd star power": "New Perspective"
    },
    {
        "id": 37,
        "name": "Griff",
        "1st gadget": "Piggy Bank",
        "2nd gadget": "Coin Shower",
        "1st star power": "Keep The Change",
        "2nd star power": "Business Resilience"
    },
    {
        "id": 38,
        "name": "Grom",
        "1st gadget": "Watchtower",
        "2nd gadget": "Radio Check",
        "1st star power": "Foot Patrol",
        "2nd star power": "X-Factor"
    },
    {
        "id": 39,
        "name": "Gus",
        "1st gadget": "Kooky Popper",
        "2nd gadget": "Soul Switcher",
        "1st star power": "Health Bonanza",
        "2nd star power": "Spirit Animal"
    },
    {
        "id": 40,
        "name": "Hank",
        "1st gadget": "Waterballoons",
        "2nd gadget": "Life Ring",
        "1st star power": "It’s Gonna Blow",
        "2nd star power": "Barricade"
    },
    {
        "id": 41,
        "name": "Jacky",
        "1st gadget": "Pneumatic Booster",
        "2nd gadget": "Counter Crush",
        "1st star power": "Hardy Hard Hat",
        "2nd star power": "Super Charge"
    },
    {
        "id": 42,
        "name": "Janet",
        "1st gadget": "Drop The Bass",
        "2nd gadget": "Backstage Pass",
        "1st star power": "Stage View",
        "2nd star power": "Vocal Warm Up"
    },
    {
        "id": 43,
        "name": "Jessie",
        "1st gadget": "Spark Plug",
        "2nd gadget": "Recoil Spring",
        "1st star power": "Energize",
        "2nd star power": "Shocky"
    },
    {
        "id": 44,
        "name": "Kit",
        "1st gadget": "Cardboard Box",
        "2nd gadget": "Cheeseburger",
        "1st star power": "Power Hungry",
        "2nd star power": "Overly Attached"
    },
    {
        "id": 45,
        "name": "Larry & Lawrie",
        "1st gadget": "Order: Swap",
        "2nd gadget": "Order: Fall Back",
        "1st star power": "Protocol: Protect",
        "2nd star power": "Protocol: Assist"
    },
    {
        "id": 46,
        "name": "Leon",
        "1st gadget": "Clone Projector",
        "2nd gadget": "Lollipop Drop",
        "1st star power": "Smoke Trails",
        "2nd star power": "Invisiheal"
    },
    {
        "id": 47,
        "name": "Lily",
        "1st gadget": "Vanish",
        "2nd gadget": "Repot",
        "1st star power": "Spiky",
        "2nd star power": "Vigilance"
    },
    {
        "id": 48,
        "name": "Lola",
        "1st gadget": "Freeze Frame",
        "2nd gadget": "Stunt Double",
        "1st star power": "Improvise",
        "2nd star power": "Sealed With A Kiss"
    },
    {
        "id": 49,
        "name": "Lou",
        "1st gadget": "Ice Block",
        "2nd gadget": "Cryo Syrup",
        "1st star power": "Supercool",
        "2nd star power": "Hypothermia"
    },
    {
        "id": 50,
        "name": "Maisie",
        "1st gadget": "Safety Net",
        "2nd gadget": "Pretty In Pink",
        "1st star power": "Shockwave",
        "2nd star power": "Trigger Finger"
    },
    {
        "id": 51,
        "name": "Mandy",
        "1st gadget": "Cookie Crumbs",
        "2nd gadget": "Pop Rocks",
        "1st star power": "In My Sights",
        "2nd star power": "Hard Candy"
    },
    {
        "id": 52,
        "name": "Max",
        "1st gadget": "Phase Shifter",
        "2nd gadget": "Sneaky Sneakers",
        "1st star power": "Super Charged",
        "2nd star power": "Run n' Gun"
    },
    {
        "id": 53,
        "name": "Meg",
        "1st gadget": "Jolting Volts",
        "2nd gadget": "Toolbox",
        "1st star power": "Force Field",
        "2nd star power": "Self Destruction"
    },
    {
        "id": 54,
        "name": "Melodie",
        "1st gadget": "Perfect Pitch",
        "2nd gadget": "Interlude",
        "1st star power": "Fast Beats",
        "2nd star power": "Extended Mix"
    },
    {
        "id": 55,
        "name": "Mico",
        "1st gadget": "Clipping Scream",
        "2nd gadget": "Presto",
        "1st star power": "Monkey Business",
        "2nd star power": "Record Smash"
    },
    {
        "id": 56,
        "name": "Mortis",
        "1st gadget": "Combo Spinner",
        "2nd gadget": "Survival Shovel",
        "1st star power": "Creepy Harvest",
        "2nd star power": "Coiled Snake"
    },
    {
        "id": 57,
        "name": "Mr. P",
        "1st gadget": "Service Bell",
        "2nd gadget": "Porter Reinforcements",
        "1st star power": "Handle With Care",
        "2nd star power": "Revolving Door"
    },
    {
        "id": 58,
        "name": "Nani",
        "1st gadget": "Warp Blast",
        "2nd gadget": "Return to Sender",
        "1st star power": "Autofocus",
        "2nd star power": "Tempered Steel"
    },
    {
        "id": 59,
        "name": "Nita",
        "1st gadget": "Bear Paws",
        "2nd gadget": "Faux Fur",
        "1st star power": "Bear With Me",
        "2nd star power": "Hyper Bear"
    },
    {
        "id": 60,
        "name": "Otis",
        "1st gadget": "Dormant Star",
        "2nd gadget": "Phat Splatter",
        "1st star power": "Ink Refill",
        "2nd star power": "Stencil Glue"
    },
    {
        "id": 61,
        "name": "Pam",
        "1st gadget": "Pulse Modulator",
        "2nd gadget": "Scrapsucker",
        "1st star power": "Mama's Hug",
        "2nd star power": "Mama's Squeeze"
    },
    {
        "id": 62,
        "name": "Pearl",
        "1st gadget": "Overcooked",
        "2nd gadget": "Made With Love",
        "1st star power": "Heat Retention",
        "2nd star power": "Heat Shield"
    },
    {
        "id": 63,
        "name": "Penny",
        "1st gadget": "Salty Barrel",
        "2nd gadget": "Trusty Spyglass",
        "1st star power": "Heavy Coffers",
        "2nd star power": "Master Blaster"
    },
    {
        "id": 64,
        "name": "Piper",
        "1st gadget": "Auto Aimer",
        "2nd gadget": "Homemade Recipe",
        "1st star power": "Ambush",
        "2nd star power": "Snappy Sniping"
    },
    {
        "id": 65,
        "name": "Poco",
        "1st gadget": "Tuning Fork",
        "2nd gadget": "Protective Tunes",
        "1st star power": "Da Capo!",
        "2nd star power": "Screeching Solo"
    },
    {
        "id": 66,
        "name": "R-T",
        "1st gadget": "Hacks",
        "2nd gadget": "Rattling Bones",
        "1st star power": "Quick Maths",
        "2nd star power": "In Line"
    },
    {
        "id": 67,
        "name": "Rico",
        "1st gadget": "Multiball Launcher",
        "2nd gadget": "Bouncy Castle",
        "1st star power": "Super Bouncy",
        "2nd star power": "Robo Retreat"
    },
    {
        "id": 68,
        "name": "Rosa",
        "1st gadget": "Grow Light",
        "2nd gadget": "Unfriendly Bushes",
        "1st star power": "Plant Life",
        "2nd star power": "Thorny Gloves"
    },
    {
        "id": 69,
        "name": "Ruffs",
        "1st gadget": "Take Cover",
        "2nd gadget": "Air Support",
        "1st star power": "Air Superiority",
        "2nd star power": "Field Promotion"
    },
    {
        "id": 70,
        "name": "Sam",
        "1st gadget": "Magnetic Field",
        "2nd gadget": "Earthquake",
        "1st star power": "Hearty Recovery",
        "2nd star power": "Remote Recharge"
    },
    {
        "id": 71,
        "name": "Sandy",
        "1st gadget": "Sleep Stimulator",
        "2nd gadget": "Sweet Dreams",
        "1st star power": "Rude Sands",
        "2nd star power": "Healing Winds"
    },
    {
        "id": 72,
        "name": "Shelly",
        "1st gadget": "Fast Forward",
        "2nd gadget": "Clay Pigeons",
        "1st star power": "Shell Shock",
        "2nd star power": "Band-Aid"
    },
    {
        "id": 73,
        "name": "Spike",
        "1st gadget": "Popping Pincushion",
        "2nd gadget": "Life Plant",
        "1st star power": "Fertilize",
        "2nd star power": "Curveball"
    },
    {
        "id": 74,
        "name": "Sprout",
        "1st gadget": "Garden Mulcher",
        "2nd gadget": "Transplant",
        "1st star power": "Overgrowth",
        "2nd star power": "Photosynthesis"
    },
    {
        "id": 75,
        "name": "Squeak",
        "1st gadget": "Windup",
        "2nd gadget": "Residue",
        "1st star power": "Chain Reaction",
        "2nd star power": "Super Sticky"
    },
    {
        "id": 76,
        "name": "Stu",
        "1st gadget": "Speed Zone",
        "2nd gadget": "Breakthrough",
        "1st star power": "Zero Drag",
        "2nd star power": "Gaso-Heal"
    },
    {
        "id": 77,
        "name": "Surge",
        "1st gadget": "Power Surge",
        "2nd gadget": "Power Shield",
        "1st star power": "To The Max!",
        "2nd star power": "Serve Ice Cold"
    },
    {
        "id": 78,
        "name": "Tara",
        "1st gadget": "Psychic Enhancer",
        "2nd gadget": "Support From Beyond",
        "1st star power": "Black Portal",
        "2nd star power": "Healing Shade"
    },
    {
        "id": 79,
        "name": "Tick",
        "1st gadget": "Backup Mine",
        "2nd gadget": "Last Hurrah",
        "1st star power": "Well Oiled",
        "2nd star power": "Automa-Tick Reload"
    },
    {
        "id": 80,
        "name": "Willow",
        "1st gadget": "Spellbound",
        "2nd gadget": "Dive",
        "1st star power": "Love Is Blind",
        "2nd star power": "Obsession"
    }
]

# List of gears
gears = [
    {
        "id": 1,
        "name": "SPEED",
        "description": "Gain 15% SPEED INCREASE when moving in bushes.",
        "rarity": "Rare"
    },
    {
        "id": 2,
        "name": "HEALTH",
        "description": "RECOVER HEALTH 50% more effectively.",
        "rarity": "Rare"
    },
    {
        "id": 3,
        "name": "DAMAGE",
        "description": "Deal 15% EXTRA DAMAGE when your Brawler is below 50% Health.",
        "rarity": "Rare"
    },
    {
        "id": 4,
        "name": "VISION",
        "description": "REVEAL opponents for 2 seconds after dealing damage to them.",
        "rarity": "Rare"
    },
    {
        "id": 5,
        "name": "SHIELD",
        "description": "Gain extra 900 HEALTH as a consumable SHIELD. The shield regenerates in 10 seconds, when at full health.",
        "rarity": "Rare"
    },
    {
        "id": 6,
        "name": "RELOAD SPEED",
        "description": "15% faster RELOAD.",
        "rarity": "Super Rare"
    },
    {
        "id": 7,
        "name": "SUPER CHARGE",
        "description": "Super CHARGES 10% FASTER.",
        "rarity": "Super Rare"
    },
    {
        "id": 8,
        "name": "THICC HEAD",
        "description": "Tick's Head gains 1000 EXTRA HEALTH.",
        "rarity": "Epic"
    },
    {
        "id": 9,
        "name": "TALK TO THE HAND",
        "description": "Extend the reach of Gene's Magic Hand.",
        "rarity": "Epic"
    },
    {
        "id": 10,
        "name": "ENDURING TOXINS",
        "description": "Increases Crow's poison damage by 30%.",
        "rarity": "Epic"
    },
    {
        "id": 11,
        "name": "STICKY SPIKES",
        "description": "Spike's Super slows 30% more effectively.",
        "rarity": "Epic"
    },
    {
        "id": 12,
        "name": "LINGERING SMOKE",
        "description": "Leon's Smoke Bomb lasts 2 seconds longer.",
        "rarity": "Epic"
    },
    {
        "id": 13,
        "name": "EXHAUSTING STORM",
        "description": "Enemies inside of Sandy's Sandstorm deal 20% less damage.",
        "rarity": "Epic"
    },
    {
        "id": 14,
        "name": "STICKY OIL",
        "description": "Amber's oil spills now also slow down enemies by 10%.",
        "rarity": "Epic"
    },
    {
        "id": 15,
        "name": "PET POWER",
        "description": "Pet power increased by 25%.",
        "rarity": "Super Rare"
    },
    {
        "id": 16,
        "name": "QUADRUPLETS",
        "description": "Eve's Super spawns 1 extra hatchling.",
        "rarity": "Epic"
    },
    {
        "id": 17,
        "name": "SUPER TURRET",
        "description": "Increases the healing of Pam's turret by 20%.",
        "rarity": "Epic"
    },
    {
        "id": 18,
        "name": "GADGET CHARGE",
        "description": "Increases number of Gadget usages per battle by 1.",
        "rarity": "Rare"
    },
    {
        "id": 19,
        "name": "BAT STORM",
        "description": "The speed of bats increased by 50%.",
        "rarity": "Epic"
    }
]

# Route for the home page, providing instructions on how to use the API
@app.route('/')
def home():
    return "Welcome to the Brawlers and Gears API! Use /brawlers to get the list of all brawlers, /brawler/id to get details of an individual brawler, /gears to get the list of all gears, or /gear/id to get details of an individual gear."

# Route to get the list of all brawlers
@app.route('/brawlers', methods=['GET'])
def get_brawlers():
    return jsonify(brawlers)  # Return JSON representation of the list of brawlers

# Route to get details of an individual brawler based on ID
@app.route('/brawler/<int:id>', methods=['GET'])
def get_brawler(id):
    # Find the brawler with the specified ID, return its details or an error if not found
    brawler_info = next((b for b in brawlers if b['id'] == id), None)
    if brawler_info:
        return jsonify(brawler_info)
    else:
        return jsonify({"error": "Brawler not found"}), 404

# Route to get the list of all gears
@app.route('/gears', methods=['GET'])
def get_gears():
    return jsonify(gears)  # Return JSON representation of the list of gears

# Route to get details of an individual gear based on ID
@app.route('/gear/<int:id>', methods=['GET'])
def get_gear(id):
    # Find the gear with the specified ID, return its details or an error if not found
    gear = next((gear for gear in gears if gear["id"] == id), None)
    if gear:
        return jsonify(gear)
    else:
        return jsonify({"error": "Gear not found"}), 404

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
