class SemesterSummary:
    def __init__(self, credits_approved=None, credits_coursing=None, pending_credits=None):
        self.__credits_approved = credits_approved
        self.__credits_coursing = credits_coursing
        self.__pending_credits = pending_credits

    @property
    def approved(self):
        return self.__credits_approved

    @approved.setter
    def approved(self, value):
        self.__credits_approved = value

    @approved.deleter
    def approved(self):
        del self.__credits_approved

    @property
    def coursing(self):
        return self.__credits_coursing

    @coursing.setter
    def coursing(self, value):
        self.__credits_coursing = value

    @coursing.deleter
    def coursing(self):
        del self.__credits_coursing

    @property
    def pending(self):
        return self.__pending_credits

    @pending.setter
    def pending(self, value):
        self.__pending_credits = value

    @pending.deleter
    def pending(self):
        del self.__pending_credits
