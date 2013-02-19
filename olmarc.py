import pymarc
import time

writer = pymarc.MARCWriter(file('free_ebooks.marc', 'w'))
error = open('errors.txt', 'w')

count = 0

for line in open('marc_urls.txt'):
    try:
        marcrec = pymarc.parse_xml_to_array(line)
        writer.write(marcrec[0])            
    except:
        error.write(line)

    count += 1
    time.sleep(0.3)
    if (count % 10) == 0:
        print count
    if (count % 1000) == 0:
        break

writer.close()

            
            
            
