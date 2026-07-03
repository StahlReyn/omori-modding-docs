Omori Modding Docs
=======================================
*TBA*

Contribution may be done by Pull Requests on GitHub.

Useful Guide for RST
--------------------

- https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
- https://sphinx-design.readthedocs.io/en/latest/index.html 
- https://lpn-doc-sphinx-primer.readthedocs.io/en/stable/index.html 

Local Testing
-------------

For local testing

Create Virtual Environment::

    python -m venv .venv
    .venv\Scripts\activate

Install Python Requirements::

    pip install -r docs/requirements.txt

Build and Serve::

    cd docs
    make html
    python -m http.server -d build/html 8000   

Auto build can be done by::

    pip install sphinx-autobuild
    sphinx-autobuild docs docs/build/html