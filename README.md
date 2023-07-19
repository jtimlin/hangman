## Hangman game 

#### This interactive word game challenges players to guess the hidden word by carefully selecting letters until the entire word is revealed. Players are initially presented with empty spaces, symbolizing the missing letters they must uncover. The game was specifically developed as part of the Code Institute's Full Stack Software Developer course, serving as the accomplished third Milestone Project.

#### Live Site [Here](#)

![alt text](doc/Ska%CC%88rmavbild%202022-07-17%20kl.%2006.31.46.png)

#### How to play

* The user need to enter their name and once entered, the game starts and user will be presented the secret word with blank spaces for each letter.

* The user need to type a letter or a word on the keybord.
* If the letter the user choses, exists in the answer, then all the blank spaces, where that letter exists, will be populated with that letter.
* The player have eight tries.
* If the player cannot guess the word and exceeds the lives, the hangman will be completed and the game will be over.

## Features
The game features a welcome message to the user and when the user starts the game, it will ask the user to type their name. 
![alt text](doc/Ska%CC%88rmavbild%202022-07-17%20kl.%2006.31.46.png)

* When the user types their name, a hello message will appear displaying their name and the game will begin. The program will also display the number of letters in the word.
![alt text](doc/Ska%CC%88rmavbild%202022-07-17%20kl.%2006.34.08.png)

If the letter guessed by the user matches any of the letters in the word, the letter will appear in the blank space where that letter belongs. In the following screenshot, the letter "a" was guessed and it appeared on the blank space.

![alt text](doc/Ska%CC%88rmavbild%202022-07-17%20kl.%2006.37.38.png)

User can only guess a letter, if they use a number or a special character, then they will get an error message that they have to select a letter.

![alt text](doc/Ska%CC%88rmavbild%202022-07-17%20kl.%2006.39.47.png)

* If the letter guessed by the user is incorrect, the hangman picture will be populated piece by piece, starting from head to the legs. Also, the wrong letter will be displayed to the user. If the user selects a letter that has already been chosen, the following message will appear "You already guessed it, please try again". The following screenshot displays the message. A list with already chosen and wrong letters appears so the user knows wich letters they already choosed.![alt text](doc/Ska%CC%88rmavbild%202022-07-17%20kl.%2006.42.07.png)
* If the user is unable to guess the word in 9 attempts, the hangman will be completed and the user will lose the game. To replay the game, the user will need to click on run the program and the game will restart.![alt text](doc/Ska%CC%88rmavbild%202022-07-17%20kl.%2006.48.39.png)

* If the user can guess the word, the user will receive a congratulations message and they will win the game.

## Future features

I'll add a function that shows what the right word was in case the choice was wrong.

## Technologies used

### Languages
. Python

## Frameworks, Deployement & Libraries

* [Github](https://github.com/)

* [Gitpod](https://gitpod.io)

## Testing

* Testing was done throughout the project mainly by running the program in the terminal as well as python debugger. I committed the codes to github after writing every new list or code.

* I used the deployed site to manually type correct and incorrect data to validate and see how the program responded.

## Accessibility

* There are no images on the site.
* The whole project was built using python, therefore no other langueges were used.

## Issues and bugs

* When I play the game I discovered that it is difficult to guess the correct word. I do not know if it is bugs in code or what it may be due to.

## Fixed bugs

I resubmitt this project because my previous code didn't have the ability to validate all types of inputs like characters and empty inputs. This also caused users to lose lives when they typed wrong inputs. Now it is fixed and in the event of incorrect entries, users are notified that "Invalid code, please enter again" ![alt text](doc/invalid.png)

## Validator Testing
I ran through my file in [](https://pep8ci.herokuapp.com/)

The Code has warnings and I did rectify these.
![alt text](doc/Ska%CC%88rmavbild%202022-12-09%20validate.png) 


## Deployment

I followed the below steps when deploying my project to Heroku, based on the Code Institute instructions:

* Add to requirements.txt file:-
pip3 freeze > requirements.txt
Commit changes to Github:
git commit -m "Add requirements for deployment”

In HEROKU after creating the account:

1. "Create new App"

2. Give the App a unique name and enter region

3. Click on "Create App"

4. Click on "Settings" on your new App Dashboard

5. Scroll down to Config Vars where in my instance I only inserted KEY: PORT and VALUE: 8000 since I have no creds.json files to add.

6. Press Add-button

7. Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon for Nodejs and save changes. These Buildpacks need to be in below order:

Python NodeJS

8. Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter search for my Github Repository "Parents Allowance Calculator" and then click connect.

9. Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to github automatically updates in Heroku.

10. Then in the Manual Deploy section, press Deploy Branch.

11. After project has been deployed successfully I clicked the View-button to see the program run in the terminal.

## Credits

[Fabio M](https://www.youtube.com/watch?v=lJ7RhvNvsnc&t=1s) This tutorial was helpful for me to build the game. I followed it step by step. 

[Github](https://github.com/) Help with add code to handle invalid input from user like numbers or other characters.

[Github](https://github.com/) Help with add function that welcomes users and ask them to type theirs name.

## Special Thanks

Specials thanks to Student Turtor Assistance for theirs patience and skills that made me complete this project. 

A special thanks my mentor Martina Terlević for being there for me and allways give inspiration and support.