# Airspeed - a Python template engine

https://github.com/purcell/airspeed


## What is Airspeed?

Airspeed is a powerful and easy-to-use templating engine for Python
that aims for a high level of compatibility with the popular
[Velocity](http://velocity.apache.org/engine/devel/user-guide.html)
library for Java.

## Selling points

* Compatible with Velocity templates
* Compatible with Python 2.1 and greater, including Jython
* Features include macros definitions, conditionals, sub-templates and much more
* Airspeed is already being put to serious use
* Comprehensive set of unit tests; the entire library was written test-first
* Reasonably fast, especially when used with [mod_python](http://www.modpython.org/)
* A single Python module of a few kilobytes, and not the 500kb of Velocity
* Liberal licence (BSD-style)

    ## Why another templating engine?

    A number of excellent templating mechanisms already exist for Python,
    including [Cheetah](http://www.cheetahtemplate.org/), which has a
    syntax similar to Airspeed.

    However, in making Airspeed's syntax *identical* to that of Velocity,
    our goal is to allow Python programmers to prototype, replace or
    extend Java code that relies on Velocity.

    A simple example:

    ```python
    t = airspeed.Template("""
                          Old people:
                          #foreach ($person in $people)
                           #if($person.age > 95)
                            $person.name
                             #end
                            #end
                            """)
    people = [{'name': 'Bill', 'age': 100}, {'name': 'Bob', 'age': 90}]
    print t.merge(locals())
    ```

    You can also use "Loaders" to allow templates to include each other using the `#include` or `#parse` directives:

    ```
    % cat /tmp/1.txt
    Bingo!
    % cat /tmp/2.txt
    #parse ("2.txt")
    % python
    Python 2.4.4 (#1, May 28 2007, 00:47:43)
    [GCC 4.0.1 (Apple Computer, Inc. build 5367)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from airspeed import CachingFileLoader
    >>> loader = CachingFileLoader("/tmp")
    >>> template = loader.load_template("1.txt")
    >>> template.merge({}, loader=loader)
    'Bingo!\n'
    ```

    ### How compatible is Airspeed with Velocity?

    All Airspeed templates should work correctly with Velocity. The vast
    majority of Velocity templates will work correctly with Airspeed.

    ### What does and doesn't work?

    Airspeed currently implements a very significant subset of the
    Velocity functionality, including `$variables`, the `#if`, `#foreach`,
    `#macro`, `#include` and `#parse` directives, and `"$interpolated #strings()"`. Templates are unicode-safe.

    Compound expressions in `#set` directives should be parenthesised, since
    no implicit operator precedence rules are implemented.

    The output of templates in Airspeed is not yet 'whitespace compatible'
    with Velocity's rendering of the same templates, which generally does
    not matter for web applications. We also have still to implement
    support for in-line math expressions and some rarely-used details such
    as map literals.

    ### Where do I get it?

    https://github.com/purcell/sanityinc

    ### Getting started

    The
    [Velocity User Guide](http://jakarta.apache.org/velocity/user-guide.html)
    shows how to write templates.  Our unit tests show how to use the
    templates from your code.

    ### Reporting bugs

    Please feel free to create tickets for bugs or desired features.

    ### Who is to blame?

    Airspeed was conceived by Chris Tarttelin, and implemented jointly in
    a test-driven manner by Steve Purcell and Chris Tarttelin. We can be
    contacted by e-mail by using our first names (at) pythonconsulting dot
    com.

    <hr>

    [![](http://api.coderwall.com/purcell/endorsecount.png)](http://coderwall.com/purcell)

    [![](http://www.linkedin.com/img/webpromo/btn_liprofile_blue_80x15.png)](http://uk.linkedin.com/in/stevepurcell)

    [Steve Purcell's blog](http://www.sanityinc.com/) // [@sanityinc on Twitter](https://twitter.com/sanityinc)



