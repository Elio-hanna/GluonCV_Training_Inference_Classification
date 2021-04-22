import os
import json
from datetime import datetime, time
from pydantic import BaseModel
from typing import Optional

class LoggingService:

    def timestamp(self):
        dateTimeObj = datetime.now()
        day = dateTimeObj.day
        month = dateTimeObj.month
        year = dateTimeObj.year
        hour = dateTimeObj.hour
        minu = dateTimeObj.minute
        sec = dateTimeObj.second
        return day, month, year, hour, minu, sec


    def log(self,name, result, parm: Optional[str] = None):
        """
        LoggingService the actions done by the user
        :param name: name of the class used
        :param result: what was the result shown to the user
        :param parm: what was the param shown used by the user
        :return: 
        """
        
        file_object = open('log.txt', 'a')
        day, mon, year, hour, minu, sec = self.timestamp()
        file_object.write(
            "[" + str(day) + "/" + str(mon) + "/" + str(year) + " " + str(hour) + ":" + str(minu) + ":" + str(sec) + "]: ")
        file_object.write("the user executed " + name + " with these parameters{ ")
        file_object.write(str(parm) + "}")
        file_object.write("the result is " + result + "\n")


    def log_error(self,name):
        """
        LoggingService the errors done by the user
        :param name: name of the class used
        :return: 
        """
        file_object = open('log.txt', 'a')
        day, mon, year, hour, minu, sec = self.timestamp()
        file_object.write(
            "[" + str(day) + "/" + str(mon) + "/" + str(year) + " " + str(hour) + ":" + str(minu) + ":" + str(sec) + "]: ")
        file_object.write("Error while executing " + name)