# HR-arch-1-tba
A text based adventure in Python, for our Basecamp Arch 1 Challenge.

---

Prerequisite:

Run the following command in PowerShell or in a command prompt:
pip install pymongo  

This installs the plugins required to connect to the MongoDb datastore we use for saving and loading data.

---

Running the Client and Server
They both use command-line arguments. You can run them without arguments to see the options.

For the server, pass host and port numbers:
```
$ python tba_server.py
Usage: tba_server.py <host> <port>
```

For the client, pass host and port numbers as well:
```
$ python tba_client.py
Usage: tba_client.py <host> <port>
```

Our launch.json includes settings for 2 clients and 1 server. This allows us to test for multiple connections.

---

**COURSE DESCRIPTION** 
**Course name**: Basecamp 1, Challenge 1 

**Course code**: INFBCC01-1 

**ECTS**: 1 ECTS 

**Study points and workload**: _This elective provides you with 1 study point (EC). The study workload is at least 28 hours during Challenge Week._

**Prior knowledge**: _The challenge is a logical continuation of the program in Basecamp. The level of the challenge is aligned to Basecamp's program of Arch 1._

**Working method**: _Students work during Challenge Week in a team of 2 (or 3) students. Students work independently on location and online. Teachers and peer coaches will be available for support._ 

**Testing**: _A working adventure game that meets the minimal requirements and is presented in class. A minimum effort of 28 hours per person is expected. Students keep a logbook for this purpose._ 

**Learning materials**: _All Basecamp material, online content._ 

**Content**: _Students will create a text-based adventure board game in Python, covering at least the concepts in Arch 1._ 

**Notes**: _Although there are minimum requirements, creativity is stimulated!_ 

**Course coordinator**: _Xenia Hasker, John Grobben_ 

**Date**: _1 September 2023_ 

---

## Introduction 

Week 4 is designed as a flexible week. If everything is going well, you will do this challenge assignment. If you experience difficulties, you can use this week to get back on track. ‘Back on track’ is described in another document. 

## The challenge 
Design, build and test a text-based adventure game. The game should be exciting, funny and a complete waste of time …. 
In the challenge week you can use your creativity! We have chosen a theme for this year: SPACETRAVEL. The first version(s) should be just text-based. In later versions you can add sound effects and/or visuals. 
So far you have learned the basics of python programming : variables, input, output, calculations, branching and looping. Even with these simple techniques you can build a nice game: a text based adventure. 
NOTE: you may also use other techniques you know. 

In a text based adventure the user is wandering in a (dangerous) world and has to solve some puzzles to reach a goal (finding a treasure, landing on the moon, reach a mountain top, etcetera). During the journey the user will meet all kind of characters and will find some objects that can be used to solve some problems/puzzles (crossing a river, killing a dragon, opening a door, finding a planet in another solar system, etc.). Characters can be dangerous  (kill the user) or give tips/items if you help them.  

To get a first impression you could look at https://www.makeuseof.com/tag/browser-text-based-games/  

You will make this challenge in pairs, so you can: 
- Exchange ideas/knowledge 
- Test each other’s code and help with debugging 
- Brainstorm 
- Divide some tasks 
NOTE: you two will make ONE product and both of you has full understanding of the product. 

In short your challenge will be: 
- explore the world of text based adventures (TBA) (analysis) 
- practice a little with examples found on the internet (orientation) 
- develop a storyline and a map for your adventure (design) 
- build your first TBA (development of prototype) 
- extend it (advanced development)  

HINTS AND TIPS: 
Zork is a famous TBA, but don't try to solve it completely !  
There are plenty of introductions, start with easy examples 

Some ideas about space travel (if you have a creativity block): 
- oxygen 
- food 
- water 
- asteroids 
- aliens 
- rockets 
- messages from outer space 
- whatever you can think of, game design is a creative process and the sky is the limit 
- for inspiration look at one of the many space/SF- series….. 

HINT: 
- Make a map of your world (universe)! 
- Start SMALL! 
- Make a simple adventure first, for example with 3 locations, a few puzzles and some items the user can find, pickup and use. Use multiple choice to ask the user for actions: 
- Kill the alien 
- Run away 
- Pick up laser beamer 
- Throw water at the alien 
- Go to the black hole 

If you have built this first prototype, extend it with (whatever you like to try): 
- sound 
- images, for example made with https://docs.python.org/3/library/turtle.html 
- more puzzles, items, personages 
- map of the environment 

Minimal requirements: 
- 10 locations 
- 10 items 
- 5 puzzles 
- All python techniques of week 1-3 
- No errors 
- No copies of work from fellow students or adventures found on the internet 
- Theme must be SPACE TRAVEL 

Nice to have: 
- Images (look at the turtle library in python) 
- Sounds (depends on your operating system) 
- Understand commands like GO WEST,OPEN THE DOOR, PICK UP LASER ….. 

Planning 
- Week 3 decision challenge or back to track, make plan for “back on track” or read this challenge document.  
- Week 4: working on challenge or back on track, visit guest lecture, feedback session, handing in 
- Week 5: showing products to teachers (and other students) 

Deliverables 
- Source code 
- Working adventure game 
- Hour registration (for each member of the team - we expect you to work at least 28 hours on your back on track challenge) 

Demonstration (week 5, in class) 
Hand in in Codegrade: A1W4C1 - Challenge week 1 (as a zip-file) 

Grading 
The challenge is a team effort, to which the students contribute individually. The grade is on an individual base. To qualify for a passing grade for this challenge, you must meet the following prerequisites and requirements: 
