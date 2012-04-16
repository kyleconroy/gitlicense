import web
from nose.tools import assert_equals

def test_timburks_nu():
    msg = web.get_license('timburks', 'nu')
    assert_equals('Apache License 2.0', msg)

def test_sstephenson_prototype():
    msg = web.get_license('sstephenson', 'prototype')
    assert_equals('MIT License', msg)

def test_FooBarWidget_passenger():
    msg = web.get_license('FooBarWidget', 'passenger')
    assert_equals('MIT License', msg)

def test_madrobby_scriptaculous():
    msg = web.get_license('madrobby', 'scriptaculous')
    assert_equals('MIT License', msg)

def test_rails_rails():
    msg = web.get_license('rails', 'rails')
    assert_equals('MIT License', msg)

def test_mootools_mootoolscore():
    msg = web.get_license('mootools', 'mootools-core')
    assert_equals('MIT License', msg)

def test_mirrors_linux26():
    msg = web.get_license('mirrors', 'linux-2.6')
    assert_equals('GNU General Public License Version 2', msg)

def test_dpp_liftweb():
    msg = web.get_license('dpp', 'liftweb')
    assert_equals('No License Found', msg)

def test_dima_restfulx_framework():
    msg = web.get_license('dima', 'restfulx_framework')
    assert_equals('MIT License', msg)

def test_pieter_gitx():
    msg = web.get_license('pieter', 'gitx')
    assert_equals('GNU General Public License Version 2', msg)

def test_pokeb_asihttprequest():
    msg = web.get_license('pokeb', 'asi-http-request')
    assert_equals('Modified BSD License', msg)

def test_git_git():
    msg = web.get_license('git', 'git')
    assert_equals('GNU General Public License Version 2', msg)

def test_sintaxi_phonegap():
    msg = web.get_license('sintaxi', 'phonegap')
    assert_equals('MIT License', msg)

def test_DmitryBaranovskiy_raphael():
    msg = web.get_license('DmitryBaranovskiy', 'raphael')
    assert_equals('MIT License', msg)

def test_TwP_turn():
    msg = web.get_license('TwP', 'turn')
    assert_equals('GNU General Public License Version 2', msg)

def test_rhomobile_rhodes():
    msg = web.get_license('rhomobile', 'rhodes')
    assert_equals('MIT License', msg)

def test_webpy_webpy():
    msg = web.get_license('webpy', 'webpy')
    assert_equals('No License Found', msg)

def test_sorccu_cufon():
    msg = web.get_license('sorccu', 'cufon')
    assert_equals('MIT License', msg)

def test_django_django():
    msg = web.get_license('django', 'django')
    assert_equals('Modified BSD License', msg)

def test_technomancy_emacsstarterkit():
    msg = web.get_license('technomancy', 'emacs-starter-kit')
    assert_equals('GNU General Public License Version 3', msg)

def test_yui_yui3():
    msg = web.get_license('yui', 'yui3')
    assert_equals('MIT License', msg)

def test_lloyd_yajl():
    msg = web.get_license('lloyd', 'yajl')
    assert_equals('ISC License', msg)

def test_djmitche_buildbot():
    msg = web.get_license('djmitche', 'buildbot')
    assert_equals('No License Found', msg)

def test_sinatra_sinatra():
    msg = web.get_license('sinatra', 'sinatra')
    assert_equals('MIT License', msg)

def test_mongodb_mongo():
    msg = web.get_license('mongodb', 'mongo')
    assert_equals('GNU Affero General Public License Version 3', msg)

def test_darwin_visor():
    msg = web.get_license('darwin', 'visor')
    assert_equals('Apache License 2.0', msg)

def test_rentzsch_clicktoflash():
    msg = web.get_license('rentzsch', 'clicktoflash')
    assert_equals('No License Found', msg)

def test_rakudo_rakudo():
    msg = web.get_license('rakudo', 'rakudo')
    assert_equals('Artistic License Version 2.0', msg)

def test_facebook_three20():
    msg = web.get_license('facebook', 'three20')
    assert_equals('Apache License 2.0', msg)

def test_klacke_yaws():
    msg = web.get_license('klacke', 'yaws')
    assert_equals('Modified BSD License', msg)

def test_petdance_ack():
    msg = web.get_license('petdance', 'ack')
    assert_equals('Artistic License Version 2.0', msg)

def test_antirez_redis():
    msg = web.get_license('antirez', 'redis')
    assert_equals('Modified BSD License', msg)

def test_apache_solr():
    msg = web.get_license('apache', 'solr')
    assert_equals('No License Found', msg)

def test_dbloete_ioctocat():
    msg = web.get_license('dbloete', 'ioctocat')
    assert_equals('MIT License', msg)

def test_pinax_pinax():
    msg = web.get_license('pinax', 'pinax')
    assert_equals('MIT License', msg)

def test_davidswelt_aquamacsemacs():
    msg = web.get_license('davidswelt', 'aquamacs-emacs')
    assert_equals('GNU General Public License Version 3', msg)

def test_jquery_jquery():
    msg = web.get_license('jquery', 'jquery')
    assert_equals('GNU General Public License Version 2', msg)

def test_memcached_memcached():
    msg = web.get_license('memcached', 'memcached')
    assert_equals('Modified BSD License', msg)

def test_Objective3_ElementParser():
    msg = web.get_license('Objective3', 'ElementParser')
    assert_equals('No License Found', msg)

