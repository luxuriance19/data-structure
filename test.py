def flatten(nested):
    try:
        try: nested+""
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

a = ['foo',['bar',['baz']]]
print(list(flatten(a)))

class Student():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "Student (name: %s)"%self.name
    def __repr__(self):
        return __str__()

s = Student('lily')
print(s)

from lxml import etree
some_xml_data = "<annotation><folder>OXIIIT</folder><filename>Abyssinian_1.jpg</filename><source><database>OXFORD-IIIT Pet Dataset</database><annotation>OXIIIT</annotation><image>flickr</image></source><size><width>600</width><height>400</height><depth>3</depth></size><segmented>0</segmented><object><name>cat</name><pose>Frontal</pose><truncated>0</truncated><occluded>0</occluded><bndbox><xmin>333</xmin><ymin>72</ymin><xmax>425</xmax><ymax>158</ymax></bndbox><difficult>0</difficult></object></annotation>"

root = etree.fromstring(some_xml_data)
if root is object:
    print(True)
print(root)
print(root.tag)
print(root.text)

import sys
sys.setrecursionlimit(1000000)

def recursive_parse_xml_to_dict(xml):
    #if not xml:
    if xml.text is not None:
        # print(xml.text)
        return {xml.tag: xml.text}
    result = {}
    for child in xml:
        child_result = recursive_parse_xml_to_dict(child)
        if child.tag != 'object':
            result[child.tag] = child_result[child.tag]
        else:
            if child.tag not in result:
                result[child.tag] = []
            result[child.tag].append(child_result[child.tag])
    return {xml.tag: result}

def recursive_parse_xml_to_dict1(xml):
    if not xml:
    # if xml.text is not None:
        # print(xml.text)
        return {xml.tag: xml.text}
    result = {}
    for child in xml:
        child_result = recursive_parse_xml_to_dict(child)
        if child.tag != 'object':
            result[child.tag] = child_result[child.tag]
        else:
            if child.tag not in result:
                result[child.tag] = []
            result[child.tag].append(child_result[child.tag])
    # print(xml.tag)
    return {xml.tag: result}

with open('/home/lily/projects/research/annotations/xmls/Abyssinian_1.xml', 'r') as f:
    xml_str = f.read()
xml = etree.fromstring(some_xml_data)


print(recursive_parse_xml_to_dict(root))
print(recursive_parse_xml_to_dict1(xml))

#for child in root:
    # print(child)


def recurse(xml):
    if xml.text is not None:
        return {xml.tag: xml.text}

    result = {}
    for child in xml:
        child_result = recurse(xml)

        # 递归之后的处理手段
        if child.tag != "object":
            result[child.tag] = child_result[child.tag]
        else:
            if child.tag not in result:
                result[child.tag] = []
            result[child.tag].append(child_result[child.tag])

    return {xml.tag: result}