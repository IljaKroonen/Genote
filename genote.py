from re import sub
from sys import argv, exit

def replace_last_occurence(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def gff(seqname, source, feature, start, end, score, strand, frame, attribute):
    s = '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\n'
    return s.format(seqname, source,feature, start, end, score, strand, frame,
                    attribute)


def line_to_gff(line):
    spl = sub(' +', ' ', line).strip().split(' ')
    seqname = spl[4]
    start = spl[5]
    end = spl[6]
    name = spl[9]
    family = spl[10]
    return gff(seqname, 'Genote', family, start, end, '.', '.', '.',
               'Name={0}'.format(name))

if len(argv) != 2:
    print 'Usage: ./launch target_file'
    exit(1)

if not argv[1].endswith('.out'):
    print 'Must input .out file'
    exit(2)

output_file = replace_last_occurence(argv[1], '.out', '.gff')
    
with open(argv[1], 'r') as i: 
    with open(output_file, 'w') as o:
        i.readline()
        i.readline()
        i.readline()
        
        for line in i:
            o.write(line_to_gff(line))
