# Periodic Table Problem

# Find a copy of the periodic table. Write a function that takes a single 
#  parameter which could be the name of an element, the symbol or group it 
#  belongs to.  The function should output the name of the element, its 
#  atomic weight and the group it belongs to.  E.g. for the parameter “Li” 
#  the program would output:
#   Element: Lithium
#   Atomic weight: 6.94
#   Group: Alkali metals
# You only need to use six elements from two different groups.

# https://github.com/Bowserinator/Periodic-Table-JSON

from json import loads

class Table:
    class Element:
        def __init__(self, data: dict):
            for k, v in data.items():
                self.__setattr__(k, v)
        def __repr__(self):
            return f"""{self.symbol} - {self.name}
{self.name} is a {self.category} discovered by {self.discovered_by}.
It has a boiling point of {self.boil} and a melting point of {self.melt}.
It has a atomic mass of {self.atomic_mass} and a density of {self.density}.
{self.summary}
"""

    def __init__(self, filepath):
        self.name_lut = {}
        self.symbol_lut = {}
        self.atomic_lut = {}

        with open(filepath, "rb") as file:
            data = loads(file.read())

        self.elements = []
        for i, el_data in enumerate(data["elements"]):
            self.elements.append(self.Element(el_data))
            self.name_lut.update({el_data['name'].upper():i})
            self.symbol_lut.update({el_data['symbol'].upper():i})
            self.atomic_lut.update({el_data['number']:i})

    def query(self):
        q = input("Enter query: ").upper()
        if q == "EXIT": raise StopIteration()
        elif q in self.name_lut.keys(): index = self.name_lut[q]
        elif q in self.symbol_lut.keys(): index = self.symbol_lut[q]
        elif not q.isnumeric(): return print("Could not find a element to match the query")
        elif int(q) in self.atomic_lut.keys(): index = self.atomic_lut[int(q)]
        else: return print("Could not find a element to match the query")
        print(self.elements[index])

T = Table("files/PeriodicTableData.json")
while True:
    try: T.query()
    except: break
