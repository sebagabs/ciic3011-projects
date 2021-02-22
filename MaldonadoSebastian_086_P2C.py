# Filename: MaldonadoSebastian_086_P2.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: Sebastian G. Maldonado Rosado
# STUDENT ID: ###-##-####
# SECTION: 086

"""Parse the contents of an HTML file and output the internal resources used.

We are looking for tags of interest: a, script, link, and img.
Within each tag of interest we're looking for a particular attribute of
interest (href for a & link, src for script & img).
A list is created for each type of tag, storing all of the internal
resources referenced by tags of that type.
Finally, the results are stored in an output file.

Input:  The file index.html will be used as an input file
Output: The results will be stored in a file named index_resources.txt
"""


def load_data():
    """Returns the contents of index.html in a list, or None if an error occurs."""
    try:
        fh = open('index.html')
    except:
        lstOfLines = None
    else:  # Only gets executed if no exception was raised
        lstOfLines = fh.readlines()
        fh.close()
    return lstOfLines


def get_tag_of_interest(line):
    """Return a tag of interest if one is found in the line, or None otherwise."""
    # Loop iterates over a list to see if a tag of interest is found in a fed line.
    tags_of_interest = ['<a', '<script', '<link', '<img']
    for tags in tags_of_interest:
        if tags in line:
            tagStart = line.find(tags)
            tagEnd = line.find('>', tagStart)
            tag = line[tagStart:tagEnd+1]
            return tag
    # If there is no tag of interest, the function returns None automatically

def get_attr_of_interest(openingTag):
    """Return value of attribute of interest if one is in the tag, or None otherwise."""
    # If the tag fed into the function is empty, it returns None.
    if openingTag is None:
        return None

    # If the tag has a value, the next elif statements will look for the
    # attribute of interest depending on the type of tag.

    # If the found attribute is external (http: or https:), the function
    # will return None.
    elif openingTag.startswith('<a') or openingTag.startswith('<link'):
        if 'href=' in openingTag:
            hrefStart = openingTag.find('href=')
            hrefEnd = openingTag.find('"', hrefStart + 6)
            attr = openingTag[hrefStart + 6:hrefEnd]
            if attr.startswith('http:') or attr.startswith('https:'):
                return None
            else:
                return attr
        else:
            return None

    elif openingTag.startswith('<script') or openingTag.startswith('<img'):
        if 'src=' in openingTag:
            srcStart = openingTag.find('src=')
            srcEnd = openingTag.find('"', srcStart + 5)
            attr = openingTag[srcStart + 5:srcEnd]
            if attr.startswith('http:') or attr.startswith('https:'):
                return None
            else:
                return attr
        else:
            return None

    # If no attribute of interest is found, the function returns None.
    else:
        return None


def write_results(outFH, sectionName, listOfResources):
    """Write the resources of a particular section to an already opened file."""
    # If the list of resources is empty, the function does not execute.
    if len(listOfResources) == 0:
        return

    # If the list of resources has elements, then the loop adds each resource to
    # a given section in an already opened file.
    else:
        outFH.write(sectionName+'\n')
        for element in listOfResources:
            outFH.write(element+'\n')


def main():
    linesInFile = load_data()
    if linesInFile is None:
        print('ERROR: Could not open index.html!')
        exit()

    else:
        # Creates the lists where found resources will be stored, to later on write them to the output file.
        CSS = []
        JavaScript = []
        Images = []
        Hyperlinks = []

        # Loops through the file's line looking for the tags, and attributes in them, then
        # adds the resources (if found) to their respective lists.
        for line in linesInFile:
            tag = get_tag_of_interest(line)
            value = get_attr_of_interest(tag)

            # If no tag was found, or a tag without an attribute was found, continues
            # to the next line in the file.
            if tag is None or value is None:
                continue

            elif tag.startswith('<a'):
                Hyperlinks.append(value)

            elif tag.startswith('<script'):
                JavaScript.append(value)

            elif tag.startswith('<link'):
                CSS.append(value)

            elif tag.startswith('<img'):
                Images.append(value)

        # Orders each list in alphabetical order.
        CSS.sort()
        JavaScript.sort()
        Images.sort()
        Hyperlinks.sort()

        # Opens the output file and writes the resources lists in their corresponding section.
        outFH = open('index_resources.txt', 'w')
        write_results(outFH, 'CSS:', CSS)
        write_results(outFH, 'JavaScript:', JavaScript)
        write_results(outFH, 'Images:', Images)
        write_results(outFH, 'Hyperlinks:', Hyperlinks)
        # Closes the output file after finishing writing all the results.
        outFH.close()


# The next lines make the program run.
if __name__ == '__main__':
    main()
