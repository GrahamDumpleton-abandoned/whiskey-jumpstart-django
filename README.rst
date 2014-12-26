==========================
Whiskey Jumpstart - Django
==========================

This is a Whiskey jumpstart example for Django.

It demonstrates how the same code based for a Django application can be
deployed against Docker, Heroku and OpenShift. The example is running in
all cases using using Apache/mod_wsgi, courtesy of ``mod_wsgi-express``.

To get it running follow the steps outlined below for each deployment type.

Docker
------

The Docker instructions assume you have already installed Docker and
Fig (https://pypi.python.org/pypi/fig).

Note that the Docker build will take longer the first time due to the
need to pull down any required images. If you have previously used the
``mod_wsgi-docker`` image, ensure that you pull down the latest version
of the ``grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild`` image.

1. Clone this git repository.
2. Run ``fig build``.
3. Run ``fig up``.
4. Open a web browser on port 8000 of the Docker host.

This example will use Python 2.7. The version of Python used can be
changed by modifying the ``Dockerfile``. Supported versions are Python
2.7, 3.3 and 3.4.

Heroku
------

The Heroku instructions assume you have already created an account at
Heroku (http://www.heroku.com) and are currently logged in to the Heroku
dashboard.

1. Click `Deploy (Python 3.4.1) <https://heroku.com/deploy?template=https://github.com/GrahamDumpleton/whiskey-jumpstart-django>`_.
2. Click the "View it" link after the application been deployed.

Note that for this deployment mechanism to work the target platform must
provide dynamically loadable, shared library variants, of the Python
runtime libraries.

At this time Heroku doesn't provide such shared libraries for all Python
runtimes they provide. The only runtime that it is known they currently
provide them for is Python 3.4.1.

Comments from Heroku suggest that they may discontinue providing shared
libraries even for Python 3.4.1. If that is the case then even that will
stop working.

If you want to see continued support for deploying using this mechanism,
including the addition of support for Python 2.7, then you will need to
raise it directly with Heroku.

OpenShift
---------

The OpenShift instructions assume you have already created an account at
OpenShift (http://openshift.redhat.com) and are currently logged in to the
OpenShift dashboard.
 
Note that the OpenShift UI doesn't give good visual feedback when creating
applications and so you may be presented with a blank screen for some time.
Just be patient and it will eventually return.

1. Click `Deploy (Python 2.7) <https://openshift.redhat.com/app/console/application_types/custom?name=whiskeyjumpstartdjango27&initial_git_url=https://github.com/GrahamDumpleton/whiskey-jumpstart-django.git&cartridges[]=python-2.7>`_.
2. Click the "Continue to application overview page" after the application
   has been deployed.
3. Click on the name of your application to open it

Note that at this time using the Python 3.3 runtime provided by OpenShift
causes creation of the initial application to fail. This issue is still
being investigated.
