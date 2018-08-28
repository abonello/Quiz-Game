import os
from flask import Flask, render_template, redirect, request

from json_file import create_riddle_data, get_player_data, set_player_turn, set_previous_answer,  check_player_answer
from gameplay import wipe_gamefiles

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')
 
 
@app.route('/setup', methods=['GET'])
def setup():
 
 if request.method == 'GET':
  players = request.args.get('players')
  if players is None:
   return render_template('setup.html')
  else:
   return redirect('/usernames/{}'.format(players))
   
   
@app.route('/usernames/<players>',methods=['POST', 'GET'])
def usernames(players):
 
 players = int(players)
 
 if request.method == 'POST':
  create_riddle_data(players)
  return redirect('/riddle')
 return render_template('usernames.html', players=players)
 
 
 
@app.route('/riddle',methods=['GET', 'POST'])
def riddle():
 
 wipe_gamefiles()
 riddle_data = get_player_data()
 
 if request.method == 'POST':
  set_player_turn()
  set_previous_answer()
  correct_check = check_previous_player_answer()
 return render_template('riddle.html')
 
 
 
@app.route('/leaderboards')
def leaderboards():
 return render_template('leaderboards.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)






