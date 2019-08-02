from __future__ import print_function # In python 2.7
from flask import Flask, render_template, request, redirect
import sys


app = Flask(__name__)
app.config.from_object(__name__)

courseNameDict = {}
majorNameDict = {}

@app.route('/')
def loadpage():
	return render_template("/mainPage.html")


####################################################################

@app.route('/select', methods= ["POST"])
def select():
    if request.method == 'POST':
        if request.form['submit'] == 'action1':
            return render_template("/learnPage.html")
        else:
            return render_template("/teachPage.html")
    
#####################################################################
						
@app.route('/teach', methods= ["POST"])


def teach():
    data =[]
    data.append(request.form['name'])
    data.append(request.form['course'])
    data.append(request.form['major']) 
    data.append(request.form['email']) 
    print(data, file=sys.stderr)

    addCourse(data) 
    addMajor(data)    
    
    return redirect('/')
    
def addCourse(data):
    
    name = str(data[0]) 
    course = str(data[1]) 
    major = str(data[2]) 
    email = str(data[3]) 
    if course in courseNameDict:
        courseNameDict[course].append(name,major,email)
    else:
        courseNameDict[course]=[name,major,email]
        
def addMajor(data):

    name = str(data[0])
    course = str(data[1]) 
    major = str(data[2]) 
    email = str(data[3]) 
    if major in majorNameDict:
        majorNameDict[major].append(name,course,email)
    else:
        majorNameDict[major]=[name,course,email]        
        
#####################################################################################3

@app.route('/learn', methods= ["POST"])

def learn():
    try:
        if request.method == 'POST':
            selected_course = str(request.form['Course'])
            selected_major = str(request.form['Major'])
            print("Printing Course:" + selected_course, file=sys.stderr)
            print("Printing Major:" + selected_major, file=sys.stderr)

            output1 = course(selected_course)     
            output2 = major(selected_major) 


            return render_template('learnPageOutput.html', output1=output1, output2=output2) 
        
    except Exception as e:
        print(e, file=sys.stderr)


def course(selected_course):
    print("inside function course() : " + selected_course, file=sys.stderr)
    if selected_course in courseNameDict:
        print("inside function course() : " + str(courseNameDict[selected_course]) , file=sys.stderr)
        return courseNameDict[selected_course] 

def major(selected_major):
    print("Inside function major ....", file=sys.stderr)

    print(str(selected_major), file=sys.stderr)
    if selected_major in majorNameDict:
        result = majorNameDict[selected_major]
        print(result, file=sys.stderr)
        print("result of function major: " + str(result), file=sys.stderr)
        return majorNameDict[selected_major]
        
#########################################################################################
    
   
@app.route('/learnoutput', methods= ["POST"])

def go_Back():
    if request.method == 'POST':
        if request.form['submit'] == 'goback':
            return render_template("/learnPage.html")
    
if __name__ == '__main__':
    app.run()
