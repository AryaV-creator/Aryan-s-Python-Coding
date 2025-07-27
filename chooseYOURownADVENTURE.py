"""This program gives the user 5 different decisions. They then pick one option, and that directs them to other options.
I commented the original options as the rest repeat. I used nested ifs to program this 'choose your own adventure'

Author: Aryan Vemulapalli
Class: ICS3UC
Date : 04/10/2024
"""
print("Hello! Welcome to choose your own adventure")
start=input("Type play to start the game: ")#Take input to start the game
if start=="play":#use if to determine the answer, else it won't start
    print("You are about to recite a valedictorian speech in front of hundreds of people but you are nervous")
    #Start crying or act confident?
    cryORconfident=input("\033[1m"+"Do you start crying on stage A or do you fake it till you make it and act confident B?: "+"\033[1m")
    if cryORconfident=="A":
        print("A teacher comes on the stage and tells you that you don't have to speak if you don't want to, but you do want to speak")
        #Wipe tears and recite speech or cry to your family
        reciteORcry=input("\033[1m"+"Do you wipe your tears and tell the teacher that you will recite the speech A or will you go crying to your family in the stands B?: "+"\033[1m")
        if reciteORcry=="A":
            print("The teacher smiles and says into the microphone, from the top!")
            
            #Brush off tears with joke or stutter the whole time
            tearsORexplain=input("\033[1m"+"Do you brush off your tears with a joke and continue your speech A or do you spend the whole time stuttering and explaining why you started crying B: "+"\033[1m")
            if tearsORexplain=="A":
                print("The audience loves your speech and everyone claps at the end")
                
                #accept mystery prize or $100
                mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                if mysteryORhundred=="A":
                    print("The prize is $500")
                    
                    #Invest in stocks or eat panda express
                    investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                    if investORfood=="A":
                        print("The stock goes so high you become a billionaire!!!!")
                        
                        #Story ends!
                        print("That is the end of the story! I hope you enjoyed:)")
                        print("Thank you for playing")
                        print("  ^    ^     /")
                        print("<( ' ; ' )> /")
                        print("(         )/")
                        print()
                        
                        #Rank how much you liked the story
                        ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                        if int(ranking)>7:
                            print("I'm glad you enjoyed it")
                            
                        elif int(ranking)<7:
                            print("Better luck next time")
                            
                            
                    #Your story is done
                    elif investORfood=="B":
                        print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                        print("That is the end of the story! I hope you enjoyed:)")
                        print("Thank you for playing")
                        print("  ^    ^     /")
                        print("<( ' ; ' )> /")
                        print("(         )/")
                        print()
                        ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                        
                        if int(ranking)>7:
                            print("I'm glad you enjoyed it")
                            
                        elif int(ranking)<7:
                            print("Better luck next time")
                            
                            
                #You choose the other option and continue the story
                elif mysteryORhundred=="B":
                    print("You end up getting motivated by the money and join a bunch of speech competitions")
                    optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                    if optionMYSTERY=="yes":
                        print("The prize is $500")
                        investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                        if investORfood=="A":
                            print("The stock goes so high you become a billionaire!!!!")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                                
                            elif int(ranking)<7:
                                print("Better luck next time")
                                
                        elif investORfood=="B":
                            print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                                
                            elif int(ranking)<7:
                                print("Better luck next time")
                                
                        
                    elif optionMYSTERY=="no":               
                        print("Thank you for playing")
                        print("  ^    ^     /")
                        print("<( ' ; ' )> /")
                        print("(         )/")
            elif tearsORexplain=="B":
                print("The audience dwells on your mistakes and the speech doesn't go well, but you are still passionate about improving and don't lose interest in public speaking.")
                optionTEARS=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                if optionTEARS=="yes":
                    print("The audience loves your speech and everyone claps at the end")
                    mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                    if mysteryORhundred=="A":
                        print("The prize is $500")
                        investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                        if investORfood=="A":
                            print("The stock goes so high you become a billionaire!!!!")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                            
                            elif int(ranking)<7:
                                print("Better luck next time")
                        elif investORfood=="B":
                            print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                                
                            elif int(ranking)<7:
                                print("Better luck next time")

                    elif mysteryORhundred=="B":
                        print("You end up getting motivated by the money and join a bunch of speech competitions")
                        optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                        if optionMYSTERY=="yes":
                            print("The prize is $500")
                            investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                            if investORfood=="A":
                                print("The stock goes so high you become a billionaire!!!!")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                    
                                elif int(ranking)<7:
                                    print("Better luck next time")
                                    
                            elif investORfood=="B":
                                print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                print()
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                    
                                elif int(ranking)<7:
                                    print("Better luck next time")
                                    
                            
                        elif optionMYSTERY=="no":               
                            print("\033[1m"+"Thank you for playing"+"\033[1m")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                elif optionTEARS=="no":
                    print("\033[1m"+"Thank you for playing"+"\033[1m")
                    print("  ^    ^     /")
                    print("<( ' ; ' )> /")
                    print("(         )/")

        elif reciteORcry=="B":
            print("Your parents tell you to get back on stage and you complete the speech. Your family is proud")
            optionSPEECH=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
            if optionSPEECH=="yes":
                print("The teacher smiles and says into the microphone, from the top!")
                tearsORexplain=input("\033[1m"+"Do you brush off your tears with a joke and continue your speech A or do you spend the whole time stuttering and explaining why you started crying B: "+"\033[1m")
                if tearsORexplain=="A":
                    print("The audience loves your speech and everyone claps at the end")
                    mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                    if mysteryORhundred=="A":
                        print("The prize is $500")
                        investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                        if investORfood=="A":
                            print("The stock goes so high you become a billionaire!!!!")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                                    
                            elif int(ranking)<7:
                                print("Better luck next time")
                        elif investORfood=="B":
                            print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                                
                            elif int(ranking)<7:
                                print("Better luck next time")
                    elif mysteryORhundred=="B":
                        
                        print("You end up getting motivated by the money and join a bunch of speech competitions")
                        optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                        if optionMYSTERY=="yes":
                            print("The prize is $500")
                            investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                            if investORfood=="A":
                                print("The stock goes so high you become a billionaire!!!!")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                    
                                elif int(ranking)<7:
                                    print("Better luck next time")
                            elif investORfood=="B":
                                print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                print()
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                
                                elif int(ranking)<7:
                                    print("Better luck next time")
                elif tearsORexplain=="B":
                    print("The audience dwells on your mistakes and the speech doesn't go well, but you are still passionate about improving and don't lose interest in public speaking.")
                    optionTEARS=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                    if optionTEARS=="yes":
                        print("The audience loves your speech and everyone claps at the end")
                        mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                        if mysteryORhundred=="A":
                            print("The prize is $500")
                            investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                            if investORfood=="A":
                                print("The stock goes so high you become a billionaire!!!!")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                print()
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                            
                                elif int(ranking)<7:
                                    print("Better luck next time")
                            elif investORfood=="B":
                                print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                print()
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                
                                elif int(ranking)<7:
                                    print("Better luck next time")

                        elif mysteryORhundred=="B":
                            print("You end up getting motivated by the money and join a bunch of speech competitions")
                            optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                            if optionMYSTERY=="yes":
                                print("The prize is $500")
                                investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                                if investORfood=="A":
                                    print("The stock goes so high you become a billionaire!!!!")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                    
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                elif investORfood=="B":
                                    print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                
                                    elif int(ranking)<7:
                                        print("Better luck next time")

            elif optionSPEECH=="no":
                print("Thank you for playing")
                print("  ^    ^     /")
                print("<( ' ; ' )> /")
                print("(         )/")
                print()
    elif cryORconfident=="B":
        print("The crowd loves you and your speech is a hit! Your teacher writes you an amazing recommendation letter for your strength in public speaking for a speech contest")
        optionCRY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
        if optionCRY=="yes":
            print("A teacher comes on the stage and tells you that you don't have to speak if you don't want to, but you do want to speak")
            reciteORcry=input("\033[1m"+"Do you wipe your tears and tell the teacher that you will recite the speech A or will you go crying to your family in the stands B?: "+"\033[1m")
            if reciteORcry=="A":
                print("The teacher smiles and says into the microphone, from the top!")
                tearsORexplain=input("\033[1m"+"Do you brush off your tears with a joke and continue your speech A or do you spend the whole time stuttering and explaining why you started crying B: "+"\033[1m")
                if tearsORexplain=="A":
                    print("The audience loves your speech and everyone claps at the end")
                    mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                    if mysteryORhundred=="A":
                        print("The prize is $500")
                        investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                        if investORfood=="A":
                            print("The stock goes so high you become a billionaire!!!!")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                                
                            elif int(ranking)<7:
                                print("Better luck next time")
                        
                        elif investORfood=="B":
                            print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                            print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                            print("Thank you for playing")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                            print()
                            ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                            if int(ranking)>7:
                                print("I'm glad you enjoyed it")
                                
                            elif int(ranking)<7:
                                print("Better luck next time")

                            
                    elif mysteryORhundred=="B":
                            print("You end up getting motivated by the money and join a bunch of speech competitions")
                            optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                            if optionMYSTERY=="yes":
                                print("The prize is $500")
                                investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                                if investORfood=="A":
                                    print("The stock goes so high you become a billionaire!!!!")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                        
                                elif investORfood=="B":
                                    print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                        
                                
                            elif optionMYSTERY=="no":
                                print("\033[1m"+"Thank you for playing"+"\033[1m")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                elif tearsORexplain=="B":
                    print("The audience dwells on your mistakes and the speech doesn't go well, but you are still passionate about improving and don't lose interest in public speaking.")
                    optionTEARS=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                    if optionTEARS=="yes":
                        print("The audience loves your speech and everyone claps at the end")
                        mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                        if mysteryORhundred=="A":
                            print("The prize is $500")
                            investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                            if investORfood=="A":
                                print("The stock goes so high you become a billionaire!!!!")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                print()
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                    
                                elif int(ranking)<7:
                                    print("Better luck next time")
                            elif investORfood=="B":
                                    print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                        elif mysteryORhundred=="B":
                            print("You end up getting motivated by the money and join a bunch of speech competitions")
                            optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                            if optionMYSTERY=="yes":
                                print("The prize is $500")
                                investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                                if investORfood=="A":
                                    print("The stock goes so high you become a billionaire!!!!")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                        
                                elif investORfood=="B":
                                    print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                        
                                
                            elif optionMYSTERY=="no":               
                                print("\033[1m"+"Thank you for playing"+"\033[1m")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                    elif optionTEARS=="no":
                        print("\033[1m"+"Thank you for playing"+"\033[1m")
                        print("  ^    ^     /")
                        print("<( ' ; ' )> /")
                        print("(         )/")
            elif reciteORcry=="B":
                print("Your parents tell you to get back on stage and you complete the speech. Your family is proud")
                optionSPEECH=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                if optionSPEECH=="yes":
                    print("The teacher smiles and says into the microphone, from the top!")
                    tearsORexplain=input("\033[1m"+"Do you brush off your tears with a joke and continue your speech A or do you spend the whole time stuttering and explaining why you started crying B: "+"\033[1m")
                    if tearsORexplain=="A":
                        print("The audience loves your speech and everyone claps at the end")
                        mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                        if mysteryORhundred=="A":
                            print("The prize is $500")
                            investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                            if investORfood=="A":
                                print("The stock goes so high you become a billionaire!!!!")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                print()
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                    
                                elif int(ranking)<7:
                                    print("Better luck next time")
                            elif investORfood=="B":
                                print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                print("Thank you for playing")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                                print()
                                ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                if int(ranking)>7:
                                    print("I'm glad you enjoyed it")
                                
                                elif int(ranking)<7:
                                    print("Better luck next time")
                                    
                        elif mysteryORhundred=="B":
                            print("You end up getting motivated by the money and join a bunch of speech competitions")
                            optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                            if optionMYSTERY=="yes":
                                print("The prize is $500")
                                investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                                if investORfood=="A":
                                    print("The stock goes so high you become a billionaire!!!!")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                        
                                elif investORfood=="B":
                                    print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                        

                            elif optionMYSTERY=="no":               
                                print("\033[1m"+"Thank you for playing"+"\033[1m")
                                print("  ^    ^     /")
                                print("<( ' ; ' )> /")
                                print("(         )/")
                    elif tearsORexplain=="B":
                        print("The audience dwells on your mistakes and the speech doesn't go well, but you are still passionate about improving and don't lose interest in public speaking.")                    
                        optionTEARS=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                        if optionTEARS=="yes":
                            print("The audience loves your speech and everyone claps at the end")
                            mysteryORhundred=input("\033[1m"+"Do you accept a mystery prize for your speech from the principle A or get $100 from your parents B: "+"\033[1m")
                            if mysteryORhundred=="A":
                                print("The prize is $500")
                                investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                                if investORfood=="A":
                                    print("The stock goes so high you become a billionaire!!!!")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")
                                elif investORfood=="B":
                                    print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                    print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                    print("Thank you for playing")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                                    print()
                                    ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                    if int(ranking)>7:
                                        print("I'm glad you enjoyed it")
                                        
                                    elif int(ranking)<7:
                                        print("Better luck next time")        
                            elif mysteryORhundred=="B":
                                print("You end up getting motivated by the money and join a bunch of speech competitions")
                                optionMYSTERY=input("\033[1m"+"That is the end for this option, but answer with yes if you would like to select A in order to continue the story and no if you want to stop: "+"\033[1m")
                                if optionMYSTERY=="yes":
                                    print("The prize is $500")
                                    investORfood=input("\033[1m"+"Do you go home and invest the money in stocks A or do you spend it on a big panda express meal B: "+"\033[1m")
                                    if investORfood=="A":
                                        print("The stock goes so high you become a billionaire!!!!")
                                        print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                        print("Thank you for playing")
                                        print("  ^    ^     /")
                                        print("<( ' ; ' )> /")
                                        print("(         )/")
                                        print()
                                        ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                        if int(ranking)>7:
                                            print("I'm glad you enjoyed it")
                                            
                                        elif int(ranking)<7:
                                            print("Better luck next time")
                                            
                                    elif investORfood=="B":
                                        print("You lost all the money but get a job to earn more! Also you apply for public speaking scholarships")
                                        print("\033[1m"+"That is the end of the story! I hope you enjoyed:)"+"\033[1m")
                                        print("Thank you for playing")
                                        print("  ^    ^     /")
                                        print("<( ' ; ' )> /")
                                        print("(         )/")
                                        print()
                                        ranking=input("\033[1m"+"On a scale of 1-10, how much did you like the game?: "+"\033[1m")
                                        if int(ranking)>7:
                                            print("I'm glad you enjoyed it")
                                            
                                        elif int(ranking)<7:
                                            print("Better luck next time")
                                            

                                elif optionMYSTERY=="no":               
                                    print("\033[1m"+"Thank you for playing"+"\033[1m")
                                    print("  ^    ^     /")
                                    print("<( ' ; ' )> /")
                                    print("(         )/")
                        elif optionTEARS=="no":
                            print("\033[1m"+"Thank you for playing"+"\033[1m")
                            print("  ^    ^     /")
                            print("<( ' ; ' )> /")
                            print("(         )/")
                    elif optionSPEECH=="no":
                        print("\033[1m"+"Thank you for playing"+"\033[1m")
                        print("  ^    ^     /")
                        print("<( ' ; ' )> /")
                        print("(         )/")
                        
                    
            elif optionCRY=="no":
                print("\033[1m"+"Thank you for playing"+"\033[1m")
                print("  ^    ^     /")
                print("<( ' ; ' )> /")
                print("(         )/")
#This final else statement is just a precausion if someone doesn't enter play properly
else:
    print("\033[1m"+"You did not enter play, refresh the game and enter play to begin playing!"+"\033[1m")
    
