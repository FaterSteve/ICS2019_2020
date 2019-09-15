#Importing everything
import time
import random
import sys

#Defining Variables
line_Count = 2
n=0
diff=2
score=2

#Defining non-ascii functions
def newpage(TxT):
	try:
		for x in range(0, ((int(full_Screen_Height))-(int(TxT)))):
			print('')
	except:
		for x in range(0, 99):
			print('')

def titlepage():
	newpage(0)
	text1()
	newpage(7)
	time.sleep(3)
	title()
	newpage(16)
	time.sleep(2.5)
	input("Press 'enter' to continue to the game.")
	
def gameStop():
	print('Ending Game')
	sys.exit(0)
#######################################################################################################################################################################

#Game Functions
def GameStart(n, score):
	newpage(0)
	scnd = int((2**(.5*n))-1)
	answer = random.randint(0,scnd)
	GamePlay(scnd, answer, n, score)
	
def GamePlay(scnd, answer, n, score):
	print('In a range of 0 to',scnd,'what is your guess for what the randomly selected integer is?')
	newpage(2)
	ans = input()
	if ans == 'reset':
		GameStart(0, score)
	if ans == 'end':
		gameStop()
	try:
		ans = int(ans)
		#print('Try passed')
	except:
		#print('Try failed')
		GamePlay(scnd, answer, n, score)
	if ans > answer:
		print('HI, try again!')
		newpage(2)
		time.sleep(1.5)
		GamePlay(scnd, answer, n, score)
	if ans < answer:
		print('LO, try again!')
		newpage(2)
		time.sleep(1.5)
		GamePlay(scnd, answer, n, score)
	if ans == answer:
		GameEnd(n, score)
	else:
		GamePlay(scnd, answer, n, score)
		
def GameEnd(n, score):
	print('HI-LO! You win!')
	newpage(2)
	time.sleep(1.5)
	score = int((score+(2**n-1))/2)
	print("Your score is now",score,"Please type by how much you would like to up the diffuculty.")
	diff = input()
	try:
		print("Your score is now",score,"Please type by how much you would like to up the diffuculty.")
		diff = int(diff)
		if diff<=0:
			print('You Wimp.')
		n = n+diff
		GameStart(n)
	except:
		if diff == "reset":
			GameStart(0, score)
		if diff == "end":
			gameStop()
		n = n+2
		GameStart(n, score)
		
#######################################################################################################################################################################
		
#Preping Ascii Text/images
def text1():
	print(''' ________        __    __________                   .___       ___________      __________.__
 /  _____/  _____/  |_  \\______   \\ ____ _____     __| _/__.__. \\__    ___/___   \\______   \\  | _____  ___.__.
/   \\  ____/ __ \\   __\\  |       _// __ \\\\__  \\   / __ <   |  |   |    | /  _ \\   |     ___/  | \\__  \\<   |  |
\\    \\_\\  \\  ___/|  |    |    |   \\  ___/ / __ \\_/ /_/ |\\___  |   |    |(  <_> )  |    |   |  |__/ __ \\\\___  |
 \\______  /\\___  >__|    |____|_  /\\___  >____  /\\____ |/ ____|   |____| \\____/   |____|   |____(____  / ____|
        \\/     \\/               \\/     \\/     \\/      \\/\\/                                           \\/\\/''')
        
def title():
	print("""    /$$   /$$ /$$$$$$         /$$        /$$$$$$
   | $$  | $$|_  $$_/        | $$       /$$__  $$
   | $$  | $$  | $$          | $$      | $$  \ $$
   | $$$$$$$$  | $$   /$$$$$$| $$      | $$  | $$
   | $$__  $$  | $$  |______/| $$      | $$  | $$
   | $$  | $$  | $$          | $$      | $$  | $$
   | $$  | $$ /$$$$$$        | $$$$$$$$|  $$$$$$/
   |__/  |__/|______/        |________/ \______/
   
   Don't know how to play? Don't worry, gameplay is simple.
   An integer is randomly generated within a range.
   You have to do your best to guess what the generated number is.
   At the end of each win you get to change the difficulty. It defaults to +2 difficulty.
   You can start back at difficulty 0 if you want to by entering 'reset' into the game if it is too hard.
   You can quit the program by entering 'end' at any point in the game as well.
   Remember, the higher the difficulty the more points you get after each round.""")
   
