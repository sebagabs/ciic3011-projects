# Filename: MaldonadoSebastian_086_P3.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: Sebastian G. Maldonado Rosado
# STUDENT ID: ###-##-####
# SECTION: 086

"""Parse the contents of an HTML file and output the internal resources used.

We are looking for tags of interest: a, script, link, img, audio, video, and form.
Within each tag of interest we're looking for a particular attribute of
interest (href for a & link, src for script & img, action for form).
Each tag of interest is to be represented by a dictionary, where the attribute names
will be the dictionary keys and the attribute values will be the dictionary values.
A list is created for each type of tag, storing all of the internal
resources referenced by tags of that type.
Finally, the results are stored in an output file.

Input:  The file index.html will be used as an input file
Output: The results will be stored in a file named index_resources.txt
"""

# CONSTANTS

INPUTFILE = 'index.html'
OUTPUTFILE = 'index_resources.txt'
# We'll use a dictionary where the keys are the tags of interest and the values
# are the corresponding attributes of interest.  That way we can process the HTML
# file using this dictionary without having to look for specific tags or attributes.
DICTOFINTEREST = {'a': 'href', 'link': 'href', 'form': 'action',
                  'img': 'src', 'script': 'src', 'audio': 'src', 'video': 'src'}


def load_data():
    """Returns the contents of the input file as a list of lines, or None if an error occurs."""
    try:
        fh = open(INPUTFILE)
    except:
        linesInFile = None
    else:  # Only gets executed if no exception was raised
        linesInFile = fh.readlines()
        fh.close()
    return linesInFile


def get_tag_of_interest(line):
    """Return a tag of interest if one is found in the line, or None otherwise.

    Parameters:
        line - A single line of text from the HTML file being processed.
    Returns:
        A string with the (opening) tag of interest, if one is found, or None otherwise.
    """
    # The tags of interest are the keys to the dictionary DICTOFINTEREST.
    for tagName in DICTOFINTEREST:
        # Note that, for a tag to have a resource, it must have a space after the tag name
        openingTag = '<' + tagName + ' '
        if openingTag in line:  # Found it!
            posTagBegin = line.find(openingTag)
            # Make sure we don't just find any '>', but the next one after the start of the tag.
            posTagEnd = line.find('>', posTagBegin)
            return line[posTagBegin:posTagEnd + 1]
    # If we're still in the function, then we didn't find any tags of interest.
    return None


def get_attr_of_interest(tag):
    """Return value of attribute of interest if one is in the tag, or None otherwise.

    Parameters:
        tag - A tag (as a dict) within which we'll look for the attribute of interest.
              Attribute names are the dict keys and attribute values are the dict values.
              The tag name can be found as the value of the 'tagName' key.
    Returns:
        A string representing the value of the attribute of interest for the tag received,
        or None if either the attribute is absent or if the resource is external.
    """
    tagType = tag['tagName']
    if tagType in DICTOFINTEREST:  # Checks if the received dictionary has a tag of interest.
        if DICTOFINTEREST[tagType] in tag:  # If the tag is of interest, checks for an attribute of interest.
            attr = DICTOFINTEREST[tagType]
            value = tag[attr]  # Extracts the value of the attribute of interest.
            if value.startswith('http:') or value.startswith('https:'):
                # If the attribute is external we don't want its value;
                # function returns None.
                return None
            else:
                return value
        # If the dictionary fed into the function does not have
        # a tag nor attribute of interest, we ignore it.
        else:
            return None
    else:
        return None


def write_results(dictOfResources):
    """Write all of the resources to an output file.

    Parameters:
        dictOfResources - Dictionary of resources to be saved in the output file.
                          The keys are the tags of interest and each value is a
                          list of all of the resouces for that type of tag.
    """
    outFH = open(OUTPUTFILE, 'w')  # Opens the output file in writing mode.
    dicc = dictOfResources.items()
    dicc = sorted(dicc)  # Sorts tag keys by alphabetical order.
    for tag, attr in dicc:
        # If the tag key has a list as a value with more than
        # zero elements, write the attribute values into the file.
        if len(attr) > 0:
            outFH.write(tag + '\n')  # Writes the title of a section.
            for element in attr:  # Writes each attribute value
                element = str(element)
                outFH.write('\t' + element + '\n')
        # If the tag key has an empty list as its value, no
        # attributes of interest were found so no need to write a blank space.
        # Continues to the next tag key.
        else:
            continue
    outFH.close()  # Closes the file when done. Remember to always close your files!


def tag_as_dict(openingTag):
    """Convert an opening HTML tag into a dictionary.

    The attribute names will be the keys of the dictionary and the attribute values
    will be the values of those keys.  In the case of boolean attributes (the ones
    that don't have a value assigned to them), the value will be set to True.
    The dictionary will also have the special key 'tagName' to store the tag name
    (e.g. img, audio).
    NOTE: We assume attribute values DO NOT have spaces, and that the only spaces
    in the tag are to separate attributes.

    Parameters:
        openingTag - The opening HTML tag to be converted into a dictionary.
    Returns:
        A dictionary representation of the tag, as detailed above.
    """
    dicc = {}
    tag = openingTag.split()
    tagName = tag[0].split('<')
    dicc['tagName'] = tagName[1]  # Determines the type of tag in the line.
    for i in range(1, len(tag)):  # Finds each attribute in the tag and their value.
        attribute = tag[i].split('=')
        # Checks for boolean attributes; if present, add them True as value.
        if len(attribute) == 1:
            attr = tag[i].split('>')
            attr = attr[0]
            dicc[attr] = True
        else:  # If no boolean attribute exists in the tag, find other attributes.
            attr = attribute[0]
            value = attribute[1]
            value = value.strip('">')  # Extracts the value of an attribute
            dicc[attr] = value
    # The function returns a dictionary, which will be used
    # to be fed into the get_attr_of_interest() function.
    return dicc


def main():
    lstOfLines = load_data()
    if lstOfLines is None:
        print('ERROR: Could not open {}!'.format(INPUTFILE))
        exit()

    # The following dictionary will store all of the tags with resources, using the
    # tag name as the keys and a list of tags as the value.
    resourcesDict = dict()

    # Creates a list for each tag in DICTOFINTEREST, and adds it as a value to the
    # corresponding key in the resourcesDict.
    for tags in DICTOFINTEREST:
        resourcesDict[tags] = list()

    # Loops through the lines of a file, looking for tags and attributes of interest within them.
    for line in lstOfLines:
        tag = get_tag_of_interest(line)
        if tag is not None:  # If a tag of interest is found.
            tag = tag_as_dict(tag)
            attrVal = get_attr_of_interest(tag)
            if attrVal is not None:  # If the tag possesses an attribute of value.
                # Adds the found value to its corresponding list inside resourcesDict
                # depending on the attribute it came from.
                if tag['tagName'] in DICTOFINTEREST:
                    resourcesDict[tag['tagName']].append(attrVal)
            # If no tag of interest or no attribute of interest is found, continues
            # to the next line of the file.
            else:
                continue
        else:
            continue

    # Orders the attribute values in the lists inside resourcesDict (lists are the value of the keys
    # inside this dictionary) by alphabetical order.
    for tagKey in resourcesDict:
        resourcesDict[tagKey].sort()

    # Saves resourcesDict in an output file.
    write_results(resourcesDict)


# This line makes python start the program from the main function
# unless our code is being imported
if __name__ == '__main__':
    main()
