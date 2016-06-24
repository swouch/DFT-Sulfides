#!/usr/bin/env python

from pymatgen import MPRester

apikey = 'fDJKEZpxSyvsXdCt'
mpr = MPRester(apikey)

formulas = []
mpid_list = []
data = mpr.query(criteria={"elements": {"$all": ['S']},"nelements": 2},properties=["band_gap", "pretty_formula", "spacegroup.symbol","e_above_hull","energy_per_atom","material_id","elements"])
rare_elements = ['Uut', 'Uuq', 'Ac', 'Th']

for mat in data:
    # print(mat)
    if (mat["e_above_hull"] < 0.01) and (mat["band_gap"] > 0.5):
        if (mat["elements"][0] not in rare_elements) and (mat["elements"][1] not in rare_elements): # This only works for binary
            formulas.append(mat["pretty_formula"])
            mpid_list.append(mat["material_id"])
            print(mat["elements"])

for formula in formulas:
    print(formula)

print(mpid_list)
print(len(mpid_list))
print(len(set(mpid_list)))