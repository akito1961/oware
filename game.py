def int_to_text(num:int) -> str:
    if num < 10:
        return " " + str(num)
    else:
        return str(num)
    
def binCheck(input, list):
    if input in list:
        return list.index(input)

def oware():
    playing = True
    
    option = ["a", "b", "c", "d", "e", "f"]
    
    bin = [4,4,4,4,4,4,
           4,4,4,4,4,4]
    
    playerOne = True
    
    messageCode = 0
    
    playerOneScore = 0
    playerTwoScore = 0
    
    while playing:
        
        ## error message
        if messageCode == -1:
            print("\nEmpty bin was chosen. Try again.")
        if messageCode == -2:
            print("\nInvalid input. Try again.")
        if messageCode == -3:
            print("\nThere are the move allowing opponent to continue. Try again.")
        
        # Score Tracking
        print("")
        print(f"Player One : {playerOneScore}, Player Two : {playerTwoScore}")
        # beginning message    
        if playerOne:
            message = "Player One's Turn ...."
        else:
            message = "Player Two's Turn ...."
        
        print("\n" + message + "\n") 
        
        # show the board
        if not playerOne:
            print("   f    e    d    c    b    a")
        print("+----+----+----+----+----+----+")
        print("| "+ int_to_text(bin[11]) +" | "+ int_to_text(bin[10]) +" | "+ int_to_text(bin[9]) +
              " | "+ int_to_text(bin[8]) +" | "+ int_to_text(bin[7]) +" | "+ int_to_text(bin[6]) +" |")
        print("+----+----+----+----+----+----+")
        print("| "+ int_to_text(bin[0]) +" | "+ int_to_text(bin[1]) +" | "+ int_to_text(bin[2]) +
              " | "+ int_to_text(bin[3]) +" | "+ int_to_text(bin[4]) +" | "+ int_to_text(bin[5]) +" |")
        print("+----+----+----+----+----+----+")
        
        if playerOne:
            print("   a    b    c    d    e    f")
        print("")
        
        # get user input phase
        userInput = input("Enter sth: ")
        messageCode = 0 ## reset error status
        

        # bin detector
        if userInput == "q":
            playing = False
            chosenBin = 0
        elif playerOne and userInput in option:
            chosenBin = binCheck(userInput, option)
        elif not playerOne and userInput in option:
            chosenBin = binCheck(userInput, option) + 6
        else:
            chosenBin = -2
            messageCode = -2
        print(chosenBin)
        
        # give opponent a chance rule
        if chosenBin >= 0:
            if playerOne and ((bin[chosenBin] + chosenBin) % 12 in list(range(0,6))) and (bin[6:] == [0 for i in range(6)]):
                messageCode = -3
            if (not playerOne) and ((bin[chosenBin] + chosenBin) % 12 in list(range(6,12))) and (bin[:6] == [0 for i in range(6)]):
                messageCode = -3

        # clearing stone from the selected bin
        if chosenBin >= 0 and messageCode >= 0:
            giveawayPile = bin[chosenBin]
            bin[chosenBin] = 0
            
            ## emypty bin checking
            if giveawayPile <= 0:
                messageCode = -1
        
            # distributing the stone
            recipient = (chosenBin + 1) % 12
            while giveawayPile > 0:
                if recipient == chosenBin: ## skip the chosen bin rule
                    recipient = (recipient + 1) % 12
                bin[recipient] += 1
                giveawayPile -= 1
                recipient = (recipient + 1) % 12
            
        # Capturing phase eaaffcdffbade/edbbfecfccaaacbeffbddffeafbaabebfcddeebf/aceffddeaf
        if messageCode >= 0:
            binIndex = (recipient - 1) % 12
            while bin[binIndex] in [2,3]:
                if playerOne and (binIndex >= 6):
                    playerOneScore += bin[binIndex]
                elif (not playerOne) and (binIndex < 6):
                    playerTwoScore += bin[binIndex]
                
                if (playerOne and (binIndex >= 6)) or ((not playerOne) and (binIndex < 6)):
                    bin[binIndex] = 0
                binIndex -= 1
                
            ## Switching player's turn
            playerOne = not(playerOne)

        print("\n-----------------------------")
        
    
    # end of the game
    
if __name__:
    oware()