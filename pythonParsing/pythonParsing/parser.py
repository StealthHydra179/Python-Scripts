file = open("data.txt","r", encoding="utf-8")
intCount = 1
prevA = False
position2 = ""
position3 = ""
position4 = ""
position5 = ""
nC = 0
import os.path
import requests
path = "C:/git/dp/web-dp/src/main/resources/public/jyconstruction/img/clients/"
##output = open("output.txt", "w", encoding="utf-8")

for currentLine in file:
    currentLine = currentLine.strip()
    if currentLine[0:2] == "<a":
        prevA = True
        splittedA = currentLine.split("href=\"")
        
        finalAhref = splittedA[1].split("\"")
        position5 = finalAhref[0]
        
        continue

    if prevA:
        prevA = False
        currentLineSplitted = currentLine.split("\"")
        position4 = "." + currentLineSplitted[3]
        position3 = currentLineSplitted[5]
        position2 = position4.split("/")[-1].split(".")[0]
        fileName = position4.split("/")[-1]

        if (not os.path.exists(path + fileName)):
            print(fileName)
            nC+=1
##            print(os.path.exists(path + fileName))
            url = "https://jyconstruction.ca" + currentLineSplitted[3]
            r = requests.get(url, allow_redirects=True)
            open(path+fileName, "wb").write(r.content)
        
##        output.write("result.add(this.createProjectVO(" + (str)(intCount) + "L, \"" + position2 + "\", \"" + position3 + "\", \"" + position4  + "\", \"" + position5 + "\"));\n")

        intCount += 1
file.close()
##output.close()
print(nC)
