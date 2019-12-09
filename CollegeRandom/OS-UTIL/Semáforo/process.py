from enum import Enum

#Process type;
class ProcType(Enum):
  Include = 1
  Exclude = -1

#Process class;
class Process:
  def __init__(self, ptype: ProcType, pid: int):
    self.ptype = ptype
    self.pid = pid
  def __str__(self):
    return f"<{self.ptype.name} {self.pid}>"