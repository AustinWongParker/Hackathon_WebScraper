def convertFile(inputFileName,outputFileName):

    # Open a file for input and a file for output
    inFile = open(inputFileName,"r")
    outFile = open(outputFileName,"w")

    outFile.write("<table>\n")

    # Make the table header
    line = inFile.readline()
    outFile.write(convertRow(line, "th"))

    # Make all the following rows
    line = inFile.readline()
    while line != "":

        # Convert this row and write it to the output file
        outFile.write(convertRow(line, "td"))

        # Get the next line
        line = inFile.readline()

    outFile.write("</table>")

    # Close the input and output files
    outFile.close()
    inFile.close()

def convertRow(row, itemTag):
    out = "\t<tr>\n"
    for item in row.split(";"):
        item = item.replace("\n","")
        if item.replace(" ","") != "":
            out += "\t\t" + convertItem(item, itemTag)
    out += "\t</tr>\n"
    return out

def convertItem(item, itemTag):
    return "<" + itemTag + ">" + item + "</" + itemTag + ">\n"
