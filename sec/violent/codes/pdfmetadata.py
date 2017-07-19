#encoding: utf-8
import pyPdf

def pdf_metadata(path):
    _fhandler = open(path, 'rb')
    _pdf_handler = pyPdf.PdfFileReader(_fhandler)
    for _key, _value in _pdf_handler.getDocumentInfo().items():
        print '%s: %s' % (_key, _value)
    _fhandler.close()

if __name__ == '__main__':
    pdf_metadata('e:/temp/ANONOPS_The_Press_Release.pdf')
