Running on OpenShift
----------------------------

Create an account at https://www.openshift.com and follow the instructions on setting up etc

Create a python application

    rhc app create rankedstats python-2.7 (or python-3.3)

Add this upstream rankedstats repo

    cd rankedstats
    git remote add upstream -m master https://github.com/CrystalMoogle/rankedstats.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://rankedstats-$yournamespace.rhcloud.com

------------------------------

To get more log messages in your OpenShift logs please add the following line to your code

app.config['PROPAGATE_EXCEPTIONS'] = True  

To read more about logging in Flask please see this email

http://flask.pocoo.org/mailinglist/archive/2012/1/27/catching-exceptions-from-flask/


This README (and the base of the repo) taken and edited from https://github.com/openshift/flask-example/
