import json 

f= open("periodic_table.json") 
reparse=[] 
data = json.load(f) 
f.close() 
propNames=data['Table']['Columns']['Column'] 

for elem in data['Table']['Row']: 
    obj={} 
    if("Table" in elem.keys() or "Highlight" in elem.keys() or "Blank" in elem.keys() or "Row" in elem.keys()): 
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
    elif("Highlight" in elem.keys()):
        output += "<td "
        for key in elem["Highlight"].keys():
            output += f"{key.lower()}='{elem['Highlight'][key]}' "
        output += ("><div class='highlight'>"
                      "<div class='row'>"
                        "<div class='col1'>"
                          "<div class='imgWrapper'><img id='elementImage'>&nbsp;</div>"
                        "</div>"
                        "<div class='col2'>"
                          "<div><div id='eNumber' class='value'>&nbsp;</div> <div id='eName' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Discovered</div><div id='eDiscovered' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Group</div><div id='eGroup' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Config</div><div id='eConfig' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Mass</div><div id='eMass' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>ElectroNegativity</div><div id='eElectronegativity' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Radius</div><div id='eRadius' class='value'>&nbsp;</div></div>"
                        "</div>"
                        "<div class='col2'>"
                          "<div class='vspacer'>&nbsp;</div>"
                          "<div><div class='label'>Energy</div><div id='eEnergy' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Affinity</div><div id='eAffinity' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Oxidation</div><div id='eOxidation' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Standard State</div><div id='eStandard' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Melting</div><div id='eMelting' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Boiling</div><div id='eBoiling' class='value'>&nbsp;</div></div>"
                          "<div><div class='label'>Density: </div><div id='eDensity' class='value'>&nbsp;</div></div>"
                        "</div>"
                        "<div class='col3'>"
                          "<div><div id='eSymbol' class='value'>&nbsp;</div></div>"
                        "</div>"
                      "</div>"
                      "<div><div class='value' id='eSummary'>&nbsp;</div>"
                      "<div class='wbg'></div>"
                    "</div>")
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
    elif("Cell" in elem.keys()):
        e = elem['Cell']
        output += f"<td class=\"wrapper {e.get('group', '').replace(' ', '').lower()} \" title=\"{e.get('name')}\" onmouseleave='unhighlight(this)' onmouseover='highlight(this)' "
        for key in e.keys():
            output += f"data-{key.lower()}='{e[key]}' "
        output += f"><div class='cell'><div id=\"element_{e.get('number', '')}\"><p class='element'><div class='circle'><p class=\"number\">{e.get('number')}</p></div><p class=\"symbol\">{e.get('symbol')}</p><p class=\"name\">{e.get('name')}</p><p class=\"display\">{e.get('mass')}</p></p></div></td>"
    else:
        print(f"unexpected key: {e.keys()}")
print(output + "</tr>")
