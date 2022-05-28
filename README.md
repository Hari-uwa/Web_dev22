# Agile Web Development - CITS3403 - Project 1 

![Numberloo Screen](https://drive.google.com/file/d/17uaoIAvOImd4nF42Pe9IPE_beDy3HCjB/view?usp=sharing)

## Students
- Jennifer Nguyen 22757325
- Carmen Leong 22789943
- Dongwoo Noh 22999339
- Hari Vignesh 22874425

## 1. Purpose
- The purpose of this project is to demonstrate fundamental skills of building a web page, fromm the front end, to back end
- This web application provides users with a daily mini puzzle game where they can play and enjoy during their break time

## 2. Architecture of the Web Application
├── README.md
├── __pycache__
│   ├── config.cpython-38.pyc
│   ├── config.cpython-39.pyc
│   ├── microblog.cpython-38.pyc
│   └── microblog.cpython-39.pyc
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── dummy.cpython-38.pyc
│   │   ├── eqn_gen.cpython-38.pyc
│   │   ├── eqn_gen.cpython-39.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── routes.cpython-38.pyc
│   │   └── routes.cpython-39.pyc
│   ├── eqn_gen.py
│   ├── models
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── images
│   │   │   ├── big_tree.png
│   │   │   ├── favicon.jpg
│   │   │   ├── hourglass.gif
│   │   │   ├── howto.gif
│   │   │   ├── howtodarkmode.gif
│   │   │   ├── plant-unscreen.gif
│   │   │   ├── plant.png
│   │   │   ├── sad_face.png
│   │   │   ├── seed.png
│   │   │   ├── small_plant.png
│   │   │   ├── statsheader.gif
│   │   │   └── tree.png
│   │   ├── interactive.js
│   │   ├── script.js
│   │   └── style.css
│   └── templates
│       └── skeleton.html
├── app.db
├── config.py
├── microblog.py
├── migrations
│   ├── README
│   ├── __pycache__
│   │   ├── config.cpython-38.pyc
│   │   └── microblog.cpython-38.pyc
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 0717e0050e16_game_table.py
│       ├── __pycache__
│       │   ├── 0717e0050e16_game_table.cpython-38.pyc
│       │   ├── b34c7e8ed962_quiz_table.cpython-38.pyc
│       │   └── e9072b3f992a_user_table.cpython-38.pyc
│       ├── b34c7e8ed962_quiz_table.py
│       └── e9072b3f992a_user_table.py
├── notebooks
│   ├── Quiz_view_insert.ipynb
│   └── sql_queries_test.ipynb
├── requirements.txt
└── venv
    ├── bin
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── alembic
    │   ├── dotenv
    │   ├── easy_install
    │   ├── easy_install-3.8
    │   ├── flask
    │   ├── mako-render
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.8
    │   ├── python -> python3
    │   └── python3 -> /Library/Developer/CommandLineTools/usr/bin/python3
    ├── include
    ├── lib
    │   └── python3.8
    │       └── site-packages
    │           ├── Flask-2.1.2.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.rst
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── top_level.txt
    │           ├── Flask_Migrate-3.1.0.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── top_level.txt
    │           ├── Flask_SQLAlchemy-2.5.1.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.rst
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── Jinja2-3.1.2.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.rst
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── top_level.txt
    │           ├── Mako-1.2.0.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── top_level.txt
    │           ├── MarkupSafe-2.1.1.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.rst
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── SQLAlchemy-1.4.36-py3.8.egg-info
    │           │   ├── PKG-INFO
    │           │   ├── SOURCES.txt
    │           │   ├── dependency_links.txt
    │           │   ├── installed-files.txt
    │           │   ├── requires.txt
    │           │   └── top_level.txt
    │           ├── Werkzeug-2.1.2.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.rst
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── __pycache__
    │           │   └── easy_install.cpython-38.pyc
    │           ├── alembic
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── autogenerate
    │           │   │   ├── __init__.py
    │           │   │   ├── api.py
    │           │   │   ├── compare.py
    │           │   │   ├── render.py
    │           │   │   └── rewriter.py
    │           │   ├── command.py
    │           │   ├── config.py
    │           │   ├── context.py
    │           │   ├── context.pyi
    │           │   ├── ddl
    │           │   │   ├── __init__.py
    │           │   │   ├── base.py
    │           │   │   ├── impl.py
    │           │   │   ├── mssql.py
    │           │   │   ├── mysql.py
    │           │   │   ├── oracle.py
    │           │   │   ├── postgresql.py
    │           │   │   └── sqlite.py
    │           │   ├── environment.py
    │           │   ├── migration.py
    │           │   ├── op.py
    │           │   ├── op.pyi
    │           │   ├── operations
    │           │   │   ├── __init__.py
    │           │   │   ├── base.py
    │           │   │   ├── batch.py
    │           │   │   ├── ops.py
    │           │   │   ├── schemaobj.py
    │           │   │   └── toimpl.py
    │           │   ├── py.typed
    │           │   ├── runtime
    │           │   │   ├── __init__.py
    │           │   │   ├── environment.py
    │           │   │   └── migration.py
    │           │   ├── script
    │           │   │   ├── __init__.py
    │           │   │   ├── base.py
    │           │   │   ├── revision.py
    │           │   │   └── write_hooks.py
    │           │   ├── templates
    │           │   │   ├── async
    │           │   │   │   ├── README
    │           │   │   │   ├── alembic.ini.mako
    │           │   │   │   ├── env.py
    │           │   │   │   └── script.py.mako
    │           │   │   ├── generic
    │           │   │   │   ├── README
    │           │   │   │   ├── alembic.ini.mako
    │           │   │   │   ├── env.py
    │           │   │   │   └── script.py.mako
    │           │   │   ├── multidb
    │           │   │   │   ├── README
    │           │   │   │   ├── alembic.ini.mako
    │           │   │   │   ├── env.py
    │           │   │   │   └── script.py.mako
    │           │   │   └── pylons
    │           │   │       ├── README
    │           │   │       ├── alembic.ini.mako
    │           │   │       ├── env.py
    │           │   │       └── script.py.mako
    │           │   ├── testing
    │           │   │   ├── __init__.py
    │           │   │   ├── assertions.py
    │           │   │   ├── env.py
    │           │   │   ├── fixtures.py
    │           │   │   ├── plugin
    │           │   │   │   ├── __init__.py
    │           │   │   │   └── bootstrap.py
    │           │   │   ├── requirements.py
    │           │   │   ├── schemacompare.py
    │           │   │   ├── suite
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── _autogen_fixtures.py
    │           │   │   │   ├── test_autogen_comments.py
    │           │   │   │   ├── test_autogen_computed.py
    │           │   │   │   ├── test_autogen_diffs.py
    │           │   │   │   ├── test_autogen_fks.py
    │           │   │   │   ├── test_autogen_identity.py
    │           │   │   │   ├── test_environment.py
    │           │   │   │   └── test_op.py
    │           │   │   ├── util.py
    │           │   │   └── warnings.py
    │           │   └── util
    │           │       ├── __init__.py
    │           │       ├── compat.py
    │           │       ├── editor.py
    │           │       ├── exc.py
    │           │       ├── langhelpers.py
    │           │       ├── messaging.py
    │           │       ├── pyfiles.py
    │           │       └── sqla_compat.py
    │           ├── alembic-1.7.7.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── top_level.txt
    │           ├── click
    │           │   ├── __init__.py
    │           │   ├── _compat.py
    │           │   ├── _termui_impl.py
    │           │   ├── _textwrap.py
    │           │   ├── _winconsole.py
    │           │   ├── core.py
    │           │   ├── decorators.py
    │           │   ├── exceptions.py
    │           │   ├── formatting.py
    │           │   ├── globals.py
    │           │   ├── parser.py
    │           │   ├── py.typed
    │           │   ├── shell_completion.py
    │           │   ├── termui.py
    │           │   ├── testing.py
    │           │   ├── types.py
    │           │   └── utils.py
    │           ├── click-8.1.3.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.rst
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── dotenv
    │           │   ├── __init__.py
    │           │   ├── cli.py
    │           │   ├── ipython.py
    │           │   ├── main.py
    │           │   ├── parser.py
    │           │   ├── py.typed
    │           │   ├── variables.py
    │           │   └── version.py
    │           ├── easy_install.py
    │           ├── flask
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── app.py
    │           │   ├── blueprints.py
    │           │   ├── cli.py
    │           │   ├── config.py
    │           │   ├── ctx.py
    │           │   ├── debughelpers.py
    │           │   ├── globals.py
    │           │   ├── helpers.py
    │           │   ├── json
    │           │   │   ├── __init__.py
    │           │   │   └── tag.py
    │           │   ├── logging.py
    │           │   ├── py.typed
    │           │   ├── scaffold.py
    │           │   ├── sessions.py
    │           │   ├── signals.py
    │           │   ├── templating.py
    │           │   ├── testing.py
    │           │   ├── typing.py
    │           │   ├── views.py
    │           │   └── wrappers.py
    │           ├── flask_migrate
    │           │   ├── __init__.py
    │           │   ├── cli.py
    │           │   └── templates
    │           │       ├── aioflask
    │           │       │   ├── README
    │           │       │   ├── alembic.ini.mako
    │           │       │   ├── env.py
    │           │       │   └── script.py.mako
    │           │       ├── aioflask-multidb
    │           │       │   ├── README
    │           │       │   ├── alembic.ini.mako
    │           │       │   ├── env.py
    │           │       │   └── script.py.mako
    │           │       ├── flask
    │           │       │   ├── README
    │           │       │   ├── alembic.ini.mako
    │           │       │   ├── env.py
    │           │       │   └── script.py.mako
    │           │       └── flask-multidb
    │           │           ├── README
    │           │           ├── alembic.ini.mako
    │           │           ├── env.py
    │           │           └── script.py.mako
    │           ├── flask_sqlalchemy
    │           │   ├── __init__.py
    │           │   ├── _compat.py
    │           │   ├── model.py
    │           │   └── utils.py
    │           ├── importlib_metadata
    │           │   ├── __init__.py
    │           │   ├── _adapters.py
    │           │   ├── _collections.py
    │           │   ├── _compat.py
    │           │   ├── _functools.py
    │           │   ├── _itertools.py
    │           │   ├── _meta.py
    │           │   ├── _text.py
    │           │   └── py.typed
    │           ├── importlib_metadata-4.11.4.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── importlib_resources
    │           │   ├── __init__.py
    │           │   ├── _adapters.py
    │           │   ├── _common.py
    │           │   ├── _compat.py
    │           │   ├── _itertools.py
    │           │   ├── _legacy.py
    │           │   ├── abc.py
    │           │   ├── py.typed
    │           │   ├── readers.py
    │           │   ├── simple.py
    │           │   └── tests
    │           │       ├── __init__.py
    │           │       ├── _compat.py
    │           │       ├── data01
    │           │       │   ├── __init__.py
    │           │       │   ├── binary.file
    │           │       │   ├── subdirectory
    │           │       │   │   ├── __init__.py
    │           │       │   │   └── binary.file
    │           │       │   ├── utf-16.file
    │           │       │   └── utf-8.file
    │           │       ├── data02
    │           │       │   ├── __init__.py
    │           │       │   ├── one
    │           │       │   │   ├── __init__.py
    │           │       │   │   └── resource1.txt
    │           │       │   └── two
    │           │       │       ├── __init__.py
    │           │       │       └── resource2.txt
    │           │       ├── namespacedata01
    │           │       │   ├── binary.file
    │           │       │   ├── utf-16.file
    │           │       │   └── utf-8.file
    │           │       ├── test_compatibilty_files.py
    │           │       ├── test_contents.py
    │           │       ├── test_files.py
    │           │       ├── test_open.py
    │           │       ├── test_path.py
    │           │       ├── test_read.py
    │           │       ├── test_reader.py
    │           │       ├── test_resource.py
    │           │       ├── update-zips.py
    │           │       ├── util.py
    │           │       ├── zipdata01
    │           │       │   ├── __init__.py
    │           │       │   └── ziptestdata.zip
    │           │       └── zipdata02
    │           │           ├── __init__.py
    │           │           └── ziptestdata.zip
    │           ├── importlib_resources-5.7.1.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── itsdangerous
    │           │   ├── __init__.py
    │           │   ├── _json.py
    │           │   ├── encoding.py
    │           │   ├── exc.py
    │           │   ├── py.typed
    │           │   ├── serializer.py
    │           │   ├── signer.py
    │           │   ├── timed.py
    │           │   └── url_safe.py
    │           ├── itsdangerous-2.1.2.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.rst
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── jinja2
    │           │   ├── __init__.py
    │           │   ├── _identifier.py
    │           │   ├── async_utils.py
    │           │   ├── bccache.py
    │           │   ├── compiler.py
    │           │   ├── constants.py
    │           │   ├── debug.py
    │           │   ├── defaults.py
    │           │   ├── environment.py
    │           │   ├── exceptions.py
    │           │   ├── ext.py
    │           │   ├── filters.py
    │           │   ├── idtracking.py
    │           │   ├── lexer.py
    │           │   ├── loaders.py
    │           │   ├── meta.py
    │           │   ├── nativetypes.py
    │           │   ├── nodes.py
    │           │   ├── optimizer.py
    │           │   ├── parser.py
    │           │   ├── py.typed
    │           │   ├── runtime.py
    │           │   ├── sandbox.py
    │           │   ├── tests.py
    │           │   ├── utils.py
    │           │   └── visitor.py
    │           ├── mako
    │           │   ├── __init__.py
    │           │   ├── _ast_util.py
    │           │   ├── ast.py
    │           │   ├── cache.py
    │           │   ├── cmd.py
    │           │   ├── codegen.py
    │           │   ├── compat.py
    │           │   ├── exceptions.py
    │           │   ├── ext
    │           │   │   ├── __init__.py
    │           │   │   ├── autohandler.py
    │           │   │   ├── babelplugin.py
    │           │   │   ├── beaker_cache.py
    │           │   │   ├── extract.py
    │           │   │   ├── linguaplugin.py
    │           │   │   ├── preprocessors.py
    │           │   │   ├── pygmentplugin.py
    │           │   │   └── turbogears.py
    │           │   ├── filters.py
    │           │   ├── lexer.py
    │           │   ├── lookup.py
    │           │   ├── parsetree.py
    │           │   ├── pygen.py
    │           │   ├── pyparser.py
    │           │   ├── runtime.py
    │           │   ├── template.py
    │           │   ├── testing
    │           │   │   ├── __init__.py
    │           │   │   ├── _config.py
    │           │   │   ├── assertions.py
    │           │   │   ├── config.py
    │           │   │   ├── exclusions.py
    │           │   │   ├── fixtures.py
    │           │   │   └── helpers.py
    │           │   └── util.py
    │           ├── markupsafe
    │           │   ├── __init__.py
    │           │   ├── _native.py
    │           │   ├── _speedups.c
    │           │   ├── _speedups.pyi
    │           │   └── py.typed
    │           ├── pip
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── __pycache__
    │           │   │   ├── __init__.cpython-38.pyc
    │           │   │   └── __main__.cpython-38.pyc
    │           │   ├── _internal
    │           │   │   ├── __init__.py
    │           │   │   ├── __pycache__
    │           │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   ├── build_env.cpython-38.pyc
    │           │   │   │   ├── cache.cpython-38.pyc
    │           │   │   │   ├── configuration.cpython-38.pyc
    │           │   │   │   ├── download.cpython-38.pyc
    │           │   │   │   ├── exceptions.cpython-38.pyc
    │           │   │   │   ├── index.cpython-38.pyc
    │           │   │   │   ├── legacy_resolve.cpython-38.pyc
    │           │   │   │   ├── locations.cpython-38.pyc
    │           │   │   │   ├── pep425tags.cpython-38.pyc
    │           │   │   │   ├── pyproject.cpython-38.pyc
    │           │   │   │   └── wheel.cpython-38.pyc
    │           │   │   ├── build_env.py
    │           │   │   ├── cache.py
    │           │   │   ├── cli
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── autocompletion.cpython-38.pyc
    │           │   │   │   │   ├── base_command.cpython-38.pyc
    │           │   │   │   │   ├── cmdoptions.cpython-38.pyc
    │           │   │   │   │   ├── main_parser.cpython-38.pyc
    │           │   │   │   │   ├── parser.cpython-38.pyc
    │           │   │   │   │   └── status_codes.cpython-38.pyc
    │           │   │   │   ├── autocompletion.py
    │           │   │   │   ├── base_command.py
    │           │   │   │   ├── cmdoptions.py
    │           │   │   │   ├── main_parser.py
    │           │   │   │   ├── parser.py
    │           │   │   │   └── status_codes.py
    │           │   │   ├── commands
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── check.cpython-38.pyc
    │           │   │   │   │   ├── completion.cpython-38.pyc
    │           │   │   │   │   ├── configuration.cpython-38.pyc
    │           │   │   │   │   ├── debug.cpython-38.pyc
    │           │   │   │   │   ├── download.cpython-38.pyc
    │           │   │   │   │   ├── freeze.cpython-38.pyc
    │           │   │   │   │   ├── hash.cpython-38.pyc
    │           │   │   │   │   ├── help.cpython-38.pyc
    │           │   │   │   │   ├── install.cpython-38.pyc
    │           │   │   │   │   ├── list.cpython-38.pyc
    │           │   │   │   │   ├── search.cpython-38.pyc
    │           │   │   │   │   ├── show.cpython-38.pyc
    │           │   │   │   │   ├── uninstall.cpython-38.pyc
    │           │   │   │   │   └── wheel.cpython-38.pyc
    │           │   │   │   ├── check.py
    │           │   │   │   ├── completion.py
    │           │   │   │   ├── configuration.py
    │           │   │   │   ├── debug.py
    │           │   │   │   ├── download.py
    │           │   │   │   ├── freeze.py
    │           │   │   │   ├── hash.py
    │           │   │   │   ├── help.py
    │           │   │   │   ├── install.py
    │           │   │   │   ├── list.py
    │           │   │   │   ├── search.py
    │           │   │   │   ├── show.py
    │           │   │   │   ├── uninstall.py
    │           │   │   │   └── wheel.py
    │           │   │   ├── configuration.py
    │           │   │   ├── distributions
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── base.cpython-38.pyc
    │           │   │   │   │   ├── installed.cpython-38.pyc
    │           │   │   │   │   ├── source.cpython-38.pyc
    │           │   │   │   │   └── wheel.cpython-38.pyc
    │           │   │   │   ├── base.py
    │           │   │   │   ├── installed.py
    │           │   │   │   ├── source.py
    │           │   │   │   └── wheel.py
    │           │   │   ├── download.py
    │           │   │   ├── exceptions.py
    │           │   │   ├── index.py
    │           │   │   ├── legacy_resolve.py
    │           │   │   ├── locations.py
    │           │   │   ├── models
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── candidate.cpython-38.pyc
    │           │   │   │   │   ├── format_control.cpython-38.pyc
    │           │   │   │   │   ├── index.cpython-38.pyc
    │           │   │   │   │   ├── link.cpython-38.pyc
    │           │   │   │   │   ├── search_scope.cpython-38.pyc
    │           │   │   │   │   ├── selection_prefs.cpython-38.pyc
    │           │   │   │   │   └── target_python.cpython-38.pyc
    │           │   │   │   ├── candidate.py
    │           │   │   │   ├── format_control.py
    │           │   │   │   ├── index.py
    │           │   │   │   ├── link.py
    │           │   │   │   ├── search_scope.py
    │           │   │   │   ├── selection_prefs.py
    │           │   │   │   └── target_python.py
    │           │   │   ├── operations
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── check.cpython-38.pyc
    │           │   │   │   │   ├── freeze.cpython-38.pyc
    │           │   │   │   │   └── prepare.cpython-38.pyc
    │           │   │   │   ├── check.py
    │           │   │   │   ├── freeze.py
    │           │   │   │   └── prepare.py
    │           │   │   ├── pep425tags.py
    │           │   │   ├── pyproject.py
    │           │   │   ├── req
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── constructors.cpython-38.pyc
    │           │   │   │   │   ├── req_file.cpython-38.pyc
    │           │   │   │   │   ├── req_install.cpython-38.pyc
    │           │   │   │   │   ├── req_set.cpython-38.pyc
    │           │   │   │   │   ├── req_tracker.cpython-38.pyc
    │           │   │   │   │   └── req_uninstall.cpython-38.pyc
    │           │   │   │   ├── constructors.py
    │           │   │   │   ├── req_file.py
    │           │   │   │   ├── req_install.py
    │           │   │   │   ├── req_set.py
    │           │   │   │   ├── req_tracker.py
    │           │   │   │   └── req_uninstall.py
    │           │   │   ├── utils
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── appdirs.cpython-38.pyc
    │           │   │   │   │   ├── compat.cpython-38.pyc
    │           │   │   │   │   ├── deprecation.cpython-38.pyc
    │           │   │   │   │   ├── encoding.cpython-38.pyc
    │           │   │   │   │   ├── filesystem.cpython-38.pyc
    │           │   │   │   │   ├── glibc.cpython-38.pyc
    │           │   │   │   │   ├── hashes.cpython-38.pyc
    │           │   │   │   │   ├── logging.cpython-38.pyc
    │           │   │   │   │   ├── marker_files.cpython-38.pyc
    │           │   │   │   │   ├── misc.cpython-38.pyc
    │           │   │   │   │   ├── models.cpython-38.pyc
    │           │   │   │   │   ├── outdated.cpython-38.pyc
    │           │   │   │   │   ├── packaging.cpython-38.pyc
    │           │   │   │   │   ├── setuptools_build.cpython-38.pyc
    │           │   │   │   │   ├── temp_dir.cpython-38.pyc
    │           │   │   │   │   ├── typing.cpython-38.pyc
    │           │   │   │   │   ├── ui.cpython-38.pyc
    │           │   │   │   │   └── virtualenv.cpython-38.pyc
    │           │   │   │   ├── appdirs.py
    │           │   │   │   ├── compat.py
    │           │   │   │   ├── deprecation.py
    │           │   │   │   ├── encoding.py
    │           │   │   │   ├── filesystem.py
    │           │   │   │   ├── glibc.py
    │           │   │   │   ├── hashes.py
    │           │   │   │   ├── logging.py
    │           │   │   │   ├── marker_files.py
    │           │   │   │   ├── misc.py
    │           │   │   │   ├── models.py
    │           │   │   │   ├── outdated.py
    │           │   │   │   ├── packaging.py
    │           │   │   │   ├── setuptools_build.py
    │           │   │   │   ├── temp_dir.py
    │           │   │   │   ├── typing.py
    │           │   │   │   ├── ui.py
    │           │   │   │   └── virtualenv.py
    │           │   │   ├── vcs
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── bazaar.cpython-38.pyc
    │           │   │   │   │   ├── git.cpython-38.pyc
    │           │   │   │   │   ├── mercurial.cpython-38.pyc
    │           │   │   │   │   ├── subversion.cpython-38.pyc
    │           │   │   │   │   └── versioncontrol.cpython-38.pyc
    │           │   │   │   ├── bazaar.py
    │           │   │   │   ├── git.py
    │           │   │   │   ├── mercurial.py
    │           │   │   │   ├── subversion.py
    │           │   │   │   └── versioncontrol.py
    │           │   │   └── wheel.py
    │           │   └── _vendor
    │           │       ├── __init__.py
    │           │       ├── __pycache__
    │           │       │   ├── __init__.cpython-38.pyc
    │           │       │   ├── appdirs.cpython-38.pyc
    │           │       │   ├── distro.cpython-38.pyc
    │           │       │   ├── ipaddress.cpython-38.pyc
    │           │       │   ├── pyparsing.cpython-38.pyc
    │           │       │   ├── retrying.cpython-38.pyc
    │           │       │   └── six.cpython-38.pyc
    │           │       ├── appdirs.py
    │           │       ├── cachecontrol
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── _cmd.cpython-38.pyc
    │           │       │   │   ├── adapter.cpython-38.pyc
    │           │       │   │   ├── cache.cpython-38.pyc
    │           │       │   │   ├── compat.cpython-38.pyc
    │           │       │   │   ├── controller.cpython-38.pyc
    │           │       │   │   ├── filewrapper.cpython-38.pyc
    │           │       │   │   ├── heuristics.cpython-38.pyc
    │           │       │   │   ├── serialize.cpython-38.pyc
    │           │       │   │   └── wrapper.cpython-38.pyc
    │           │       │   ├── _cmd.py
    │           │       │   ├── adapter.py
    │           │       │   ├── cache.py
    │           │       │   ├── caches
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   ├── file_cache.cpython-38.pyc
    │           │       │   │   │   └── redis_cache.cpython-38.pyc
    │           │       │   │   ├── file_cache.py
    │           │       │   │   └── redis_cache.py
    │           │       │   ├── compat.py
    │           │       │   ├── controller.py
    │           │       │   ├── filewrapper.py
    │           │       │   ├── heuristics.py
    │           │       │   ├── serialize.py
    │           │       │   └── wrapper.py
    │           │       ├── certifi
    │           │       │   ├── __init__.py
    │           │       │   ├── __main__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── __main__.cpython-38.pyc
    │           │       │   │   └── core.cpython-38.pyc
    │           │       │   ├── cacert.pem
    │           │       │   └── core.py
    │           │       ├── chardet
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── big5freq.cpython-38.pyc
    │           │       │   │   ├── big5prober.cpython-38.pyc
    │           │       │   │   ├── chardistribution.cpython-38.pyc
    │           │       │   │   ├── charsetgroupprober.cpython-38.pyc
    │           │       │   │   ├── charsetprober.cpython-38.pyc
    │           │       │   │   ├── codingstatemachine.cpython-38.pyc
    │           │       │   │   ├── compat.cpython-38.pyc
    │           │       │   │   ├── cp949prober.cpython-38.pyc
    │           │       │   │   ├── enums.cpython-38.pyc
    │           │       │   │   ├── escprober.cpython-38.pyc
    │           │       │   │   ├── escsm.cpython-38.pyc
    │           │       │   │   ├── eucjpprober.cpython-38.pyc
    │           │       │   │   ├── euckrfreq.cpython-38.pyc
    │           │       │   │   ├── euckrprober.cpython-38.pyc
    │           │       │   │   ├── euctwfreq.cpython-38.pyc
    │           │       │   │   ├── euctwprober.cpython-38.pyc
    │           │       │   │   ├── gb2312freq.cpython-38.pyc
    │           │       │   │   ├── gb2312prober.cpython-38.pyc
    │           │       │   │   ├── hebrewprober.cpython-38.pyc
    │           │       │   │   ├── jisfreq.cpython-38.pyc
    │           │       │   │   ├── jpcntx.cpython-38.pyc
    │           │       │   │   ├── langbulgarianmodel.cpython-38.pyc
    │           │       │   │   ├── langcyrillicmodel.cpython-38.pyc
    │           │       │   │   ├── langgreekmodel.cpython-38.pyc
    │           │       │   │   ├── langhebrewmodel.cpython-38.pyc
    │           │       │   │   ├── langhungarianmodel.cpython-38.pyc
    │           │       │   │   ├── langthaimodel.cpython-38.pyc
    │           │       │   │   ├── langturkishmodel.cpython-38.pyc
    │           │       │   │   ├── latin1prober.cpython-38.pyc
    │           │       │   │   ├── mbcharsetprober.cpython-38.pyc
    │           │       │   │   ├── mbcsgroupprober.cpython-38.pyc
    │           │       │   │   ├── mbcssm.cpython-38.pyc
    │           │       │   │   ├── sbcharsetprober.cpython-38.pyc
    │           │       │   │   ├── sbcsgroupprober.cpython-38.pyc
    │           │       │   │   ├── sjisprober.cpython-38.pyc
    │           │       │   │   ├── universaldetector.cpython-38.pyc
    │           │       │   │   ├── utf8prober.cpython-38.pyc
    │           │       │   │   └── version.cpython-38.pyc
    │           │       │   ├── big5freq.py
    │           │       │   ├── big5prober.py
    │           │       │   ├── chardistribution.py
    │           │       │   ├── charsetgroupprober.py
    │           │       │   ├── charsetprober.py
    │           │       │   ├── cli
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   └── chardetect.cpython-38.pyc
    │           │       │   │   └── chardetect.py
    │           │       │   ├── codingstatemachine.py
    │           │       │   ├── compat.py
    │           │       │   ├── cp949prober.py
    │           │       │   ├── enums.py
    │           │       │   ├── escprober.py
    │           │       │   ├── escsm.py
    │           │       │   ├── eucjpprober.py
    │           │       │   ├── euckrfreq.py
    │           │       │   ├── euckrprober.py
    │           │       │   ├── euctwfreq.py
    │           │       │   ├── euctwprober.py
    │           │       │   ├── gb2312freq.py
    │           │       │   ├── gb2312prober.py
    │           │       │   ├── hebrewprober.py
    │           │       │   ├── jisfreq.py
    │           │       │   ├── jpcntx.py
    │           │       │   ├── langbulgarianmodel.py
    │           │       │   ├── langcyrillicmodel.py
    │           │       │   ├── langgreekmodel.py
    │           │       │   ├── langhebrewmodel.py
    │           │       │   ├── langhungarianmodel.py
    │           │       │   ├── langthaimodel.py
    │           │       │   ├── langturkishmodel.py
    │           │       │   ├── latin1prober.py
    │           │       │   ├── mbcharsetprober.py
    │           │       │   ├── mbcsgroupprober.py
    │           │       │   ├── mbcssm.py
    │           │       │   ├── sbcharsetprober.py
    │           │       │   ├── sbcsgroupprober.py
    │           │       │   ├── sjisprober.py
    │           │       │   ├── universaldetector.py
    │           │       │   ├── utf8prober.py
    │           │       │   └── version.py
    │           │       ├── colorama
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── ansi.cpython-38.pyc
    │           │       │   │   ├── ansitowin32.cpython-38.pyc
    │           │       │   │   ├── initialise.cpython-38.pyc
    │           │       │   │   ├── win32.cpython-38.pyc
    │           │       │   │   └── winterm.cpython-38.pyc
    │           │       │   ├── ansi.py
    │           │       │   ├── ansitowin32.py
    │           │       │   ├── initialise.py
    │           │       │   ├── win32.py
    │           │       │   └── winterm.py
    │           │       ├── distlib
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── compat.cpython-38.pyc
    │           │       │   │   ├── database.cpython-38.pyc
    │           │       │   │   ├── index.cpython-38.pyc
    │           │       │   │   ├── locators.cpython-38.pyc
    │           │       │   │   ├── manifest.cpython-38.pyc
    │           │       │   │   ├── markers.cpython-38.pyc
    │           │       │   │   ├── metadata.cpython-38.pyc
    │           │       │   │   ├── resources.cpython-38.pyc
    │           │       │   │   ├── scripts.cpython-38.pyc
    │           │       │   │   ├── util.cpython-38.pyc
    │           │       │   │   ├── version.cpython-38.pyc
    │           │       │   │   └── wheel.cpython-38.pyc
    │           │       │   ├── _backport
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   ├── misc.cpython-38.pyc
    │           │       │   │   │   ├── shutil.cpython-38.pyc
    │           │       │   │   │   ├── sysconfig.cpython-38.pyc
    │           │       │   │   │   └── tarfile.cpython-38.pyc
    │           │       │   │   ├── misc.py
    │           │       │   │   ├── shutil.py
    │           │       │   │   ├── sysconfig.cfg
    │           │       │   │   ├── sysconfig.py
    │           │       │   │   └── tarfile.py
    │           │       │   ├── compat.py
    │           │       │   ├── database.py
    │           │       │   ├── index.py
    │           │       │   ├── locators.py
    │           │       │   ├── manifest.py
    │           │       │   ├── markers.py
    │           │       │   ├── metadata.py
    │           │       │   ├── resources.py
    │           │       │   ├── scripts.py
    │           │       │   ├── t32.exe
    │           │       │   ├── t64.exe
    │           │       │   ├── util.py
    │           │       │   ├── version.py
    │           │       │   ├── w32.exe
    │           │       │   ├── w64.exe
    │           │       │   └── wheel.py
    │           │       ├── distro.py
    │           │       ├── html5lib
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── _ihatexml.cpython-38.pyc
    │           │       │   │   ├── _inputstream.cpython-38.pyc
    │           │       │   │   ├── _tokenizer.cpython-38.pyc
    │           │       │   │   ├── _utils.cpython-38.pyc
    │           │       │   │   ├── constants.cpython-38.pyc
    │           │       │   │   ├── html5parser.cpython-38.pyc
    │           │       │   │   └── serializer.cpython-38.pyc
    │           │       │   ├── _ihatexml.py
    │           │       │   ├── _inputstream.py
    │           │       │   ├── _tokenizer.py
    │           │       │   ├── _trie
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   ├── _base.cpython-38.pyc
    │           │       │   │   │   ├── datrie.cpython-38.pyc
    │           │       │   │   │   └── py.cpython-38.pyc
    │           │       │   │   ├── _base.py
    │           │       │   │   ├── datrie.py
    │           │       │   │   └── py.py
    │           │       │   ├── _utils.py
    │           │       │   ├── constants.py
    │           │       │   ├── filters
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   ├── alphabeticalattributes.cpython-38.pyc
    │           │       │   │   │   ├── base.cpython-38.pyc
    │           │       │   │   │   ├── inject_meta_charset.cpython-38.pyc
    │           │       │   │   │   ├── lint.cpython-38.pyc
    │           │       │   │   │   ├── optionaltags.cpython-38.pyc
    │           │       │   │   │   ├── sanitizer.cpython-38.pyc
    │           │       │   │   │   └── whitespace.cpython-38.pyc
    │           │       │   │   ├── alphabeticalattributes.py
    │           │       │   │   ├── base.py
    │           │       │   │   ├── inject_meta_charset.py
    │           │       │   │   ├── lint.py
    │           │       │   │   ├── optionaltags.py
    │           │       │   │   ├── sanitizer.py
    │           │       │   │   └── whitespace.py
    │           │       │   ├── html5parser.py
    │           │       │   ├── serializer.py
    │           │       │   ├── treeadapters
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   ├── genshi.cpython-38.pyc
    │           │       │   │   │   └── sax.cpython-38.pyc
    │           │       │   │   ├── genshi.py
    │           │       │   │   └── sax.py
    │           │       │   ├── treebuilders
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   ├── base.cpython-38.pyc
    │           │       │   │   │   ├── dom.cpython-38.pyc
    │           │       │   │   │   ├── etree.cpython-38.pyc
    │           │       │   │   │   └── etree_lxml.cpython-38.pyc
    │           │       │   │   ├── base.py
    │           │       │   │   ├── dom.py
    │           │       │   │   ├── etree.py
    │           │       │   │   └── etree_lxml.py
    │           │       │   └── treewalkers
    │           │       │       ├── __init__.py
    │           │       │       ├── __pycache__
    │           │       │       │   ├── __init__.cpython-38.pyc
    │           │       │       │   ├── base.cpython-38.pyc
    │           │       │       │   ├── dom.cpython-38.pyc
    │           │       │       │   ├── etree.cpython-38.pyc
    │           │       │       │   ├── etree_lxml.cpython-38.pyc
    │           │       │       │   └── genshi.cpython-38.pyc
    │           │       │       ├── base.py
    │           │       │       ├── dom.py
    │           │       │       ├── etree.py
    │           │       │       ├── etree_lxml.py
    │           │       │       └── genshi.py
    │           │       ├── idna
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── codec.cpython-38.pyc
    │           │       │   │   ├── compat.cpython-38.pyc
    │           │       │   │   ├── core.cpython-38.pyc
    │           │       │   │   ├── idnadata.cpython-38.pyc
    │           │       │   │   ├── intranges.cpython-38.pyc
    │           │       │   │   ├── package_data.cpython-38.pyc
    │           │       │   │   └── uts46data.cpython-38.pyc
    │           │       │   ├── codec.py
    │           │       │   ├── compat.py
    │           │       │   ├── core.py
    │           │       │   ├── idnadata.py
    │           │       │   ├── intranges.py
    │           │       │   ├── package_data.py
    │           │       │   └── uts46data.py
    │           │       ├── ipaddress.py
    │           │       ├── lockfile
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── linklockfile.cpython-38.pyc
    │           │       │   │   ├── mkdirlockfile.cpython-38.pyc
    │           │       │   │   ├── pidlockfile.cpython-38.pyc
    │           │       │   │   ├── sqlitelockfile.cpython-38.pyc
    │           │       │   │   └── symlinklockfile.cpython-38.pyc
    │           │       │   ├── linklockfile.py
    │           │       │   ├── mkdirlockfile.py
    │           │       │   ├── pidlockfile.py
    │           │       │   ├── sqlitelockfile.py
    │           │       │   └── symlinklockfile.py
    │           │       ├── msgpack
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── _version.cpython-38.pyc
    │           │       │   │   ├── exceptions.cpython-38.pyc
    │           │       │   │   └── fallback.cpython-38.pyc
    │           │       │   ├── _version.py
    │           │       │   ├── exceptions.py
    │           │       │   └── fallback.py
    │           │       ├── packaging
    │           │       │   ├── __about__.py
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __about__.cpython-38.pyc
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── _compat.cpython-38.pyc
    │           │       │   │   ├── _structures.cpython-38.pyc
    │           │       │   │   ├── markers.cpython-38.pyc
    │           │       │   │   ├── requirements.cpython-38.pyc
    │           │       │   │   ├── specifiers.cpython-38.pyc
    │           │       │   │   ├── utils.cpython-38.pyc
    │           │       │   │   └── version.cpython-38.pyc
    │           │       │   ├── _compat.py
    │           │       │   ├── _structures.py
    │           │       │   ├── markers.py
    │           │       │   ├── requirements.py
    │           │       │   ├── specifiers.py
    │           │       │   ├── utils.py
    │           │       │   └── version.py
    │           │       ├── pep517
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── _in_process.cpython-38.pyc
    │           │       │   │   ├── build.cpython-38.pyc
    │           │       │   │   ├── check.cpython-38.pyc
    │           │       │   │   ├── colorlog.cpython-38.pyc
    │           │       │   │   ├── compat.cpython-38.pyc
    │           │       │   │   ├── envbuild.cpython-38.pyc
    │           │       │   │   └── wrappers.cpython-38.pyc
    │           │       │   ├── _in_process.py
    │           │       │   ├── build.py
    │           │       │   ├── check.py
    │           │       │   ├── colorlog.py
    │           │       │   ├── compat.py
    │           │       │   ├── envbuild.py
    │           │       │   └── wrappers.py
    │           │       ├── pkg_resources
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   └── py31compat.cpython-38.pyc
    │           │       │   └── py31compat.py
    │           │       ├── progress
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── bar.cpython-38.pyc
    │           │       │   │   ├── counter.cpython-38.pyc
    │           │       │   │   └── spinner.cpython-38.pyc
    │           │       │   ├── bar.py
    │           │       │   ├── counter.py
    │           │       │   └── spinner.py
    │           │       ├── pyparsing.py
    │           │       ├── pytoml
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── core.cpython-38.pyc
    │           │       │   │   ├── parser.cpython-38.pyc
    │           │       │   │   ├── test.cpython-38.pyc
    │           │       │   │   ├── utils.cpython-38.pyc
    │           │       │   │   └── writer.cpython-38.pyc
    │           │       │   ├── core.py
    │           │       │   ├── parser.py
    │           │       │   ├── test.py
    │           │       │   ├── utils.py
    │           │       │   └── writer.py
    │           │       ├── requests
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── __version__.cpython-38.pyc
    │           │       │   │   ├── _internal_utils.cpython-38.pyc
    │           │       │   │   ├── adapters.cpython-38.pyc
    │           │       │   │   ├── api.cpython-38.pyc
    │           │       │   │   ├── auth.cpython-38.pyc
    │           │       │   │   ├── certs.cpython-38.pyc
    │           │       │   │   ├── compat.cpython-38.pyc
    │           │       │   │   ├── cookies.cpython-38.pyc
    │           │       │   │   ├── exceptions.cpython-38.pyc
    │           │       │   │   ├── help.cpython-38.pyc
    │           │       │   │   ├── hooks.cpython-38.pyc
    │           │       │   │   ├── models.cpython-38.pyc
    │           │       │   │   ├── packages.cpython-38.pyc
    │           │       │   │   ├── sessions.cpython-38.pyc
    │           │       │   │   ├── status_codes.cpython-38.pyc
    │           │       │   │   ├── structures.cpython-38.pyc
    │           │       │   │   └── utils.cpython-38.pyc
    │           │       │   ├── __version__.py
    │           │       │   ├── _internal_utils.py
    │           │       │   ├── adapters.py
    │           │       │   ├── api.py
    │           │       │   ├── auth.py
    │           │       │   ├── certs.py
    │           │       │   ├── compat.py
    │           │       │   ├── cookies.py
    │           │       │   ├── exceptions.py
    │           │       │   ├── help.py
    │           │       │   ├── hooks.py
    │           │       │   ├── models.py
    │           │       │   ├── packages.py
    │           │       │   ├── sessions.py
    │           │       │   ├── status_codes.py
    │           │       │   ├── structures.py
    │           │       │   └── utils.py
    │           │       ├── retrying.py
    │           │       ├── six.py
    │           │       ├── urllib3
    │           │       │   ├── __init__.py
    │           │       │   ├── __pycache__
    │           │       │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   ├── _collections.cpython-38.pyc
    │           │       │   │   ├── connection.cpython-38.pyc
    │           │       │   │   ├── connectionpool.cpython-38.pyc
    │           │       │   │   ├── exceptions.cpython-38.pyc
    │           │       │   │   ├── fields.cpython-38.pyc
    │           │       │   │   ├── filepost.cpython-38.pyc
    │           │       │   │   ├── poolmanager.cpython-38.pyc
    │           │       │   │   ├── request.cpython-38.pyc
    │           │       │   │   └── response.cpython-38.pyc
    │           │       │   ├── _collections.py
    │           │       │   ├── connection.py
    │           │       │   ├── connectionpool.py
    │           │       │   ├── contrib
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   ├── _appengine_environ.cpython-38.pyc
    │           │       │   │   │   ├── appengine.cpython-38.pyc
    │           │       │   │   │   ├── ntlmpool.cpython-38.pyc
    │           │       │   │   │   ├── pyopenssl.cpython-38.pyc
    │           │       │   │   │   ├── securetransport.cpython-38.pyc
    │           │       │   │   │   └── socks.cpython-38.pyc
    │           │       │   │   ├── _appengine_environ.py
    │           │       │   │   ├── _securetransport
    │           │       │   │   │   ├── __init__.py
    │           │       │   │   │   ├── __pycache__
    │           │       │   │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   │   ├── bindings.cpython-38.pyc
    │           │       │   │   │   │   └── low_level.cpython-38.pyc
    │           │       │   │   │   ├── bindings.py
    │           │       │   │   │   └── low_level.py
    │           │       │   │   ├── appengine.py
    │           │       │   │   ├── ntlmpool.py
    │           │       │   │   ├── pyopenssl.py
    │           │       │   │   ├── securetransport.py
    │           │       │   │   └── socks.py
    │           │       │   ├── exceptions.py
    │           │       │   ├── fields.py
    │           │       │   ├── filepost.py
    │           │       │   ├── packages
    │           │       │   │   ├── __init__.py
    │           │       │   │   ├── __pycache__
    │           │       │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   └── six.cpython-38.pyc
    │           │       │   │   ├── backports
    │           │       │   │   │   ├── __init__.py
    │           │       │   │   │   ├── __pycache__
    │           │       │   │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   │   └── makefile.cpython-38.pyc
    │           │       │   │   │   └── makefile.py
    │           │       │   │   ├── rfc3986
    │           │       │   │   │   ├── __init__.py
    │           │       │   │   │   ├── __pycache__
    │           │       │   │   │   │   ├── __init__.cpython-38.pyc
    │           │       │   │   │   │   ├── _mixin.cpython-38.pyc
    │           │       │   │   │   │   ├── abnf_regexp.cpython-38.pyc
    │           │       │   │   │   │   ├── api.cpython-38.pyc
    │           │       │   │   │   │   ├── builder.cpython-38.pyc
    │           │       │   │   │   │   ├── compat.cpython-38.pyc
    │           │       │   │   │   │   ├── exceptions.cpython-38.pyc
    │           │       │   │   │   │   ├── iri.cpython-38.pyc
    │           │       │   │   │   │   ├── misc.cpython-38.pyc
    │           │       │   │   │   │   ├── normalizers.cpython-38.pyc
    │           │       │   │   │   │   ├── parseresult.cpython-38.pyc
    │           │       │   │   │   │   ├── uri.cpython-38.pyc
    │           │       │   │   │   │   └── validators.cpython-38.pyc
    │           │       │   │   │   ├── _mixin.py
    │           │       │   │   │   ├── abnf_regexp.py
    │           │       │   │   │   ├── api.py
    │           │       │   │   │   ├── builder.py
    │           │       │   │   │   ├── compat.py
    │           │       │   │   │   ├── exceptions.py
    │           │       │   │   │   ├── iri.py
    │           │       │   │   │   ├── misc.py
    │           │       │   │   │   ├── normalizers.py
    │           │       │   │   │   ├── parseresult.py
    │           │       │   │   │   ├── uri.py
    │           │       │   │   │   └── validators.py
    │           │       │   │   ├── six.py
    │           │       │   │   └── ssl_match_hostname
    │           │       │   │       ├── __init__.py
    │           │       │   │       ├── __pycache__
    │           │       │   │       │   ├── __init__.cpython-38.pyc
    │           │       │   │       │   └── _implementation.cpython-38.pyc
    │           │       │   │       └── _implementation.py
    │           │       │   ├── poolmanager.py
    │           │       │   ├── request.py
    │           │       │   ├── response.py
    │           │       │   └── util
    │           │       │       ├── __init__.py
    │           │       │       ├── __pycache__
    │           │       │       │   ├── __init__.cpython-38.pyc
    │           │       │       │   ├── connection.cpython-38.pyc
    │           │       │       │   ├── queue.cpython-38.pyc
    │           │       │       │   ├── request.cpython-38.pyc
    │           │       │       │   ├── response.cpython-38.pyc
    │           │       │       │   ├── retry.cpython-38.pyc
    │           │       │       │   ├── ssl_.cpython-38.pyc
    │           │       │       │   ├── timeout.cpython-38.pyc
    │           │       │       │   ├── url.cpython-38.pyc
    │           │       │       │   └── wait.cpython-38.pyc
    │           │       │       ├── connection.py
    │           │       │       ├── queue.py
    │           │       │       ├── request.py
    │           │       │       ├── response.py
    │           │       │       ├── retry.py
    │           │       │       ├── ssl_.py
    │           │       │       ├── timeout.py
    │           │       │       ├── url.py
    │           │       │       └── wait.py
    │           │       └── webencodings
    │           │           ├── __init__.py
    │           │           ├── __pycache__
    │           │           │   ├── __init__.cpython-38.pyc
    │           │           │   ├── labels.cpython-38.pyc
    │           │           │   ├── mklabels.cpython-38.pyc
    │           │           │   ├── tests.cpython-38.pyc
    │           │           │   └── x_user_defined.cpython-38.pyc
    │           │           ├── labels.py
    │           │           ├── mklabels.py
    │           │           ├── tests.py
    │           │           └── x_user_defined.py
    │           ├── pip-19.2.3.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.txt
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── top_level.txt
    │           ├── pkg_resources
    │           │   ├── __init__.py
    │           │   ├── __pycache__
    │           │   │   ├── __init__.cpython-38.pyc
    │           │   │   └── py31compat.cpython-38.pyc
    │           │   ├── _vendor
    │           │   │   ├── __init__.py
    │           │   │   ├── __pycache__
    │           │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   ├── appdirs.cpython-38.pyc
    │           │   │   │   ├── pyparsing.cpython-38.pyc
    │           │   │   │   └── six.cpython-38.pyc
    │           │   │   ├── appdirs.py
    │           │   │   ├── packaging
    │           │   │   │   ├── __about__.py
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __about__.cpython-38.pyc
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── _compat.cpython-38.pyc
    │           │   │   │   │   ├── _structures.cpython-38.pyc
    │           │   │   │   │   ├── markers.cpython-38.pyc
    │           │   │   │   │   ├── requirements.cpython-38.pyc
    │           │   │   │   │   ├── specifiers.cpython-38.pyc
    │           │   │   │   │   ├── utils.cpython-38.pyc
    │           │   │   │   │   └── version.cpython-38.pyc
    │           │   │   │   ├── _compat.py
    │           │   │   │   ├── _structures.py
    │           │   │   │   ├── markers.py
    │           │   │   │   ├── requirements.py
    │           │   │   │   ├── specifiers.py
    │           │   │   │   ├── utils.py
    │           │   │   │   └── version.py
    │           │   │   ├── pyparsing.py
    │           │   │   └── six.py
    │           │   ├── extern
    │           │   │   ├── __init__.py
    │           │   │   └── __pycache__
    │           │   │       └── __init__.cpython-38.pyc
    │           │   └── py31compat.py
    │           ├── python_dotenv-0.20.0.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── top_level.txt
    │           ├── setuptools
    │           │   ├── __init__.py
    │           │   ├── __pycache__
    │           │   │   ├── __init__.cpython-38.pyc
    │           │   │   ├── _deprecation_warning.cpython-38.pyc
    │           │   │   ├── archive_util.cpython-38.pyc
    │           │   │   ├── build_meta.cpython-38.pyc
    │           │   │   ├── config.cpython-38.pyc
    │           │   │   ├── dep_util.cpython-38.pyc
    │           │   │   ├── depends.cpython-38.pyc
    │           │   │   ├── dist.cpython-38.pyc
    │           │   │   ├── extension.cpython-38.pyc
    │           │   │   ├── glibc.cpython-38.pyc
    │           │   │   ├── glob.cpython-38.pyc
    │           │   │   ├── launch.cpython-38.pyc
    │           │   │   ├── lib2to3_ex.cpython-38.pyc
    │           │   │   ├── monkey.cpython-38.pyc
    │           │   │   ├── msvc.cpython-38.pyc
    │           │   │   ├── namespaces.cpython-38.pyc
    │           │   │   ├── package_index.cpython-38.pyc
    │           │   │   ├── pep425tags.cpython-38.pyc
    │           │   │   ├── py27compat.cpython-38.pyc
    │           │   │   ├── py31compat.cpython-38.pyc
    │           │   │   ├── py33compat.cpython-38.pyc
    │           │   │   ├── sandbox.cpython-38.pyc
    │           │   │   ├── site-patch.cpython-38.pyc
    │           │   │   ├── ssl_support.cpython-38.pyc
    │           │   │   ├── unicode_utils.cpython-38.pyc
    │           │   │   ├── version.cpython-38.pyc
    │           │   │   ├── wheel.cpython-38.pyc
    │           │   │   └── windows_support.cpython-38.pyc
    │           │   ├── _deprecation_warning.py
    │           │   ├── _vendor
    │           │   │   ├── __init__.py
    │           │   │   ├── __pycache__
    │           │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   ├── pyparsing.cpython-38.pyc
    │           │   │   │   └── six.cpython-38.pyc
    │           │   │   ├── packaging
    │           │   │   │   ├── __about__.py
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __pycache__
    │           │   │   │   │   ├── __about__.cpython-38.pyc
    │           │   │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   │   ├── _compat.cpython-38.pyc
    │           │   │   │   │   ├── _structures.cpython-38.pyc
    │           │   │   │   │   ├── markers.cpython-38.pyc
    │           │   │   │   │   ├── requirements.cpython-38.pyc
    │           │   │   │   │   ├── specifiers.cpython-38.pyc
    │           │   │   │   │   ├── utils.cpython-38.pyc
    │           │   │   │   │   └── version.cpython-38.pyc
    │           │   │   │   ├── _compat.py
    │           │   │   │   ├── _structures.py
    │           │   │   │   ├── markers.py
    │           │   │   │   ├── requirements.py
    │           │   │   │   ├── specifiers.py
    │           │   │   │   ├── utils.py
    │           │   │   │   └── version.py
    │           │   │   ├── pyparsing.py
    │           │   │   └── six.py
    │           │   ├── archive_util.py
    │           │   ├── build_meta.py
    │           │   ├── cli-32.exe
    │           │   ├── cli-64.exe
    │           │   ├── cli.exe
    │           │   ├── command
    │           │   │   ├── __init__.py
    │           │   │   ├── __pycache__
    │           │   │   │   ├── __init__.cpython-38.pyc
    │           │   │   │   ├── alias.cpython-38.pyc
    │           │   │   │   ├── bdist_egg.cpython-38.pyc
    │           │   │   │   ├── bdist_rpm.cpython-38.pyc
    │           │   │   │   ├── bdist_wininst.cpython-38.pyc
    │           │   │   │   ├── build_clib.cpython-38.pyc
    │           │   │   │   ├── build_ext.cpython-38.pyc
    │           │   │   │   ├── build_py.cpython-38.pyc
    │           │   │   │   ├── develop.cpython-38.pyc
    │           │   │   │   ├── dist_info.cpython-38.pyc
    │           │   │   │   ├── easy_install.cpython-38.pyc
    │           │   │   │   ├── egg_info.cpython-38.pyc
    │           │   │   │   ├── install.cpython-38.pyc
    │           │   │   │   ├── install_egg_info.cpython-38.pyc
    │           │   │   │   ├── install_lib.cpython-38.pyc
    │           │   │   │   ├── install_scripts.cpython-38.pyc
    │           │   │   │   ├── py36compat.cpython-38.pyc
    │           │   │   │   ├── register.cpython-38.pyc
    │           │   │   │   ├── rotate.cpython-38.pyc
    │           │   │   │   ├── saveopts.cpython-38.pyc
    │           │   │   │   ├── sdist.cpython-38.pyc
    │           │   │   │   ├── setopt.cpython-38.pyc
    │           │   │   │   ├── test.cpython-38.pyc
    │           │   │   │   ├── upload.cpython-38.pyc
    │           │   │   │   └── upload_docs.cpython-38.pyc
    │           │   │   ├── alias.py
    │           │   │   ├── bdist_egg.py
    │           │   │   ├── bdist_rpm.py
    │           │   │   ├── bdist_wininst.py
    │           │   │   ├── build_clib.py
    │           │   │   ├── build_ext.py
    │           │   │   ├── build_py.py
    │           │   │   ├── develop.py
    │           │   │   ├── dist_info.py
    │           │   │   ├── easy_install.py
    │           │   │   ├── egg_info.py
    │           │   │   ├── install.py
    │           │   │   ├── install_egg_info.py
    │           │   │   ├── install_lib.py
    │           │   │   ├── install_scripts.py
    │           │   │   ├── launcher manifest.xml
    │           │   │   ├── py36compat.py
    │           │   │   ├── register.py
    │           │   │   ├── rotate.py
    │           │   │   ├── saveopts.py
    │           │   │   ├── sdist.py
    │           │   │   ├── setopt.py
    │           │   │   ├── test.py
    │           │   │   ├── upload.py
    │           │   │   └── upload_docs.py
    │           │   ├── config.py
    │           │   ├── dep_util.py
    │           │   ├── depends.py
    │           │   ├── dist.py
    │           │   ├── extension.py
    │           │   ├── extern
    │           │   │   ├── __init__.py
    │           │   │   └── __pycache__
    │           │   │       └── __init__.cpython-38.pyc
    │           │   ├── glibc.py
    │           │   ├── glob.py
    │           │   ├── gui-32.exe
    │           │   ├── gui-64.exe
    │           │   ├── gui.exe
    │           │   ├── launch.py
    │           │   ├── lib2to3_ex.py
    │           │   ├── monkey.py
    │           │   ├── msvc.py
    │           │   ├── namespaces.py
    │           │   ├── package_index.py
    │           │   ├── pep425tags.py
    │           │   ├── py27compat.py
    │           │   ├── py31compat.py
    │           │   ├── py33compat.py
    │           │   ├── sandbox.py
    │           │   ├── script (dev).tmpl
    │           │   ├── script.tmpl
    │           │   ├── site-patch.py
    │           │   ├── ssl_support.py
    │           │   ├── unicode_utils.py
    │           │   ├── version.py
    │           │   ├── wheel.py
    │           │   └── windows_support.py
    │           ├── setuptools-41.2.0.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── dependency_links.txt
    │           │   ├── entry_points.txt
    │           │   ├── top_level.txt
    │           │   └── zip-safe
    │           ├── sqlalchemy
    │           │   ├── __init__.py
    │           │   ├── connectors
    │           │   │   ├── __init__.py
    │           │   │   ├── mxodbc.py
    │           │   │   └── pyodbc.py
    │           │   ├── databases
    │           │   │   └── __init__.py
    │           │   ├── dialects
    │           │   │   ├── __init__.py
    │           │   │   ├── firebird
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── fdb.py
    │           │   │   │   └── kinterbasdb.py
    │           │   │   ├── mssql
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── information_schema.py
    │           │   │   │   ├── json.py
    │           │   │   │   ├── mxodbc.py
    │           │   │   │   ├── provision.py
    │           │   │   │   ├── pymssql.py
    │           │   │   │   └── pyodbc.py
    │           │   │   ├── mysql
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── aiomysql.py
    │           │   │   │   ├── asyncmy.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── cymysql.py
    │           │   │   │   ├── dml.py
    │           │   │   │   ├── enumerated.py
    │           │   │   │   ├── expression.py
    │           │   │   │   ├── json.py
    │           │   │   │   ├── mariadb.py
    │           │   │   │   ├── mariadbconnector.py
    │           │   │   │   ├── mysqlconnector.py
    │           │   │   │   ├── mysqldb.py
    │           │   │   │   ├── oursql.py
    │           │   │   │   ├── provision.py
    │           │   │   │   ├── pymysql.py
    │           │   │   │   ├── pyodbc.py
    │           │   │   │   ├── reflection.py
    │           │   │   │   ├── reserved_words.py
    │           │   │   │   └── types.py
    │           │   │   ├── oracle
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── cx_oracle.py
    │           │   │   │   └── provision.py
    │           │   │   ├── postgresql
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── array.py
    │           │   │   │   ├── asyncpg.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── dml.py
    │           │   │   │   ├── ext.py
    │           │   │   │   ├── hstore.py
    │           │   │   │   ├── json.py
    │           │   │   │   ├── pg8000.py
    │           │   │   │   ├── provision.py
    │           │   │   │   ├── psycopg2.py
    │           │   │   │   ├── psycopg2cffi.py
    │           │   │   │   ├── pygresql.py
    │           │   │   │   ├── pypostgresql.py
    │           │   │   │   └── ranges.py
    │           │   │   ├── sqlite
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── aiosqlite.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── dml.py
    │           │   │   │   ├── json.py
    │           │   │   │   ├── provision.py
    │           │   │   │   ├── pysqlcipher.py
    │           │   │   │   └── pysqlite.py
    │           │   │   └── sybase
    │           │   │       ├── __init__.py
    │           │   │       ├── base.py
    │           │   │       ├── mxodbc.py
    │           │   │       ├── pyodbc.py
    │           │   │       └── pysybase.py
    │           │   ├── engine
    │           │   │   ├── __init__.py
    │           │   │   ├── base.py
    │           │   │   ├── characteristics.py
    │           │   │   ├── create.py
    │           │   │   ├── cursor.py
    │           │   │   ├── default.py
    │           │   │   ├── events.py
    │           │   │   ├── interfaces.py
    │           │   │   ├── mock.py
    │           │   │   ├── reflection.py
    │           │   │   ├── result.py
    │           │   │   ├── row.py
    │           │   │   ├── strategies.py
    │           │   │   ├── url.py
    │           │   │   └── util.py
    │           │   ├── event
    │           │   │   ├── __init__.py
    │           │   │   ├── api.py
    │           │   │   ├── attr.py
    │           │   │   ├── base.py
    │           │   │   ├── legacy.py
    │           │   │   └── registry.py
    │           │   ├── events.py
    │           │   ├── exc.py
    │           │   ├── ext
    │           │   │   ├── __init__.py
    │           │   │   ├── associationproxy.py
    │           │   │   ├── asyncio
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── engine.py
    │           │   │   │   ├── events.py
    │           │   │   │   ├── exc.py
    │           │   │   │   ├── result.py
    │           │   │   │   ├── scoping.py
    │           │   │   │   └── session.py
    │           │   │   ├── automap.py
    │           │   │   ├── baked.py
    │           │   │   ├── compiler.py
    │           │   │   ├── declarative
    │           │   │   │   ├── __init__.py
    │           │   │   │   └── extensions.py
    │           │   │   ├── horizontal_shard.py
    │           │   │   ├── hybrid.py
    │           │   │   ├── indexable.py
    │           │   │   ├── instrumentation.py
    │           │   │   ├── mutable.py
    │           │   │   ├── mypy
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── apply.py
    │           │   │   │   ├── decl_class.py
    │           │   │   │   ├── infer.py
    │           │   │   │   ├── names.py
    │           │   │   │   ├── plugin.py
    │           │   │   │   └── util.py
    │           │   │   ├── orderinglist.py
    │           │   │   └── serializer.py
    │           │   ├── future
    │           │   │   ├── __init__.py
    │           │   │   ├── engine.py
    │           │   │   └── orm
    │           │   │       └── __init__.py
    │           │   ├── inspection.py
    │           │   ├── log.py
    │           │   ├── orm
    │           │   │   ├── __init__.py
    │           │   │   ├── attributes.py
    │           │   │   ├── base.py
    │           │   │   ├── clsregistry.py
    │           │   │   ├── collections.py
    │           │   │   ├── context.py
    │           │   │   ├── decl_api.py
    │           │   │   ├── decl_base.py
    │           │   │   ├── dependency.py
    │           │   │   ├── descriptor_props.py
    │           │   │   ├── dynamic.py
    │           │   │   ├── evaluator.py
    │           │   │   ├── events.py
    │           │   │   ├── exc.py
    │           │   │   ├── identity.py
    │           │   │   ├── instrumentation.py
    │           │   │   ├── interfaces.py
    │           │   │   ├── loading.py
    │           │   │   ├── mapper.py
    │           │   │   ├── path_registry.py
    │           │   │   ├── persistence.py
    │           │   │   ├── properties.py
    │           │   │   ├── query.py
    │           │   │   ├── relationships.py
    │           │   │   ├── scoping.py
    │           │   │   ├── session.py
    │           │   │   ├── state.py
    │           │   │   ├── strategies.py
    │           │   │   ├── strategy_options.py
    │           │   │   ├── sync.py
    │           │   │   ├── unitofwork.py
    │           │   │   └── util.py
    │           │   ├── pool
    │           │   │   ├── __init__.py
    │           │   │   ├── base.py
    │           │   │   ├── dbapi_proxy.py
    │           │   │   ├── events.py
    │           │   │   └── impl.py
    │           │   ├── processors.py
    │           │   ├── schema.py
    │           │   ├── sql
    │           │   │   ├── __init__.py
    │           │   │   ├── annotation.py
    │           │   │   ├── base.py
    │           │   │   ├── coercions.py
    │           │   │   ├── compiler.py
    │           │   │   ├── crud.py
    │           │   │   ├── ddl.py
    │           │   │   ├── default_comparator.py
    │           │   │   ├── dml.py
    │           │   │   ├── elements.py
    │           │   │   ├── events.py
    │           │   │   ├── expression.py
    │           │   │   ├── functions.py
    │           │   │   ├── lambdas.py
    │           │   │   ├── naming.py
    │           │   │   ├── operators.py
    │           │   │   ├── roles.py
    │           │   │   ├── schema.py
    │           │   │   ├── selectable.py
    │           │   │   ├── sqltypes.py
    │           │   │   ├── traversals.py
    │           │   │   ├── type_api.py
    │           │   │   ├── util.py
    │           │   │   └── visitors.py
    │           │   ├── testing
    │           │   │   ├── __init__.py
    │           │   │   ├── assertions.py
    │           │   │   ├── assertsql.py
    │           │   │   ├── asyncio.py
    │           │   │   ├── config.py
    │           │   │   ├── engines.py
    │           │   │   ├── entities.py
    │           │   │   ├── exclusions.py
    │           │   │   ├── fixtures.py
    │           │   │   ├── mock.py
    │           │   │   ├── pickleable.py
    │           │   │   ├── plugin
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── bootstrap.py
    │           │   │   │   ├── plugin_base.py
    │           │   │   │   ├── pytestplugin.py
    │           │   │   │   └── reinvent_fixtures_py2k.py
    │           │   │   ├── profiling.py
    │           │   │   ├── provision.py
    │           │   │   ├── requirements.py
    │           │   │   ├── schema.py
    │           │   │   ├── suite
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── test_cte.py
    │           │   │   │   ├── test_ddl.py
    │           │   │   │   ├── test_deprecations.py
    │           │   │   │   ├── test_dialect.py
    │           │   │   │   ├── test_insert.py
    │           │   │   │   ├── test_reflection.py
    │           │   │   │   ├── test_results.py
    │           │   │   │   ├── test_rowcount.py
    │           │   │   │   ├── test_select.py
    │           │   │   │   ├── test_sequence.py
    │           │   │   │   ├── test_types.py
    │           │   │   │   ├── test_unicode_ddl.py
    │           │   │   │   └── test_update_delete.py
    │           │   │   ├── util.py
    │           │   │   └── warnings.py
    │           │   ├── types.py
    │           │   └── util
    │           │       ├── __init__.py
    │           │       ├── _collections.py
    │           │       ├── _compat_py3k.py
    │           │       ├── _concurrency_py3k.py
    │           │       ├── _preloaded.py
    │           │       ├── compat.py
    │           │       ├── concurrency.py
    │           │       ├── deprecations.py
    │           │       ├── langhelpers.py
    │           │       ├── queue.py
    │           │       └── topological.py
    │           ├── werkzeug
    │           │   ├── __init__.py
    │           │   ├── _internal.py
    │           │   ├── _reloader.py
    │           │   ├── datastructures.py
    │           │   ├── datastructures.pyi
    │           │   ├── debug
    │           │   │   ├── __init__.py
    │           │   │   ├── console.py
    │           │   │   ├── repr.py
    │           │   │   ├── shared
    │           │   │   │   ├── ICON_LICENSE.md
    │           │   │   │   ├── console.png
    │           │   │   │   ├── debugger.js
    │           │   │   │   ├── less.png
    │           │   │   │   ├── more.png
    │           │   │   │   └── style.css
    │           │   │   └── tbtools.py
    │           │   ├── exceptions.py
    │           │   ├── formparser.py
    │           │   ├── http.py
    │           │   ├── local.py
    │           │   ├── middleware
    │           │   │   ├── __init__.py
    │           │   │   ├── dispatcher.py
    │           │   │   ├── http_proxy.py
    │           │   │   ├── lint.py
    │           │   │   ├── profiler.py
    │           │   │   ├── proxy_fix.py
    │           │   │   └── shared_data.py
    │           │   ├── py.typed
    │           │   ├── routing.py
    │           │   ├── sansio
    │           │   │   ├── __init__.py
    │           │   │   ├── multipart.py
    │           │   │   ├── request.py
    │           │   │   ├── response.py
    │           │   │   └── utils.py
    │           │   ├── security.py
    │           │   ├── serving.py
    │           │   ├── test.py
    │           │   ├── testapp.py
    │           │   ├── urls.py
    │           │   ├── user_agent.py
    │           │   ├── utils.py
    │           │   ├── wrappers
    │           │   │   ├── __init__.py
    │           │   │   ├── request.py
    │           │   │   └── response.py
    │           │   └── wsgi.py
    │           ├── zipp-3.8.0.dist-info
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           └── zipp.py
    └── pyvenv.cfg


## 3. Assessment and Context mechanism

## 4. How to launch the application
- Open your terminal and run the following commands:
- Use pip or pip3 to install all the required packages
`pip3 install -r requirements.txt`
- Run the application
`flask run`

- If the Web Application cannot run, check the environmental variable
`FLASK_APP=start.py`
and store it as environmental variable