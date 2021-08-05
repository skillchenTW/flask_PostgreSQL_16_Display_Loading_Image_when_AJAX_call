from re import search
from flask import Flask, render_template, request, jsonify, json
import psycopg2
import psycopg2.extras

app = Flask(__name__)

app.secret_key = "SkillChen_Secret_Key"
DB_HOST='localhost'
DB_PORT='5433'
DB_NAME='sampledb'
DB_USER='postgres'
DB_PASS='dba'

conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fetchdata", methods=["POST","GET"])
def fetchdata():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)    
    if request.method == "POST":
        search = request.form["search"]
        query = "select * from posts where upper(title) like upper('%{}%')".format(search,)
        cursor.execute(query)
        postslist = cursor.fetchall()
        cursor.close()        
    return jsonify({'htmlresponse': render_template('response.html', postslist=postslist)})

if __name__ == '__main__':
    app.run(debug=True)
