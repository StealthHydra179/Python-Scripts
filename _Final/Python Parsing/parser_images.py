import os.path
import requests

inputFile = open("input.txt","r", encoding="utf-8")
outputFile = open("output.txt", "w", encoding="utf-8")

storageFolder = "img/"

lineNumber = 0
count = 0

urlName = ""
imgUrl = ""
imgName = ""
locationName = ""

for currentLine in inputFile:
    # Remove leading and trailing whitespaces
    currentLine = currentLine.strip()

    # Check if the current line is an anchor tag
    if currentLine[0:2] == "<a":
        count += 1
        lineNumber = 1

        # Split the current to find the contents of the href attribute
        url = currentLine.split("href=\"")[1].split("\"")[0]

        # Get the last directory (the urlName) of the URL by splitting the URL by "/" and taking the last element
        urlName = url.split("/")[-1]
        continue

    if lineNumber == 1:
        # Skip the intermediary line based on the input data.
        lineNumber = 2

    if lineNumber == 2:
        lineNumber = 3

        # Get the URL of the image by getting the contents of the data-bgset attribute
        imgUrl = currentLine.split("data-bgset=\"")[1].split("\"")[0]
        imgName = imgUrl.split("/")[-1]
        continue

    if lineNumber > 2 and lineNumber < 9:
        #skip the intermediary lines based on the input data.
        lineNumber += 1

    if lineNumber == 9:
        # last line of the data
        lineNumber = 0
        
        # Get the location name by splitting the current line by ">" and "<" and taking the second element
        locationName = currentLine.split(">")[1].split("<")[0]

        if (not os.path.exists(storageFolder + imgName)):
            r = requests.get(imgUrl, allow_redirects = True)
            open(storageFolder + imgName, "wb").write(r.content)

        # Replace single quotes with double single quotes to escape them in SQL
        urlName = urlName.replace("'", "''")
        imgUrl = imgUrl.replace("'","''")
        imgName = imgName.replace("'","''")
        locationName = locationName.replace("'","''")

        # Write the SQL queries to the output file
        outputFile.write(f"INSERT INTO CONTENT (CONTENT_TYPE_ID, CONTENT_KEY, ENABLE_FG, CREATED_DATE_TIME, USER_ID, SELLER_ID, PLATFORM_ID, BRANDING_ID, EFFECTIVE_DATE_TIME, EXPIRY_DATE_TIME) VALUES (29, '{urlName}', 'Y', current_date, (SELECT USER_ID FROM USERS WHERE PRIMARY_EMAIL = 'redacted@gmail.com' AND BRANDING_ID = (SELECT BRANDING_ID FROM BRANDING WHERE BRANDING_CD = 'redacted.ca')), null, (SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='redacted.ca'), (SELECT BRANDING_ID FROM BRANDING WHERE BRANDING_CD = 'redacted.ca'), current_date, null);\n")
        outputFile.write(f"INSERT INTO CONTENT_ATTRIBUTE (CONTENT_ID, ATTR_KEY, ATTR_SUB_KEY, VALUE) VALUES ((SELECT CONTENT_ID FROM CONTENT WHERE CONTENT_KEY = '{urlName}' AND PLATFORM_ID=(SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='redacted.ca')), 'TITLE', '2', '{locationName}');\n")
        outputFile.write(f"INSERT INTO CONTENT_ATTRIBUTE (CONTENT_ID, ATTR_KEY, ATTR_SUB_KEY, VALUE) VALUES ((SELECT CONTENT_ID FROM CONTENT WHERE CONTENT_KEY = '{urlName}' AND PLATFORM_ID=(SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='redacted.ca')), 'LOGO_PATH', '1', '{storageFolder}/{imgName}');\n")
        outputFile.write(f"INSERT INTO CONTENT_ATTRIBUTE (CONTENT_ID, ATTR_KEY, ATTR_SUB_KEY, VALUE) VALUES ((SELECT CONTENT_ID FROM CONTENT WHERE CONTENT_KEY = '{urlName}' AND PLATFORM_ID=(SELECT PLATFORM_ID FROM PLATFORM WHERE ROOT_DOMAIN='redacted.ca')), 'SEQUENCE', null, '{count}');\n")
        outputFile.write("\n")



inputFile.close()
outputFile.close()