def test_atebits_SimFinger():
    msg = web.get_license('atebits', 'SimFinger')
    assert_equals('No License Found', msg)

def test_apache_httpd():
    msg = web.get_license('apache', 'httpd')
    assert_equals('MIT License', msg)

def test_mxcl_homebrew():
    msg = web.get_license('mxcl', 'homebrew')
    assert_equals('No License Found', msg)

def test_apache_couchdb():
    msg = web.get_license('apache', 'couchdb')
    assert_equals('MIT License', msg)

def test_apache_cassandra():
    msg = web.get_license('apache', 'cassandra')
    assert_equals('Apache License 2.0', msg)

def test_voldemort_voldemort():
    msg = web.get_license('voldemort', 'voldemort')
    assert_equals('Apache License 2.0', msg)

def test_richhickey_clojure():
    msg = web.get_license('richhickey', 'clojure')
    assert_equals('Modified BSD License', msg)

def test_henon_GitSharp():
    msg = web.get_license('henon', 'GitSharp')
    assert_equals('No License Found', msg)

def test_rupa_z():
    msg = web.get_license('rupa', 'z')
    assert_equals('No License Found', msg)

def test_probablycorey_wax():
    msg = web.get_license('probablycorey', 'wax')
    assert_equals('MIT License', msg)

def test_omz_AppSalesMobile():
    msg = web.get_license('omz', 'AppSales-Mobile')
    assert_equals('BSD-2 License', msg)

def test_greasemonkey_greasemonkey():
    msg = web.get_license('greasemonkey', 'greasemonkey')
    assert_equals('Mozilla Public License', msg)

def test_gimite_websocketjs():
    msg = web.get_license('gimite', 'web-socket-js')
    assert_equals('No License Found', msg)

def test_slact_nginx_http_push_module():
    msg = web.get_license('slact', 'nginx_http_push_module')
    assert_equals('No License Found', msg)

def test_andymatuschak_Sparkle():
    msg = web.get_license('andymatuschak', 'Sparkle')
    assert_equals('MIT License', msg)

def test_v8_v8():
    msg = web.get_license('v8', 'v8')
    assert_equals('Modified BSD License', msg)

def test_wayneeseguin_rvm():
    msg = web.get_license('wayneeseguin', 'rvm')
    assert_equals('Apache License 2.0', msg)

def test_documentcloud_cloudcrowd():
    msg = web.get_license('documentcloud', 'cloud-crowd')
    assert_equals('MIT License', msg)

def test_facebook_tornado():
    msg = web.get_license('facebook', 'tornado')
    assert_equals('No License Found', msg)

def test_apenwarr_bup():
    msg = web.get_license('apenwarr', 'bup')
    assert_equals('No License Found', msg)

def test_documentcloud_underscore():
    msg = web.get_license('documentcloud', 'underscore')
    assert_equals('MIT License', msg)

def test_markhuot_projectplus():
    msg = web.get_license('markhuot', 'projectplus')
    assert_equals('No License Found', msg)

def test_erlang_otp():
    msg = web.get_license('erlang', 'otp')
    assert_equals('No License Found', msg)

def test_ice799_memprof():
    msg = web.get_license('ice799', 'memprof')
    assert_equals('No License Found', msg)

def test_jashkenas_coffeescript():
    msg = web.get_license('jashkenas', 'coffee-script')
    assert_equals('MIT License', msg)

def test_tobeytailor_gordon():
    msg = web.get_license('tobeytailor', 'gordon')
    assert_equals('MIT License', msg)

def test_facebook_hiphopphp():
    msg = web.get_license('facebook', 'hiphop-php')
    assert_equals('No License Found', msg)

def test_symfony_symfony():
    msg = web.get_license('symfony', 'symfony')
    assert_equals('MIT License', msg)

def test_phpbb_phpbb():
    msg = web.get_license('phpbb', 'phpbb')
    assert_equals('GNU General Public License Version 3', msg)

def test_tinymce_tinymce():
    msg = web.get_license('tinymce', 'tinymce')
    assert_equals('No License Found', msg)

def test_processone_ejabberd():
    msg = web.get_license('processone', 'ejabberd')
    assert_equals('GNU General Public License Version 2', msg)

def test_ruby_ruby():
    msg = web.get_license('ruby', 'ruby')
    assert_equals('No License Found', msg)

def test_alandipert_step():
    msg = web.get_license('alandipert', 'step')
    assert_equals('No License Found', msg)

def test_postgres_postgres():
    msg = web.get_license('postgres', 'postgres')
    assert_equals('No License Found', msg)

def test_robhudson_djangodebugtoolbar():
    msg = web.get_license('robhudson', 'django-debug-toolbar')
    assert_equals('Modified BSD License', msg)

def test_280north_cappuccino():
    msg = web.get_license('280north', 'cappuccino')
    assert_equals('No License Found', msg)

def test_ry_node():
    msg = web.get_license('ry', 'node')
    assert_equals('MIT License', msg)

def test_mbostock_d3():
    msg = web.get_license('mbostock', 'd3')
    assert_equals('Modified BSD License', msg)

def test_editorconfig_core():
    msg = web.get_license('editorconfig', 'editorconfig-core-py')
    assert_equals('Python Software Foundation License Version 2', msg)

def test_python_python():
    msg = web.get_license('python-git', 'python')
    assert_equals('Python Software Foundation License Version 2', msg)
