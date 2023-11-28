import PyPDF3 as pypdf



def main():

    ifile = pypdf.PdfFileReader("./homework-8.pdf")

    output = pypdf.PdfFileWriter()



    for i in range(ifile.getNumPages()):
        page = ifile.getPage(i)
        output.addPage(page)

    # output = pypdf.PdfFileWriter()
    js_code = open("./sample.js")

    output.addJS(js_code.read())



    outputStream = open("document-output.pdf", "wb")
    output.write(outputStream)
    outputStream.close()



if __name__ == "__main__":
    main()
