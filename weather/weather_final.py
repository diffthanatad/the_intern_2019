import xmltodict, json

infile = open("weather_ori.xml", "r")
sample = infile.readlines()
infile.close()

##get rid of newline character
for i in range (len(sample)):
    sample[i] = sample[i].strip()
    print(sample[i])

with open('weather_ori.xml') as inp:
    data = xmltodict.parse(inp.read())

##show data input (debugging)
##print("data:", data)

info = json.dumps(data, indent = 4)

##show info after convert (debugging)
##print(info)

outfile = open("data.json", "w")
outfile.write(info)
outfile.close()
