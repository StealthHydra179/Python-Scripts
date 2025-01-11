#put into parser images

file = open("commercial-listing-cn.txt","r", encoding="utf-8")


lineN = 0
count = 0
urlName = ""
imgUrl = ""
imgName = ""
locationName = ""

import os.path
import requests

folder = "commercial-listing-img/"

output = open("commercial-listing_output-cn.txt", "w", encoding="utf-8")

for currentLine in file:
    currentLine = currentLine.strip()
    if currentLine[0:2] == "<a":
        count += 1
        lineN = 1
        splittedHref = currentLine.split("href=\"")
        splittedQuotes = splittedHref[1].split("\"")
        url = splittedQuotes[0]

        lastDirectory = url.split("/")[-1]
        urlName = lastDirectory
        continue

    if lineN == 1:
        lineN = 2

    if lineN == 2:
        lineN = 3
        splittedDataSrcSet = currentLine.split("data-bgset=\"")
        splittedQuotes = splittedDataSrcSet[1].split("\"")
        imgUrl = splittedQuotes[0]
        imgName = imgUrl.split("/")[-1]
        continue

    if lineN > 2 and lineN < 9:
        lineN += 1
        continue

    if lineN == 9:
        lineN = 0
        
        endCaret = currentLine.split(">")
        startCaret = endCaret[1].split("<")
        name = startCaret[0]
        locationName = name
    
##        if (not os.path.exists(folder + imgName)):
##            print(imgName)
##            r = requests.get(imgUrl, allow_redirects = True)
##            open(folder + imgName, "wb").write(r.content)

        urlName = urlName.replace("'", "''")
        imgUrl = imgUrl.replace("'","''")
        imgName = imgName.replace("'","''")
        locationName = locationName.replace("'","''") # title
##        output.write(f"INSERT INTO CONTENT (CONTENT_TYPE_ID, CONTENT_KEY, ENABLE_FG, CREATED_DATE_TIME, USER_ID, SELLER_ID, PLATFORM_ID, BRANDING_ID, EFFECTIVE_DATE_TIME, EXPIRY_DATE_TIME) VALUES (29, '{urlName}', 'Y', current_date, (SELECT USER_ID FROM USERS WHERE PRIMARY_EMAIL = 'zhangweiheng1213@gmail.com' AND BRANDING_ID = (SELECT BRANDING_ID FROM BRANDING WHERE BRANDING_CD = 'jyconstruction.ca')), null, (SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='jyconstruction.ca'), (SELECT BRANDING_ID FROM BRANDING WHERE BRANDING_CD = 'jyconstruction.ca'), current_date, null);\n")
        output.write(f"INSERT INTO CONTENT_ATTRIBUTE (CONTENT_ID, ATTR_KEY, ATTR_SUB_KEY, VALUE) VALUES ((SELECT CONTENT_ID FROM CONTENT WHERE CONTENT_KEY = '{urlName}' AND PLATFORM_ID=(SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='jyconstruction.ca')), 'TITLE', '2', '{locationName}');\n")
##        output.write(f"INSERT INTO CONTENT_ATTRIBUTE (CONTENT_ID, ATTR_KEY, ATTR_SUB_KEY, VALUE) VALUES ((SELECT CONTENT_ID FROM CONTENT WHERE CONTENT_KEY = '{urlName}' AND PLATFORM_ID=(SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='jyconstruction.ca')), 'LOGO_PATH', '1', './jyconstruction/img/commercial-listing/{imgName}');\n")
##        output.write(f"INSERT INTO CONTENT_ATTRIBUTE (CONTENT_ID, ATTR_KEY, ATTR_SUB_KEY, VALUE) VALUES ((SELECT CONTENT_ID FROM CONTENT WHERE CONTENT_KEY = '{urlName}' AND PLATFORM_ID=(SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='jyconstruction.ca')), 'SEQUENCE', null, '{count}');\n")
        output.write("\n")



file.close()
output.close()
