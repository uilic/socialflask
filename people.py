
class human:
    """Class human with the atributes given in the data.json file, and also with
        one extra atribute, string ID for easier work with picture urls"""

    def __init__(self, ident, firstName, surName, age, gender, friendsId):
        self.ident = ident
        self.firstName = firstName
        self.surName = surName
        self.age = age
        self.gender = gender
        self.friendsId = friendsId
        self.strId = str(ident)

    def getFriends(self, group):  # returns list of human objects of friends
        friendsList = []
        for g in group:
            for i in self.friendsId:
                if i == g.ident:
                    h = human(g.ident, g.firstName, g.surName, g.age, g.gender, g.friendsId)
                    friendsList.append(h)
        return friendsList

    def getFriendsOfFriends(self, group):  # returns list of friends of friends
        friendsOfFriendsList = []
        fofId = []
        for f in self.getFriends(group):
            for fre in f.getFriends(group):
                if fre.ident not in self.friendsId + fofId and fre.ident != self.ident:
                    h = human(fre.ident, fre.firstName, fre.surName,
                              fre.age, fre.gender, fre.friendsId)
                    friendsOfFriendsList.append(h)
                    fofId.append(h.ident)
        return friendsOfFriendsList

    def getSuggestedFriends(self, group):
        """returns a list of the suggested friends by first calculating mutual
        friends and separating those friends who have two or more mutuals"""
        suggestedFriends = []
        mutualFriendsId = []
        for fof in self.getFriendsOfFriends(group):
            for f in fof.getFriends(group):
                if f.ident in self.friendsId:
                    mutualFriendsId.append(f.ident)
            if len(mutualFriendsId) > 1:
                suggestedFriends.append((fof, len(mutualFriendsId)))
            mutualFriendsId = []

        return suggestedFriends
