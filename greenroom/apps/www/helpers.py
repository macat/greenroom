from django_facebook.api import FacebookUserConverter, get_persistent_graph
from open_facebook.api import FacebookAuthorization


FB_FRIENDS_PAGINATION_LIMIT = 5

def get_facebook_friends(request):
    app_access_token = FacebookAuthorization.get_cached_app_access_token()
    graph = get_persistent_graph(request, access_token=app_access_token)
    converter = FacebookUserConverter(graph)
    friends_uids = ','.join([str(f['uid']) for f in converter.get_friends()][:FB_FRIENDS_PAGINATION_LIMIT])
    return graph.fql('SELECT name, username, pic_square, pic FROM user WHERE uid IN (%s)' % friends_uids)
