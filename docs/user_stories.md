# User Stories

## Priority Grading
This is a loose system that states a general starting point for the priority of a user story. From that starting point, the priority can change based on what user stories rely on others, whether the function affects the site's basic functionality, and whether the function affects the difficulty of getting other user stories to work.

### Highest(HH)
Gathering a WPM Score (Basic Func of site)

### High(H)
Getting stats from user and others
### Medium(M)
Sources of text
### Low(L)
Connecting different users for SCOREBOARD

## Effort Estimation Grading
6 | More than a week, more than a person

5 | More than a week, one person

4 | One week, one person

3 | Less than a week, one person (Specifically half of a 6)

2 | Less than half of a week, one person

1 | Several Hours or one day, one person

0 | Hour long, one person 

-------------------------------
## Stories List
[EPIC] Typing Challenges
-----------------------
As a User, I want to attempt typing challenges so that I can track my typing speed and accuracy.

 - Priority: HH
 - Estimate: 6
 - Confirmation:

   1. Start challenge
   2. Type challenge content
   3. Finish challenge
   4. Collect Results
   5. View Results

[Typing Challenges] Challenge Text
-----------------------
As a Challenger, I want to view the text of the challenge so that I can type the correct content.

 - Priority: HH
 - Estimate: 0
 - Confirmation:

   1. Start Challenge
   2. View challenge text

[Typing Challenges] Challenge Typing 
-----------------------
As a Typist, I want to type the challenge text into some text input so that I can work towards completing the challenge.

 - Priority: HH
 - Estimate: 3
 - Confirmation:

   1. Start Challenge
   2. View challenge text
   3. Begin typing challenge text

[Typing Challenges] Challenge START
-----------------------
As a Challenger, I want to have a restart button for the challenge so that I can decide when to cut my losses and redo the challenge if/when I make a mistake.

 - Priority: H
 - Estimate: 1
 - Confirmation:

   1. Start Challenge
   2. Continue typing
   3. Press restart button
   4. Challenge starts from beginning

[Typing Challenges] Track Progress in Challenge
-----------------------
As a Typist, I want to track my progress so that I can see how much of the challenge remains

 - Priority: H
 - Estimate: 3
 - Confirmation:

   1. Start challenge
   2. View 0% completion
   3. Continue challenge
   4. View completion % change
   5. Finish challenge
   6. View 100% completion


[Typing Challenges] View Results
-----------------------
As a Typist, I want to see my typing statistic results after I finish a challenge so that I can gain the benefit of knowing my typing speed and accuracy

 - Priority: H
 - Estimate: 5
 - Confirmation:

   1. Finish challenge
   2. Collect stats based on time and correctness
   3. View collected stats

[Typing Challenges] Different Challenge Text
-----------------------
As a Challenger, I want the text to be different every time I begin a new challenge so that I can test my stats in general and not in one situation.

 - Priority: H
 - Estimate: 5
 - Confirmation:

   1. View Challenge selection OR Click “new challenge”
   2. Start challenge
   2. View unique challenge text

[Typing Statistics Tracking] WPM
-----------------------
As a User, I want to see my aggregate wpm so that I can have a better understanding of my typing speed.

 - Priority: H
 - Estimate: 5
 - Confirmation:

   1. Complete Challenges
   2. Collect challenge WPM scores
   3. Generate Average
   4. Store Average

[Typing Statistics Tracking] Accuracy
-----------------------
As a User, I want to see my aggregate accuracy so that I can have a better understanding of my typing accuracy.

 - Priority: H
 - Estimate: 5
 - Confirmation:

   1. Complete Challenges
   2. Collect challenge accuracy scores
   3. Generate Average
   4. Store Average

[EPIC] Typing Statistics Tracking
-----------------------
As a User, I want to track all my typing  statis so that I can see my own improvement and current typing level.

 - Priority: H
 - Estimate: 6
 - Confirmation:

   1. Collect typing statistics
   2. Store typing statistics
   3. View the current statistics on user screen

