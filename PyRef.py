
def grab_references(bibfile):
    with open(bibfile,'r') as f:
        lines = f.readlines()
    refs = [line for line in lines if '@' in line.lower()]
    return ['\\cite{'+line.split('{')[1].split(',')[0]+'}' for line in refs]

def write_tex_file(refs,fname,bibfile, documentclass='emulateapj',packages=['natbib','aas_macros'],bibliographystyle='apj'):

    with open(fname,'w') as f:
        f.write('\\documentclass{' + documentclass + '}\n')

        f.write('\n'.join(['\\usepackage{'+package+'}\n' for package in packages]))
        f.write('\\bibliographystyle{'+bibliographystyle+'}\n')

        f.write('\\begin{document}\n')

        f.write('\n'.join(refs) + '\n')

        f.write('\\thebibliography{' + bibfile+'}\n')

        f.write('\\end{document}\n')


if __name__ == "__main__":
    import sys

    bibfile = sys.argv[1]
    outname = sys.argv[2]

    print('Reading .bib file: {}'.format(bibfile))
    print('Outputting .tex file: {}'.format(outname))

    refs =  grab_references(bibfile)
    bibfile = bibfile.split('/')[-1]
    write_tex_file(refs,outname,bibfile)
