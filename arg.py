def plist(key,*argu,**kw):
    print(key)
    for i in argu:
        print(i)
    for key,value in kw.items():
        print(f"{key} is a key of {value}")

names={"arpit","patel","kumar"}
key="hi there"

intro={"name":"aepit","work":"software tester","salary":"22000"}

plist(key,*names,**intro)
    