[Typing Challenges] Challenge START
-----------------------
As a Challenger, I want to have a start button for the challenge so that I can decide when to begin.

 - Priority: M
 - Estimate: 1
 - Confirmation:

   1. View Challenge with button
   2. Click button
   2. Challenge begins

[Administrator Challenge Insertion] No Copyright
-----------------------
As an Administrator, I want to use non-copyright text so that I don’t get sued.

 - Priority: M
 - Estimate: 2
 - Confirmation:

   1. Collect non-copyright text
   2. Insert Text as Challenge


[Typing Challenges] Character Confirmation
-----------------------
As a Typist, I want the application to let me know when I input a character so that I can track where in a sentence I am typing and see what character comes next.

 - Priority: M
 - Estimate: 3
 - Confirmation:

   1. Type character
   2. View *some* character change

HI-SCORE
-----------------------
As a User, I want to see my own high score after I complete a challenge so that I can track my peak stats.

 - Priority: M
 - Estimate: 4
 - Confirmation:

   1. Collect typing statistics
   2. Store highest statistics
   3. View the current highest statistics on user screen


[Administrator Challenge Insertion] Admin Sign-In
-----------------------
As an Administrator, I want to be able to sign into the website so that I can access different options from a standard user.

 - Priority: M
 - Estimate: 5
 - Confirmation:

   1. View sign in page
   2. Type in admin user information
   3. Access site with ADMIN status/functions.

[Typing Statistics Tracking] Challenge Completion
-----------------------
As a User, I want to see which challenges I have completed with my associated typing statistics on those challenges so that I can compare separate data by challenge to the aggregate scores.

 - Priority: M
 - Estimate: 5
 - Confirmation:

   1. Complete Challenges
   2. Collect challenge statistics
   3. Store challenge statistics
   4. View on user screen

User Registration
-----------------------
As a User, I want to register into the site with my personal information so that I can separate my progress from others by signing in.

 - Priority: M
 - Estimate: 5
 - Confirmation:

   1. Go to registration interface
   2. Type new user information
   3. Get confirmation
   4. Able to use information to sign in later*


User Sign-In
-----------------------
As a User, I want to sign into the site so that I can record my specific progress.

 - Priority: M
 - Estimate: 6
 - Confirmation:

   1. Register as User
   2. Go to Sign-In interface
   3. Type in user information
   4. View site as specific user



[EPIC] Administrator Challenge Insertion
-----------------------
As an Administrator, I want to add a challenge database so that my users can access different challenges/text.

 - Priority: M
 - Estimate: 6
 - Confirmation:

   1. Sign in as ADMIN
   2. Insert Text as Challenge
   3. Add text to challenge selection
   4. Challenge made available to users.

Typing Statistics Sharing
-----------------------
As a User, I want to export my score data so that I can share it with others.

 - Priority: L
 - Estimate: 3
 - Confirmation:

   1. Finish Challenge
   2. Collect challenge data into copyable format
   3. Copy Data

[Typing Challenges] Challenge Timer
-----------------------
As a Challenger, I want a timer that counts down so that I can gauge my time remaining.

 - Priority: L
 - Estimate: 4
 - Confirmation:

   1. Start Challenge
   2. Time counter lowers each second
   3. Challenge ends at 0

[Administrator Challenge Insertion] Language Filtering
-----------------------
As an Administrator, I want the option of filtering adult language out of the text so that underage users can test their typing stats.

 - Priority: L
 - Estimate: 4
 - Confirmation:

   1. Check challenge text against “adult language” database. 
   2. Remove adult language from challenge
   2X. OR filter challenges out of challenge list.

Cross-User Typing Speed 
-----------------------
As a User, I want to see other users’ overall typing speed so that I can compare my stats & progress to theirs.

 - Priority: L
 - Estimate: 4
 - Confirmation:

   1. Sign in as User
   2. Select other registered user
   3. View other user’s typing speed  

High Score Leaderboard
-----------------------
As a User, I want to see other users’ high scores so that I can compare my stats & progress to theirs.

 - Priority: L
 - Estimate: 5
 - Confirmation:

   1. Sign in as User
   2. Select Challenge & View stats
   3. Collect stats from other registered users
   3. Display other users’ stats


