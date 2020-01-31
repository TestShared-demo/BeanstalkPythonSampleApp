from flask import Flask, render_template
import os
import random
import boto3
import sqlalchemy as db
from datetime import datetime

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "Hello World"

@app.route("/")
def index():
#    try:
#        print ("Index function called: {}".format(datetime.now()), flush=True)
#        connection_str = f'mysql+pymysql://admin123:admin123@database-1.cwccoglqaq27.us-east-1.rds.amazonaws.com:3306/Bullet'
#        engine = db.create_engine(connection_str)
#        print ("Getting bd schema: {}".format(datetime.now()), flush=True)
#        insp = db.inspect(engine)
#        db_list = insp.get_schema_names()
#        print ("Fetching list of tables from the databases: {}".format(datetime.now()), flush=True)
#        rds_table_list = []
#        result = engine.execute("show tables;")
#        print ("Retrieved list of tables from the databases: {}".format(datetime.now()), flush=True)
#        for tables in result:
#            table_name = str(tables).replace(",","").replace("(","").replace(")","").replace("\'","")
#            rds_table_list.append(table_name)
#    except Exception as e:
#        print("RDS connection failed: {} - {}".format(datetime.now(), e), flush=True)
#        rds_table_list = ["*** Database not accessible. ***"]
#    print ("Rendering HTMl : {}".format(datetime.now()), flush=True)
    return render_template("index.html", rds_table_list=["*** Database not accessible. ***"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 80)))