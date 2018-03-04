To Start the Project:

IF IN DOUBT: https://tutorial.djangogirls.org/en/

1.) Create a folder on your computer

2.) Create a virtual environment (python -m venv myvenv) MAKE SURE IT IS PYTHON 3.6

3.) On Mac ACTIVATE venv (source myvenv/bin/activate) 
 	On Windows Activate venv (myvenv/Scripts/activate)
	
4.) Clone github repository (git clone https://github.com/dmayers340/itech.git)

5.) (cd itech)-could probably install django without doing this

6.) Install Django (pip install django~=1.11.0)


Itech Folder Structure:

	-fountain (PROJECT FOLDER-has settings/urls/wsgi)
	
	-findafountain (app--has app shit)
	
	-static 
	
		-css
		
		-img
		
		-jquery
		
		-js
		
	-templates
	
	-manage.py 


GIT:

ALWAYS RUN git status FIRST

1.) git status

2.) git add --all .

3.) git commit -m "Detailed message about changes"

4.) git push

TO Checkout New Branch:

git checkout -b newbranch

git add --all .

git commit -m "changes stuff write detailed message"
git push --set-upstream origin newbranch
