#This program is used to calculate the happiness score from different timezones


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




    keyFileName = input("Enter the keyword filename")
    #Needed in python in order to avoid encoding errors
    keyFile = open("keywords.txt", "r", encoding="utf-8")
    #emptyDictionary.split(value)

    #for each line in the key file
    for line in keyFile:
    #In this situation it will be broken up into two parts: index 1 and 2, between the commas and it will be put into a list
    #split returns a list of all the words in a string
    #Splitting a string is taking a string and splitting it into two or more parts
        arr = line.split(",")
    #Create the dictionary. so everytime it is index 0, join with index 1 and forget the "/n" (next line) by stripping it
    #Strip will return a copy of the string, with the changes made
    #returns elements of the list 'arr' connected by an empty string
        keyWordsDictionary[arr[0]] = "".join(arr[1].strip("\n"))
    #Dictionary is formed here
    #emptyDictionary.items() returns a list of dictionary (key,value)
    #the .items() creates the dictionary for you

    for key, value in keyWordsDictionary.items():
        #for the dictionary, every index must be recognized as the key and the value must be recognized as an integer
        #access the key, in keyWordsDictionary by typing in key but not searching for a string (no quotations)
            keyWordsDictionary[key] = int(value)
        #Loops until all the items in the list is formed into the dictionary


    # print(emptyDictionary)
    # print(emptyDictionary.get('love'))

    tweetFileName = input("Enter the tweet filename")
    tweetFile = open("tweets.txt", "r", encoding="utf-8")

    for line in tweetFile:
        arr = line.split(",")
        #latitude is now index 0
        t = arr[0]
        #Here you are defining the latitude
        #character from position 1 to the end of t= 'array 0' (in each line tweet) and the numbers will be a float
        latitude = float(t[1:])

        #from array 1, you split ']' which makes the longitude index 0 as well
        arr2 = arr[1].split("]")
        #the longitude is now called array 2 has index 0 and the numbers are a float
        longitude = float(arr2[0])


        # for l in tweetFile:
        #We split a tweet line into 3 parts, this is the 3rd
        #in array 3 we split the 5 white spaces
        arr3 = line.split(' ', 5)
        #tweet will represent us keeping whatever is left from the 5th white space
        tweet = arr3[5]
        #do a for loop for a single tweet here
        #word represents every word in the line
        for word in tweet.split():
                #Pacific
            if latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -125.242264 and longitude <= -115.236428:
                #for every index or 'key' in the keyWordsDictionary
                for i in keyWordsDictionary:
                    numKeyWords = 0
                    totalSentiment=0
                    if i == word:
                        #.get() will associate the key with the value in the dictionary. x is now representing the value
                        x = keyWordsDictionary.get(i)
                        numKeywords = numKeyWords+1
                        totalSentiment = totalSentiment+x
                        #print("numKeyWords:" , numKeyWords)
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
                # count = count + 1
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

        #tweets.split() returns a list with all the strings
        #word rep each word or "string" in that list
        for word in tweet.split():
                #Pacific
            if latitude <= 49.189787 and latitude >= 24.660845 and longitude >= -125.242264 and longitude <= -115.236428:
                #for every index or 'key' in the keyWordsDictionary
                for i in keyWordsDictionary:
                    #if i == word:
                    if i == word:
                        #.get() will associate the key with the value in the dictionary. x is now representing the value
                        x = keyWordsDictionary.get(i)
                        #happiness score will be added back to pacific
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
                # count = count + 1
                for i in keyWordsDictionary:
                    if i == word:
                        x = keyWordsDictionary.get(i)
                        eastern = eastern + x

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
    printScore(pacific)
    printScore(mountain)
    printScore(central)
    printScore(eastern)
    print(count)
    print("")
    print("Therefore, the happiest timezone is eastern, with score of" , eastern)





#ignoring tweets with no keywords
except KeyError:
    print("Error: no keywords are found/ not in time zone")



keyFile.close()
tweetFile.close()

         # print(arr[1])
        # print(line)


