# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import jpype

def start():
    """
    Start the JVM if not already started and set the Java classpath with all available PowSyBl libraries
    """
    if jpype.isJVMStarted():
        return

    classpath = [os.path.join(os.path.dirname(__file__), 'lib', '*')]

    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", classpath=classpath, convertStrings=False)

def stop():
    """
    Stop the JVM if started
    """
    if jpype.isJVMStarted():
        jpype.shutdownJVM()