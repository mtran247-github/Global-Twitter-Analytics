#This program is used to calculate the happiness score from different timezones
#author: Melissa Tran


# Initialize dictionary and variables
try:
    keyWordsDictionary = {}
    pacific = 0
    mountain = 0
    central = 0
    count = 0
    eastern = 0
    # p1Lat = 49.189787
    # p1Long = -67.444574
    # p2Lat = 24.660845
    # p2Long = -67.444574
    # p3Lat = 49.189787
    # p3Long = -87.518395
    # p4Lat = 24.660845
    # p4Long = -87.518395
    # p5Lat = 49.189787
    # p5Long = -101.998892
    # p6Lat = 24.660845
    # p6Long = -101.998892
    # p7Lat = 49.189787
    # p7Long = -115.236428
    # p8Lat = 24.660845
    # p8Long = -115.236428
    # p9Lat = 49.189787
    # p9Long = -125.242264
    # p10Lat = 24.660845
    # p10Long = -125.242264

    # Input keyword file name
    keyFileName = input("Enter the KEYWORD filename: ")
    keyFile = open("keywords.txt", "r", encoding="utf-8")

    # Populate keyword dictionary
    for line in keyFile:
        arr = line.split(",")
        keyWordsDictionary[arr[0]] = "".join(arr[1].strip("\n"))

    # Convert keyword values to integers
    for key, value in keyWordsDictionary.items():
            keyWordsDictionary[key] = int(value)


    #input tweets file name
    # Open and read tweet file and tterate through each tweet
    tweetFileName = input("Enter the TWEETS filename: ")
    tweetFile = open("tweets.txt", "r", encoding="utf-8")

    for line in tweetFile:
        arr = line.split(",")
        #latitude is now index 0
        t = arr[0]
        latitude = float(t[1:])
        arr2 = arr[1].split("]")
        longitude = float(arr2[0])
        arr3 = line.split(' ', 5)
        tweet = arr3[5]

        # Calculate happiness score for each word in tweet
        for word in tweet.split():
                #Pacific
            if latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -125.242264 and longitude <= -115.236428:
                for i in keyWordsDictionary:
                    numKeyWords = 0
                    totalSentiment=0
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        numKeywords = numKeyWords+1
                        totalSentiment = totalSentiment+x
                        totalScore = numKeyWords/totalSentiment
                        print("Tweet:" , tweet, "happiness score:" , totalScore , "in Pacific Timezone")
             #Mountain
            elif latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -115.236428 and longitude <= -101.998892:
                for i in keyWordsDictionary:
                    numKeyWords = 0
                    totalSentiment=0
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        numKeywords = numKeyWords+1
                        totalSentiment = totalSentiment+x
                        totalScore = numKeyWords/totalSentiment
                        print("Tweet:" , tweet, "happiness score:" , totalScore , "in Mountain Timezone")

            #Central
            elif latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -101.998892 and longitude <= -87.518395:
                for i in keyWordsDictionary:
                    numKeyWords = 0
                    totalScore=0
                    totalSentiment = 0
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        numKeywords = numKeyWords+1
                        totalSentiment = totalSentiment+x
                        totalScore = numKeyWords/totalSentiment
                        print("Tweet:" , tweet, "happiness score:" , totalScore , "in Central Timezone")

            #Eastern
            elif latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -87.518395 and longitude <= -67.444574:
                for i in keyWordsDictionary:
                    numKeyWords = 0
                    totalScore=0
                    totalSentiment = 0
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        numKeywords = numKeyWords+1
                        totalSentiment = totalSentiment+x
                        totalScore = numKeyWords/totalSentiment
                        print("Tweet:" , tweet, "happiness score:" , totalScore , "in Eastern Timezone")

            else:
                print("Tweet:" ,tweet, "Tweet is outside of timezone")


        #word rep each word or "string" in that list
        for word in tweet.split():
            #Pacific
            if latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -125.242264 and longitude <= -115.236428:
                for i in keyWordsDictionary:
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        pacific = pacific + x
            #Mountain
            elif latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -115.236428 and longitude <= -101.998892:
                for i in keyWordsDictionary:
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        mountain = mountain + x
            #Central
            elif latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -101.998892 and longitude <= -87.518395:
                for i in keyWordsDictionary:
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        central = central + x

            #Eastern
            #elif latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -67.444574 and longitude <= -87.518395:
            elif latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -87.518395 and longitude <= -67.444574:
                for i in keyWordsDictionary:
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        eastern = eastern + x


    # Function to print happiness score for each timezone
    def printScore(timeZone):
        if timeZone == pacific:
            print("The total happiness score for Pacific timezone is:", pacific)
        if timeZone == mountain:
            print("The total happiness score for Mountain timezone is:", mountain)
        if timeZone == central:
            print("The total happiness score for Central timezone is:", central)
        if timeZone == eastern:
            print("The total happiness score for eastern timezone is:", eastern)

    print (" ")
    print(" ")

    # Print happiness scores for each timezone
    printScore(pacific)
    printScore(mountain)
    printScore(central)
    printScore(eastern)
    print(count)
    print("")
    print("Therefore, the happiest timezone is eastern, with score of" , eastern)

    # Prompt the user to press Enter before exiting
    input("Press Enter to exit...")



## Handle key error: ignoring tweets with no keywords
except KeyError:
    print("Error: no keywords are found/ not in time zone")



keyFile.close()
tweetFile.close()



