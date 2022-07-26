
# takes name in the format usually given and returns firstnames, lastname in that order


def formatName(name):
    splt = name.split(', ')
    lname = splt.pop(0)
    fnameSplt = splt[0]
    fnameSplt = fnameSplt.split(' ')
    
    try: 
        # seperates the first names and removes country code
        if not(fnameSplt[len(fnameSplt) - 1][0] == '('):
            fnameSplt.append('s')
    except:
        print('except Ran ' + name)
        pass
    
    fname = fnameSplt.pop(0)
    mnames = ''
    if not (len(fnameSplt) == 0):
        for i in range(0, len(fnameSplt) - 1):
            mnames = mnames + fnameSplt[i] + ' '
        mnames = mnames[:-1]
    
    return (fname, mnames, lname)
    

def formatData(data):
    formatted = [[''] * 9][0]
    # gets first and last names from the data
    formatted[0], formatted[1], formatted[2] = formatName(data.pop(0))
    address = []
    for i in data:
        if i == 'No further information available.':
            return formatted
        elif 'Email:' in i:
            formatted[4] = i[7:]
        elif 'Tel.:' in i:
            formatted[6] = i.strip('Tel.: ')
        elif 'Fax:' in i:
            formatted[7] = i.strip('Fax: ')
        elif 'URL' in i:
            formatted[5] = i.strip('URL: ')
        else:
            address.append(i) 
    if (len(address) > 1):
        formatted[3] = address[0]
    
    address = '\n'.join(address)
    formatted[8] = address
    return formatted
        
