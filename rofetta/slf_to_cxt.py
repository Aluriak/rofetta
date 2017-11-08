"""Conversion of slf to cxt formats.

"""


SLF_HEADERS = {'lattice', 'objects', 'attributes', 'relation'}


def file_to_file(slffile:str, cxtfile:str):
    """Write in cxtfile in cxt format the context found in slf format in
    given slf file.
    """

    with open(slffile) as ifd, open(cxtfile, 'w') as ofd:
        ofd.write('B\n\n')
        lines = iter(ifd)
        for line in lines:
            if line.startswith('['):
                header = line.strip('[]\n').lower()
                assert header in SLF_HEADERS, header
                if header == 'lattice':
                    nb_obj, nb_att = map(int, (next(lines), next(lines)))
                    ofd.write('{}\n{}\n\n'.format(nb_obj, nb_att))
                elif header == 'objects':
                    for _ in range(nb_obj):
                        ofd.write(next(lines))
                elif header == 'attributes':
                    for _ in range(nb_att):
                        ofd.write(next(lines))
                elif header == 'relation':
                    for line in lines:
                        ofd.write(''.join('.' if attr == '0' else 'X' for attr in line.strip().split()) + '\n')
                else:
                    raise ValueError("Header {} is not handled".format(header))



if __name__ == '__main__':
    file_to_file('contexts/rfc_foobar.slf', 'contexts/rfc_foobar.cxt')




