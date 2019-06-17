template = '{0:10} {1:8} {2:6} {3:6} {4:6} {5:6} {6:6} {7:4}'

sdict = {}


def display_menu():
    print ('\nMENU')
    print '1. Add student information'
    print '2. Modify student information'
    print '3. Delete student information'
    print '4. Save student information'
    print '5. Retrieve student information'
    print '6. Display student information'
    print '7. Quit'
    print '8. Debug\n'

    ch = int(raw_input('Enter your choice: '))
    if ((ch > 0 and ch < 7) or (ch == 8)):
        return ch
    elif (ch == 7):
        return -1
    else:
        return 0


def getinfo():
    print ('\nEnter the student details: \n')
    name = raw_input('Name         :')
    sid  = raw_input('Student RN   :')
    cls  = raw_input('Class        :')
    phy  = raw_input('Physics      :')
    chem = raw_input('Chemistry    :')
    math = raw_input('Maths        :')
    eng  = raw_input('English      :')

    student = {}
    student['name'] = name
    student['sid'] = sid
    student['cls'] = cls
    student['phy'] = phy
    student['chem'] = chem
    student['math'] = math
    student['eng'] = eng
    
    sdict[name] = student
    
    #DEBUG Code Starts
    print student
    print sdict
    #DEBUG Code Ends
    
    return 1

def deleteRecord(sid):
    #Search sid
    for item in sdict.keys():
        # Debug Start
        #print 'Accessing: ' + item
        #print sdict[item]
        # Debug End
        if(sdict[item]['sid'] == sid):
            del sdict[item]
            return 1
    return 0

def getFieldChoice():
    print('\n\nWhich field to modify?')
    print('1.SID\n2.CLASS\n3.Physics\n4.Chemistry\n5.Maths\n6.English\n')
    ch = int(raw_input('Enter your choice: '))
    if(ch == 1):
        key = 'sid'
    if(ch == 2):
        key = 'cls'
    if(ch == 3):
        key = 'phy'
    if(ch == 4):
        key = 'chem'
    if(ch == 5):
        key = 'math'
    if(ch == 6):
        key = 'eng'
    return key
    

def modifyRecord(sid):
    #Search sid
    for item in sdict.keys():
        # Debug Start
        print 'Accessing: ' + item
        print sdict[item]
        # Debug End
        if(sdict[item]['sid'] == sid):
            key = getFieldChoice()
            print('Current Value: ' + sdict[item][key])
            newValue = raw_input('Enter new value: ')
            sdict[item][key] = newValue
            return 1
    return 0

def printInfo():
    print('\n\n' + '-'*60)
    print template.format('Name', 'SID', 'CLASS', 'PHY', 'CHEM', 'MATH', 'ENG', 'RANK')
    print('\n\n' + '-'*60)
    for item in sdict.keys():
        name = sdict[item]['name']
        sid = sdict[item]['sid']
        cls = sdict[item]['cls']
        phy = sdict[item]['phy']
        chem = sdict[item]['chem']
        math = sdict[item]['math']
        eng = sdict[item]['eng']
        print template.format(name, sid, cls, phy, chem, math, eng, '0')
    print('\n\n' + '-'*60)

if __name__ == '__main__':
    #ch = display_menu()
    #print str(ch) + ' Chosen!'
    for i in range(2):
        print 'calling function getinfo'
        getinfo()
    #sid = raw_input('Enter sid')
    #deleteRecord(sid)
    #modifyRecord(sid)
    print sdict
    printInfo()



    
