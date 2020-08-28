#!/usr/bin/env python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                        NASA Jet Propulsion Laboratory
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object
from future import standard_library

standard_library.install_aliases()
import threading
import logging

logger = logging.getLogger()


class StreamObserverQueue(object):
    """
    Stores stream to a thread queue.
    """

    def __init__(self, queue):
        """
        Initializer.
        """
        self._queue = queue

    # end def

    #    def __del__(self):
    #        """
    #        Finalizer.
    #        """
    #    # end def

    def __str__(self):
        """
        Gets the string representation of this object.
        @return: the string representation of this object.
        @rtype: str
        """
        return 'queue: "%s"' % (self._queue)

    # end def

    def notifyLine(self, line):
        """
        Invoked after a new line of data is read from the stream.
        Note that lines include the line separator.
        """
        self._queue.put(line)

    # end def

    def notifyEOF(self):
        """
        Invoked when end of stream is reached.
        """
        self._queue.put(None)

    # end def


# end class
