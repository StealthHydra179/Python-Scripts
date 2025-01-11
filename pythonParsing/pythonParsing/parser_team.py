file = open("team.txt","r", encoding="utf-8")
intCount = 1
lineN = 0
position2 = ""
position3 = ""
position4 = ""
position5 = ""
fileName = ""
url = ""
nC = 0
import os.path
import requests
path = "C:/git/dp/web-dp/src/main/resources/public/jyconstruction/img/team/"
output = open("team_output.txt", "w", encoding="utf-8")

for currentLine in file:
    currentLine = currentLine.strip()
    if currentLine[0:4] == "<img":
        lineN = 1
        splittedA = currentLine.split("src=\"")
        
        position5 = splittedA[1].split("\"")[0]
        position4 = position5.split("/")[-1]
        url = position5                             
        fileName = position4
        
        continue

    if lineN == 1 and currentLine[0:2] == "<p":
        ##lineN = False
        lineN = 2
        currentLineSplitted = currentLine.split("\">")
        position2 = currentLineSplitted[1].split("<")[0]

        continue

    if lineN == 2  and currentLine[0:2] == "<p":
        ##lineN = False
        lineN = 3
        currentLineSplitted = currentLine.split("\">")
        position3 = currentLineSplitted[1].split("<")[0]

##      print (fileName, url, position2, position3)

        if (not os.path.exists(path + fileName)):
            print(fileName)
            nC+=1
##            print(os.path.exists(path + fileName))
            r = requests.get(url, allow_redirects=True)
            open(path+fileName, "wb").write(r.content)
      
        output.write("result.add(this.createTeamVO(" + (str)(intCount) + "L, \"" + position2.replace(' ','-').lower() + "\", \"" + position2 + "\", \"" + position3 + "\", \"" + "./jyconstruction/img/team/"  + fileName + "\"));\n")

        intCount += 1

file.close()
##output.close()
print(nC)
output.close()