def logo():
	print('''                                                    (@@@@@@@@@@@@@@@@@@@%,
                                             /@@@#.........................,&@@@
                                         &@@,....................................#@@/
                                     #@@............................................./@@.
                                  &@#....................................................@@,
                               ,@&..........................................................@@
                             @@,..............................................................#@,
                           &@...................................................................(@
                         (@.......................................................................#@
                        @*..........................................................................@@
                      @@..............................................................................@.
                     @*................................................................................@@
                    @,..................................................................................#@
                   @.....................................................................................(@
                  @......................................................................#@@@@@@,........./@
                 @.....................................................................@@        @@,.......&@
                @*....................................................................@            *@.......@&
               (@....................................................................@&              @*......@
               @.....................................................................@          *@@,  @#.....(@
              &@.....................................................................@         @@@@@@( @*.....@
              @......................................................................@,        @@@@@@@,.@.....&@
              @......................................................................#@        /@@@@@@@ @.....,@
             *@.......................................................................@.        ,@@@@@@ &/.....@
             %%........................................................................@           &@,  @*.....@
             &(................................................/@@@@@@@@@@@@@...........@%              @......@.
             .............................................@@@@@@@&/,..,(@,............../@            @#.......@,.
             (&...........................................@@@@@,.........................../@%       /@........@,,,,,
             .@.........................................(@@@&................................./@@@@@@..........@,,,,,,
              @........................................#@@@.................................................../@,,,,,
              @(..............................................................................................@#,,,.
              ,@..............................................................................................@//*
               @%........................................,...................................................@(,,,,,,,,,,,,,,,,,,,,,,,,,,,,                    ╔═╗┬─┐┌─┐┌─┐┌─┐  ╔═╗┌┐┌┌┬┐┌─┐┬─┐
                @.....................................&@@,,,*(@.............................................*@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                   ╠═╝├┬┘├┤ └─┐└─┐  ║╣ │││ │ ├┤ ├┬┘
                *@................................%@@,,,,,,,,,,@*...........................................@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                   ╩  ┴└─└─┘└─┘└─┘  ╚═╝┘└┘ ┴ └─┘┴└─
                 @@.........................../@@*,,,,,,,,,,,,,@%..........................................@/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                  @%......................*@@/,,,,,,,,,,,,,,,,@&..........................................@/,,,,,,,
                   @@..................@@%,,,,,,,,,,,,,,,,,,#@....@%%....................................@(,,,,,,,,,
                    &@.............%@@,,,,,,,,,,,,,,,,,,,*/@@@@@&%%%%&..................................@*,,,,,,,,,,
                     .@..........@@,,,,,,,,,,,,,,*////////*,,,,,,,,,,,,,,,*(#&@@@@@@@@@...............#@,,,,,,,,,,,
                       @%......@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@............@%,,,,,,,,,,,,
                        *@*#@@%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@(.........#@,,,,,,,,,,,,,,
                .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@(........#@*,,,,,,,,,,,,,,
               .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*/(%&&@@@@@@@@@@@@#.......*@/,,,,,,,,,,,,,,,
               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@........#%////////////////////%@@,,,,,,,,,,,,,,,,,,
               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@..........&%//////////////%%&@&,,,,,,,,,,,,,,,,,,,
               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@............%%////////%&@@
               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@,..............*@%////%@@&
               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@..................%@@/
               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@*........,(@@@@&.
               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*/(//,.
               .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''')
	input('                                  .,,,,,,,,,,,,,,,,,,,,,,')


print('Please go fullscreen for best experience.')
time.sleep(7)
for x in range(0, 99):
	print(line_Count)
	line_Count = line_Count+1
full_Screen_Height = (input('Please scroll to the top and enter the biggest number you see.'))
title()
logo()
newpage(0)
titlepage()
GameStart(n, score)