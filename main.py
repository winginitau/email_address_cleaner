"""
Clean up and de-dupe a heap of email addresses from different
sources with inconsistent formatting.
"""

with open('list1.txt') as f:
    lines = f.readlines()
   
block = " ".join(lines)

estart= ['<', '(']
eend = ['>', ')']
delims = [';', ',', ' ', '\n']


class StripDetect():
    def __init__(self):
        self.strip_prefixes = [ 'mailto:', 'http://', 'https://' ]
        self.strip = []
        self. match_array = []
        for d in delims:
            for s in self.strip_prefixes:
                self.strip.append(d+s)
                self.match_array.append(0)
        self.buf = ''
        
        self.matching_count = 0
        self.unique_match = False
        self.matching = False
        self.last_complete_i = None

    def add_check(self, c):
        self.buf += c
        
        for i in range(0, len(self.strip)):
            #ss = self.strip[i][:self.match_array[i]+1]
            ssi = self.strip[i]
            mai = self.match_array[i]
            ss = ssi[:mai+1]
            buf_end = self.buf[-self.match_array[i]-1:]
            if ss in buf_end:
                self.matching = True
                self.match_array[i] += 1
            else:
                self.match_array[i] = 0

        partials = 0
        completes = 0
        last_complete_i = None
        
        if self.matching:
            for i in range(0, len(self.strip)):
                if self.match_array[i] > 0:
                    partials +=1
                    if self.match_array[i] == len(self.strip[i]):
                        completes +=1
                        last_complete_i = i
                        
        if completes == 1 and partials == 1:
            for i in range(0, len(self.match_array)):
                self.match_array[i] = 0
            
            return len(self.strip[last_complete_i])
        else: return 0


name_buf = ""
email_buf = "" 

in_name = False
in_email = False

emails = []
names = []

sd = StripDetect()

name_count = 0

for i in range(0, len(block)):

    c = block[i]
    
    if sd.add_check(c) != 0:
        # match - fix it
        name_buf = ''
        email_buf = ''
    
    else:
        if c not in delims:
            if c in estart:
                in_email = True
            elif c in eend:
                if not in_email:
                    raise ValueError('Closing > found before opening <')
                if name_count <= 1:
                    in_email = False
                    in_name = False
                    emails.append(email_buf)
                    names.append(name_buf)
                    email_buf = ""
                    name_buf = ""
                    name_count = 0
                else:
                    raise ValueError('Delimited names without assoicated email')
            elif in_email:
                email_buf = email_buf + c
            elif in_name and c == '@':
                # switch it to email
                email_buf = name_buf
                name_buf = ""
                in_name = False
                in_email = True
                email_buf += c
            else: 
                in_name = True
                name_buf = name_buf + c
        else:
            # is delim
            if in_name:
                if c == ' ':
                    # spaces ok in names
                    name_buf += c
                else: 
                    in_name = False
                    name_count +=1
                    #names.append(name_buf)
                    #name_buf = ""
            elif in_email:
                #due to email detected by '@' while in name rather than <>
                if name_count == 0:
                    in_email = False
                    in_name = False
                    emails.append(email_buf)
                    names.append(name_buf)
                    email_buf = ""
                    name_buf = ""
                    #name_count = 0
                else:
                    raise ValueError('Token was email but name already in name buf')

unique = {}


def add(i):
    unique[emails[i].lower()] = [emails[i], names[i]]


for i in range(0, len(emails)):
    if emails[i].lower() in unique.keys():
        if  len(names[i]) > len (unique[emails[i].lower()][1]):
            add(i)
    else:
        add(i)
    
sorted_list_tup = sorted(unique.items())

res = ''
for _i, v in sorted_list_tup:
    e, n = v
    if n == '':
        recipient = f'{e}'
    else:
        recipient = f'{n} <{e}>'
    print(recipient)

