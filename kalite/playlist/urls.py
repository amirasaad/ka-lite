from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(__package__ + '.views',
                       url(r'^$', 'playlists'),
                       url(r'^sample', 'sample_json'),
)
