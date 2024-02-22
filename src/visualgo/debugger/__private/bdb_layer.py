import bdb


class BdbLayer(bdb.Bdb):
    def user_line(self, frame):
        pass

    def user_return(self, frame, return_value):
        pass

    def user_call(self, frame, argument_list):
        pass

    def user_exception(self, frame, exc_info):
        pass