<h1 align="center" >
    <img src="robotinic.png">
</h1>
<h2 align="center" >
    A simple chatbot for WhatsApp! 🤖💬 <br>
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/CleoMenezes/WhatsApp-ChatBot?style=social">
    <img alt="GitHub followers" src="https://img.shields.io/github/followers/CleoMenezes?label=Follow%20me%20%3A%29&style=social">
</h2>

<h1>⚈ About & How to use</h1>
<p>
Disclaimer: this is my first project with chatbot. This will evolve over time. I appreciate any contribution. Thank you!

Quite simply, the program can create an uninterrupted conversation between the computer and the selected person.
The program starts by asking for the name of the person or group you want to start a conversation with. Pay attention as it is necessary that the name of the person or group is written exactly as in your WhatsApp application.
The program will open a Google Chrome window directly on the page. You must log in as you normally would. <br>
** Gosh, NOTHING HAPPENED ** <br>
Easy, easy. You simply need to confirm the login with an Enter in the terminal.

Now wait and ... It will start like magic! err... Sorry, Elon Musk. I mean "Like intense study days".
</p>

<h4 align="center"> 
	🚧  Don't forget that it's still in progress...  🚧
</h4> 

<br>

<h1>⚈ How the bot Works?</h1>
<p>
The bot uses a selection of machine learning algorithms to produce different types of responses.
The responses are stored in a file called db.sqlite3.
There are already several different conversations from his database (They are in Portuguese, but you can change it easily by accessing here).
You can delete it if you want to remit the training as another one will be generated automatically.

Specifically in this project, I had already trained, so I turned off the training based on the corpus, so I commented:
```python
from chatterbot.trainers import ChatterBotCorpusTrainer
         trainer = ChatterBotCorpusTrainer (bot)
         trainer = ListTrainer (bot)
         trainer.train ("chatterbot.corpus.portuguese")
```

I left the listening mode on, where you keep new and different answers. Don't worry, I left this part commented so you know what it is.
If you are going to activate one, disable the other.
</p>

<h1>⚈ Tech Stack</h1>

The following tools were used in the construction of the project:

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [ChatterBot](https://chatterbot.readthedocs.io/en/stable/)

<h1>⚈ Bugs</h1>
<p>
If the program cannot find the contact, it may be far down in the chat list. I still don't know how to solve this. Bringing him into the most recent conversations solves this problem. :)
</p>
