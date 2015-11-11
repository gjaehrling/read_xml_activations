#!/usr/bin/env python

import sys
import os
import xml.etree.ElementTree as ET

# Path for spark source folder
os.environ['SPARK_HOME'] = "/Users/hadoop/spark-1.3.1-bin-hadoop1"

# Append pyspark  to Python Path
sys.path.append("/Users/hadoop/spark-1.3.1-bin-hadoop1/bin")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print ("Successfully imported Spark Modules")

except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)


# calling the main function:


def main():
    filename = "hdfs:/user/hadoop/data/*.xml"
    activations = sc.textFile(filename)
    activationTrees = activations.mapPartitions(lambda xml: parseXML(s))


# example for a user defined function:
# parsing an XML file getting the name of the tag 'model'

def parseXML(s):
    tree = ET.parse(s)
    root = tree.getroot()
    for element in root.iter('model'):
        print element.text


if __name__ == '__main__':
    main()
