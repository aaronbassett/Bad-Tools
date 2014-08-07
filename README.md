Bad Tools
=========

[![Compiling](http://imgs.xkcd.com/comics/compiling.png)](http://xkcd.com/303/)

[![Build Status](https://travis-ci.org/aaronbassett/Bad-Tools.svg?branch=master)](https://travis-ci.org/aaronbassett/Bad-Tools)

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Blame your tools, blame the vendors, blame your workmates. Just as long as it is not your fault. Take the effort out of shifting the blame by using one of these ultra handy pre-written excuses.

The excuses are available in every format you could need so you can be properly lazy. For some basic examples of how to use the excuses in your code code see the [examples](examples/).

Plain Text
----------

    curl -X GET "http://www.codingexcuses.com/" \
     -H "Accept: text/plain" \
     -m 30 \
     -v \

JSON
----

    curl -X GET "http://www.codingexcuses.com/" \
     -H "Accept: application/json" \
     -m 30 \
     -v \

XML
---

    curl -X GET "http://www.codingexcuses.com/" \
     -H "Accept: application/xml" \
     -m 30 \
     -v \

JSONP
-----

    curl -X GET "http://www.codingexcuses.com/" \
     -H "Accept: application/javascript" \
     -m 30 \
     -v \

Or you can pass in the query string argument `?jsonp`

    <script src="http://www.codingexcuses.com/?jsonp"></script>

And of course HTML
------------------

    curl -X GET "http://www.codingexcuses.com/" \
     -m 30 \
     -v \

What if my boss sees!?
----------------------

The site also supports **https**, but you'll have to ignore the certificate.

    curl "https://www.codingexcuses.com/" -H "Accept: text/plain" --insecure

Install your own
----------------

    git clone git@github.com:aaronbassett/Bad-Tools.git
    cd Bad-Tools
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    export SECRET_KEY="ct=!)09l4(q*z3uf(+c9ra7@(10ni!x1%f6vlxc"
    # don't use that key though for obvious reasons
    python views.py

You can also deploy to Heroku

    heroku login
    heroku create
    git push heroku master
    heroku config:set SECRET_KEY="ct=!)09l4(q*z3uf(+c9ra7@(10ni!x1%f6vlxc"
    heroku ps:scale web=1
    heroku open

License
-------

http://aaron.mit-license.org/

