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
        
    def _get(self, path):
        return self._c._get("room/%s/%s" % (self.id, path))

    def _post(self, path):
        return self._c._post("room/%s/%s" % (self.id, path))
        
    def join(self):
        "Joins the room."
        self._post("join")

    def leave(self):
        "Leaves the room."
        self._post("leave")
        
    def lock(self):
        "Locks the room to prevent new users from entering."
        self._post("lock")

    def unlock(self):
        "Unlocks the room."
        self._post("unlock")

    def users(self):
        "Gets info about users chatting in the room."
        return self._c.users(self.data['name'])
        
    def transcript(self, date=None):
        "Gets the transcript for today or the given date (a datetime.date instance)."
        date = datetime.date.today() or date
        transcript_path = "transcript/%s/%s/%s" % (date.year, date.month, date.day)
        return self._get(transcript_path)['messages']

    def uploads(self):
        "Lists recently uploaded files."
        return self._get('uploads')['uploads']