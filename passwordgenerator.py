import string
import random
if __name__ == "__main__":
    st1=string.ascii_lowercase
    st2=string.ascii_uppercase
    st3=string.digits
    st4=string.punctuation
    password_length=int(input("Enter the length of password:"))
    s=[]
    s.extend(list(st1))
    s.extend(list(st2))
    s.extend(list(st3))
    s.extend(list(st4))

    print("Password is: ")
    print("".join(random.sample(s,password_length)))




    