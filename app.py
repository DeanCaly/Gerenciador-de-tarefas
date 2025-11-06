from flask import Flask, jsonify
from tasks_dib import get_all_tasks



app = Flask(__name__)

@app.route('/')
def get_tasks():
    tasks =  get_all_tasks()
    
    return jsonify(tasks)



if __name__ == '__main__':
    app.run(debug=True)
    
    
    