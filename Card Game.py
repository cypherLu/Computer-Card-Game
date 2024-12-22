import random

def displayBanner():
   print("""
         ╭───────────────────────────╮
         │     Computer Software     │
         │         Card Game         │
         ╰───────────────────────────╯
          """)

#---------------------------------------------------------------------------------

score = 0
while True:   
	OS = ["Windows 10","Linux","MacOS","iOS","Android","MS DoS"]
	utilities = ["Anti-Virus Software","Firewall","Encryption Software","File Compression Software","Disk Defragmentation Software","Backup Software"]
	application = ["Word Processing Software","Presentation Software","Spreadsheet Software","Web Browser","Graphic Editing Software","Video Editing Software"]
	#put all three lists in only one list 'software'
	software = OS + utilities + application
	
	displayBanner()
	
	 #Let's pick a card from the deck!
	i=1
	points = 0
	cards = [ ]
	while i<=3:
		 i+=1
		 card = random.choice(software)
		 #add the three chosen cards to the 'cards' list
		 cards.append(card)
		 
	#check if the three chosen cards are from the same category, if so, the player scores 100 points
	if all(card in OS for card in cards):
			points+=100
			score+=100
	elif all(card in utilities for card in cards):
		points+=100
		score+=100
	elif all(card in application for card in cards):
		points+=100
		score+=100
		
	#check if either the first two cards or the last two cards are from the same category, if so, the player scores 30 points	
	elif all(card in OS for card in cards[:2]) and cards[2] not in OS:
		points+=30
		score+=30
	elif all(card in OS for card in cards[1:3]) and cards[0] not in OS:
		points+=30
		score+=30
	elif all(card in utilities for card in cards[:2]) and cards[2] not in utilities:
		points+=30
		score+=30
	elif all(card in utilities for card in cards[1:3]) and cards[0] not in utilities:
		points+=30
		score+=30
	elif all(card in application for card in cards[:2]) and cards[2] not in application:
		points+=30
		score+=30
	elif all(card in application for card in cards[1:3]) and cards[0] not in application:
		points+=30
		score+=30
	
	#check if the first card and the third card are from the same category and the card in the middle is from a different category, if so, the player scores 50 points
	elif cards[0] in OS and cards[2] in OS and cards[1] not in OS:
		points+=50
		score+=50
	elif cards[0] in utilities and cards[2] in utilities and cards[1] not in utilities:
		points+=50
		score+=50
	elif cards[0] in application and cards[2] in application and cards[1] not in application:
		points+=50
		score+=50	
	
	#output the chosen cards and its categories
	for card in cards:		
		if card in OS:
		   print(card + " is an example of Operating System.")
		elif card in utilities:
		   print(card + " is an example of Utility Software.")
		elif card in application:
		   print(card + " is an example of Application Software.")
			
	print("\nPoints:",points)
	print("Score:",score)

	PlayAgain = input("\n\nType any key for YES or 'N' for NO.\n\nCONTINUE? ").upper()
	if PlayAgain == "N":
		break
