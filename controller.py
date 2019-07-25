#!/usr/bin/python3

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])



   '''
    # tmp = diff_doc.sections
    # print(tmp)
    # # from gi.repository import Gtk
    # label = Gtk.Label()
    # label.set_text(tmp)
    # txt = label.get_text()
    # print(type(txt), txt)
    # print(txt == tmp)


    # logging.debug("NFD:diff_doc.sections: {}".format(tmp))

    # tmp = unicodedata.normalize('NFC', str(diff_doc.sections))
    # print(tmp)
    # logging.debug("NFC:diff_doc.sections: {}".format(tmp))

    # tmp = unicodedata.normalize('NFKD', str(diff_doc.sections))
    # print(tmp)
    # logging.debug("NFKD:diff_doc.sections: {}".format(tmp))

    # tmp = unicodedata.normalize('NFKC', str(diff_doc.sections))
    # print(tmp)
    # logging.debug("NFKC:diff_doc.sections: {}".format(tmp))

    # logging.debug("diff_doc.sections: {}".format(unicodedata.normalize('NFKC', str(diff_doc.sections))))

    # unicodedata.normalize(NFD, unistr)
    # unicodedata.normalize(NFC, unistr)
    # unicodedata.normalize(NFKD, unistr)
    # unicodedata.normalize(NFKC, unistr)
  


   '''