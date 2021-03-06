"""autogenerated by genpy from vector_slam_msgs/CobotLocalizationMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CobotLocalizationMsg(genpy.Message):
  _md5sum = "88e4cd133e897255a68320aa8fedc7f7"
  _type = "vector_slam_msgs/CobotLocalizationMsg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 timeStamp
float32 x
float32 y
float32 angle
float32 angleUncertainty
float32 locationUncertainty
string map

float64 lastLaserRunTime
float64 laserRunTime
int32 laserNumObservedPoints
int32 laserNumCorrespondences
float32 laserStage0Weights
float32 laserStageRWeights
float32 laserMeanSqError

float64 lastPointCloudRunTime
float64 pointCloudRunTime
int32 pointCloudNumObservedPoints
int32 pointCloudNumCorrespondences
float32 pointCloudStage0Weights
float32 pointCloudStageRWeights
float32 pointCloudMeanSqError


"""
  __slots__ = ['timeStamp','x','y','angle','angleUncertainty','locationUncertainty','map','lastLaserRunTime','laserRunTime','laserNumObservedPoints','laserNumCorrespondences','laserStage0Weights','laserStageRWeights','laserMeanSqError','lastPointCloudRunTime','pointCloudRunTime','pointCloudNumObservedPoints','pointCloudNumCorrespondences','pointCloudStage0Weights','pointCloudStageRWeights','pointCloudMeanSqError']
  _slot_types = ['float64','float32','float32','float32','float32','float32','string','float64','float64','int32','int32','float32','float32','float32','float64','float64','int32','int32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timeStamp,x,y,angle,angleUncertainty,locationUncertainty,map,lastLaserRunTime,laserRunTime,laserNumObservedPoints,laserNumCorrespondences,laserStage0Weights,laserStageRWeights,laserMeanSqError,lastPointCloudRunTime,pointCloudRunTime,pointCloudNumObservedPoints,pointCloudNumCorrespondences,pointCloudStage0Weights,pointCloudStageRWeights,pointCloudMeanSqError

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CobotLocalizationMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timeStamp is None:
        self.timeStamp = 0.
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.angle is None:
        self.angle = 0.
      if self.angleUncertainty is None:
        self.angleUncertainty = 0.
      if self.locationUncertainty is None:
        self.locationUncertainty = 0.
      if self.map is None:
        self.map = ''
      if self.lastLaserRunTime is None:
        self.lastLaserRunTime = 0.
      if self.laserRunTime is None:
        self.laserRunTime = 0.
      if self.laserNumObservedPoints is None:
        self.laserNumObservedPoints = 0
      if self.laserNumCorrespondences is None:
        self.laserNumCorrespondences = 0
      if self.laserStage0Weights is None:
        self.laserStage0Weights = 0.
      if self.laserStageRWeights is None:
        self.laserStageRWeights = 0.
      if self.laserMeanSqError is None:
        self.laserMeanSqError = 0.
      if self.lastPointCloudRunTime is None:
        self.lastPointCloudRunTime = 0.
      if self.pointCloudRunTime is None:
        self.pointCloudRunTime = 0.
      if self.pointCloudNumObservedPoints is None:
        self.pointCloudNumObservedPoints = 0
      if self.pointCloudNumCorrespondences is None:
        self.pointCloudNumCorrespondences = 0
      if self.pointCloudStage0Weights is None:
        self.pointCloudStage0Weights = 0.
      if self.pointCloudStageRWeights is None:
        self.pointCloudStageRWeights = 0.
      if self.pointCloudMeanSqError is None:
        self.pointCloudMeanSqError = 0.
    else:
      self.timeStamp = 0.
      self.x = 0.
      self.y = 0.
      self.angle = 0.
      self.angleUncertainty = 0.
      self.locationUncertainty = 0.
      self.map = ''
      self.lastLaserRunTime = 0.
      self.laserRunTime = 0.
      self.laserNumObservedPoints = 0
      self.laserNumCorrespondences = 0
      self.laserStage0Weights = 0.
      self.laserStageRWeights = 0.
      self.laserMeanSqError = 0.
      self.lastPointCloudRunTime = 0.
      self.pointCloudRunTime = 0.
      self.pointCloudNumObservedPoints = 0
      self.pointCloudNumCorrespondences = 0
      self.pointCloudStage0Weights = 0.
      self.pointCloudStageRWeights = 0.
      self.pointCloudMeanSqError = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_d5f.pack(_x.timeStamp, _x.x, _x.y, _x.angle, _x.angleUncertainty, _x.locationUncertainty))
      _x = self.map
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2d2i3f2d2i3f.pack(_x.lastLaserRunTime, _x.laserRunTime, _x.laserNumObservedPoints, _x.laserNumCorrespondences, _x.laserStage0Weights, _x.laserStageRWeights, _x.laserMeanSqError, _x.lastPointCloudRunTime, _x.pointCloudRunTime, _x.pointCloudNumObservedPoints, _x.pointCloudNumCorrespondences, _x.pointCloudStage0Weights, _x.pointCloudStageRWeights, _x.pointCloudMeanSqError))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 28
      (_x.timeStamp, _x.x, _x.y, _x.angle, _x.angleUncertainty, _x.locationUncertainty,) = _struct_d5f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map = str[start:end].decode('utf-8')
      else:
        self.map = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.lastLaserRunTime, _x.laserRunTime, _x.laserNumObservedPoints, _x.laserNumCorrespondences, _x.laserStage0Weights, _x.laserStageRWeights, _x.laserMeanSqError, _x.lastPointCloudRunTime, _x.pointCloudRunTime, _x.pointCloudNumObservedPoints, _x.pointCloudNumCorrespondences, _x.pointCloudStage0Weights, _x.pointCloudStageRWeights, _x.pointCloudMeanSqError,) = _struct_2d2i3f2d2i3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_d5f.pack(_x.timeStamp, _x.x, _x.y, _x.angle, _x.angleUncertainty, _x.locationUncertainty))
      _x = self.map
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2d2i3f2d2i3f.pack(_x.lastLaserRunTime, _x.laserRunTime, _x.laserNumObservedPoints, _x.laserNumCorrespondences, _x.laserStage0Weights, _x.laserStageRWeights, _x.laserMeanSqError, _x.lastPointCloudRunTime, _x.pointCloudRunTime, _x.pointCloudNumObservedPoints, _x.pointCloudNumCorrespondences, _x.pointCloudStage0Weights, _x.pointCloudStageRWeights, _x.pointCloudMeanSqError))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 28
      (_x.timeStamp, _x.x, _x.y, _x.angle, _x.angleUncertainty, _x.locationUncertainty,) = _struct_d5f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map = str[start:end].decode('utf-8')
      else:
        self.map = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.lastLaserRunTime, _x.laserRunTime, _x.laserNumObservedPoints, _x.laserNumCorrespondences, _x.laserStage0Weights, _x.laserStageRWeights, _x.laserMeanSqError, _x.lastPointCloudRunTime, _x.pointCloudRunTime, _x.pointCloudNumObservedPoints, _x.pointCloudNumCorrespondences, _x.pointCloudStage0Weights, _x.pointCloudStageRWeights, _x.pointCloudMeanSqError,) = _struct_2d2i3f2d2i3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d2i3f2d2i3f = struct.Struct("<2d2i3f2d2i3f")
_struct_d5f = struct.Struct("<d5f")
