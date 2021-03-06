#!/usr/bin/env python

import time
import cec

adapters = cec.list_adapters()

test_power = False

print adapters

if len(adapters) > 0:
   adapter = adapters[0]
   print "Using Adapter %s"%(adapter)
   cec.init(adapter)

   print "Devices:", cec.list_devices()

   d = cec.Device(0)

   # print fields
   print "Address:", d.address
   print "Physical Address:", d.physical_address
   print "Vendor ID:", d.vendor
   print "OSD:", d.osd_string
   print "CEC Version:", d.cec_version
   print "Language:", d.language

   # call functions
   print "ON:", d.is_on()

