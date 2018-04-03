# C:\Users\Hlim\Desktop\TK.zip ' PATH '
# Programmer by HALIM_HIOUANI
# This script is for beginners in the field of Python
# Explain some library properties zipfile

import zipfile
import datetime
import os
import abc
import exceptions
import time
ALL = ['ZIP']


class ZIP (object):
    __doc__ = 'This category contains compressed file data and other things <CLASS : HALIM__HIOUANI>'
    __slots__ = ['__INPUT__', '__ZIP__', 'PATH_TEXT', 'SELF']
    __metaclass__ = abc.ABCMeta

    def __init__(self, Input, ZIP__FILE=None, Path_TEXT='C:\Users\Hlim\PycharmProjects\untitled3\TEXT'):
        self.PATH_TEXT = Path_TEXT   # C:\Users\Hlim\PycharmProjects\untitled3\TEXT
        self.__INPUT__ = Input
        self.__ZIP__ = ZIP__FILE

    def CHANGE_PATH(self):
        FINAL_PATH = os.getcwd ()  # C:\Users\Halim\PycharmProjects\untitled3 + TEXT
        TAMI = FINAL_PATH.__add__('\TEXT')

    def __ceil__(self):
        """ Here we opened the text file and saved it and took the data from it """
        OPEN_FILE_AND_READ = open (self.PATH_TEXT, 'r')
        READ_LINES = OPEN_FILE_AND_READ.readlines ()
        for __READ__ in READ_LINES:
            self.SELF = __READ__
        print OPEN_FILE_AND_READ.name   # NAME OF FILE ZIP
        print OPEN_FILE_AND_READ.closed    # VERIFY FILE ZIP
        OPEN_FILE_AND_READ.close()    # CLOSE FILE ZIP

    def DATA(self):
        """ This function retrieves all the data of the file you have extended ZIP """
        self.__ZIP__ = zipfile.ZipFile (self.__INPUT__, mode='r')
        for ALL_FILE_in_YOUR__FILE in self.__ZIP__.infolist ():
            print('Comment: %2s' % ALL_FILE_in_YOUR__FILE.comment)  # Comment Dissolved file
            print 'NAME OF SYSTEM %2s' % ALL_FILE_in_YOUR__FILE.create_system, '\t ->', repr (
                self.SELF)  # Operating system data
            print('Modified: %2s' % datetime.datetime (*ALL_FILE_in_YOUR__FILE.date_time))  # DATE and TIME
            print('ZIP version: %2s' % ALL_FILE_in_YOUR__FILE.create_version)  # version of the file
            print 'Compressed: %2s' % ALL_FILE_in_YOUR__FILE.compress_size, 'bytes' # The size of the file is compressed
            print 'Uncompressed: %2s' % ALL_FILE_in_YOUR__FILE.file_size, 'bytes'  # The file size is normal
            print 'NAME: %2s' % self.__ZIP__.namelist()


if __name__ == '__main__':
    print(' ** IF YOU WANT TEACH CLICK NUMBER 1 **')
    YOUR__FILE = raw_input ('PLEASE GIVE YOUR FILE :')
    APPLICATION = ZIP (Input=YOUR__FILE)
    if YOUR__FILE == '1':
        var = APPLICATION.__doc__
        print(var)
    elif zipfile.is_zipfile(YOUR__FILE):
        try:
            APPLICATION.CHANGE_PATH()
            APPLICATION.__ceil__ ()
            APPLICATION.DATA ()
        except KeyError:
            print('Error %s' % exceptions.UnicodeWarning)
    else:
        print('NOTHING ZIP FILE')
        time.sleep(5)
        exit()
