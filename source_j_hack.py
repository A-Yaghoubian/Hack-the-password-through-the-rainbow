import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        name = list()
        hash_pass = list()
        for x in reader:
            name.append(x[0].strip())
            hash_pass.append(x[1].strip())
        # print(name , hash_pass)

    HashOrPass = dict()
    for i in range(0,10000):
        ii = hashlib.sha256(str(i).encode('utf-8' ))
        HashOrPass[ii.hexdigest()] = i
    # print(HashOrPass)

    with open(output_file_name , 'w+') as ff:
        u = 0
        for hashh in hash_pass:
            for hashhh in HashOrPass.keys():
                if hashh == hashhh:
                    if u == 0:
                        st = name[u] + ',' + str(HashOrPass[hashhh])
                    else:
                        st = '\n' + name[u] + ',' + str(HashOrPass[hashhh])
                    ff.write(st)
                    u += 1

    f.close()
    ff.close()
