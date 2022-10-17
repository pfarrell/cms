import json

f= open("periodic_table.json")

reparse=[]

data = json.load(f)
f.close()

propNames=data['Table']['Columns']['Column']
for elem in data['Table']['Row']:
    obj={}
    if("Table" in elem.keys() or "Blank" in elem.keys() or "Row" in elem.keys()):
        reparse.append(elem)
    else:
        obj["Cell"]={}
        for idx, prop in enumerate(propNames):
            obj["Cell"][prop]=elem['Cell'][idx]
        reparse.append(obj)
output = ""
for idx, elem in enumerate(reparse):
    if("Blank" in elem.keys()):
        output += f"<td "
        for key in elem["Blank"].keys():
            if(key != "value"):
                output += f"{key.lower()}='{elem['Blank'][key]}' "
        output += f">{elem['Blank'].get('value', '')}</td>"
    elif("Table" in elem.keys()):
        output += f"</table><table "
        for key in elem["Table"].keys():
          output += f"{key.lower()}=\"{elem['Table'][key]}\""
        output += ">"
    elif("Row" in elem.keys()):
        output += "<tr " if (idx ==  0) else "</tr><tr "

        for key in elem["Row"].keys():
            if(key != "value"):
                output += f"{key.lower()}=\"{elem['Row'][key]}\""
        output += ">"
    else:
        e = elem['Cell']
        output += f"<td id=\"element_{e['number']}\" class=\"wrapper {e.get('group', '').replace(' ', '').lower()} \" title=\"{e.get('name')}\" "
        for key in e.keys():
            output += f"data-{key.lower()}='{e[key]}' "
        output += f"><p class=\"element\"><p class=\"number\">{e.get('number')}</p><p class=\"symbol\">{e.get('symbol')}</p><p class=\"name\">{e.get('name')}</p><p class=\"display\">{e.get('mass')}</p></p></td>"
print(output + "</tr>")
