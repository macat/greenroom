#from greenroom.apps.django_facebook_patched.api import FacebookUserConverter, get_persistent_graph
#from open_facebook.api import FacebookAuthorization
#
#
#def get_facebook_friends(request):
#    app_access_token = FacebookAuthorization.get_cached_app_access_token()
#    graph = get_persistent_graph(request, access_token=app_access_token)
#    converter = FacebookUserConverter(graph)
#    friends_uids = ','.join([str(f['uid']) for f in converter.get_friends()])
#    return graph.fql('SELECT name, username, pic_square, pic FROM user WHERE uid IN (%s)' % friends_uids)
