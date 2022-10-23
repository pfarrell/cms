#import pymediawikipedia
from mediawiki import MediaWiki
import json

wikipedia=MediaWiki()

elems = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", 
        "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", 
        "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", 
        "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", 
        "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", 
        "Iodine", "Xenon", "Cesium", "Barium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", 
        "Gold", "Mercury (element)", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Rutherfordium", 
        "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", 
        "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", 
        "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", 
        "Lutetium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", 
        "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium"]

output={}
for elem in elems:
    output[elem] = wikipedia.summary(elem, sentences=3)

print(json.dumps(output))
