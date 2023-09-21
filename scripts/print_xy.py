#!/usr/bin/env python3
import rospy
import tf
import geometry_msgs.msg
import math




if __name__ == '__main__':

    rospy.init_node('print_xy')
    listener = tf.TransformListener()
    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
            print(trans)
            rate.sleep()
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

       