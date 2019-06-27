from abc import ABCMeta, abstractclassmethod


class DisplayInterface:
    ___metaclass___ = ABCMeta

    @classmethod
    def version(cls):
        return "1.0"

    @classmethod
    def show_msg(cls, msg):
        raise NotImplementedError


class ConsoleDisplay(DisplayInterface):
    @classmethod
    def show_msg(cls, msg):
        print(msg)


class LCDDisplay(DisplayInterface):

    @classmethod
    def show_msg(cls, msg):
        pass
#
# class MyClient(object):
#     def __init__(self, server):
#         if not isinstance(server, DisplayInterface):
#             raise Exception("Bad interface")
#
#         if not DisplayInterface.version() == "1.0":
#             raise Exception("Bad version")
#
#         self.__server = server
#
#     def client_show(cls):
#         cls.__server.show()
#
#
# x = MyClient(MyServer())
#
# x.client_show()
