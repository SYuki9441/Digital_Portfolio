from flaskapp import app as application


# Debugger
if __name__ == '__main__':
    application.run(debug=True)



# note
# export FLASK_APP=flaskapp.py
# source env/bin/activate   (to activate virtual environment)
# deactivate   (to deactivate virtual environment)