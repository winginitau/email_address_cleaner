## How NOT to use Python

#### Note: although this works, it is not recommended. It is only kept for the purpose of illustrating bad python coding.

Good python, or being ‘pythonic’ is a combination of code style, architecture patterns, design approach, documentation, testing and writing code in a way that leverages the performance and readability of the language and the standard library.

A good place to start the ‘pythonic’ journey is https://peps.python.org/pep-0008/ and the great tutorials that teach the unique and powerful features of python: https://www.python.org/about/gettingstarted/

#### TL;DR

The code here is a python anti-pattern. Possibly the worst python 
code ever written :)

Coming from years of furious ANSI’ish C programing for embedded systems, becoming ‘pythonic’ was, and still is, a struggle.

Tired, under pressure and on a midnight deadline, this piece of C’ish, python vomit got the job done!

A good example of the wrong way to be pythonic and maybe useful for a giggle.

Please be kind :)

#### Background

I was leading a not-for-profit community organisation and for various reasons needed to call a general meeting with a prescribed notice period. To make dates work, the notice had to be sent by
midnight. It was 8pm.

It was decided that the recipient list needed to be broad. We had an Excel sheet with member emails (various formats), maintained inconsistently; an old mailing list in a Word document; several CC copies from MS Outlook; miscellaneous other lists; fragments updating addresses etc. In all, a large number of email addresses, in different formats, with many duplicates.

#### The Task

Combine all lists (manual paste to a single text file), strip noise (mailto: http: etc) parse various formats, check syntax accuracy, identify duplicates and produce a clean list for pasting into a BCC
field.

After years of C code with nothing but a cut-down ANSI C standard library it seemed that the elegance, utility and power of Python should get the job done easily and quickly.

3 hours and 50 minutes of fatigued, list indices debugging later, the email flew with a good result! This was prior to discovering a good python IDE too - was still using Eclipse C/C++ with the pydev
plugin.