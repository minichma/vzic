#!/usr/bin/env python 
from LibicalWrap import *

class Property:
    """ Represent any iCalendar Property """

    def __init__(self,dict):
        self.dict = dict

    def name(self,v=None):
        """ Return the name of the property """
        if(v != None):
            self.dict['name'] = v

        return self.dict['name']

    def value_type(self,v=None):
        """ Return the RFC2445 name of the value """
        if(v != None):
            self.dict['value_type'] = v

        return self.dict['value_type']

    def value(self,v=None):
        """ Return the RFC2445 representation of the value """
        if(v != None):
            self.dict['value'] = v

        return self.dict['value']


    def __getitem__(self,key):
        """ Return property values by name """
        if self.dict.has_key(key):
            return self.dict[key]
        else:
            return None

    def __setitem__(self,key,value):
        """ Set Property Values by Name """
        self.dict[key] = value

        return self.dict[key]


class Time(Property):
    """ Represent iCalendar DATE, TIME and DATE-TIME """
    def __init__(self,dict):
        Property.__init__(self,dict)

        self.tt = icaltime_from_string(self.dict['value'])

    def utc_seconds(self,v=None):
        """ Return or set time in  seconds past POSIX epoch"""
        if (v!=None):
            self.tt = icaltime_from_timet(v,0)

        return icaltime_as_timet(self.tt)

    def is_utc(self,v=None):
        """ Return or set boolean indicating if time is in UTC """
        if(v != None):
            icaltimetype_is_utc_set(self.tt,v)

        return icaltimetype_is_utc_get(self.tt)

    def is_date(self,v=None):
        """ Return or set boolean indicating if time is actually a date """
        if(v != None):
            icaltimetype_is_date_set(self.tt,v)

        return icaltimetype_is_date_get(self.tt)


    def timezone(self,v=None):
        """ Return or set the timezone string for this time """
        if (v != None):
            self.dict['TZID'] = v

        return  self.dict['TZID']

    def second(self,v=None):
        """ Get or set the seconds component of this time """
        if(v != None):
            icaltimetype_second_set(self.tt,v)
            self.dict['value'] = icaltime_as_ical_string(self.tt)

        return icaltimetype_second_get(self.tt)

    def minute(self,v=None):
        """ Get or set the minute component of this time """
        if(v != None):
            icaltimetype_minute_set(self.tt,v)
            self.dict['value'] = icaltime_as_ical_string(self.tt)
        return icaltimetype_minute_get(self.tt)

    def hour(self,v=None):
        """ Get or set the hour component of this time """
        if(v != None):
            icaltimetype_hour_set(self.tt,v)
            self.dict['value'] = icaltime_as_ical_string(self.tt)
        return icaltimetype_hour_get(self.tt)

    def day(self,v=None):
        """ Get or set the month day component of this time """
        if(v != None):
            icaltimetype_day_set(self.tt,v)
            self.dict['value'] = icaltime_as_ical_string(self.tt)
        return icaltimetype_day_get(self.tt)

    def month(self,v=None):
        """ Get or set the month component of this time. January is month 1 """
        if(v != None):
            icaltimetype_month_set(self.tt,v)
            self.dict['value'] = icaltime_as_ical_string(self.tt)
        return icaltimetype_month_get(self.tt)

    def year(self,v=None):
        """ Get or set the year component of this time """
        if(v != None):
            icaltimetype_year_set(self.tt,v)
            self.dict['value'] = icaltime_as_ical_string(self.tt)
        return icaltimetype_year_get(self.tt)


class Duration(Property):
    """ Represent a length of time, like 3 minutes, or 6 days, 20 seconds."""

    def __init__(self,dict):
        """Create a new duration from an RFC2445 string or number of seconds."""
        Property.__init__(self,dict)

    def seconds(self,v=None):
        """Return duration in seconds"""
        if(v != None):
            icaltimetype_year_set(self.tt,v)
            self.dict['value'] = icaltime_as_ical_string(self.tt)
        return icaltimetype_year_get(self.tt)



class Period(Property):
    """Represent a span of time"""
    def __init__(self,dict):
        """ """
        Property.__init__(self,dict)


    def start(self,v=None):
        """
        Return or set start time of the period. The start time may be
        expressed as an RFC2445 format string or an instance of Time.
        The return value is an instance of Time
        """

        if(v != None):
            pass
        return 

    def end(self,v=None):
        """
        Return or set end time of the period. The end time may be
        expressed as an RFC2445 format string or an instance of Time.
        The return value is an instance of Time
        """        
        if(v != None):
            pass
        return 

    def duration(self,v=None):
        """
        Return or set the duration of the period. The duration may be
        expressed as an RFC2445 format string or an instance of Duration.
        The return value is an instance of Duration
        """        

        if(v != None):
            pass
        return 


class Component:

    def __init__(self,str):
        self.comp_p = 'NULL'

        self.comp_p = icalparser_parse_string(str)

    def __del__(self):
        if self.comp_p != 'NULL' and icalcomponent_get_parent(self.comp_p) != 'NULL':
            icalcomponent_free(self.comp_p)

            self.comp_p = 'NULL'

    def properties(self,type='ANY'): 
        """  
        Return a list of Property instances, each representing a
        property of the type 'type.'
        """

        props = []

        p = icallangbind_get_first_property(self.comp_p,type)
        while p != 'NULL':
            d_string = icallangbind_property_eval_string(p,":")

            d = eval(d_string)

            p = icallangbind_get_next_property(self.comp_p,type)

            if d['value_type'] == 'DATE-TIME':
                props.append(Time(d))
            elif d['value_type'] == 'PERIOD':
                props.append(Period(d))
            elif d['value_type'] == 'DURATION':
                props.append(Duration(d))
            else :
                props.append(Property(d))

        return props

    def addProperty(self,property):
        pass

    def removeProperty(self,property):
        pass

    def components(self,type='ANY'):        
        props = []



        return props


class Store:

    def __init__(self):

	def path(self):
            pass

	def mark(self):
            pass

        def commit(self): 
            pass

	def addComponent(self, comp):
            pass

	def removeComponent(self, comp):
            pass

	def countComponents(self, kind):
            pass

	def select(self, gauge):
            pass

	def clearSelect(self):
            pass

	def fetch(self, uid):
            pass

	def fetchMatch(self, comp):
            pass

	def modify(self, oldc, newc):
            pass

	def currentComponent(self):
            pass

	def firstComponent(self):
            pass

	def nextComponent(self):
            pass



class FileStore(Store):

    def __init__(self):
        pass

    def path(self):
        pass

    def mark(self):
        pass

    def commit(self): 
        pass

    def addComponent(self, comp):
        pass

    def removeComponent(self, comp):
        pass

    def countComponents(self, kind):
        pass

    def select(self, gauge):
        pass

    def clearSelect(self):
        pass

    def fetch(self, uid):
        pass

    def fetchMatch(self, comp):
        pass

    def modify(self, oldc, newc):
        pass

    def currentComponent(self):
        pass

    def firstComponent(self):
        pass

    def nextComponent(self):
        pass
