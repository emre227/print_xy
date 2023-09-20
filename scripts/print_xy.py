#!/usr/bin/env python3
import rospy
import tf
import geometry_msgs.msg
import math

listener = tf.TransformListener()

rate = rospy.Rate(10.0)
while not rospy.is_shutdown():
    try:
        (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
        print(trans)
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        continue