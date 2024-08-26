import random
import copy
cards = ["red heart 2", "red heart 3", "red heart 4", "red heart 5", "red heart 6 ", "red heart 7", "red heart 8", "red heart 9", "red heart 10", "red heart jack", "red heart queen", "red heart king", "red heart ace", "red diamond 2", "red diamond 3", "red diamond 4", "red diamond 5", "red diamond 6 ", "red diamond 7", "red diamond 8", "red diamond 9", "red diamond 10", "red diamond jack", "red diamond queen", "red diamond king", "red diamond ace", "black club 2", "black club 3", "black club 4", "black club 5", "black club 6 ", "black club 7", "black club 8", "black club 9", "black club 10", "black club jack", "black club queen", "black club king", "black club ace", "black spade 2", "black spade 3", "black spade 4", "black spade 5", "black spade 6 ", "black spade 7", "black spade 8", "black spade 9", "black spade 10", "black spade jack", "black spade queen", "black spade king", "black spade ace"]
cardvalue = [2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10, 10, 10, 10, 11, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10, 10, 10, 10, 11, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10, 10, 10, 10, 11, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10, 10, 10, 10, 11]
#above are just the set default 52 card decks
wins = 0
loses = 0
class blackjack:
  def __init__(self):        #construtors
    self.cardstemp = copy.deepcopy(cards)
    self.cardvaluetemp = copy.deepcopy(cardvalue)
    self.wins1 = wins
    self.loses1 = loses


    #RESETY THE CLASS 
  def shuffle(self):     #re instanciates the arrays (sets back to default value, aka shuffling)
    self.cardstemp = copy.deepcopy(cards)    #MUST USE DEEP/SHALLOW(dosent matter) COPY AS THE ORIGINAL GETS AFFECTED SOMEHOW
    self.cardvaluetemp = copy.deepcopy(cardvalue )
  def play(self):  
    win = 0
    a = len(self.cardstemp)
    b = len(cards)
    print("cards left in deck %s" %(str(a)))
    print("cards left in deck DEFAULT %s" %(str(b)))
    dcard1 = random.randint(0, len(self.cardstemp)-1)   #sets dealer cards
    dname1 = self.cardstemp[dcard1]
    dvalue1 = self.cardvaluetemp[dcard1]
    self.cardvaluetemp.pop(dcard1)        #pop in order to make sure the same card does not 
    self.cardstemp.pop(dcard1)
    dcard2 = random.randint(0, len(self.cardstemp)-1)
    dname2 = self.cardstemp[dcard2]
    dvalue2 = self.cardvaluetemp[dcard2]
    self.cardvaluetemp.pop(dcard2)
    self.cardstemp.pop(dcard2)
    card1 = random.randint(0, len(self.cardstemp)-1)   #sets player cards (random value within length of current card deck)
    name1 = self.cardstemp[card1]
    value1 = self.cardvaluetemp[card1]
    self.cardstemp.pop(card1)            #pops so same 2 cards cannot be drawn unless next round you "shuffle"
    self.cardvaluetemp.pop(card1)  
    card2 = random.randint(0, len(self.cardstemp)-1)      
    name2 = self.cardstemp[card2]
    value2 = self.cardvaluetemp[card2]
    self.cardstemp.pop(card2)
    self.cardvaluetemp.pop(card2)
    print("flipped card of dealer is " + dname1)
    print("your cards are %s and %s" %(name1, name2))
    dsum = dvalue1 + dvalue2
    psum = value1 + value2
    if value1 == 11 and value2 == 11 and psum > 21:     #in case of 2 aces to start
      value1 == 1
      psum = value1 + value2
    if psum != 21:  
          ask = input("press 1 to hit and 2 to stay")
          values = [value1, value2]    #set value array to keep trak in order to ace convert accurately
          while ask == "1": 
                tcard1 = random.randint(0, len(self.cardstemp)-1)      #temp card to get new one
                tname = self.cardstemp[tcard1]
                tvalue = self.cardvaluetemp[tcard1]
                psum += tvalue
                self.cardstemp.pop(tcard1)
                self.cardvaluetemp.pop(tcard1)
                print("your new card is " + tname)
                values.append(tvalue)
                if psum > 21:               #ace conversion in case over 21 with default ace value(11)
                  for i in range(len(values)):
                    if values[i] == 11:
                      values[i] = 1
                      psum = 0
                      for i in range(len(values)):
                        psum += values[i]
                    if psum <= 21:
                      break
                print("current value is " + str(psum))
                if psum > 21:
                  print("you bust")
                  win = 0
                  break
                ask = input("press 1 to hit and 2 to stay")
          print("dealers cards are %s and %s" %(dname1, dname2))
          print("your total is " + str(psum))
          values = [dvalue1, dvalue2] #set value array(with dealer values) to keep track in order to ace convert accurately
          if dvalue1 == 11 and dvalue2 == 11 and dsum > 21:     #in case of 2 aces to start
             dvalue1 == 1
             dsum = dvalue1 + dvalue2
          while dsum < 17:          #dealer must hit below 17
            tcard1 = random.randint(0, len(self.cardstemp)-1)
            tname = self.cardstemp[tcard1]
            tvalue = self.cardvaluetemp[tcard1]
            dsum += tvalue
            self.cardvaluetemp.pop(tcard1)
            self.cardstemp.pop(tcard1)
            print("dealer new card is " + tname)
            values.append(tvalue)
            if dsum > 21:  #dealer ace conversion in case of over 21          
              for i in range(len(values)):
               if values[i] == 11:
                  values[i] = 1
                  dsum = 0
                  for i in range(len(values)):
                    dsum += values[i]
               if dsum <= 21:
                  break
              if dsum > 21:
                print("dealer bust")
                if psum > 21:
                    print("draw!")
                    win = 2
                    break
                else:
                    print("you win!")
                    win = 1
                    break
            print("dealer total is " + str(dsum))
          print("dealer total is " + str(dsum))
          if dsum <= 21:       #checks if without a bust, then checks to see who wins   
            if psum <= 21:
              if dsum == psum:
                print("draw")
                win = 2
              if dsum > psum:
                win = 0
                print("you lose")
              if psum > dsum:
                win = 1
                print("you win")
    else:
      print("blackjack! you win")    
      win = 1   #blackjack is default victory
    if win == 1:
      self.wins1 += 1
    if win == 0:
      self.loses1 += 1
    print("wins: " + str(self.wins1))    #prints wins and loses and winrate percent
    print("loses: " + str(self.loses1))
    sum = self.loses1 + self.wins1
    if self.loses1 != 0:
      print("winrate percentage: " + str(float((self.wins1/sum)*100)) )
    else:
      print("winrate percentage: 100")
     
play = True
playask = input("1 to play 2 to stop")
black = blackjack()  
if playask == "1":
  play = True
else:
  play = False
while play == True:
  shuffleask = input("1 to shuffle 2 to not (cannot do this forever)")     
  if shuffleask == "1":
    black.shuffle()

  black.play()
  print("--------------------------------------------------------------------------------------------")
  playask = input("1 to play 2 to stop") #asks if you want to continue playing, can play in a constant loop
  
  if playask == "1":
     play = True
  else:
     play = False
