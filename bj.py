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
		self.low = False
		self.cards = []
		self.card_vals = {'2' : 2,'3' : 3,'4' : 4,'5' : 5,'6' : 6,'7' :7,'8' : 8,'9' : 9,'10' : 10,'J' : 10,'Q' : 10,'K' : 10,'A' : 11}
	def lowAce(self):
		self.card_vals['A'] = 1
		self.low = True
	def addCards(self,number,deck,pint=0):
		for i in range(number):
			self.cards.append(deck.deal(pint))
	def length(self):
		return length(cards)
	def value(self):
		sum = 0
		for card in self.cards:
			sum += self.card_vals[card[0]]
		return sum
	def display(self):
		for card in self.cards:
			print card
def printGame(dealer_hand, player_hand,num=0):
	print "Dealer Cards:"
	if num != 0:
		print dealer_hand.cards[num-1]
	else:
		for card in dealer_hand.cards:
			print card
	print "Your Cards:"
	for card in player_hand.cards:
		print card
	print "Total Value:"
	print player_hand.value()
def play_blackjack(deck):
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
	while run == True:
		#prints the game state
		printGame(dealer_cards,player_cards,1)
		#gets user decision
		response =  raw_input("Hit or Stand? (h/s):  ")
		while response != 'h' and response != 's':
			response =  raw_input("Try Again, Hit or Stand? (h/s):  ")
		if response == 'h':
			player_cards.addCards(1,deck)
			printGame(dealer_cards,player_cards,1)
		elif response == 's':
			run = False
		if player_cards.value() > 21 and player_cards.low == False:
			player_cards.lowAce()
		if player_cards.value() > 21:
			run = False
	if response == 'h':
		if player_cards.value() > 21:
			printGame(dealer_cards,player_cards)
			print "BUST! You lost."
			game = False
		elif player_cards.value() == 21:
			printGame(dealer_cards,player_cards)
			print " Blackjack! You've won 3:2!"
			game = False
	if response == 's':
		print "Dealer's Turn:"
		print ""
		dealer_cards.display()
		while dealer_cards.value() < 17:
			raw_input("Press Enter to Continue...")
			dealer_cards.addCards(1,deck,1)
			printGame(dealer_cards,player_cards)
		print "Dealer Final Card Value: %d" %(dealer_cards.value())
		print "Your Final Card Value: %d" %(player_cards.value())
		if dealer_cards.value() > 21:
			print "Dealer busts, you win 2:1"
		elif player_cards.value() == dealer_cards.value():
			print "You receive your original bet!"
		elif player_cards.value() > dealer_cards.value():
			print"You win! Pay is 2:1"
		else:
			print"You've lost your original bet"

my_deck = Deck()
play_blackjack(my_deck)
#my_cards = Hand()
#my_cards.addCards(2,my_deck)
#print my_cards.value()