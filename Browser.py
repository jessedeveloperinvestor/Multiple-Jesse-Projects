import urllib.request, urllib.parse, urllib.error
n = 0
while n > -1:
    try:
        x = input("Hello, type in the link that you'd like to load\n")
        fhand= urllib.request.urlopen(x)
    except:
        x = 'http://data.pr4e.org/romeo.txt'
        print("This URL is wrong\nLoading" + x + '\n')
    fhand= urllib.request.urlopen(x)
    for line in fhand:
        print(line.decode().strip())
    print('\n')
    n = n + 1
