make the appropriate changes for your system and try again.

ago@home-nbdell1:~/PycharmProjects/aws-es-auth-proxy$ sudo python setup.py install
[sudo] password for ago:
running install
running bdist_egg
running egg_info
writing requirements to aws_es_auth_proxy.egg-info/requires.txt
writing aws_es_auth_proxy.egg-info/PKG-INFO
writing top-level names to aws_es_auth_proxy.egg-info/top_level.txt
writing dependency_links to aws_es_auth_proxy.egg-info/dependency_links.txt
package init file 'src/__init__.py' not found (or not a regular file)
reading manifest file 'aws_es_auth_proxy.egg-info/SOURCES.txt'
writing manifest file 'aws_es_auth_proxy.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/src
copying src/server.py -> build/lib.linux-x86_64-2.7/src
copying src/config.py -> build/lib.linux-x86_64-2.7/src
copying src/aws_proxy.py -> build/lib.linux-x86_64-2.7/src
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/src
copying build/lib.linux-x86_64-2.7/src/server.py -> build/bdist.linux-x86_64/egg/src
copying build/lib.linux-x86_64-2.7/src/config.py -> build/bdist.linux-x86_64/egg/src
copying build/lib.linux-x86_64-2.7/src/aws_proxy.py -> build/bdist.linux-x86_64/egg/src
byte-compiling build/bdist.linux-x86_64/egg/src/server.py to server.pyc
byte-compiling build/bdist.linux-x86_64/egg/src/config.py to config.pyc
byte-compiling build/bdist.linux-x86_64/egg/src/aws_proxy.py to aws_proxy.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying aws_es_auth_proxy.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying aws_es_auth_proxy.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying aws_es_auth_proxy.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying aws_es_auth_proxy.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying aws_es_auth_proxy.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating 'dist/aws_es_auth_proxy-0.1.0-py2.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing aws_es_auth_proxy-0.1.0-py2.7.egg
Copying aws_es_auth_proxy-0.1.0-py2.7.egg to /usr/local/lib/python2.7/dist-packages
Adding aws-es-auth-proxy 0.1.0 to easy-install.pth file

Installed /usr/local/lib/python2.7/dist-packages/aws_es_auth_proxy-0.1.0-py2.7.egg
Processing dependencies for aws-es-auth-proxy==0.1.0
Searching for requests==2.10.0
Reading https://pypi.python.org/simple/requests/
Best match: requests 2.10.0
Downloading https://pypi.python.org/packages/49/6f/183063f01aae1e025cf0130772b55848750a2f3a89bfa11b385b35d7329d/requests-2.10.0.tar.gz#md5=a36f7a64600f1bfec4d55ae021d232ae
Processing requests-2.10.0.tar.gz
Writing /tmp/easy_install-zGzB1R/requests-2.10.0/setup.cfg
Running requests-2.10.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-zGzB1R/requests-2.10.0/egg-dist-tmp-U6PyWP
warning: no files found matching 'test_requests.py'
creating /usr/local/lib/python2.7/dist-packages/requests-2.10.0-py2.7.egg
Extracting requests-2.10.0-py2.7.egg to /usr/local/lib/python2.7/dist-packages
Adding requests 2.10.0 to easy-install.pth file

Installed /usr/local/lib/python2.7/dist-packages/requests-2.10.0-py2.7.egg
Searching for boto3==1.3.1
Reading https://pypi.python.org/simple/boto3/
Best match: boto3 1.3.1
Downloading https://pypi.python.org/packages/d9/6c/1063a4984d13f1b22edb30f3b97b6df7e0bdc7792ebc2f638b31f8b2ff79/boto3-1.3.1.tar.gz#md5=e6be09a90230390640873979702dd6da
Processing boto3-1.3.1.tar.gz
Writing /tmp/easy_install-UZQW9d/boto3-1.3.1/setup.cfg
Running boto3-1.3.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-UZQW9d/boto3-1.3.1/egg-dist-tmp-r7TwNz
zip_safe flag not set; analyzing archive contents...
boto3.session: module references __file__
boto3.docs.service: module references __file__
creating /usr/local/lib/python2.7/dist-packages/boto3-1.3.1-py2.7.egg
Extracting boto3-1.3.1-py2.7.egg to /usr/local/lib/python2.7/dist-packages
Adding boto3 1.3.1 to easy-install.pth file

Installed /usr/local/lib/python2.7/dist-packages/boto3-1.3.1-py2.7.egg
Searching for requests-aws4auth==0.9
Best match: requests-aws4auth 0.9
Adding requests-aws4auth 0.9 to easy-install.pth file

Using /usr/local/lib/python2.7/dist-packages
Searching for bottle==0.12.9
Best match: bottle 0.12.9
Adding bottle 0.12.9 to easy-install.pth file

Using /usr/local/lib/python2.7/dist-packages
Searching for futures==3.0.5
Best match: futures 3.0.5
Adding futures 3.0.5 to easy-install.pth file

Using /usr/local/lib/python2.7/dist-packages
Searching for jmespath==0.9.0
Best match: jmespath 0.9.0
Adding jmespath 0.9.0 to easy-install.pth file

Using /usr/local/lib/python2.7/dist-packages
Searching for botocore==1.4.13
Best match: botocore 1.4.13
Adding botocore 1.4.13 to easy-install.pth file

Using /home/ago/.local/lib/python2.7/site-packages
Searching for docutils==0.12
Best match: docutils 0.12
Adding docutils 0.12 to easy-install.pth file

Using /usr/local/lib/python2.7/dist-packages
Searching for python-dateutil==2.5.3
Best match: python-dateutil 2.5.3
Adding python-dateutil 2.5.3 to easy-install.pth file

Using /home/ago/.local/lib/python2.7/site-packages
Searching for six==1.10.0
Best match: six 1.10.0
Adding six 1.10.0 to easy-install.pth file

Using /usr/lib/python2.7/dist-packages
Finished processing dependencies for aws-es-auth-proxy==0.1.0
