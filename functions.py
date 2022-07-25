
# takes name in the format usually given and returns firstnames, lastname in that order
from email.utils import formatdate


def formatName(name):
    splt = name.split(', ')
    lname = splt.pop(0)
    fnames = ""
    fnameSplt = splt[0]
    fnameSplt = fnameSplt.split(' ')
    
    try: 
        # seperates the first names and removes country code
        if not(fnameSplt[len(fnameSplt) - 1][0] == '('):
            fnameSplt.append('s')
    except:
        print('except Ran ' + name)
        pass
        
    for i in range(0, len(fnameSplt) - 1):
        fnames = fnames + fnameSplt[i] + ' '
    fnames = fnames[:-1]
    
    return (fnames, lname)
    

def formatData(data):
    formatted = [[''] * 7][0]
    # gets first and last names from the data
    formatted[0], formatted[1] = formatName(data.pop(0))
    address = []
    for i in data:
        if i == 'No further information available.':
            return formatted
        elif 'Email:' in i:
            formatted[3] = i[7:]
        elif 'Tel.:' in i:
            formatted[5] = i.strip('Tel.: ')
        elif 'Fax:' in i:
            formatted[6] = i.strip('Fax: ')
        elif 'URL' in i:
            formatted[4] = i.strip('URL: ')
        else:
            address.append(i) 
    address = '\n'.join(address)
    formatted[2] = address
    return formatted
        
