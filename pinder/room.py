import datetime

class Room(object):
    def __init__(self, campfire, room_id, data):
        self._c = campfire
        # The id of the room
        self.id = room_id
        # The raw data of the room
        self.data = data
        # The name of the room
        self.name = data["name"]

    def __repr__(self):
        return "<Room: %s>" % self.id

    def __eq__(self, other):
        return self.id == other.id
        
    def _path_for_room(self, path):
        uri = 'room/%s' % self.id
        if path:
            uri = '%s/%s' % (uri, path)
        return uri

    def _get(self, path=''):
        return self._c._get(self._path_for_room(path))

    def _post(self, path, data={}):
        return self._c._post(self._path_for_room(path), data)
        
    def _put(self, path, data={}):
        return self._c._put(self._path_for_room(path), data)

    def _send(self, message, type='TextMessage'):
        data = {'message': {'body': message, 'type': type}}
        return self._post('speak', data)

    def join(self):
        "Joins the room."
        self._post("join")

    def leave(self):
        "Leaves the room."
        self._post("leave")
        
    def lock(self):
        "Locks the room to prevent new users from entering."
        self.join()
        self._post("lock")

    def unlock(self):
        "Unlocks the room."
        self._post("unlock")

    def users(self):
        "Gets info about users chatting in the room."
        return self._c.users(self.data['name'])
        
    def transcript(self, date=None):
        "Gets the transcript for today or the given date (a datetime.date instance)."
        self.join()
        date = datetime.date.today() or date
        transcript_path = "transcript/%s/%s/%s" % (date.year, date.month, date.day)
        return self._get(transcript_path)['messages']

    def uploads(self):
        "Lists recently uploaded files."
        self.join()
        return self._get('uploads')['uploads']
        
    def speak(self, message):
        "Sends a message to the room. Returns the message data."
        self.join()
        return self._send(message, type='TextMessage')['message']

    def paste(self, message):
        "Pastes a message to the room. Returns the message data."
        self.join()
        return self._send(message, type='PasteMessage')['message']

    def sound(self, message):
        "Plays a sound into the room. Returns the message data."
        self.join()
        return self._send(message, type='SoundMessage')['message']
    
    def update(self, name, topic):
        "Updates name and/or topic of the room."
        data = {'room': {'name': name, 'topic': topic}}
        self._put('', data)
