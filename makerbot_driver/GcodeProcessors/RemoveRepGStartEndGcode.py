from __future__ import absolute_import

import makerbot_driver
from .Processor import Processor

class RemoveRepGStartEndGcode(Processor):

  def __init__(self):
    pass

  def process_gcode(self, gcodes):
    startgcode = False
    endgcode = False
    output = []

    for code in gcodes:
      if startgcode:
        if(self.get_comment_match(code, 'end of start.gcode')):
          startgcode = False
      elif endgcode:
        if(self.get_comment_match(code, 'end End.gcode')):
          endgcode = False
      else:
        if (self.get_comment_match(code, '**** start.gcode')):
          startgcode = True
        elif (self.get_comment_match(code, '**** End.gcode')):
          endgcode = True
        else:
          output.append(code)
    return output

  def get_comment_match(self, gcode, match):
    (codes, flags, comments) = makerbot_driver.Gcode.parse_line(gcode)
    axis = None
    if comments.find(match) is -1:
      return False
    else:
      return True