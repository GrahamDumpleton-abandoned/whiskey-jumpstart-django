==========================
Whiskey Jumpstart - Django
==========================

This is a Whiskey jumpstart example for Django.

It demonstrates how the same code based for a Django application can be
deployed against Docker, Heroku and OpenShift.

To get it running follow the steps outlined below for each deployment type.

Docker
------

The Docker instructions assume you have already installed Docker and
Fig (https://pypi.python.org/pypi/fig).

Note that the Docker build will take longer the first time due to the
need to pull down any required images. If you have previously used the
``mod_wsgi-docker`` image, ensure that you pull down the latest version
of the ``grahamdumpleton/mod-wsgi-docker:python-3.4-onbuild`` image.

1. Clone this git repository.
2. Run ``fig build``.
3. Run ``fig up``.
4. Open a web browser on port 8000 of the Docker host.

Heroku
------

The Heroku instructions assume you have already created an account at
Heroku (http://www.heroku.com) and are currently logged in to the Heroku
dashboard.

1. Click `Deploy <https://heroku.com/deploy?template=https://github.com/GrahamDumpleton/whiskey-jumpstart-django>`_.
2. Click the "View it" link after the app is deployed

OpenShift
---------

The OpenShift instructions assume you have already created an account at
OpenShift (http://openshift.redhat.com) and are currently logged in to the
OpenShift dashboard.
 
1. Click `Deploy <https://openshift.redhat.com/app/console/application_types/custom?name=whiskey-jumpstart-django&initial_git_url=https://github.com/GrahamDumpleton/whiskey-jumpstart-django.git&cartridges[]=python-2.7>`_.
2. Click the "Continue to application overview page" after the application
   has been deployed.
3. Click on the name of your application to open it
