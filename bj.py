import random
#Program to Simulate a BlackJack Game

#Class for a given deck of standard playing cards
class Deck(object):
	#Creates deck of cards [is in deck, card [a,b]]
	#ex. [1,[A,H]]
	numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	suits = ['S','H','C','D']
	deck = []
	for num in numbers:
		for suit in suits:
			deck.append([1,[num,suit]])
	#row by row prints which cards are in deck
	def display(self):
		for card in self.deck:
			print card
	#returns a random card, and removes it from deck
	def deal(self,pint=0):
		#finds number of remaining cards
		card_number = 0
		for card in self.deck:
			if card[0] ==1:
				card_number+=1
		dealt_card_num = random.SystemRandom().randint(0,card_number-1) #SystemRandom used for best random
		if pint != 0:
			print self.deck[dealt_card_num][1]
		return self.deck[dealt_card_num][1]
	#returns all cards to deck
	def refresh(self):
		for i in range(52):
			self.deck[i][0] = 1
class Hand(object):
	def __init__(self):
		self.low = False #the ace currently counts as 11
		self.cards = [] #list which holds the cards
		self.card_vals = {   #tells the numeric value of the given card
						'2': 2,'3': 3,'4': 4,
						'5': 5,'6': 6,'7':7,
						'8': 8,'9': 9,'10': 10,
						'J': 10,'Q': 10,'K': 10,'A': 11
							}
	def lowAce(self): #makes the ace count as 1
		self.card_vals['A'] = 1
		self.low = True
	def addCards(self,number,deck,pint=0): #removes random card from given deck adds to hand
		for i in range(number):
			self.cards.append(deck.deal(pint))
	def value(self): #compares to card_vals dict to find total value of given hand
		sum = 0
		for card in self.cards:
			sum += self.card_vals[card[0]]
		return sum
	def display(self): #shows all cards in the hand
		for card in self.cards:
			print card
	def number(self):
		return len(self.cards)
def printGame(dealer_hand, player_hand,num=0): #prints both hands as in poker game
	print "Dealer Cards:"
	if num != 0: #prints only one card when num is 1
		print dealer_hand.cards[num-1]
		print "['?','?']"
	else:
		for card in dealer_hand.cards: #prints all cards if empty
			print card
	print "Dealer Value:"
	print dealer_hand.value()
	print "Your Cards:" #prints players cards
	for card in player_hand.cards:
		print card
	print "Player Value:"
	print player_hand.value()
	print ""
def play_blackjack(deck): #runs the blackjack game w/ a given deck
	end_responses = {
					'bj': 'You got blackjack! Payout- 3:2',
					'win': 'You beat the dealer! Payout- 1:1',
					'dbust': 'The dealer busted! Payout- 1:1',
					'tie': 'You matched the dealer. Payout- Push',
					'bust': "You busted. Payout- None",
					'lost': "The dealer beat you. Payout - None"

	}
	#initalizes the two hands
	dealer_cards = Hand()
	player_cards = Hand()
	#deals cards from deck to players
	dealer_cards.addCards(2,deck)
	player_cards.addCards(2,deck)
	#prints the state of the game which the player can know
	game = True #creates game loop which continues until game is finished
	card_value = 0
	response = ''
	run = True
	end = ''
	while run == True:
		#prints the game state
		printGame(dealer_cards,player_cards,1)
		#gets user decision
		response =  raw_input("Hit or Stand? (h/s):  ")
		while response != 'h' and response != 's': #loops until response is of correct format
			response =  raw_input("Try Again, Hit or Stand? (h/s):  ")
		if response == 'h': #hit draws another card and adds to deck
			player_cards.addCards(1,deck)
			printGame(dealer_cards,player_cards,1)
		elif response == 's': #standing ends the run
			run = False
		if player_cards.value() > 21 and player_cards.low is False: #the value of the ace is changed when hand >21
			player_cards.lowAce()
		if player_cards.value() > 21: #if still > 21 after making aces worth 1, then the run ends
			run = False
	if response == 'h': #end game from a hit
		if player_cards.value() > 21: #exceeding 21 points, a bust
			printGame(dealer_cards,player_cards)
			end = 'bust'
	if response == 's': #end game from a stand
		print "Dealer's Turn:" #dealer begins hitting 
		print ""
		printGame(dealer_cards,player_cards)
		while dealer_cards.value() < 17: #dealer stops on any 17
			raw_input("Press Enter to Continue...") #slows dealers move for user comprehension
			dealer_cards.addCards(1,deck) #draws dealer card
			if dealer_cards.value() > 21:
				dealer_cards.lowAce()
			printGame(dealer_cards,player_cards)
	raw_input("Press Enter to Continue...")
	#Begins print out of end game
	print ""
	print "Dealer Final Card Value: %d" %(dealer_cards.value())
	print "Your Final Card Value: %d" %(player_cards.value())
	print end
	print player_cards.number()
	#judges the specific end game
	if player_cards.value() == 21 and player_cards.number() == 2 and (dealer_cards.value != 21 or dealer_cards.number() != 2):
		end = 'bj'
	elif end == 'bust':
		end = 'bust'
	elif player_cards.value() > dealer_cards.value():
		end = 'win'
	elif dealer_cards.value() > 21:
		end = 'dbust'
	elif player_cards.value() == dealer_cards.value():
		end = 'tie'
	elif player_cards.value() < dealer_cards.value():
		end = 'lost'
	print ""
	print ""
	print end
	print end_responses[end]
my_deck = Deck()
play_blackjack(my_deck)