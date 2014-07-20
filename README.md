Bad Tools
=========

[![Compiling](http://imgs.xkcd.com/comics/compiling.png)](http://xkcd.com/303/)

[![Build Status](https://travis-ci.org/aaronbassett/Bad-Tools.svg?branch=master)](https://travis-ci.org/aaronbassett/Bad-Tools)

Blame your tools, blame the vendors, blame your workmates. Just as long as it is not your fault. Take the effort out of shifting the blame by using one of these ultra handy pre-written excuses.

The excuses are available in every format you could need so you can be properly lazy.

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

Configuration
-------------

You'll need to set an environment variable `SECRET_KEY` for the sessions to work.

    export SECRET_KEY="ct=!)09l4)hl8gmwgid%(q*z3uf(+c9ra7@(10ni!x1%f6vlxc"

_don't use that key though for obvious reasons_

License
-------

http://aaron.mit-license.org/

