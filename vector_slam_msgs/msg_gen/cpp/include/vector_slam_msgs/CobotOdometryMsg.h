/* Auto-generated by genmsg_cpp for file /home/samer/code_release/hitl-slam/vector_slam_msgs/msg/CobotOdometryMsg.msg */
#ifndef VECTOR_SLAM_MSGS_MESSAGE_COBOTODOMETRYMSG_H
#define VECTOR_SLAM_MSGS_MESSAGE_COBOTODOMETRYMSG_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"

namespace vector_slam_msgs
{
template <class ContainerAllocator>
struct CobotOdometryMsg_ {
  typedef CobotOdometryMsg_<ContainerAllocator> Type;

  CobotOdometryMsg_()
  : header()
  , dr(0.0)
  , dx(0.0)
  , dy(0.0)
  , v0(0.0)
  , v1(0.0)
  , v2(0.0)
  , v3(0.0)
  , vr(0.0)
  , vx(0.0)
  , vy(0.0)
  , VBatt(0.0)
  , status(0)
  {
  }

  CobotOdometryMsg_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , dr(0.0)
  , dx(0.0)
  , dy(0.0)
  , v0(0.0)
  , v1(0.0)
  , v2(0.0)
  , v3(0.0)
  , vr(0.0)
  , vx(0.0)
  , vy(0.0)
  , VBatt(0.0)
  , status(0)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef float _dr_type;
  float dr;

  typedef float _dx_type;
  float dx;

  typedef float _dy_type;
  float dy;

  typedef float _v0_type;
  float v0;

  typedef float _v1_type;
  float v1;

  typedef float _v2_type;
  float v2;

  typedef float _v3_type;
  float v3;

  typedef float _vr_type;
  float vr;

  typedef float _vx_type;
  float vx;

  typedef float _vy_type;
  float vy;

  typedef float _VBatt_type;
  float VBatt;

  typedef uint8_t _status_type;
  uint8_t status;


  typedef boost::shared_ptr< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator>  const> ConstPtr;
}; // struct CobotOdometryMsg
typedef  ::vector_slam_msgs::CobotOdometryMsg_<std::allocator<void> > CobotOdometryMsg;

typedef boost::shared_ptr< ::vector_slam_msgs::CobotOdometryMsg> CobotOdometryMsgPtr;
typedef boost::shared_ptr< ::vector_slam_msgs::CobotOdometryMsg const> CobotOdometryMsgConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace vector_slam_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> > {
  static const char* value() 
  {
    return "aa3d834c58b9c20e209a4310ffd09de1";
  }

  static const char* value(const  ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xaa3d834c58b9c20eULL;
  static const uint64_t static_value2 = 0x209a4310ffd09de1ULL;
};

template<class ContainerAllocator>
struct DataType< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> > {
  static const char* value() 
  {
    return "vector_slam_msgs/CobotOdometryMsg";
  }

  static const char* value(const  ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
\n\
float32 dr\n\
float32 dx\n\
float32 dy\n\
\n\
float32 v0\n\
float32 v1\n\
float32 v2\n\
float32 v3\n\
\n\
float32 vr\n\
float32 vx\n\
float32 vy\n\
\n\
float32 VBatt\n\
uint8 status\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.dr);
    stream.next(m.dx);
    stream.next(m.dy);
    stream.next(m.v0);
    stream.next(m.v1);
    stream.next(m.v2);
    stream.next(m.v3);
    stream.next(m.vr);
    stream.next(m.vx);
    stream.next(m.vy);
    stream.next(m.VBatt);
    stream.next(m.status);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct CobotOdometryMsg_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::vector_slam_msgs::CobotOdometryMsg_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "dr: ";
    Printer<float>::stream(s, indent + "  ", v.dr);
    s << indent << "dx: ";
    Printer<float>::stream(s, indent + "  ", v.dx);
    s << indent << "dy: ";
    Printer<float>::stream(s, indent + "  ", v.dy);
    s << indent << "v0: ";
    Printer<float>::stream(s, indent + "  ", v.v0);
    s << indent << "v1: ";
    Printer<float>::stream(s, indent + "  ", v.v1);
    s << indent << "v2: ";
    Printer<float>::stream(s, indent + "  ", v.v2);
    s << indent << "v3: ";
    Printer<float>::stream(s, indent + "  ", v.v3);
    s << indent << "vr: ";
    Printer<float>::stream(s, indent + "  ", v.vr);
    s << indent << "vx: ";
    Printer<float>::stream(s, indent + "  ", v.vx);
    s << indent << "vy: ";
    Printer<float>::stream(s, indent + "  ", v.vy);
    s << indent << "VBatt: ";
    Printer<float>::stream(s, indent + "  ", v.VBatt);
    s << indent << "status: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.status);
  }
};


} // namespace message_operations
} // namespace ros

#endif // VECTOR_SLAM_MSGS_MESSAGE_COBOTODOMETRYMSG_H

