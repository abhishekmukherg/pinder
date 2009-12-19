import json
import urlparse

import httplib2

from exc import HTTPUnauthorizedException, HTTPNotFoundException
from room import Room

__version__ = 'X.Y.Z'

class Campfire(object):
    "Initialize a Campfire client with the given subdomain and token."
    def __init__(self, subdomain, token):
        # The Campfire's subdomain.
        self.subdomain = subdomain
        self._token = token
        # The U{urlparsed<http://docs.python.org/library/urlparse.html#urlparse.urlparse>} URI of the Campfire account.
        self.uri = urlparse.urlparse("http://%s.campfirenow.com" % self.subdomain)
        self._c = httplib2.Http(timeout=5)
        self._c.force_exception_to_status_code = True
        self._c.add_credentials(token, 'X')

    def rooms(self):
        "Returns the rooms available in the Campfire account"
        return self._get('rooms')['rooms']

    def rooms_names(self):
        "Returns the rooms names available in the Campfire account"
        rooms = self._get('rooms')['rooms']
        return sorted([room['name'] for room in rooms])
        
    def room(self, room_id):
        "Returns the room info for the room with the given id."
        data = self._get("room/%s" % room_id)['room']
        return Room(self, room_id, data)

    def find_room_by_name(self, name):
        """Finds a Campfire room with the given name.
        
        Returns a Room instance if found, None otherwise."""
        rooms = self.rooms()
        for room in rooms:
            if room['name'] == name:
                return Room(self, room['id'], data=room)

    def users(self, *rooms_ids):
        "Returns info about users chatting in any room or in the given room(s)."
        rooms = self.rooms()
        users = []
        for room in rooms:
            if not rooms_ids or room['id'] in rooms_ids:
                if room.get('users'):
                    users.append(room.get('users'))
        return users
        
    def user(self, user_id):
        "Returns info about the user with the given user_id."
        return self._get("users/%s" % user_id)
        
    def me(self):
        "Returns info about the authenticated user."
        return self._get("users/me")['user']
        
    def search(self, term):
        "Returns all the messages containing the given term."
        return self._get("search/%s" % term)['messages']

    def _uri_for(self, path=''):
        return "%s/%s.json" % (urlparse.urlunparse(self.uri), path)
        
    def _request(self, method, path, data={}, **options):
        headers = {}
        headers['user-agent'] = 'Pinder/%s' % __version__
        headers['content-type'] = 'application/json'

        if method in ('GET', 'POST', 'PUT', 'DELETE'):
            location = self._uri_for(path)
        else:
            raise Exception('Unsupported HTTP method: %s' % method)

        response, body = self._c.request(
            location, method, json.dumps(data), headers)
            
        if response.status == 401:
            raise HTTPUnauthorizedException(
                "You are not authorized to access the resource: '%s'" % path)
        elif response.status == 404:
            raise HTTPNotFoundException(
                "The resource you are looking for does not exist (%s)" % path)

        try:
            return json.loads(body)
        except ValueError, e:
            if response.status != 200:
                raise Exception("Something did not work fine: %s" % str(e))

    def _post(self, path, data={}, **options):
        return self._request('POST', path, data, **options)

    def _get(self, path=''):
        return self._request('GET', path)
