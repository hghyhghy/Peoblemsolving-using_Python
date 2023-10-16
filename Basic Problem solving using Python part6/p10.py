# slicing in python to rotate a string

# creating a function


def ofrotate(s, d):
    lfirst = s[0:d]  # starting of slicing for left rotation

    lsecond = s[d:]

    # starting of slicing for right rotation

    rfirst = s[0 : len(s) - d]

    rsecond = s[len(s) - d :]

    print(f"Left rotation of {s} is ", lsecond + lfirst)

    print(f"Right rotation of {s} is ", rsecond + rfirst)


s = "Subham and Shreyoshi"

d = 2

ofrotate(s, d)  # calling the function
