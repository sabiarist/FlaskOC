from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# config options - Make sure you created a config.py file.
app.config.from_object('config')


# to get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
@app.route('/index/')
def index():
    description = """
              Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif,
        tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère 
        et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, 
        tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
    """
    return render_template('index.html',
                           user_name="Tomy",
                           user_image=url_for('static', filename='img/profile.png'),
                           description=description,
                           blur=True)


@app.route('/result/')
def result():
    description = """
              Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. 
        D'ailleurs, Koh Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. 
        Tu es aussi un idéaliste chevronné. Quelle chance !
    """
    gender = request.args.get('gender')
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    profil_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    return render_template('result.html',
                           user_name=user_name,
                           user_image=profil_pic,
                           description=description)


@app.route('/contents/<int:content_id>/')
def content(content_id):
    return '%s' % content_id


if __name__ == "__main__":
    app.run()